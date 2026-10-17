#!/usr/bin/env python3
"""
JamuClinician AI — Clinical Pharmacognosy & Herb-Drug Interaction (HDI) Decision Engine
Author: THEANA (Clinical Pharmacist Specialist)
Version: 3.0.0 (Pure Gemini 1.5 Flash Dynamic Engine)

Arsitektur: Multi-Agent Clinical Decision Support System (CDSS)
Server Flask & Standalone Python Engine terintegrasi secara murni ke Gemini 1.5 Flash.
"""

import os
import sys
import json
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

# ==============================================================================
# SECRET ENVIRONMENT CONFIGURATION (LOAD FROM .env)
# ==============================================================================
def load_env():
    """Load environment variables from .env file into os.environ."""
    env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(env_file):
        try:
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        if k and k not in os.environ:
                            os.environ[k] = v
        except Exception:
            pass

load_env()

MISSING_KEY_ERROR = "Kunci API Gemini Belum Dimasukkan. Silakan masukkan API Key Anda di panel integrasi pojok kiri bawah."

def get_server_api_key(payload=None):
    """Retrieve Gemini API Key from request payload or .env (os.getenv)."""
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

# Import core reasoning engine from serve.py
try:
    from serve import (
        call_gemini_api,
        call_gemini_nlp_extract,
        extract_patient_nlp_rules,
        build_ebm_fallback,
        format_analyze_response
    )
except ImportError:
    pass

# Try importing Google Generative AI for dynamic configuration
try:
    import google.generativeai as genai
except ImportError:
    genai = None

# ==============================================================================
# UNIFIED PATIENT DATA NORMALIZER (FORMULIR CEPAT & CERITA BEBAS)
# ==============================================================================
def normalize_patient_payload(payload):
    """
    Menyelaraskan struktur data pasien dari Formulir Cepat (checkbox/dropdown)
    maupun Cerita Bebas Pasien ke dalam satu format objek JSON terstandar
    sebelum diserahkan secara murni ke call_gemini_api.
    """
    raw = payload.get("patient") if isinstance(payload.get("patient"), dict) else payload
    if not isinstance(raw, dict):
        raw = {}

    narrative = str(
        raw.get("narrative") or 
        payload.get("narrative") or 
        raw.get("keluhanBebas") or 
        payload.get("keluhanBebas") or 
        raw.get("story") or 
        payload.get("story") or 
        raw.get("text") or 
        payload.get("text") or 
        raw.get("case") or 
        payload.get("case") or 
        ""
    ).strip()

    complaints = raw.get("complaints") or payload.get("complaints") or []
    if isinstance(complaints, str):
        complaints = [c.strip() for c in complaints.split(",") if c.strip()]
    elif not isinstance(complaints, list):
        complaints = []

    if not complaints and narrative:
        complaints = [narrative]

    comorbidities = raw.get("comorbidities") or raw.get("komorbid") or payload.get("comorbidities") or payload.get("komorbid") or []
    if isinstance(comorbidities, str):
        comorbidities = [c.strip() for c in comorbidities.split(",") if c.strip()]
    elif not isinstance(comorbidities, list):
        comorbidities = []

    drugs = raw.get("drugs") or raw.get("obatMedis") or payload.get("drugs") or payload.get("obatMedis") or []
    if isinstance(drugs, str):
        drugs = [d.strip() for d in drugs.split(",") if d.strip()]
    elif not isinstance(drugs, list):
        drugs = []

    age = raw.get("age") or raw.get("usia") or payload.get("age") or payload.get("usia") or 50
    try:
        age = int(age)
    except (ValueError, TypeError):
        age = 50

    gender = raw.get("gender") or payload.get("gender") or "Pria"
    preferred = raw.get("preferredJamu") or raw.get("targetJamu") or payload.get("preferredJamu") or payload.get("targetJamu") or "Formulasi Klinis Teroptimasi"

    return {
        "age": age,
        "gender": str(gender),
        "comorbidities": comorbidities,
        "drugs": drugs,
        "complaints": complaints,
        "preferredJamu": str(preferred),
        "narrative": narrative
    }

# ==============================================================================
# FLASK WEB SERVER (JIKA FLASK TERPASANG DI SISTEM DOSEN / PENGUJI)
# ==============================================================================
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Import top-level Flask application instance from api.index
from api.index import app
has_flask = True


