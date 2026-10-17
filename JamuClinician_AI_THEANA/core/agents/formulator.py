"""Agent 4: Evidence-Based Jamu Formulator"""

class JamuFormulatorAgent:
    def __init__(self):
        self.agent_name = "Agent 04 - Jamu Formulator"

    def run(self, triage_data, target_jamu):
        comorb = triage_data.get("comorbidities", [])
        is_gout = any("gout" in c.lower() or "asam urat" in c.lower() for c in comorb)

        if is_gout or "Asam Urat" in target_jamu:
            formula_name = "Formulasi Urikosurik Sambiloto & Kumis Kucing Terstandar"
            items = [
                {"role": "REMEDIUM CARDINALE", "name": "Sambiloto (Andrographis paniculata)", "dose": "5 g (Simplisia Kering)", "kitchen": "1 sdm simplisia kering", "active": "Andrographolide (Urikosurik & Antiinflamasi)"},
                {"role": "REMEDIUM ADJUVANS", "name": "Kumis Kucing (Orthosiphon stamineus)", "dose": "7 g (Daun Segar)", "kitchen": "1 genggam kecil daun segar", "active": "Sinensetin (Diuresis Kristal Asam Urat)"},
                {"role": "REMEDIUM CORRIGENS", "name": "Kayu Manis (Cinnamomum burmannii)", "dose": "3 g (Kulit Batang)", "kitchen": "1 ruas jari kulit kayu", "active": "Cinnamaldehyde (Penyelaras Rasa & Glukosa)"}
            ]
            rationality = "Formula kombinasi Sambiloto dan Kumis Kucing bekerja ganda: menghambat sintesis asam urat sekaligus memperlancar ekskresi ginjal secara alami."
        else:
            formula_name = "Formulasi Temulawak-Jahe Merah (Safe Anti-Inflammatory Blend)"
            items = [
                {"role": "REMEDIUM CARDINALE", "name": "Temulawak (Curcuma xanthorrhiza)", "dose": "15 g (Rimpang Segar Cuci Bersih)", "kitchen": "1 potong seukuran ibu jari", "active": "Kurkuminoid & Xanthorrhizol (Antiinflamasi & Hepatoprotektor)"},
                {"role": "REMEDIUM ADJUVANS", "name": "Jahe Merah (Zingiber officinale rubrum)", "dose": "10 g (Rimpang Memar)", "kitchen": "1 ruas jari tangan sedang", "active": "6-Gingerol & Shogaol (Analgesik & Relaksan Otot)"},
                {"role": "REMEDIUM CORRIGENS", "name": "Serai (Cymbopogon citratus)", "dose": "5 g (Batang Bagian Putih)", "kitchen": "1 batang bagian putih", "active": "Sitral (Spasmolitik & Aroma Penenang)"}
            ]
            rationality = "Kombinasi Temulawak dan Jahe Merah menekan mediator pro-inflamasi (COX-2) meredakan pegal linu dan sendi kaku tanpa risiko iritasi lambung."

        return {
            "formula_name": formula_name,
            "items": items,
            "rationality": rationality
        }
