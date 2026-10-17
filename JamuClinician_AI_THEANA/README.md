# JAMUCLINICIAN AI — Clinical Pharmacognosy & Herb-Drug Interaction (HDI) Decision Engine

> **System Architecture:** Evidence-Based Multi-Agent Clinical Decision Support System (CDSS)  
> **UI Aesthetic:** Precision Clinical Telemetry Dashboard (Dual Mode: Clean Medical Light & Dark Obsidian)  
> **Core Engine:** Standalone Python Multi-Agent Backend (`app.py`) + Interactive Web Dashboard (`index.html`)

---

## 🌿 Gambaran Sistem (System Overview)

**JamuClinician AI** adalah platform pemecah studi kasus pasien dan sistem pendukung keputusan herbal klinis. Platform ini dirancang untuk menyelesaikan kasus polifarmasi pasien yang ingin mengonsumsi jamu tradisional di samping obat resep dokter, dengan fokus utama pada mitigasi risiko **Herb-Drug Interactions (HDI)** berbasis bukti ilmiah (*Evidence-Based Medicine* & Saintifikasi Jamu Kemenkes RI).

Tampilan aplikasi mengusung disiplin **Clinical Telemetry**:
* **Tema Default: Medical Clean Light** — Latar putih bersih dan abu-abu klinis yang sangat nyaman dibaca, dengan tombol toggle instan ke **Dark Obsidian Mode** jika diinginkan.
* **Tipografi Tabular Monospace** untuk dosis simplisia, nama enzim sitokrom (CYP450), dan timeline konsumsi 24 jam.
* **Format Split-View / Bento Grid**: Panel input kasus di sebelah kiri dan panel radar telemetri di sebelah kanan tanpa perlu reload halaman.

---

## ⚡ Fitur Utama

1. **Dual Input Mode:**
   * **Formulir Cepat:** Pemilihan Usia, Gender, Riwayat Komorbiditas, Daftar Obat Medis (bisa tambah/hapus), Keluhan, dan Pilihan Jamu.
   * **Narasi Studi Kasus:** Kotak teks bebas untuk memasukkan narasi kasus klinis secara natural.
   * **1-Click Clinical Benchmarks:** Tombol kasus terstandar untuk demonstrasi instan (#1 DM2 + Hipertensi, #2 Gout & Gastritis, #3 Statin + Dislipidemia, #4 Lansia Polifarmasi).

2. **Herb-Drug Interaction (HDI) Telemetry Matrix:**
   * Audit farmakokinetika dan farmakodinamika obat kimia vs fitokimia jamu (enzim CYP3A4, transporter OCT2, dll.) dengan klasifikasi risiko klinis.

3. **Formulasi Jamu Presisi (Kaidah Saintifikasi Jamu):**
   * Peracikan terstruktur: *Remedium Cardinale*, *Adjuvans*, dan *Corrigens* dengan takaran gram terstandar dan zat aktif target.

4. **SOP Ekstraksi & Galenika Rumah Tangga:**
   * Metode Infusa 90°C selama 15 menit dan peringatan wajib: dilarang memakai panci aluminium/besi, wajib wadah tanah liat/kaca borosilikat/enamel.

5. **24-Hour Chronopharmacology Regimen:**
   * Garis waktu visual yang menjamin jarak aman (jeda &ge; 2.5 jam) antara konsumsi obat dokter dan jamu.

6. **Salinan Resep Klinis (R/ Sheet):**
   * Lembar resep resmi yang ramah cetak (*print-ready*) dan dapat disalin dalam 1 klik.

---

## 🚀 Cara Menjalankan

### Cara 1: Menjalankan via Python (`app.py`)
Di terminal/command prompt:
```bash
# Jalankan web server lokal
python3 app.py

# Atau tentukan port khusus:
python3 app.py --port 8080

# Atau uji coba langsung di terminal (Mode CLI):
python3 app.py --cli --case "Pasien wanita 54 tahun, DM2 dan Hipertensi, minum Metformin dan Amlodipin"
```
Buka browser pada: **http://localhost:8080**

### Cara 2: Menjalankan Langsung Tanpa Terminal
Cukup klik dua kali file **`index.html`** di peramban apa pun (Chrome, Safari, Edge, Firefox). Seluruh fungsi dan kalkulasi interaksi langsung aktif 100%.

---

## 📚 Landasan Bukti Ilmiah (References)
* Farmakope Herbal Indonesia (FHI) Edisi VI, Kementerian Kesehatan RI.
* Formularium Ramuan Obat Tradisional Indonesia (FORMI).
* Stockley’s Herbal Medicines Interactions.
* WHO Monographs on Selected Medicinal Plants.
