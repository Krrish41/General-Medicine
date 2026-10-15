# -*- coding: utf-8 -*-
"""
Interactive data presets, comparison pairs, and spotters for General Medicine.
"""

CLASSIFICATION_PRESETS = {
    "chap1": {
        "title": "Interactive Hepatitis B Serology Explorer",
        "types": [
            {
                "name": "Acute HBV (Early / Highly Infectious)",
                "badge": "Active Viral Replication",
                "hemodynamics": "HBsAg: (+) | Anti-HBs: (-) | Anti-HBc IgM: (+) | HBeAg: (+)",
                "summary": "Patient is acutely infected and highly contagious. The presence of HBeAg indicates intense viral replication and high viral DNA levels. ALT/AST typically >1,000 IU/L."
            },
            {
                "name": "The Core Window Period",
                "badge": "Diagnostic Blindspot",
                "hemodynamics": "HBsAg: (-) | Anti-HBs: (-) | Anti-HBc IgM: (+) ONLY | HBeAg: (+/-)",
                "summary": "HBsAg has been cleared by host immunity, but neutralizing anti-HBs antibodies have not yet reached detectable levels. Anti-HBc IgM is the sole serological proof of acute infection."
            },
            {
                "name": "Chronic HBV (High Replicative)",
                "badge": "Active Chronic Infection",
                "hemodynamics": "HBsAg: (+) > 6 months | Anti-HBc IgG: (+) | HBeAg: (+) | HBV DNA: >20,000 IU/mL",
                "summary": "Sustained necroinflammation. High risk of progression to cirrhosis and hepatocellular carcinoma. First-line therapy: Tenofovir (TDF) or Entecavir."
            },
            {
                "name": "Natural Immunity (Past Infection)",
                "badge": "Resolved Infection",
                "hemodynamics": "HBsAg: (-) | Anti-HBs: (+) | Anti-HBc IgG: (+) | HBeAg: (-)",
                "summary": "Patient has cleared the virus naturally. The presence of Anti-HBc IgG proves that the patient was exposed to true wild-type viral nucleocapsid (unlike vaccine-induced immunity)."
            },
            {
                "name": "Vaccine-Induced Immunity",
                "badge": "Recombinant Protection",
                "hemodynamics": "HBsAg: (-) | Anti-HBs: (+) (≥10 mIU/mL) | Anti-HBc: NEGATIVE (All)",
                "summary": "Immunity derived from recombinant HBsAg vaccination. Because only surface antigen was administered, no antibodies to core antigens (anti-HBc) are ever produced."
            }
        ]
    },
    "chap2": {
        "title": "Interactive Shock Hemodynamics Explorer",
        "types": [
            {
                "name": "Hypovolemic Shock",
                "badge": "Volume Depletion",
                "hemodynamics": "CO: Low | SVR: High | CVP/PCWP: Low | Extremities: Cold, clammy",
                "summary": "Hemorrhage or dehydration. Baroreceptor reflex induces intense sympathetic vasoconstriction. First-line therapy is rapid balanced crystalloid infusion or blood products."
            },
            {
                "name": "Cardiogenic Shock",
                "badge": "Pump Failure",
                "hemodynamics": "CO: Markedly Low | SVR: High | CVP/PCWP: Markedly Elevated | Extremities: Cold, cyanotic",
                "summary": "Massive acute MI or severe acute mitral regurgitation. Engorged jugular veins and pulmonary edema. Requires inotropes (Dobutamine) and emergent revascularization (PCI)."
            },
            {
                "name": "Septic / Distributive Shock",
                "badge": "Hyperdynamic Vasodilation",
                "hemodynamics": "CO: High / Normal | SVR: Extremely Low | CVP: Low/Normal | Extremities: Warm, flushed",
                "summary": "Bacterial endotoxins induce nitric oxide storm, collapsing vascular resistance. Requires 30 mL/kg IV crystalloids, early broad-spectrum antibiotics, and Noradrenaline."
            },
            {
                "name": "Anaphylactic Shock",
                "badge": "Type I Hypersensitivity",
                "hemodynamics": "CO: Low | SVR: Profoundly Low | Airway: Laryngeal stridor & Bronchospasm",
                "summary": "IgE-mediated mast cell degranulation. Drug of choice: Intramuscular Adrenaline (0.5 mg 1:1,000 IM into anterolateral thigh)."
            },
            {
                "name": "Neurogenic Shock",
                "badge": "Sympathectomy",
                "hemodynamics": "CO: Low/Normal | SVR: Low | HR: Paradoxical Bradycardia | Extremities: Warm, dry",
                "summary": "High spinal cord trauma. Loss of sympathetic vasomotor tone produces hypotension with paradoxical bradycardia."
            }
        ]
    }
}

