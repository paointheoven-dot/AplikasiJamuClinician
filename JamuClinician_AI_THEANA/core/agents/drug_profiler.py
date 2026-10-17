"""Agent 2: Pharmacotherapy & Drug Profiler"""

class DrugProfilerAgent:
    def __init__(self):
        self.agent_name = "Agent 02 - Drug Profiler"

    def run(self, raw_drugs):
        analyzed_drugs = []
        for d in raw_drugs:
            d_clean = d.strip()
            if not d_clean:
                continue
            d_lower = d_clean.lower()
            pathway = "Sistemik Hepatik / Renal"
            if "metformin" in d_lower:
                pathway = "Substrat Transporter Kation Organik (OCT2) & Eliminasi Renal"
            elif "amlodip" in d_lower:
                pathway = "Metabolisme Sitokrom P450 Hepar (CYP3A4 Utama)"
            elif "allopurinol" in d_lower:
                pathway = "Inhibitor Xantin Oksidase (Metabolit Aloksantin Renal)"
            elif "statin" in d_lower or "atorvastatin" in d_lower:
                pathway = "Metabolisme CYP3A4 & Transporter Hepatosit OATP1B1"
            elif "captopril" in d_lower:
                pathway = "Inhibitor ACE & Klirens Ginjal"

            analyzed_drugs.append({
                "name": d_clean,
                "pathway": pathway
            })
        return analyzed_drugs
