"""Agent 3: Herb-Drug Interaction (HDI) Auditor"""
from core.database.cyp450_matrix import CYP_INTERACTION_RULES

class HdiAuditorAgent:
    def __init__(self):
        self.agent_name = "Agent 03 - HDI Auditor"

    def run(self, drugs, target_jamu):
        hdi_results = []
        for drug in drugs:
            drug_name_lower = drug["name"].lower()
            matched = False
            for rule in CYP_INTERACTION_RULES:
                if rule["keyword"] in drug_name_lower:
                    hdi_results.append({
                        "drug": drug["name"],
                        "herb_compound": rule["phytochemical"],
                        "risk_level": rule["risk_level"],
                        "level_code": rule["level_type"],
                        "pathway": rule["pathway"],
                        "mechanism": rule["mechanism"],
                        "recommendation": rule["clinical_action"]
                    })
                    matched = True
                    break
            if not matched:
                hdi_results.append({
                    "drug": drug["name"],
                    "herb_compound": "Fitokonstituen Terstandar",
                    "risk_level": "SAFE (Jeda 2.5 Jam)",
                    "level_code": "safe",
                    "pathway": "Metabolisme Hepatik Standar",
                    "mechanism": "Tidak ditemukan interaksi toksik mayor. Terapkan jeda waktu 2.5 jam.",
                    "recommendation": "Boleh dikonsumsi dengan jeda waktu minum terstandar."
                })
        return hdi_results
