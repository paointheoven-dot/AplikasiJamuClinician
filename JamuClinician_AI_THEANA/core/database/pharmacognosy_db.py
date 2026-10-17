"""
Pharmacognosy Database: Active Phytoconstituents & Standardized Simplisia
Reference: Farmakope Herbal Indonesia (FHI) Edisi VI & FORMI Kemenkes RI
"""

HERBAL_MONOGRAPHS = {
    "temulawak": {
        "latin": "Curcuma xanthorrhiza rhizoma",
        "name": "Temulawak",
        "active_compounds": [
            "Kurkuminoid (Kurkumin, Desmetoksikurkumin)",
            "Xanthorrhizol",
            "Minyak Atsiri (Germakron)"
        ],
        "pharmacodynamics": "Antiinflamasi via inhibisi COX-2; modulasi sekresi asam empedu (kolagogum); hepatoprotektif.",
        "standard_dose": "15 g rimpang segar cuci bersih (atau 5 g simplisia kering)",
        "kitchen_measure": "1 potong seukuran ibu jari tangan",
        "cyp_interactions": ["Inhibisi ringan CYP3A4", "Inhibisi ringan CYP2C9"]
    },
    "jahe_merah": {
        "latin": "Zingiber officinale var. rubrum",
        "name": "Jahe Merah",
        "active_compounds": [
            "6-Gingerol",
            "6-Shogaol",
            "Zingiberen"
        ],
        "pharmacodynamics": "Analgesik muskuloskeletal; vasodilator perifer; spasmolitik saluran cerna.",
        "standard_dose": "10 g rimpang memar",
        "kitchen_measure": "1 ruas jari tangan sedang",
        "cyp_interactions": ["Inhibisi ringan CYP3A4 pada konsentrasi tinggi"]
    },
    "serai": {
        "latin": "Cymbopogon citratus",
        "name": "Serai Dapur",
        "active_compounds": [
            "Sitral",
            "Geraniol",
            "Sitronelal"
        ],
        "pharmacodynamics": "Corrigens odoris (penyelaras aroma); karminatif; spasmolitik ringan.",
        "standard_dose": "5 g batang bagian putih",
        "kitchen_measure": "1 batang bagian putih",
        "cyp_interactions": ["Netral pada dosis oral umum"]
    },
    "sambiloto": {
        "latin": "Andrographis paniculata folium",
        "name": "Sambiloto",
        "active_compounds": [
            "Andrographolide",
            "Neoandrographolide"
        ],
        "pharmacodynamics": "Urikosurik alami; imunomodulator; penurun glukosa darah.",
        "standard_dose": "5 g simplisia kering",
        "kitchen_measure": "1 sendok makan simplisia kering",
        "cyp_interactions": ["Inhibisi ringan CYP1A2"]
    },
    "kumis_kucing": {
        "latin": "Orthosiphon stamineus folium",
        "name": "Kumis Kucing",
        "active_compounds": [
            "Sinensetin",
            "Orthosiphol",
            "Garam Kalium"
        ],
        "pharmacodynamics": "Diuretik saluretik pembilas kristal urat; antibakteri saluran kemih.",
        "standard_dose": "7 g daun segar",
        "kitchen_measure": "1 genggam kecil daun segar",
        "cyp_interactions": ["Ekskresi renal aktif"]
    }
}
