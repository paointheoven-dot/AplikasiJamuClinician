"""Test Precision Jamu Formulator"""
import unittest
from core.agents.formulator import JamuFormulatorAgent

class TestFormulator(unittest.TestCase):
    def setUp(self):
        self.formulator = JamuFormulatorAgent()

    def test_gout_formula_generation(self):
        triage = {"comorbidities": ["Hiperurisemia / Gout"]}
        res = self.formulator.run(triage, "Jamu Asam Urat Sambiloto")
        self.assertIn("Sambiloto", res["formula_name"])
        self.assertEqual(len(res["items"]), 3)

    def test_standard_joint_formula(self):
        triage = {"comorbidities": ["Diabetes Tipe 2", "Hipertensi"]}
        res = self.formulator.run(triage, "Jamu Pegal Linu")
        self.assertIn("Temulawak", res["formula_name"])
        self.assertEqual(len(res["items"]), 3)

if __name__ == "__main__":
    unittest.main()
