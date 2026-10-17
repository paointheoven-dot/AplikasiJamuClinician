import unittest
import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from serve import call_gemini_api, call_gemini_nlp_extract, NoCacheHandler

class TestGeminiApiIntegration(unittest.TestCase):
    def test_missing_api_key_raises(self):
        with self.assertRaises(Exception):
            call_gemini_api("", {}, [])

    def test_knowledge_base_structure_in_html(self):
        index_path = os.path.join(ROOT_DIR, "index.html")
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("JAMU_KNOWLEDGE_BASE", content)
        self.assertIn("salam_gout", content)
        self.assertIn("kayumanis_diabetes", content)
        self.assertIn("seledri_hipertensi", content)
        self.assertIn("gastro", content)
        self.assertIn("pegal_linu", content)
        self.assertIn("renderAiClinicalResults", content)

    def test_zero_hardcoded_sambiloto_in_right_panel(self):
        index_path = os.path.join(ROOT_DIR, "index.html")
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        start = content.find('id="verdictJamuBox"')
        end = content.find('id="verdictJamuPillsRow"')
        box_snippet = content[start:end]
        self.assertNotIn("Jamu Sambiloto", box_snippet)

    def test_gemini_model_targeting_active_flash(self):
        with open(os.path.join(ROOT_DIR, "serve.py"), "r") as f:
            serve_code = f.read()
        self.assertIn('"gemini-3.5-flash"', serve_code)
        self.assertIn('call_gemini_nlp_extract', serve_code)

    def test_dual_mode_tabs_and_nlp_in_html(self):
        with open(os.path.join(ROOT_DIR, "index.html"), "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn('id="tabModeBtnStructured"', html)
        self.assertIn('id="tabModeBtnFreeText"', html)
        self.assertIn('id="modeFreeText"', html)
        self.assertIn('id="narrativeInput"', html)
        self.assertIn('id="btnNlpExtract"', html)
        self.assertIn('extractPatientNarrativeNLP', html)
        self.assertIn('id="nlpExtractionPreviewBox"', html)

    def test_precision_formulation_confidence_score_badge(self):
        with open(os.path.join(ROOT_DIR, "index.html"), "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn('id="precisionScoreBadge"', html)
        self.assertIn('CONFIDENCE', html)
        self.assertIn('id="precisionProgressBar"', html)

    def test_api_key_panel_and_gemini_status(self):
        with open(os.path.join(ROOT_DIR, "index.html"), "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn('id="panelGeminiIntegration"', html)
        self.assertIn('GEMINI_API_KEY', html)
        self.assertIn('/api/gemini-status', html)

    def test_static_js_app_logic(self):
        js_path = os.path.join(ROOT_DIR, "static", "js", "app.js")
        self.assertTrue(os.path.exists(js_path))
        with open(js_path, "r", encoding="utf-8") as f:
            js = f.read()
        self.assertGreater(len(js), 1000)
        self.assertIn("switchInputMode", js)
        self.assertIn("tabModeBtnFreeText", js)
        self.assertIn("modeFreeText", js)
        self.assertIn("/api/analyze", js)
        self.assertIn("precision_formulation", js)
        self.assertIn("confidence_score", js)
        self.assertIn("hdi_matrix_html", js)
        self.assertIn("chrono_schedule", js)

    def test_index_html_includes_app_js(self):
        index_path = os.path.join(ROOT_DIR, "index.html")
        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn('<script src="static/js/app.js"></script>', html)

    def test_serve_and_app_analyze_response_format(self):
        from serve import format_analyze_response, build_ebm_fallback
        patient = {
            "age": 54,
            "gender": "Wanita",
            "comorbidities": ["Diabetes Tipe 2", "Hipertensi"],
            "drugs": ["Metformin 500mg BID", "Amlodipine 5mg QD"],
            "complaints": ["Pegal Linu & Nyeri Otot"],
            "narrative": "Pasien wanita 54 tahun dengan diabetes tipe 2 dan hipertensi."
        }
        fallback = build_ebm_fallback(patient)
        formatted = format_analyze_response(fallback, patient)
        
        self.assertIn("precision_formulation", formatted)
        self.assertIn("confidence_score", formatted)
        self.assertIn("hdi_matrix_html", formatted)
        self.assertIn("chrono_schedule", formatted)
        self.assertTrue(formatted["confidence_score"].endswith("%"))
        self.assertIn("<tr", formatted["hdi_matrix_html"])
        self.assertIn("gap_rule", formatted["chrono_schedule"])

    def test_offline_lucide_suite(self):
        lucide_path = os.path.join(ROOT_DIR, "static", "js", "lucide.min.js")
        self.assertTrue(os.path.exists(lucide_path))
        with open(lucide_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("shield-plus", content)
        self.assertIn("moon", content)
        self.assertIn("printer", content)
        self.assertIn("createIcons", content)

        index_path = os.path.join(ROOT_DIR, "index.html")
        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()
        self.assertIn('<script src="static/js/lucide.min.js"></script>', html)

    def test_templates_index_html_and_tab_attributes(self):
        tmpl_path = os.path.join(ROOT_DIR, "templates", "index.html")
        self.assertTrue(os.path.exists(tmpl_path))
        with open(tmpl_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn('data-tab="cerita"', content)
        self.assertIn('data-tab="cepat"', content)
        self.assertIn('id="narrativeInput"', content)

    def test_app_js_tab_switching_and_payload(self):
        js_path = os.path.join(ROOT_DIR, "static", "js", "app.js")
        with open(js_path, "r", encoding="utf-8") as f:
            js = f.read()
        self.assertIn('data-tab="cerita"', js)
        self.assertIn('display = \'none\'', js)
        self.assertIn('obatMedis', js)
        self.assertIn('keluhanBebas', js)
        self.assertIn('komorbid', js)
        self.assertIn('apiKey', js)
        self.assertIn('/api/analyze', js)

    def test_backend_dynamic_configure_and_missing_key_check(self):
        expected_error = "Kunci API Gemini Belum Dimasukkan. Silakan masukkan API Key Anda di panel integrasi pojok kiri bawah."
        for path in [os.path.join(ROOT_DIR, "app.py"),
                     os.path.join(ROOT_DIR, "serve.py")]:
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()
            self.assertIn("google.generativeai", code)
            self.assertIn("configure", code)
            self.assertIn(expected_error, code)

    def test_mulai_analisis_kasus_and_gemini_api_key_storage(self):
        js_path = os.path.join(ROOT_DIR, "static", "js", "app.js")
        with open(js_path, "r", encoding="utf-8") as f:
            js = f.read()
        self.assertIn("mulaiAnalisisKasus", js)
        self.assertIn("GEMINI_API_KEY", js)
        self.assertIn("🟢 Terhubung", js)

    def test_dynamic_triage_by_checkboxes(self):
        from serve import build_ebm_fallback
        
        # Test 1: Hipertensi tanpa keluhan aktif (chronic fallback)
        res_hipertensi = build_ebm_fallback({
            "comorbidities": ["Hipertensi"],
            "drugs": ["Amlodipine 5mg"],
            "complaints": []
        })
        self.assertEqual(res_hipertensi["selectedJamuId"], "seledri_kumiskucing")
        self.assertGreater(len(res_hipertensi["ingredients"]), 0)
        self.assertGreater(len(res_hipertensi["brewingSteps"]), 0)

        # Test 2: Hipertensi dengan keluhan Lemas / Cepat Lelah (Keluhan aktif memandu pemilihan tonikum aman)
        res_lemas = build_ebm_fallback({
            "comorbidities": ["Hipertensi"],
            "drugs": ["Amlodipine 5mg"],
            "complaints": ["Lemas & Badan Cepat Lelah"]
        })
        self.assertEqual(res_lemas["selectedJamuId"], "beras_kencur")

        # Test 3: Kolesterol tanpa keluhan aktif
        res_kolesterol = build_ebm_fallback({
            "comorbidities": ["Dislipidemia"],
            "drugs": ["Simvastatin 20mg"],
            "complaints": []
        })
        self.assertEqual(res_kolesterol["selectedJamuId"], "jati_belanda")
        self.assertGreater(len(res_kolesterol["ingredients"]), 0)

        # Test 3: Gastritis / Maag
        res_maag = build_ebm_fallback({
            "comorbidities": ["Gastritis / Maag"],
            "drugs": [],
            "complaints": ["Kembung & Tidak Enak Perut"]
        })
        self.assertEqual(res_maag["selectedJamuId"], "kunyit_temulawak_gastro")
        self.assertGreater(len(res_maag["ingredients"]), 0)

        # Test 4: Batuk / Sesak
        res_batuk = build_ebm_fallback({
            "comorbidities": [],
            "drugs": [],
            "complaints": ["Sesak Napas & Batuk"]
        })
        self.assertEqual(res_batuk["selectedJamuId"], "asma_pernapasan")
        self.assertGreater(len(res_batuk["ingredients"]), 0)

    def test_extract_patient_nlp_rules_offline(self):
        from serve import extract_patient_nlp_rules
        res = extract_patient_nlp_rules("Pasien wanita 54 tahun punya riwayat hipertensi dan batuk kering.")
        self.assertEqual(res["gender"], "Wanita")
        self.assertEqual(res["age"], 54)
        self.assertIn("Hipertensi", res["comorbidities"])
        self.assertIn("Sesak Napas & Batuk", res["complaints"])

    def test_cerita_bebas_hierarchy_complaints_over_comorbidities(self):
        from serve import build_ebm_fallback, normalize_patient_payload

        # Case 1: Narrative with Hipertensi + Batuk -> MUST produce asma_pernapasan (Jahe Merah & Kencur)
        raw_payload_batuk = {
            "narrative": "Saya menderita hipertensi sudah 5 tahun dan rutin minum amlodipin 5mg. Tapi akhir-akhir ini dada sesak dan batuk berdahak tidak sembuh-sembuh."
        }
        patient_batuk = normalize_patient_payload(raw_payload_batuk)
        res_batuk = build_ebm_fallback(patient_batuk)
        self.assertEqual(res_batuk["selectedJamuId"], "asma_pernapasan", "Hipertensi + Batuk harus menghasilkan Jamu Jahe Merah & Kencur, bukan Seledri!")

        # Case 2: Narrative with Hipertensi + Lemas -> MUST produce beras_kencur (Beras Kencur)
        raw_payload_lemas = {
            "narrative": "Pasien pria 60 tahun dengan tensi tinggi minum amlodipin, saat ini merasa badan lemas sekali dan cepat lelah sehabis jalan sedikit."
        }
        patient_lemas = normalize_patient_payload(raw_payload_lemas)
        res_lemas = build_ebm_fallback(patient_lemas)
        self.assertEqual(res_lemas["selectedJamuId"], "beras_kencur", "Hipertensi + Lemas harus menghasilkan Jamu Beras Kencur, bukan Seledri!")

        # Case 3: Narrative with Hipertensi TANPA keluhan aktif -> MUST fallback to seledri_kumiskucing
        raw_payload_chronic = {
            "narrative": "Pasien berusia 55 tahun menderita hipertensi rutin minum amlodipin. Tidak ada keluhan khusus, ingin jamu untuk menjaga tekanan darah."
        }
        patient_chronic = normalize_patient_payload(raw_payload_chronic)
        res_chronic = build_ebm_fallback(patient_chronic)
        self.assertEqual(res_chronic["selectedJamuId"], "seledri_kumiskucing", "Hipertensi tanpa keluhan harus menghasilkan Jamu Seledri!")

if __name__ == '__main__':
    unittest.main()


