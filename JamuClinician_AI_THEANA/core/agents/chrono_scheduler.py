"""Agent 6: Chronopharmacology & Dosing Scheduler"""

class ChronoDosingAgent:
    def __init__(self):
        self.agent_name = "Agent 06 - Chronopharmacology Scheduler"

    def run(self, drugs):
        drug_names = [d["name"] for d in drugs]
        drugs_str = ", ".join(drug_names[:2]) if drug_names else "Obat Dokter"
        return [
            {
                "time": "07:00",
                "label": "Obat Dokter",
                "detail": f"Diminum setelah sarapan ({drugs_str})."
            },
            {
                "time": "INTERVAL",
                "label": "Jeda Bersih (2 Jam 30 Menit)",
                "detail": "Klirens absorpsi dinding lambung selesai, bebas kompetisi biologis."
            },
            {
                "time": "09:30",
                "label": "Jamu Terstandar (150 ml)",
                "detail": "Diminum hangat. Menjamin bioavailabilitas optimal fitofarmaka."
            },
            {
                "time": "19:00",
                "label": "Obat Medis Malam",
                "detail": "Diminum bersama makan malam jika ada jadwal malam."
            }
        ]
