"""Test HDI Matrix Detection"""
import unittest
from core.agents.hdi_auditor import HdiAuditorAgent

class TestHdiAuditor(unittest.TestCase):
    def setUp(self):
        self.auditor = HdiAuditorAgent()

    def test_metformin_synergy_detection(self):
        drugs = [{"name": "Metformin 500mg BID", "pathway": "OCT2"}]
        results = self.auditor.run(drugs, "Jamu Pegal Linu")
        self.assertEqual(len(results), 1)
        self.assertIn("MODERATE", results[0]["risk_level"])

    def test_amlodipine_cyp3a4_detection(self):
        drugs = [{"name": "Amlodipine 5mg QD", "pathway": "CYP3A4"}]
        results = self.auditor.run(drugs, "Jamu Pegal Linu")
        self.assertEqual(len(results), 1)
        self.assertIn("MILD", results[0]["risk_level"])

if __name__ == "__main__":
    unittest.main()
