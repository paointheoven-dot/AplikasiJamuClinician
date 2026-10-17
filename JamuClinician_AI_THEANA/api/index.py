import os
import sys
import json
import urllib.request
import urllib.error
from flask import Flask, render_template, request, jsonify, send_from_directory

# Add parent directory to sys.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

templates_dir = os.path.join(ROOT_DIR, 'templates')
static_dir = os.path.join(ROOT_DIR, 'static')

# Explicit top-level Flask instance required by Vercel
app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir, static_url_path='/static')

# Import reasoning engines and helpers from serve
from serve import (
    call_gemini_api,
    call_gemini_nlp_extract,
    extract_patient_nlp_rules,
    build_ebm_fallback,
    format_analyze_response,
    normalize_patient_payload,
    load_env
)

load_env()

def get_server_api_key(payload=None):
    payload = payload or {}
    key = (
        payload.get("apiKey") or 
        payload.get("GEMINI_API_KEY") or 
        payload.get("api_key") or 
        os.getenv("GEMINI_API_KEY") or 
        os.getenv("GOOGLE_API_KEY") or 
        ""
    ).strip()
    return key

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        res = app.make_default_options_response()
        res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, HEAD, PUT, DELETE'
        res.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        return res

@app.after_request
def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, HEAD, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
    return response

@app.errorhandler(405)
def handle_405(e):
    if request.path.startswith('/api/'):
        return jsonify({
            "status": "online",
            "service": "JamuClinician AI Decision Engine",
            "method": request.method,
            "path": request.path,
            "message": "Endpoint is active. For analysis, submit data via POST."
        }), 200
    return index()

@app.errorhandler(404)
def handle_404(e):
    if request.path.startswith('/api/'):
        return jsonify({
            "status": "error",
            "error": f"Endpoint {request.path} not found"
        }), 404
    return index()

@app.route('/', methods=['GET', 'POST', 'OPTIONS', 'HEAD'])
@app.route('/index.html', methods=['GET', 'POST', 'OPTIONS', 'HEAD'])
def index():
    if request.method == 'OPTIONS':
        return ('', 204)
    tmpl = os.path.join(templates_dir, "index.html")
    if not os.path.exists(tmpl):
        tmpl = os.path.join(ROOT_DIR, "index.html")
    if os.path.exists(tmpl):
        with open(tmpl, "r", encoding="utf-8") as f:
            return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    return "JamuClinician AI Vercel Deployment Ready", 200

@app.route('/api/gemini-status', methods=['GET', 'POST', 'OPTIONS', 'HEAD'])
def gemini_status():
    if request.method == 'OPTIONS':
        return ('', 204)
    env_key = get_server_api_key()
    return jsonify({
        "status": "online",
        "hasServerKey": bool(env_key),
        "model": "gemini-3.5-flash-lite",
        "maskedKey": (env_key[:6] + "..." + env_key[-4:]) if env_key else ""
    })

@app.route('/api/gemini-nlp-extract', methods=['GET', 'POST', 'OPTIONS', 'HEAD'])
def gemini_nlp_extract():
    if request.method == 'OPTIONS':
        return ('', 204)
    
    if request.method in ('GET', 'HEAD'):
        return jsonify({
            "status": "online",
            "service": "Gemini NLP Patient Case Extractor",
            "model": "gemini-3.5-flash-lite",
            "hasServerKey": bool(get_server_api_key()),
            "usage": "Send POST request with JSON payload: {'narrative': '...'}"
        })

    payload = request.get_json(silent=True) or request.form.to_dict() or {}
    if not payload and request.data:
        try:
            payload = json.loads(request.data.decode('utf-8'))
        except Exception:
            payload = {"narrative": request.data.decode('utf-8')}

    narrative = (
        payload.get("narrative") or 
        payload.get("keluhanBebas") or 
        payload.get("story") or 
        payload.get("text") or 
        payload.get("case") or 
        ""
    ).strip()

    api_key = get_server_api_key(payload)

    if not narrative:
        return jsonify({"success": False, "error": "Teks narasi pasien tidak boleh kosong."}), 400

    extracted = None
    if api_key:
        try:
            extracted = call_gemini_nlp_extract(api_key, narrative)
        except Exception as g_err:
            print(f"[Vercel Serverless] Gemini NLP error: {g_err}. Using rule parser.")
            extracted = None

    if not extracted:
        extracted = extract_patient_nlp_rules(narrative)

    return jsonify({"success": True, "data": extracted})

@app.route('/api/analyze', methods=['GET', 'POST', 'OPTIONS', 'HEAD'])
@app.route('/api/gemini-analyze', methods=['GET', 'POST', 'OPTIONS', 'HEAD'])
def analyze():
    if request.method == 'OPTIONS':
        return ('', 204)
    
    if request.method in ('GET', 'HEAD'):
        return jsonify({
            "status": "online",
            "service": "JamuClinician AI Decision Engine",
            "model": "gemini-3.5-flash-lite",
            "hasServerKey": bool(get_server_api_key()),
            "usage": "Send POST request with JSON payload containing patient profile and complaints."
        })

    payload = request.get_json(silent=True) or request.form.to_dict() or {}
    if not payload and request.data:
        try:
            payload = json.loads(request.data.decode('utf-8'))
        except Exception:
            payload = {}

    patient = normalize_patient_payload(payload)
    knowledge_base = payload.get("knowledgeBase") or []
    api_key = get_server_api_key(payload)

    result = None
    is_gemini_ai = False

    if api_key:
        try:
            result = call_gemini_api(api_key, patient, knowledge_base)
            if result:
                result["source"] = "gemini_ai"
                result["model_used"] = result.get("model_used", "gemini-3.5-flash-lite")
                is_gemini_ai = True
        except Exception as g_err:
            print(f"[Vercel Serverless] Gemini API call error: {g_err}. Falling back to EBM.")
            result = None

    if not result:
        result = build_ebm_fallback(patient)
        result["source"] = "ebm_local"

    formatted = format_analyze_response(result, patient)
    formatted["success"] = True
    formatted["is_gemini_ai"] = is_gemini_ai
    formatted["api_key_detected"] = bool(api_key)
    formatted["data"] = dict(formatted)
    return jsonify(formatted)

@app.route('/JamuClinician_AI_THEANA.zip', methods=['GET', 'POST', 'OPTIONS', 'HEAD'])
@app.route('/download-zip', methods=['GET', 'POST', 'OPTIONS', 'HEAD'])
def download_zip():
    if request.method == 'OPTIONS':
        return ('', 204)
    zip_paths = [
        os.path.join(ROOT_DIR, "JamuClinician_AI_THEANA.zip"),
        os.path.join(ROOT_DIR, "static", "JamuClinician_AI_THEANA.zip")
    ]
    for zp in zip_paths:
        if os.path.exists(zp):
            return send_from_directory(os.path.dirname(zp), os.path.basename(zp), as_attachment=True)
    return "ZIP not found", 404

# Expose WSGI handler
handler = app
