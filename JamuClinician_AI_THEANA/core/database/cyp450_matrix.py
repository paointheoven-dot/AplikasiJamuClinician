"""
Cytochrome P450 (CYP450) & Transporter Interaction Matrix (Extended Clinical Edition)
Reference: Stockley's Herbal Medicines Interactions, Farmakope Indonesia VI, & AHFS Drug Information
"""

CYP_INTERACTION_RULES = [
    # 1. ANTIDIABETIK
    {
        "keyword": "metformin",
        "official_name": "Metformin",
        "phytochemical": "Kurkuminoid (Temulawak/Kunyit)",
        "risk_level": "MODERATE (Waspada Sinergis)",
        "level_type": "warning",
        "pathway": "AMPK Activation & OCT2 Transporter",
        "mechanism": "Kurkuminoid menstimulasi ekspresi GLUT4 & AMPK, menurunkan glukosa darah secara sinergis dengan Metformin.",
        "clinical_action": "Boleh diminum. Beri jeda 2.5 jam setelah Metformin dan pantau tanda hipoglikemia (keringat dingin/gemetar)."
    },
    {
        "keyword": "glimepirid",
        "official_name": "Glimepiride / Sulfonilurea",
        "phytochemical": "Kurkuminoid & Gingerol",
        "risk_level": "MODERATE (Risiko Hipoglikemia)",
        "level_type": "warning",
        "pathway": "CYP2C9 Substrat & Sekresi Insulin",
        "mechanism": "Kurkuminoid menghambat ringan CYP2C9, berpotensi meningkatkan kadar glimepiride plasma dan memicu hipoglikemia.",
        "clinical_action": "Gunakan dosis jamu rendah, pisahkan jadwal minum minimal 3 jam, monitor gula darah berkala."
    },
    {
        "keyword": "glibenclamid",
        "official_name": "Glibenclamide",
        "phytochemical": "Kurkuminoid",
        "risk_level": "MODERATE (Risiko Hipoglikemia)",
        "level_type": "warning",
        "pathway": "CYP2C9 Metabolisme",
        "mechanism": "Efek ganda hipoglikemik herbal dan sulfonilurea generasi lama. Risiko hipoglikemia berkepanjangan.",
        "clinical_action": "Konsultasikan penyesuaian dosis obat dengan dokter dan beri jeda waktu ketat."
    },
    {
        "keyword": "insulin",
        "official_name": "Insulin (Lantus / Novorapid)",
        "phytochemical": "Fitokonstituen Jamu",
        "risk_level": "MODERATE (Sinergis Glukosa)",
        "level_type": "warning",
        "pathway": "Sensitivitas Reseptor Insulin",
        "mechanism": "Senyawa rimpang meningkatkan sensitivitas insulin perifer, memperkuat respon penurunan glukosa darah.",
        "clinical_action": "Aman diminum dengan jeda 2 jam, selalu siapkan permen/air gula jika timbul gejala lemas gemetar."
    },
    {
        "keyword": "empagliflozin",
        "official_name": "Empagliflozin / Dapagliflozin (SGLT-2)",
        "phytochemical": "Flavonoid & Diuretik Alami",
        "risk_level": "MILD (Hidrasi Wajib)",
        "level_type": "safe",
        "pathway": "Glukosuria Renal & Eliminasi Glukosa",
        "mechanism": "Kombinasi dengan jamu bersifat diuretik ringan (seperti kumis kucing) meningkatkan volume urin.",
        "clinical_action": "Cukupi hidrasi air putih minimal 2.5 liter per hari untuk mencegah dehidrasi."
    },

    # 2. ANTIHIPERTENSI & KARDIOVASKULAR
    {
        "keyword": "amlodip",
        "official_name": "Amlodipine (CCB)",
        "phytochemical": "Gingerol & Kurkumin",
        "risk_level": "MILD (Jeda Waktu)",
        "level_type": "safe",
        "pathway": "CYP3A4 Metabolism & Ca2+ Channel",
        "mechanism": "Amlodipin dimetabolisme oleh CYP3A4 di hati. Ekstrak rimpang memiliki potensi inhibisi ringan terhadap CYP3A4.",
        "clinical_action": "Boleh diminum dengan protokol jeda waktu minum minimal 2.5 jam. Pantau tekanan darah."
    },
    {
        "keyword": "nifedipin",
        "official_name": "Nifedipine",
        "phytochemical": "Kurkuminoid",
        "risk_level": "MILD-MODERATE",
        "level_type": "warning",
        "pathway": "CYP3A4 First-Pass Clearance",
        "mechanism": "Inhibisi CYP3A4 usus oleh kurkuminoid dosis tinggi dapat meningkatkan bioavailabilitas nifedipin.",
        "clinical_action": "Beri jeda waktu minum 3 jam untuk mencegah lonjakan vasodilatasi mendadak."
    },
    {
        "keyword": "captopril",
        "official_name": "Captopril (ACE-Inhibitor)",
        "phytochemical": "Kurkuminoid & Gingerol",
        "risk_level": "SAFE (Sinergis Positif)",
        "level_type": "safe",
        "pathway": "Renin-Angiotensin System & Vasodilatasi",
        "mechanism": "Efek relaksan pembuluh darah alami dari rimpang mendukung kerja captopril tanpa interaksi toksik.",
        "clinical_action": "Aman dikonsumsi dengan jeda waktu minum standar 2.5 jam setelah obat dokter."
    },
    {
        "keyword": "candesartan",
        "official_name": "Candesartan / Valsartan (ARB)",
        "phytochemical": "Kurkuminoid",
        "risk_level": "SAFE (Jeda Waktu Standar)",
        "level_type": "safe",
        "pathway": "Reseptor AT1 Angiotensin II",
        "mechanism": "Tidak ditemukan interaksi farmakokinetik mayor. Mendukung kontrol tensi yang stabil.",
        "clinical_action": "Boleh dikonsumsi berdampingan dengan jeda waktu 2-3 jam."
    },
    {
        "keyword": "bisoprolol",
        "official_name": "Bisoprolol / Beta-Blocker",
        "phytochemical": "Zingiberen & Kurkuminoid",
        "risk_level": "MILD (Pantau Denyut Nadi)",
        "level_type": "safe",
        "pathway": "CYP2D6 & Reseptor Beta-1 Adrenergik",
        "mechanism": "Ekstrak jahe hangat menyeimbangkan sirkulasi perifer tanpa mengganggu efek modulasi nodus SA bisoprolol.",
        "clinical_action": "Aman diminum dengan jeda 2.5 jam. Pantau denyut nadi tetap di atas 60 bpm."
    },
    {
        "keyword": "furosemid",
        "official_name": "Furosemide / Diuretik Kuat",
        "phytochemical": "Kumis Kucing / Orthosiphon",
        "risk_level": "MODERATE (Risiko Hipokalemia)",
        "level_type": "warning",
        "pathway": "Kotranporter Na-K-2Cl Loop Henle",
        "mechanism": "Penggabungan furosemid dengan simplisia diuretik kuat melipatgandakan ekskresi cairan & elektrolit.",
        "clinical_action": "Hindari simplisia kumis kucing dosis tinggi bersamaan furosemid; ganti dengan temulawak/jahe biasa."
    },

    # 3. ANTILIPIDEMIA (KOLESTEROL)
    {
        "keyword": "atorvastatin",
        "official_name": "Atorvastatin (Statin)",
        "phytochemical": "Kurkuminoid & Allicin",
        "risk_level": "MILD-MODERATE (Jeda Pagi-Malam)",
        "level_type": "warning",
        "pathway": "CYP3A4 & OATP1B1 Transporter Hepar",
        "mechanism": "Mencegah kompetisi enzim CYP3A4 di hepar dengan memisahkan konsumsi pagi vs malam.",
        "clinical_action": "Aman jika diminum terpisah: jamu di pagi hari (pk 09:30), atorvastatin di malam hari sebelum tidur (pk 21:00)."
    },
    {
        "keyword": "simvastatin",
        "official_name": "Simvastatin",
        "phytochemical": "Kurkuminoid",
        "risk_level": "MODERATE (Jeda Pagi-Malam Wajib)",
        "level_type": "warning",
        "pathway": "CYP3A4 Substrat Sensitif",
        "mechanism": "Simvastatin sangat bergantung pada CYP3A4. Jamu harus dipisah minimal 8-10 jam (minum malam).",
        "clinical_action": "Wajib beri jarak: jamu pagi hari, simvastatin malam hari sebelum tidur."
    },
    {
        "keyword": "rosuvastatin",
        "official_name": "Rosuvastatin",
        "phytochemical": "Kurkuminoid",
        "risk_level": "SAFE (Jeda 2.5 Jam)",
        "level_type": "safe",
        "pathway": "CYP2C9 Minor / BCRP Transporter",
        "mechanism": "Rosuvastatin tidak dimetabolisme oleh CYP3A4 sehingga risiko interaksinya jauh lebih rendah dibanding simvastatin.",
        "clinical_action": "Aman diminum dengan jeda standar 2.5 jam."
    },
    {
        "keyword": "fenofibrat",
        "official_name": "Fenofibrate (Trigliserida)",
        "phytochemical": "Kurkuminoid & Gingerol",
        "risk_level": "SAFE (Sinergis Positif)",
        "level_type": "safe",
        "pathway": "Aktivasi PPAR-alpha",
        "mechanism": "Kurkuminoid dan fenofibrat saling mendukung dalam menurunkan trigliserida dan melindungi hepar.",
        "clinical_action": "Kombinasi aman. Beri jeda waktu minum 2.5 jam."
    },

    # 4. DARAH, ANTIPLATELET & ANTIKOAGULAN (KRUSIAL!)
    {
        "keyword": "aspilet",
        "official_name": "Aspilet / Aspirin Dosis Rendah",
        "phytochemical": "Gingerol & Kurkumin",
        "risk_level": "MODERATE (Waspada Agregasi Trombosit)",
        "level_type": "warning",
        "pathway": "Inhibisi Tromboksan A2 (TXA2)",
        "mechanism": "Kandungan jahe dan kunyit memiliki efek antitrombotik alami ringan yang menambah efek pengenceran darah.",
        "clinical_action": "Boleh diminum jika dosis jamu normal (1 cangkir/hari), hindari konsumsi ekstrak pekat, pantau jika muncul lebam."
    },
    {
        "keyword": "clopidogrel",
        "official_name": "Clopidogrel (Plavix)",
        "phytochemical": "Kurkuminoid & Gingerol",
        "risk_level": "MODERATE (Antiplatelet Ganda)",
        "level_type": "warning",
        "pathway": "Reseptor P2Y12 & CYP2C19",
        "mechanism": "Ekstrak rimpang dalam dosis tinggi berpotensi menambah waktu perdarahan jika digabung antiplatelet kuat.",
        "clinical_action": "Konsumsi dalam takaran encer terstandar, hindari konsumsi bersamaan, laporkan bila ada gusi berdarah."
    },
    {
        "keyword": "warfarin",
        "official_name": "Warfarin",
        "phytochemical": "Kurkuminoid",
        "risk_level": "HIGH RISK / KONTRAINDIKASI RELATIF",
        "level_type": "danger",
        "pathway": "CYP2C9 & Faktor Pembekuan Vitamin K",
        "mechanism": "Kurkumin menghambat CYP2C9 yang memetabolisme S-warfarin, berpotensi menaikkan nilai INR dan risiko perdarahan hebat.",
        "clinical_action": "KONTRAINDIKASI: Sangat disarankan TIDAK mengonsumsi jamu rimpang pekat saat terapi warfarin aktif."
    },

    # 5. ANALGESIK & ANTIINFLAMASI (NSAID & GOUT)
    {
        "keyword": "meloxicam",
        "official_name": "Meloxicam (NSAID)",
        "phytochemical": "Gingerol & Ekstrak Asam",
        "risk_level": "KONTRAINDIKASI BERSAMAAN",
        "level_type": "danger",
        "pathway": "Inhibisi COX-2 & Mukosa Lambung",
        "mechanism": "Kombinasi obat kimia NSAID dengan ramuan rimpang pedas/asam secara bersamaan melipatgandakan iritasi lambung.",
        "clinical_action": "Jangan diminum bersamaan. Hentikan NSAID jika gejala nyeri telah teratasi oleh jamu."
    },
    {
        "keyword": "ibuprofen",
        "official_name": "Ibuprofen / Asam Mefenamat",
        "phytochemical": "Gingerol & Kurkumin",
        "risk_level": "KONTRAINDIKASI BERSAMAAN",
        "level_type": "danger",
        "pathway": "Inhibisi COX-1 / Prostaglandin Lambung",
        "mechanism": "Kombinasi NSAID non-selektif bersamaan jamu meningkatkan risiko erosi lambung dan dispepsia.",
        "clinical_action": "Pisahkan jadwal atau hentikan NSAID. Utamakan temulawak pelindung lambung."
    },
    {
        "keyword": "diklofenak",
        "official_name": "Natrium / Kalium Diklofenak",
        "phytochemical": "Kurkuminoid & Gingerol",
        "risk_level": "KONTRAINDIKASI BERSAMAAN",
        "level_type": "danger",
        "pathway": "Inhibisi Sintesis Prostaglandin",
        "mechanism": "Beban hepatik ganda dan risiko tukak lambung jika dikonsumsi berbarengan.",
        "clinical_action": "Hindari konsumsi bersamaan. Prioritaskan salah satu terapi antiinflamasi."
    },
    {
        "keyword": "allopurinol",
        "official_name": "Allopurinol 100mg",
        "phytochemical": "Andrographolide (Sambiloto)",
        "risk_level": "SINERGIS POSITIF",
        "level_type": "safe",
        "pathway": "Xanthine Oxidase & Renal Excretion",
        "mechanism": "Andrographolide bekerja sebagai urikosurik alami membantu mempercepat ekskresi asam urat bersama Allopurinol.",
        "clinical_action": "Kombinasi rasional aman. Pastikan hidrasi air putih minimal 2 liter per hari."
    },
    {
        "keyword": "kolkisin",
        "official_name": "Kolkisin / Colchicine",
        "phytochemical": "Andrographolide & Sinensetin",
        "risk_level": "MILD-MODERATE",
        "level_type": "warning",
        "pathway": "P-glikoprotein & Klirens Renal",
        "mechanism": "Kolkisin memiliki indeks terapi sempit. Jamu pembersih asam urat membantu meredakan serangan akut.",
        "clinical_action": "Minum jamu dengan jeda 3 jam setelah kolkisin. Waspadai diare berlebih."
    },
    {
        "keyword": "parasetamol",
        "official_name": "Paracetamol / Panadol",
        "phytochemical": "Temulawak & Jahe",
        "risk_level": "SAFE (Aman Penuh)",
        "level_type": "safe",
        "pathway": "Glukuronidasi & Sulfasi Hepar",
        "mechanism": "Temulawak (kurkuminoid) justru bersifat hepatoprotektif melindungi sel hati dari metabolit toksik parasetamol (NAPQI).",
        "clinical_action": "Sangat aman dikonsumsi berdampingan dengan jeda waktu minum wajar 1-2 jam."
    },

    # 6. GASTROINTESTINAL & LAMBUNG
    {
        "keyword": "omeprazole",
        "official_name": "Omeprazole / Lansoprazole (PPI)",
        "phytochemical": "Kurkuminoid (Temulawak/Kunyit)",
        "risk_level": "SINERGIS GASTROPROTEKTIF",
        "level_type": "safe",
        "pathway": "Pompa Proton H+/K+ ATPase & Mukus Lambung",
        "mechanism": "PPI menurunkan asam lambung, sedangkan temulawak/kunyit merangsang sekresi mukus pelindung dinding lambung.",
        "clinical_action": "Sangat baik untuk pemulihan gastritis/maag. Minum PPI sebelum sarapan, jamu pk 09:30 (jeda 2.5 jam)."
    },
    {
        "keyword": "antasida",
        "official_name": "Antasida (Al/Mg Hidroksida)",
        "phytochemical": "Tanin & Flavonoid",
        "risk_level": "MILD (Kelasi / Penurunan Serapan)",
        "level_type": "warning",
        "pathway": "Netralisasi Asam & Pembentukan Kompleks Logam",
        "mechanism": "Kation logam Al3+ dan Mg2+ dalam antasida dapat mengikat senyawa tanin/flavonoid jamu di lambung.",
        "clinical_action": "Wajib jeda waktu minimal 2 jam agar zat aktif jamu tidak terikat oleh antasida."
    },

    # 7. KORTIKOSTEROID & IMUNOSUPRESAN
    {
        "keyword": "deksametason",
        "official_name": "Deksametason / Metilprednisolon",
        "phytochemical": "Kurkuminoid",
        "risk_level": "MILD-MODERATE (Efek Lambung)",
        "level_type": "warning",
        "pathway": "CYP3A4 Induksi & Glukokortikoid",
        "mechanism": "Kortikosteroid menekan kekebalan dan mengiritasi lambung. Sambiloto bersifat imunostimulan yang berlawanan.",
        "clinical_action": "Gunakan temulawak ramah lambung, hindari sambiloto dosis tinggi pada terapi steroid imunosupresif."
    },

    # 8. SISTEM SARAF & PSIKIATRI
    {
        "keyword": "alprazolam",
        "official_name": "Alprazolam / Diazepam",
        "phytochemical": "Minyak Atsiri Serai & Jahe",
        "risk_level": "MODERATE (Sinergis Sedatif)",
        "level_type": "warning",
        "pathway": "Reseptor GABA-A & CYP3A4",
        "mechanism": "Senyawa aromaterapik serai dan efek penenang herbal dapat menambah rasa kantuk obat penenang.",
        "clinical_action": "Hindari mengemudi jika mengonsumsi keduanya. Beri jeda konsumsi 3 jam."
    },

    # 9. PERNAPASAN & ALERGI
    {
        "keyword": "cetirizine",
        "official_name": "Cetirizine / Antihistamin",
        "phytochemical": "Gingerol & Curcumin",
        "risk_level": "SAFE (Sinergis Anti-alergi)",
        "level_type": "safe",
        "pathway": "Reseptor H1 Histamin",
        "mechanism": "Jahe dan temulawak memiliki sifat stabilisator sel mast yang bersinergi meredakan gatal dan alergi.",
        "clinical_action": "Kombinasi aman. Beri jeda waktu minum 2 jam."
    },
    {
        "keyword": "salbutamol",
        "official_name": "Salbutamol (Bronkodilator)",
        "phytochemical": "Gingerol",
        "risk_level": "SAFE (Relaksasi Bronkus)",
        "level_type": "safe",
        "pathway": "Reseptor Beta-2 Adrenergik Paru",
        "mechanism": "Ekstrak jahe hangat membantu melegakan saluran napas tanpa mengganggu kerja salbutamol.",
        "clinical_action": "Aman dikonsumsi dengan jeda waktu minum standar."
    },

    # 10. ANTIBIOTIK
    {
        "keyword": "amoksisilin",
        "official_name": "Amoksisilin / Cefixime",
        "phytochemical": "Kurkuminoid",
        "risk_level": "SAFE (Jeda 2 Jam)",
        "level_type": "safe",
        "pathway": "Sintesis Dinding Sel Bakteri",
        "mechanism": "Tidak mengganggu khasiat bakterisida antibiotik asalkan diberi jeda agar absorpsi lambung tidak terhambat.",
        "clinical_action": "Habiskan antibiotik sesuai resep dokter, beri jeda 2-3 jam sebelum minum jamu."
    },
    {
        "keyword": "ciprofloxacin",
        "official_name": "Ciprofloxacin / Fluorokuinolon",
        "phytochemical": "Garam Mineral Herbal (K, Mg)",
        "risk_level": "MODERATE (Penurunan Absorpsi)",
        "level_type": "warning",
        "pathway": "Kelasi Mineral Saluran Cerna",
        "mechanism": "Mineral alami dalam rebusan herbal dapat mengkelat siprofloksasin dan menurunkan penyerapannya drastis.",
        "clinical_action": "Wajib jeda waktu ketat minimal 3 jam antara antibiotik kuinolon dan rebusan jamu."
    }
]