COMPARISON_PAIRS = [
    {
        "id": "comp_kwashiorkor_marasmus",
        "title": "Kwashiorkor vs Nutritional Marasmus",
        "table": [
            ["Nutritional Deficit", "Selective Protein deficiency with preserved calories", "Total Starvation (Both Protein and Caloric deficiency)"],
            ["Bilateral Pitting Edema", "**Mandatory Hallmark Present**", "**Strictly Absent**"],
            ["Facial Appearance", "'Moon face' (edematous, puffy)", "'Old man / Monkey facies' (sunken cheeks)"],
            ["Subcutaneous Fat", "Preserved", "Completely absent / melted away"],
            ["Liver", "Hepatomegaly with massive Fatty Infiltration", "Normal liver, no fatty changes"],
            ["Cutaneous & Hair Signs", "'Flaky paint' dermatosis, 'Flag sign' hair", "Skin loose, dry, wrinkled; hair normal"],
            ["Serum Albumin", "Severely low (< 2.0 g/dL)", "Normal or slightly reduced (> 2.8 g/dL)"],
            ["Appetite & Mood", "Anorexic, miserable, irritable, apathetic", "Voracious ravenous appetite, alert"]
        ]
    },
    {
        "id": "comp_aml_cml",
        "title": "Acute Myeloid Leukemia vs Chronic Myelogenous Leukemia",
        "table": [
            ["Clinical Tempo", "Sudden, rapid, acute fulminant course (weeks)", "Insidious, indolent, slow progression (years)"],
            ["Bone Marrow Blasts", "**Immature Myeloblasts ≥ 20%**", "**Maturing Granulocytes**; Blasts usually < 10%"],
            ["Cytological Sign", "**Auer Rods** in cytoplasm of myeloblasts", "All stages of granulocytes + absolute **Basophilia**"],
            ["Cytogenetic Marker", "Variable (t(8;21), inv(16), t(15;17))", "**Philadelphia Chromosome t(9;22)** (*BCR-ABL1*)"],
            ["Gingival Infiltration", "**Common & Severe** (especially M4/M5 subtypes)", "Rare in chronic phase; may occur in blast crisis"],
            ["First-Line Therapy", "Intensive Chemotherapy ('7+3': Cytarabine + Daunorubicin)", "Targeted Tyrosine Kinase Inhibitor (Imatinib)"]
        ]
    },
    {
        "id": "comp_nephrotic_nephritic",
        "title": "Nephrotic vs Nephritic Syndrome",
        "table": [
            ["Primary Defect", "Podocyte injury with charge/size barrier loss", "Endocapillary inflammation with capillary necrosis"],
            ["24-Hour Proteinuria", "**Massive (> 3.5 g/24 hours)**", "Sub-nephrotic (usually 1 to 2 g/24 hours)"],
            ["Hematuria & Casts", "Absent or microscopic; **Fatty casts**", "**Gross Hematuria ('Cola-colored')** with **RBC Casts**"],
            ["Serum Albumin", "**Severe Hypoalbuminemia (< 2.5 g/dL)**", "Normal or mildly reduced"],
            ["Edema Characteristics", "**Anasarca (Severe, generalized pitting edema)**", "Mild dependent morning periorbital edema"],
            ["Blood Pressure", "Usually normal", "**Hypertension (Universal finding)**"]
        ]
    },
    {
        "id": "comp_janeway_osler",
        "title": "Janeway Lesions vs Osler's Nodes",
        "table": [
            ["Pain Sensation", "**Completely Painless** (Non-tender)", "**Exquisitely Painful & Tender**"],
            ["Pathological Mechanism", "**Septic Micro-Emboli** producing microabscesses", "**Immune Complex Deposition** producing vasculitis"],
            ["Typical Location", "Palms of hands, soles of feet, thenar eminences", "Pulps (pads) of fingers and toes"],
            ["Lesion Appearance", "Flat, erythematous or hemorrhagic macules", "Raised, violaceous, nodular subcutaneous bumps"],
            ["IE Subtype Association", "Acute Staphylococcal Endocarditis", "Subacute Streptococcal Endocarditis"]
        ]
    },
    {
        "id": "comp_umn_lmn_facial",
        "title": "Upper vs Lower Motor Neuron Facial Paralysis",
        "table": [
            ["Site of Lesion", "Above facial nucleus in pons (Motor cortex / Stroke)", "Facial nucleus in pons or CN VII trunk (Bell's palsy)"],
            ["Forehead Wrinkling", "**Preserved / Normal** (Bilateral cortical input)", "**Paralyzed / Absent** on affected side"],
            ["Eye Closure (Orbicularis)", "**Intact / Blinking preserved**", "**Impaired (Lagophthalmos)**; Bell's phenomenon (+)"],
            ["Distribution of Weakness", "Contralateral lower face only", "Ipsilateral entire half of face (Upper + Lower)"],
            ["Etiology", "Middle Cerebral Artery (MCA) Stroke, Brain Tumor", "Bell's Palsy, Trauma, Parotid Neoplasms"]
        ]
    }
]

