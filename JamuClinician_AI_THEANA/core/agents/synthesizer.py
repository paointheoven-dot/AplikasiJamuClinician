"""Agent 7 & 8: Chief Pharmacist Synthesizer (R/ Generator)"""
from datetime import datetime

class ChiefPharmacistSynthesizer:
    def __init__(self):
        self.agent_name = "Agent 07 & 08 - Chief Pharmacist Synthesizer"

    def run(self, triage, drugs, hdi, formula, galenical, chrono):
        date_str = datetime.now().strftime("%d %B %Y")
        drugs_str = ", ".join([d["name"] for d in drugs])
        
        rx_sheet = f"""========================================================================
LEMBAR REKOMENDASI TERAPI JAMU KLINIS & SALINAN RESEP (R/)
Konsultan: Spesialis Saintifikasi Jamu Klinis & Farmakologi Herbal
Tanggal: {date_str}
========================================================================

PRO: Pasien ({triage['age']} Thn, {triage['gender']})
KOMORBID: {', '.join(triage['comorbidities'])}
OBAT RUTIN: {drugs_str}

R/ {formula['items'][0]['name']} {formula['items'][0]['dose']}
   {formula['items'][1]['name']} {formula['items'][1]['dose']}
   {formula['items'][2]['name']} {formula['items'][2]['dose']}
   Aqua destilata ad 300 ml
   m.f. infusa in vaso fictili (wadah tanah liat/kaca) ad 150 ml

S. 1 d. d. c. 1 (Diminum 1 kali sehari 1 cangkir hangat pada pk 09:30)

§ ATURAN KONSULTASI KLINIS:
1. ATURAN JEDA WAKTU: Wajib beri jarak minimal 2.5 jam setelah obat dokter.
2. ATURAN WADAH: Dilarang menggunakan panci aluminium/besi.
3. MONITORING: Hentikan konsumsi jika muncul tanda hipoglikemia (keringat dingin, gemetar).
========================================================================"""
        return rx_sheet