# ==============================================================================
# STANDALONE HTTP SERVER (ZERO-DEPENDENCY PURE GEMINI 1.5 FLASH ENGINE)
# ==============================================================================
class JamuApiServer(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_GET(self):
        if self.path in ("/", "", "/index.html"):
            tmpl_file = os.path.join(DIRECTORY, "templates", "index.html")
            if not os.path.exists(tmpl_file):
                tmpl_file = os.path.join(DIRECTORY, "index.html")
            if os.path.exists(tmpl_file):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                with open(tmpl_file, 'rb') as f:
                    self.wfile.write(f.read())
                return

        if self.path in ("/JamuClinician_AI_THEANA.zip", "/download-zip", "/download"):
            zip_paths = [
                os.path.join(DIRECTORY, "JamuClinician_AI_THEANA.zip"),
                os.path.join(DIRECTORY, "static", "JamuClinician_AI_THEANA.zip")
            ]
            for zp in zip_paths:
                if os.path.exists(zp):
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/zip')
                    self.send_header('Content-Disposition', 'attachment; filename="JamuClinician_AI_THEANA.zip"')
                    self.send_header('Content-Length', str(os.path.getsize(zp)))
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    with open(zp, 'rb') as f:
                        self.wfile.write(f.read())
                    return

        if self.path == "/api/gemini-status":
            env_key = get_server_api_key()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({
                "hasServerKey": bool(env_key),
                "model": "gemini-1.5-flash",
                "maskedKey": (env_key[:6] + "..." + env_key[-4:]) if env_key else ""
            }).encode('utf-8'))
            return

        super().do_GET()

    def do_POST(self):
        if self.path == "/api/gemini-nlp-extract":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            try:
                body = json.loads(post_data) if post_data else {}
                narrative = (
                    body.get("narrative") or 
                    body.get("keluhanBebas") or 
                    body.get("story") or 
                    body.get("text") or 
                    body.get("case") or 
                    ""
                ).strip()

                api_key = get_server_api_key(body)

                if not api_key:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        "success": False,
                        "error": MISSING_KEY_ERROR,
                        "requiresKey": True
                    }).encode('utf-8'))
                    return

                if not narrative:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        "success": False,
                        "error": "Teks keluhan/narasi pasien tidak boleh kosong."
                    }).encode('utf-8'))
                    return

                if genai:
                    try:
                        genai.configure(api_key=api_key)
                    except Exception:
                        pass

                extracted = call_gemini_nlp_extract(api_key, narrative)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": True,
                    "data": extracted
                }, ensure_ascii=False).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": False,
                    "error": f"Ekstraksi NLP Gemini 1.5 Flash gagal: {str(e)}"
                }).encode('utf-8'))
            return

        if self.path in ("/api/analyze", "/api/gemini-analyze"):
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            try:
                payload = json.loads(post_data) if post_data else {}
                patient = normalize_patient_payload(payload)
                knowledge_base = payload.get("knowledgeBase") or []
                api_key = get_server_api_key(payload)

                if not api_key:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        "success": False,
                        "error": MISSING_KEY_ERROR,
                        "requiresKey": True
                    }).encode('utf-8'))
                    return

                if genai:
                    try:
                        genai.configure(api_key=api_key)
                    except Exception:
                        pass

                result = call_gemini_api(api_key, patient, knowledge_base)
                formatted = format_analyze_response(result, patient)
                formatted["success"] = True
                formatted["data"] = dict(formatted)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(formatted, ensure_ascii=False, indent=2).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": False,
                    "error": f"Analisis Klinis Gemini 1.5 Flash gagal: {str(e)}"
                }).encode('utf-8'))
            return

        super().do_POST()

def start_server(port=8080):
    """Start standalone server (or Flask if available)."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, JamuApiServer)
    print(f"JamuClinician AI Server running on port {port} (Pure Gemini 1.5 Flash)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down JamuClinician AI server.")
        httpd.server_close()

def main():
    parser = argparse.ArgumentParser(description="JamuClinician AI CDSS Server")
    parser.add_argument("--port", type=int, default=8080, help="Port to listen on")
    parser.add_argument("--flask", action="store_true", help="Force Flask server mode")
    args = parser.parse_args()

    if args.flask and has_flask and app:
        print(f"Starting Flask server on port {args.port}...")
        app.run(host="0.0.0.0", port=args.port, debug=False)
    else:
        start_server(args.port)

if __name__ == '__main__':
    main()