SPOTTER_HOTSPOTS = [
    {
        "id": "spot1_koplik",
        "title": "Koplik's Spots in Measles",
        "image_file": "koplik_spots.png",
        "clue": "Tiny, irregular, bluish-white spots resembling grains of salt on a red background opposite the lower molars.",
        "diagnosis": "Koplik's Spots (Pathognomonic enanthem of Measles / Rubeola).",
        "viva_pearl": "Appears 1 to 2 days before the generalized maculopapular cutaneous rash and disappears within 2 to 3 days."
    },
    {
        "id": "spot2_snail_track",
        "title": "Snail-Track Ulcers of Secondary Syphilis",
        "image_file": "snail_track_ulcers.png",
        "clue": "Multiple glistening, wavy, serpentine mucosal erosions on the soft palate and tonsillar pillars.",
        "diagnosis": "Snail-Track Ulcers (Secondary Syphilis - Treponema pallidum).",
        "viva_pearl": "Teeming with millions of active spirochetes; highly contagious. Confirm with VDRL/TPHA."
    },
    {
        "id": "spot3_leukemic_gingiva",
        "title": "Leukemic Gingival Hyperplasia",
        "image_file": "leukemic_gingival_enlargement.png",
        "clue": "Diffuse, boggy, purplish-red swelling of the interdental papillae and marginal gingiva covering tooth crowns with spontaneous bleeding.",
        "diagnosis": "Leukemic Gingival Infiltration (AML FAB M4 / M5).",
        "viva_pearl": "Caused by infiltration of immature neoplastic myelomonocytic blasts. Platelets are low (<50,000/mm³). Never excise without CBC!"
    },
    {
        "id": "spot4_hutchinson_teeth",
        "title": "Hutchinson's Incisors & Mulberry Molars",
        "image_file": "hutchinsons_teeth.png",
        "clue": "Screwdriver-shaped upper central incisors with central crescentic incisal notch, accompanied by multi-cusped mulberry molars.",
        "diagnosis": "Dental Stigmata of Late Congenital Syphilis (Hutchinson's Triad).",
        "viva_pearl": "Result of direct spirochetal damage to the developing tooth germ during calcification."
    }
]

EXAM_RUBRIC_CRITERIA = [
    {
        "section": "1. Definition & Classification",
        "weight": "2 Marks",
        "criteria": "Standard WHO/Harrison definition, clear etiological/clinical classification table with subtypes and epidemiology."
    },
    {
        "section": "2. Pathogenesis & Applied Physiology",
        "weight": "3 Marks",
        "criteria": "Clear sequential hemodynamic or biochemical cascade, molecular triggers, and Layman's explanation box."
    },
    {
        "section": "3. Clinical Presentation & Physical Signs",
        "weight": "3 Marks",
        "criteria": "Detailed systemic examination (Inspection, Palpation, Percussion, Auscultation) and named bedside clinical signs."
    },
    {
        "section": "4. Diagnostic Workup & Criteria",
        "weight": "2 Marks",
        "criteria": "Specific criteria sets (Duke, Jones, ADA, Child-Pugh), laboratory investigations, imaging, and biopsy/culture protocols."
    },
    {
        "section": "5. Comprehensive Management & Dental Precautions",
        "weight": "3 Marks",
        "criteria": "Emergency resuscitation (ABCs), first-line drug classes with generic names, exact dosages, and dental considerations (prophylaxis, bleeding cutoffs)."
    },
    {
        "section": "6. Must-Draw Diagrams & Flowcharts",
        "weight": "2 Marks",
        "criteria": "Neat, labeled clinical algorithm, anatomical schematic, or biochemical flowchart."
    }
]
