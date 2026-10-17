"""
Clinical Multi-Agent Orchestration Pipeline
"""
from core.agents import (
    ClinicalTriageAgent,
    DrugProfilerAgent,
    HdiAuditorAgent,
    JamuFormulatorAgent,
    GalenicalExtractionAgent,
    ChronoDosingAgent,
    ChiefPharmacistSynthesizer
)

class ClinicalPipeline:
    def __init__(self):
        self.triage_agent = ClinicalTriageAgent()
        self.drug_profiler = DrugProfilerAgent()
        self.hdi_auditor = HdiAuditorAgent()
        self.formulator = JamuFormulatorAgent()
        self.galenical = GalenicalExtractionAgent()
        self.chrono_scheduler = ChronoDosingAgent()
        self.synthesizer = ChiefPharmacistSynthesizer()

    def process(self, case_payload):
        triage = self.triage_agent.run(case_payload)
        drugs = self.drug_profiler.run(case_payload.get("drugs", ["Metformin 500mg BID", "Amlodipine 5mg QD"]))
        target_jamu = case_payload.get("targetJamu", "Jamu Pegal Linu / Kunyit Asam")
        hdi = self.hdi_auditor.run(drugs, target_jamu)
        formula = self.formulator.run(triage, target_jamu)
        galenical = self.galenical.run()
        chrono = self.chrono_scheduler.run(drugs)
        prescription = self.synthesizer.run(triage, drugs, hdi, formula, galenical, chrono)

        return {
            "status": "SUCCESS",
            "triage": triage,
            "drugs": drugs,
            "hdi_matrix": hdi,
            "formula": formula,
            "galenical": galenical,
            "chronopharmacology": chrono,
            "prescription": prescription
        }
