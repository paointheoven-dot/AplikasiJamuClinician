"""Agent 1: Clinical Triage & Patient Phenotyper"""

class ClinicalTriageAgent:
    def __init__(self):
        self.agent_name = "Agent 01 - Clinical Triage"

    def run(self, raw_input):
        age = raw_input.get("age", 54)
        gender = raw_input.get("gender", "Wanita")
        comorbidities = raw_input.get("comorbidities", ["Diabetes Tipe 2", "Hipertensi"])
        complaints = raw_input.get("complaints", ["Pegal Linu & Nyeri Otot", "Kekakuan Sendi Pagi Hari"])

        contraindications = []
        if "Wanita Hamil" in gender:
            contraindications.append("Peringatan Kehamilan: Simplisia bersifat emenagoga atau stimulan rahim dilarang keras.")
        if "Gangguan Fungsi Ginjal" in comorbidities:
            contraindications.append("Penurunan Klirens Ginjal: Batasi volume kalium simplisia, gunakan pelarut terukur.")

        return {
            "age": age,
            "gender": gender,
            "comorbidities": comorbidities,
            "complaints": complaints,
            "contraindications": contraindications,
            "summary": f"Pasien {age} thn, {gender} | Komorbid: {', '.join(comorbidities)}"
        }
