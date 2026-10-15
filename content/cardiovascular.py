# -*- coding: utf-8 -*-
"""
General Medicine: Cardiovascular System & Valvular Heart Disease
Chapters:
6. Acute Rheumatic Fever & Rheumatic Heart Disease
7. Infective Endocarditis & AHA Dental Prophylaxis Guidelines
8. Ischemic Heart Disease & Acute ST-Elevation Myocardial Infarction (STEMI)
9. Heart Failure & Systemic Hypertension
10. Congenital Heart Diseases (ASD, VSD, PDA, Tetralogy of Fallot)
"""

CHAPTERS = [
    {
        "id": "chap6_rheumatic_fever",
        "title": "Acute Rheumatic Fever & Rheumatic Heart Disease",
        "badge": "15-Mark Essay Model",
        "category": "Cardiovascular Medicine",
        "reading_time": "15 min read",
        "key_points": [
            "Acute Rheumatic Fever (ARF) is a multi-system autoimmune inflammatory sequela occurring 2 to 3 weeks after an untreated Group A Beta-Hemolytic Streptococcal (GABHS / Streptococcus pyogenes) pharyngeal infection.",
            "Pathogenesis is driven by molecular mimicry: Streptococcal cell wall M-proteins share antigenic homology with human cardiac myosin, sarcolemma, and valve glycoproteins, triggering cross-reactive CD4+ T-cell and antibody attack.",
            "Revised Jones Criteria (2015 AHA Update) requires documented preceding streptococcal infection (elevated ASO titer >200-330 IU/mL or throat culture) PLUS 2 Major Criteria OR 1 Major + 2 Minor Criteria.",
            "Major Criteria (JONES): J - Joints (Migratory Polyarthritis), O - Carditis / Valvulitis (Pancarditis), N - Subcutaneous Nodules, E - Erythema Marginatum, S - Sydenham Chorea.",
            "Pathognomonic histological lesion: The Aschoff Nodule—fibrinoid collagen necrosis surrounded by lymphocytes, plasma cells, and Anitschkow cells (caterpillar cells with wavy chromatin).",
            "Mitral valve is the most frequently affected valve (65-70%), followed by Aortic valve (25%); leads to chronic fibrotic thickening, chordal shortening, and commissural fusion ('fish-mouth' / 'button-hole' mitral stenosis).",
            "Secondary prophylaxis: Intramuscular Benzathine Penicillin G (1.2 million units IM every 3 to 4 weeks); duration depends on carditis presence (up to age 21 or 10 years for carditis, up to age 40 or lifelong for carditis with persistent valvular disease)."
        ],
        "clinical_pearl": "The joint involvement in Acute Rheumatic Fever is a classical MIGRATORY (fleeting) polyarthritis that affects large joints (knees, ankles, elbows, wrists) sequentially, NOT simultaneously. It responds exquisitely and dramatically to Salicylates (Aspirin); failure of joint inflammation to subside within 48 to 72 hours of therapeutic aspirin strongly casts doubt on the diagnosis of ARF.",
        "sections": [
            {
                "title": "1. Definition, Epidemiology & Molecular Mimicry",
                "content": """**Definition**: Acute Rheumatic Fever (ARF) is a non-suppurative, delayed systemic autoimmune inflammatory disease affecting collagen connective tissues—predominantly the heart, joints, central nervous system, skin, and subcutaneous tissues—occurring as a delayed complication of pharyngeal infection with *Streptococcus pyogenes* (Group A Beta-Hemolytic Streptococcus).

### Epidemiology
* Peak incidence: Children aged 5 to 15 years (rare < 3 years and adults).
* Socioeconomic factors: Overcrowding, poor sanitation, poverty, and limited access to healthcare.
* Geographically endemic in developing countries (sub-Saharan Africa, South Asia, indigenous populations of Australasia).

### Pathogenesis: The Concept of Molecular Mimicry
```
Pharyngeal infection with Streptococcus pyogenes (GABHS)
               │
               ▼
Bacterial cell wall contains highly antigenic M-Proteins & N-acetylglucosamine
               │
               ▼
Host Antigen-Presenting Cells present epitopes to CD4+ T-Lymphocytes
               │
               ▼
Cross-Reactivity (Antigenic Homology / Molecular Mimicry):
Streptococcal M-protein mimics Cardiac Myosin, Tropomyosin & Valve Endothelium
               │
               ▼
Host B-cells produce cross-reactive autoantibodies & Cytotoxic T-cells infiltrate heart
               │
               ▼
Endothelial VCAM-1 upregulation ──► Extravasation of CD4+ T-cells into Valvular Stroma
               │
               ▼
PANCARDITIS (Endocarditis + Myocarditis + Pericarditis)
```

**Layman's Explanation**: The body's immune soldiers get trained to attack a bad bacterial throat bug (*Streptococcus*). Unfortunately, the uniform worn by the bacteria (M-protein) looks almost identical to the uniform worn by your heart valve cells and joint cartilage. After defeating the throat bug, the confused immune soldiers mistakenly turn around and fire upon your own heart valves and joints, causing scarring and irreversible damage."""
            },
            {
                "title": "2. Diagnostic Criteria: The Revised Jones Criteria (2015 AHA)",
                "content": """Diagnosis requires evidence of **preceding Group A Streptococcal infection** PLUS:
* **2 Major Criteria**, OR
* **1 Major Criteria + 2 Minor Criteria**.

*Evidence of Prior Streptococcal Infection*:
* Rising or elevated Anti-Streptolysin O (**ASO**) titer (>200–330 Todd units in children).
* Positive throat culture or rapid streptococcal antigen test.
* Recent scarlet fever.

### Comparison of Major & Minor Criteria (Low-Risk vs Moderate/High-Risk Populations)
| Criteria Category | Major Criteria (JONES) | Minor Criteria |
| :--- | :--- | :--- |
| **Joints** | **Migratory Polyarthritis** (Low-risk)<br>**Monoarthritis / Polyarthralgia** (Moderate/High-risk) | **Arthralgia** (in absence of arthritis as major) |
| **Heart** | **Carditis** (Clinical or Subclinical on Echocardiography: Valvulitis) | **Prolonged PR Interval** on ECG (adjusted for age) |
| **Nodules** | **Subcutaneous Nodules** (Painless, firm over bony prominences) | — |
| **Skin** | **Erythema Marginatum** (Evanescent, non-pruritic serpiginous rash) | — |
| **Nervous** | **Sydenham Chorea** (St. Vitus dance: involuntary purposeless movements) | — |
| **Systemic Markers**| — | **Fever** (≥ 38.5°C in low-risk; ≥ 38.0°C in high-risk)<br>**Elevated ESR** (≥ 60 mm/hr) or **CRP** (≥ 3.0 mg/dL) |"""
            },
            {
                "title": "3. Clinical Presentation: Major Manifestations in Detail",
                "content": """1. **Carditis (Pancarditis: 50–60% of cases)**:
   * **Endocarditis (Valvulitis)**: Almost universally present in carditis; causes valve regurgitation.
     * **Mitral Regurgitation**: Apical pansystolic murmur radiating to the left axilla.
     * **Carey Coombs Murmur**: Soft, low-pitched, mid-diastolic apical rumble caused by turbulent flow across inflamed, edematous mitral valve leaflets (differentiated from mitral stenosis by the absence of an opening snap).
     * **Aortic Regurgitation**: Early diastolic decrescendo murmur at left sternal border.
   * **Myocarditis**: Unexplained resting tachycardia (out of proportion to fever), soft S1, cardiomegaly, gallop rhythm (S3), acute congestive heart failure.
   * **Pericarditis**: Precordial friction rub, pleuritic chest pain relieved by sitting forward, low-voltage QRS with diffuse ST elevation on ECG.
2. **Migratory Polyarthritis (75% of cases)**:
   * Severe, painful inflammation involving large joints sequentially (knee, ankle, elbow, wrist). As inflammation subsides in one joint, it erupts in another. Joints are hot, red, swollen, exquisitely tender. Resolves without permanent joint deformity.
3. **Sydenham's Chorea (St. Vitus Dance: 10–15%)**:
   * Delayed presentation (2 to 6 months after infection); female predominance.
   * Involuntary, rapid, non-repetitive, purposeless choreiform movements of face and limbs; emotional lability, irritability, muscle weakness. Disappears during sleep.
   * Classical signs: 'Milkmaid's grip' (irregular hand contractions), 'Choreic tongue' (inability to maintain tongue protrusion: darting tongue), 'Pronator sign'.
4. **Subcutaneous Nodules (1–5%)**:
   * Firm, painless, mobile nodules (0.5 to 2 cm) over extensor surfaces of tendons and bony prominences (elbows, knees, occiput, spine). Almost always associated with severe carditis!
5. **Erythema Marginatum (< 3%)**:
   * Non-pruritic, pink, evanescent erythematous rings with clear central pale zones and raised, serpiginous (wavy) borders, occurring on trunk and proximal extremities; spares the face."""
            },
            {
                "title": "4. Pathology: The Aschoff Nodule",
                "content": """The **Aschoff Nodule** is the pathognomonic granulomatous lesion of rheumatic carditis located in the myocardial interstitium and perivascular subendocardial tissues.

```
Fibrinoid Collagen Necrosis (Central zone)
               │
               ▼
Surrounded by inflammatory infiltrate: T-Lymphocytes, Plasma Cells, Macrophages
               │
               ▼
ANITSCHKOW CELLS ('Caterpillar Cells')
(Enlarged modified histiocytes with abundant amphophilic cytoplasm &
central vesicular nucleus containing a wavy ribbon of chromatin)
               │
               ▼
ASCHOFF GIANT CELLS
(Multinucleated giant cells with 1 to 4 nuclei formed by coalescence of Anitschkow cells)
               │
               ▼
Healing by Fibrotic Scarring ──► Chronic Valvular Deformity
```

### Rheumatic Heart Disease (Chronic Sequelae)
Decades of recurrent low-grade inflammation cause progressive valvular fibrosis:
* **Mitral Stenosis**: Commissural fusion, cusp retraction, and calcification produce the pathognomonic **'Fish-mouth'** or **'Button-hole'** mitral orifice.
* **MacCallum's Patch**: A roughened, corrugated fibrotic plaque in the posterior wall of the left atrium caused by chronic turbulent jet regurgitation."""
            },
            {
                "title": "5. Comprehensive Management & Prophylaxis Protocols",
                "content": """### A. Acute Phase Management
1. **Bed Rest**: Strict bed rest until inflammatory markers (ESR, CRP) normalize and carditis stabilizes.
2. **Eradication of Streptococcal Throat Carriage**:
   * **Benzathine Penicillin G**: Single dose of 1.2 million units IM (600,000 units if < 27 kg), OR
   * **Oral Penicillin V**: 500 mg orally BD or TID for 10 days (in penicillin allergy: Oral Azithromycin 500 mg Day 1, then 250 mg/day for 4 days).
3. **Anti-inflammatory Therapy**:
   * **Arthritis alone (Without Carditis)**: High-dose **Aspirin** (75–100 mg/kg/day divided in 4 doses) for 4–6 weeks, then tapered.
   * **Carditis with Cardiomegaly / Heart Failure**: **Prednisolone** (1 to 2 mg/kg/day orally, max 60 mg/day) for 2 to 3 weeks, then tapered over 2 to 4 weeks with overlapping aspirin to prevent rebound.
4. **Heart Failure Resuscitation**: Diuretics (Furosemide), ACE inhibitors, fluid/salt restriction. Avoid Digoxin if possible due to increased myocardial sensitivity.
5. **Chorea Management**: Valproate (15–20 mg/kg/day), Carbamazepine, or Haloperidol; quiet room.

### B. Secondary Long-Term Antibiotic Prophylaxis (Mandatory to Prevent Recurrence)
* **Drug of Choice**: **Intramuscular Benzathine Penicillin G 1.2 million units IM every 3 to 4 weeks** (every 3 weeks in high-risk populations).
* **Oral Alternative**: Penicillin V 250 mg orally BD (Sulfadiazine 1 g OD or Erythromycin 250 mg BD if penicillin-allergic).

### Duration of Secondary Prophylaxis (AHA Guidelines)
| Clinical Category | Recommended Duration of Prophylaxis |
| :--- | :--- |
| **ARF without Carditis** | For 5 years after last attack OR until age 21 years (whichever is longer) |
| **ARF with Carditis (No residual valvular disease)** | For 10 years after last attack OR until age 21 years (whichever is longer) |
| **ARF with Carditis & Residual Valvular Disease (RHD)** | For 10 years OR until age 40 years (whichever is longer); lifelong in high-risk patients / valve replacement |"""
            },
            {
                "title": "6. Dental & Maxillofacial Considerations",
                "content": """1. **Infective Endocarditis Vulnerability**: Damaged rheumatic heart valves (especially mitral and aortic regurgitation/stenosis) create turbulent blood flow, predisposing to bacterial seeding during invasive dental procedures.
2. **Anticoagulation in RHD**: Patients with chronic mitral stenosis and atrial fibrillation or mechanical prosthetic valves are maintained on lifelong **Warfarin**. Check INR 24 hours prior to dental surgical procedures (safe target for dental extractions is INR 2.0 to 3.0; do NOT discontinue warfarin for simple extractions).
3. **Aspirin / NSAID Precautions**: Patients on therapeutic aspirin for acute rheumatic arthritis have altered platelet function (elevated bleeding time); perform meticulous local hemostasis."""
            }
        ],
        "comparisons": [
            {
                "title": "Acute Rheumatic Arthritis vs Rheumatoid Arthritis",
                "headers": ["Clinical Feature", "Acute Rheumatic Fever", "Rheumatoid Arthritis"],
                "rows": [
                    ["Joint Pattern", "Migratory (fleeting) Polyarthritis", "Additive, Symmetrical Polyarthritis"],
                    ["Joint Types Involved", "Large joints (Knee, Ankle, Elbow, Wrist)", "Small joints of hands (MCP, PIP, MTP)"],
                    ["Joint Deformity / Erosion", "Zero permanent damage (Completely reversible)", "Progressive joint destruction, pannus, deformities"],
                    ["Response to Aspirin", "Dramatic, rapid resolution within 24–48 hours", "Partial symptomatic relief only"],
                    ["Serological Markers", "Elevated ASO titer, Anti-DNase B", "Rheumatoid Factor (+), Anti-CCP (+)"],
                    ["Heart Involvement", "Pancarditis with chronic valvular scarring", "Rheumatoid nodules, pericarditis"]
                ]
            }
        ],
        "must_draw": "Histological schematic of the Aschoff nodule showing central fibrinoid necrosis, surrounded by T-lymphocytes, plasma cells, and Anitschkow 'caterpillar' cells with wavy nuclear chromatin ribbons.",
        "viva_questions": [
            "What is an Anitschkow cell? (Answer: A pathognomonic modified histiocyte seen in rheumatic Aschoff nodules with abundant cytoplasm and a central nucleus showing a characteristic wavy caterpillar-like chromatin ribbon).",
            "What is the Carey Coombs murmur? (Answer: A transient soft, low-pitched mid-diastolic apical murmur heard in acute rheumatic valvulitis due to turbulent flow across edematous mitral leaflets, distinguishing it from the opening snap and rumble of chronic mitral stenosis).",
            "Why is secondary penicillin prophylaxis required for decades in rheumatic fever? (Answer: Recurrent streptococcal pharyngeal infections trigger rapid reactivation of memory T-cells, progressively worsening valvular destruction with each attack).",
            "Which heart valve is most frequently damaged in Chronic Rheumatic Heart Disease? (Answer: Mitral valve (65–70%), followed by combined Mitral + Aortic valve (25%))."
        ]
    },
    {
        "id": "chap7_infective_endocarditis",
        "title": "Infective Endocarditis & AHA Dental Prophylaxis Guidelines",
        "badge": "15-Mark Essay Model",
        "category": "Cardiovascular Medicine",
        "reading_time": "16 min read",
        "key_points": [
            "Infective Endocarditis (IE) is a microbial infection of the endothelial surface of the heart, characterized by the formation of 'vegetations'—friable, bulky masses of platelets, fibrin, microcolonies of microorganisms, and scant inflammatory cells.",
            "Classification: Acute IE (virulent organisms, classically Staphylococcus aureus, attacking normal native valves, rapid destruction, fatal in days) vs Subacute IE (low-virulence organisms, classically Streptococcus viridans / oral streptococci, attacking previously diseased/prosthetic valves, indolent course).",
            "Pathogenetic Triad: Endothelial injury ──► Non-Bacterial Thrombotic Endocarditis (NBTE platelet-fibrin nidus) ──► Transient Bacteremia (dental extraction, flossing) ──► Bacterial Adherence & Vegetation Formation.",
            "Diagnostic Standard: Modified Duke Criteria requires 2 Major, or 1 Major + 3 Minor, or 5 Minor Criteria (Major: Typical blood culture positive from 2 separate venipunctures + Positive 2D-Echocardiogram showing oscillating intracardiac vegetation/abscess/dehiscence).",
            "Peripheral Immune-Vascular Signs: Osler's Nodes (painful, tender erythematous nodules on finger pulps), Janeway Lesions (painless hemorrhagic macules on palms/soles), Roth's Spots (retinal hemorrhages with pale fibrin centers), Splinter Hemorrhages.",
            "AHA 2021 Dental Prophylaxis Guidelines: Mandatory ONLY in highest-risk cardiac conditions (prosthetic heart valves, prior history of IE, unrepaired cyanotic congenital heart disease, or repaired CHD with residual defects) undergoing procedures involving manipulation of gingival tissue or periapical region of teeth.",
            "Prophylactic Regimen: Amoxicillin 2.0 g orally 30 to 60 minutes before the procedure (in penicillin allergy: Clindamycin 600 mg, Azithromycin 500 mg, or Cephalexin 2.0 g)."
        ],
        "clinical_pearl": "Janeway lesions are PAINLESS, erythematous macules on the palms and soles caused by septic emboli. In contrast, Osler's nodes are EXQUISITELY PAINFUL, tender, violaceous subcutaneous nodules on the pulps of fingers and toes caused by immune complex deposition (type III hypersensitivity). Remember: 'O' for Osler = 'O' for Ouch (Painful)! 'J' for Janeway = Just painless emboli.",
        "sections": [
            {
                "title": "1. Definition, Classification & Microbiology",
                "content": """**Definition**: Infective Endocarditis (IE) is an invasive microbial colonization of the cardiac endocardium—predominantly involving heart valves (native or prosthetic), chordae tendineae, or mural endocardium—characterized by the pathognomonic development of **vegetations** and associated with persistent bacteremia, valve destruction, septic embolization, and immune complex phenomena.

### Classification: Acute vs Subacute Infective Endocarditis
| Parameter | Acute Infective Endocarditis | Subacute Infective Endocarditis (SBE) |
| :--- | :--- | :--- |
| **Underlying Valve State** | Classically attacks **Normal, Healthy Native Valves** | Attacks **Previously Damaged, Rheumatic, or Prosthetic Valves** |
| **Causative Organisms** | Highly virulent: ***Staphylococcus aureus*** (commonest), *Streptococcus pneumoniae*, Group A Strep | Low virulence: ***Streptococcus viridans*** (oral flora: *S. mutans, S. mitis, S. sanguis*), *Enterococci* |
| **Clinical Course** | Fulminant, acute toxemic illness evolving over days | Indolent, insidious illness lasting weeks to months |
| **Vegetation Character** | Bulky, necrotic, highly destructive; early annular ring abscess, leaflet perforation | Smaller, firmer, granular; less invasive tissue destruction |
| **Mortality without Therapy** | Fatal within days to < 6 weeks | Fatal within 6 weeks to 6 months |

### Special Microbiological Categories
* **Prosthetic Valve Endocarditis (PVE)**:
  * Early (< 1 year post-op): *Staphylococcus epidermidis* (Coagulase-Negative Staphylococci - CoNS: 60–70%), *S. aureus*.
  * Late (> 1 year post-op): Same spectrum as native valve endocarditis (*S. viridans*, *S. aureus*).
* **Intravenous Drug Users (IVDU)**: *Staphylococcus aureus* (>60%), classically involving the **Tricuspid Valve** (Right-sided IE with septic pulmonary emboli).
* **HACEK Group (Fastidious Gram-Negative Bacilli)**: *Haemophilus*, *Aggregatibacter*, *Cardiobacterium*, *Eikenella corrodens*, *Kingella kingae* (require prolonged culture).
* **Culture-Negative IE (5–10%)**: *Coxiella burnetii* (Q fever), *Bartonella*, *Chlamydia*, *Tropheryma whipplei*, or prior antibiotic suppression."""
            },
            {
                "title": "2. Pathogenesis: The Four Sequential Steps",
                "content": """```
Turbulent Blood Flow (Valvular Stenosis / Regurgitation / VSD)
               │
               ▼
1. ENDOTHELIAL INJURY & DENUDATION
Loss of protective anti-thrombotic endothelium exposes subendothelial collagen
               │
               ▼
2. NON-BACTERIAL THROMBOTIC ENDOCARDITIS (NBTE)
Deposition of platelets and fibrin creates a sterile microscopic nidus / clot
               │
               ▼
3. TRANSIENT BACTEREMIA
Mucosal trauma (dental extraction, periodontal scaling, toothbrushing)
allows oral bacteria (S. viridans) to invade bloodstream
               │
               ▼
4. BACTERIAL ADHERENCE & VEGETATION PROPAGATION
Bacteria bind via surface adhesins (dextran, fibronectin-binding proteins) to NBTE clot
Microorganisms replicate rapidly, encased in fresh layers of fibrin & platelets
               │
               ▼
Avascular sanctuary shields bacteria from host neutrophils, antibodies & antibiotics
```

**Layman's Explanation**: Think of a heart valve as a smooth, Teflon-coated swing door. When blood rushes through too fast or awkwardly, it scuffs and scratches the Teflon coating (endothelial injury). The body tries to patch the scratch with a sticky band-aid made of platelets and fibrin. When you have a tooth pulled or bleed from your gums, bacteria from your mouth enter the bloodstream and go on a ride through the heart. If they bump into that sticky band-aid, they stick, hide inside the clot, and multiply into bacterial colonies called vegetations, chewing away at the heart valve."""
            },
            {
                "title": "3. Clinical Presentation: Physical Examination & Peripheral Stigmata",
                "content": """### Cardinal Manifestations
1. **Fever**: Present in >90% of patients; low-grade remittent in subacute, high swinging septic spikes with rigors in acute.
2. **Heart Murmurs (85%)**: Pre-existing murmur or the crucial emergence of a **NEW or CHANGING regurgitant murmur** (mitral or aortic).
3. **Splenomegaly**: Congestive or reactive enlargement seen in 20–40% of subacute cases.

### Classical Peripheral Immune-Vascular Signs
* **Petechiae**: Most common cutaneous sign; pinpoint hemorrhages on conjunctiva, buccal mucosa, palate, and suprascapular regions.
* **Splinter Hemorrhages**: Linear, dark-red to black subungual streaks located in the distal third of nail beds.
* **Janeway Lesions**: **Painless**, flat, erythematous or hemorrhagic macules on palms and soles; represent micro-abscesses with neutrophil necrosis caused by **septic micro-emboli**.
* **Osler's Nodes**: **Exquisitely tender**, painful, violaceous subcutaneous nodules on the pulps of fingers and toes; caused by **immune complex deposition** with focal arteritis.
* **Roth's Spots**: Oval retinal hemorrhages with a pale, white central fibrin center visible on fundoscopy; immune-mediated vasculitis.
* **Glomerulonephritis**: Immune complex deposition causing focal or diffuse proliferative glomerulonephritis (manifesting as microscopic hematuria, red cell casts, and mild proteinuria)."""
            },
            {
                "title": "4. Diagnostic Workup: The Modified Duke Criteria",
                "content": """A definitive clinical diagnosis of Infective Endocarditis requires:
* **2 Major Criteria**, OR
* **1 Major + 3 Minor Criteria**, OR
* **5 Minor Criteria**.

### Modified Duke Criteria Table
| Major Criteria | Minor Criteria |
| :--- | :--- |
| **1. Positive Blood Cultures for IE**: <br>• Typical microorganisms consistent with IE from 2 separate blood cultures (*S. viridans, S. bovis, HACEK, S. aureus* or *Enterococci*), OR<br>• Persistently positive blood cultures drawn > 12 hours apart, OR<br>• Single positive culture for *Coxiella burnetii* or Phase I IgG antibody titer > 1:800. | **1. Predisposition**: Heart condition (prosthetic valve, prior IE, cyanotic CHD) or IV drug abuse. |
| **2. Evidence of Endocardial Involvement on Echo**: <br>• Oscillating intracardiac mass (Vegetation) on valve or supporting structures, OR<br>• Annular abscess, OR<br>• New partial dehiscence of prosthetic valve, OR<br>• New valvular regurgitation (worsening of pre-existing murmur insufficient). | **2. Fever**: Temperature ≥ 38.0°C (100.4°F). |
| — | **3. Vascular Phenomena**: Major arterial emboli, septic pulmonary infarcts, mycotic aneurysm, intracranial hemorrhage, conjunctival hemorrhages, **Janeway lesions**. |
| — | **4. Immunological Phenomena**: Glomerulonephritis, **Osler's nodes**, **Roth's spots**, positive Rheumatoid Factor (RF). |
| — | **5. Microbiological Evidence**: Positive blood culture not meeting major criteria or serological evidence of active infection. |

* **Echocardiography Modalities**:
  * **Transthoracic Echocardiography (TTE)**: Sensitivity ~65–70%; excellent initial non-invasive screening tool.
  * **Transesophageal Echocardiography (TEE)**: Sensitivity >95%; investigation of choice for prosthetic valves, suspected annular abscesses, or bacteremia with negative TTE."""
            },
            {
                "title": "5. Comprehensive Medical Management & Surgical Indications",
                "content": """### A. Antimicrobial Pharmacotherapy (Bactericidal & Prolonged)
* Blood cultures (3 sets from separate venipuncture sites over 1 hour) MUST be drawn BEFORE administering antibiotics.
* **Empiric Therapy for Native Valve Acute IE**:
  * **Flucloxacillin** (2 g IV every 4h) + **Gentamicin** (1 mg/kg IV every 8h), OR
  * **Vancomycin** (15–20 mg/kg IV every 12h) + **Gentamicin** (in MRSA/penicillin-allergic patients).
* **Empiric Therapy for Subacute Native Valve IE**:
  * **Ampicillin** (2 g IV every 4h) + **Gentamicin** (1 mg/kg IV every 8h), OR **Vancomycin** + **Gentamicin**.
* **Empiric Therapy for Prosthetic Valve Endocarditis (PVE)**:
  * **Vancomycin** (15–20 mg/kg IV Q12H) + **Gentamicin** (1 mg/kg IV Q8H) + **Rifampicin** (300 mg orally/IV Q8H to penetrate biofilm) for ≥ 6 weeks.
* **Targeted Viridans Streptococcal IE (Penicillin-susceptible: MIC ≤ 0.12 mcg/mL)**:
  * IV **Ceftriaxone** (2 g IV OD) for 4 weeks, OR
  * IV **Penicillin G** (12–18 million units/day continuous infusion) + IV **Gentamicin** (3 mg/kg OD) for 2 weeks.

### B. Indications for Urgent Cardiac Valve Surgery (50% of Cases)
1. **Refractory Heart Failure**: Severe acute aortic or mitral regurgitation causing pulmonary edema or cardiogenic shock.
2. **Uncontrolled Infection**: Persistent bacteremia or fever > 7–10 days despite optimal bactericidal antimicrobial therapy.
3. **Invasive Complications**: Annular ring abscess, heart block (indicating aortic root abscess eroding bundle of His), fistula, valve perforation.
4. **Recurrent Embolization**: Persistent large, highly mobile vegetations (> 10 mm in diameter) despite therapy."""
            },
            {
                "title": "6. AHA & ADA Antibiotic Prophylaxis Guidelines in Dental Practice",
                "content": """The American Heart Association (AHA) and American Dental Association (ADA) maintain strict evidence-based prophylaxis criteria.

### Patient Cardiac Conditions Requiring Prophylaxis (Highest Risk Only!)
1. **Prosthetic Cardiac Valves** (mechanical, bioprosthetic, or homograft) or prosthetic material used for cardiac valve repair.
2. **Previous History of Infective Endocarditis**.
3. **Congenital Heart Disease (CHD)**:
   * Unrepaired cyanotic CHD (including palliative shunts and conduits).
   * Completely repaired congenital heart defect with prosthetic material or device during the **first 6 months** after the procedure.
   * Repaired CHD with residual defects at or adjacent to the site of a prosthetic patch or prosthetic device.
4. **Cardiac Transplant Recipients** who develop cardiac valvulopathy.

*Conditions NO LONGER Requiring Routine Prophylaxis*: Mitral valve prolapse (with or without regurgitation), Rheumatic heart disease, Bicuspid aortic valve, Calcified aortic stenosis, ASD, VSD, or PDA repaired > 6 months.

### Dental Procedures Requiring Prophylaxis
All dental procedures that involve:
* **Manipulation of gingival tissue**, OR
* **Manipulation of the periapical region of teeth**, OR
* **Perforation of the oral mucosa** (e.g., extractions, periodontal scaling, root planning, endodontic instrumentation beyond apex, placement of orthodontic bands, subgingival retraction cord).
* *Prophylaxis NOT required for*: Routine local anesthetic injections through non-infected tissue, taking dental radiographs, placement of removable appliances, shedding of deciduous teeth, bleeding from trauma to lips/mucosa.

### Standard Antibiotic Prophylactic Regimens (Administered 30 to 60 Minutes Before Dental Procedure)
| Situation | Antibiotic | Adult Dosing | Pediatric Dosing |
| :--- | :--- | :--- | :--- |
| **Standard Oral Regimen** | **Amoxicillin** | **2.0 g orally** | 50 mg/kg orally |
| **Unable to take Oral Meds** | **Ampicillin** OR **Cefazolin / Ceftriaxone** | 2.0 g IM/IV<br>1.0 g IM/IV | 50 mg/kg IM/IV<br>50 mg/kg IM/IV |
| **Allergic to Penicillin (Oral)** | **Clindamycin**<br>OR **Azithromycin / Clarithromycin**<br>OR **Cephalexin** | **600 mg orally**<br>**500 mg orally**<br>2.0 g orally | 20 mg/kg orally<br>15 mg/kg orally<br>50 mg/kg orally |
| **Allergic to Penicillin (IV)** | **Clindamycin** OR **Cefazolin** | 600 mg IV<br>1.0 g IM/IV | 20 mg/kg IV<br>50 mg/kg IM/IV |"""
            }
        ],
        "comparisons": [
            {
                "title": "Janeway Lesions vs Osler's Nodes",
                "headers": ["Clinical Feature", "Janeway Lesions", "Osler's Nodes"],
                "rows": [
                    ["Pain Sensation", "**Completely Painless** (Non-tender)", "**Exquisitely Painful & Tender**"],
                    ["Primary Mechanism", "**Septic Micro-Emboli** producing microabscesses", "**Immune Complex Deposition** producing vasculitis"],
                    ["Typical Location", "Palms of hands, soles of feet, thenar eminences", "Pulps (pads) of fingers and toes"],
                    ["Lesion Morphology", "Flat, erythematous or hemorrhagic macules", "Raised, violaceous, nodular subcutaneous bumps"],
                    ["Histopathology", "Neutrophilic abscess with microvascular necrosis", "Perivascular lymphocytic infiltrate (leukocytoclastic vasculitis)"],
                    ["Association", "Acute Staphylococcal Endocarditis", "Subacute Streptococcal Endocarditis"]
                ]
            }
        ],
        "must_draw": "Schematic of the heart showing vegetation on the mitral valve, accompanied by an anatomical drawing of the hand depicting painless Janeway lesions on the palm versus painful Osler's nodes on the finger pulps.",
        "viva_questions": [
            "Why is Amoxicillin preferred over Penicillin V for dental endocarditis prophylaxis? (Answer: Amoxicillin has superior gastrointestinal absorption, higher bioavailability, and produces higher sustained bactericidal serum concentrations).",
            "What should you do if a patient forgot to take their antibiotic prophylaxis before an extraction? (Answer: The antibiotic may be administered up to 2 hours AFTER the procedure according to AHA guidelines without compromising prophylactic efficacy).",
            "What is the difference between Janeway lesions and Osler nodes? (Answer: Janeway lesions are painless embolic macules on palms/soles; Osler nodes are painful immune-complex nodules on finger/toe pulps).",
            "Does a patient with mitral valve prolapse with regurgitation require routine antibiotic prophylaxis today? (Answer: NO. Under the revised AHA/ADA guidelines, MVP is no longer classified as highest-risk; prophylaxis is restricted to prosthetic valves, prior IE, and cyanotic CHD)."
        ]
    },
    {
        "id": "chap8_mi_and_ischemia",
        "title": "Ischemic Heart Disease & Acute Myocardial Infarction (STEMI)",
        "badge": "15-Mark Essay Model",
        "category": "Cardiovascular Medicine",
        "reading_time": "15 min read",
        "key_points": [
            "Acute Myocardial Infarction (AMI) is myocardial necrosis resulting from acute, sustained mismatch between myocardial oxygen supply and demand, most commonly caused by rupture of an unstable coronary atheromatous plaque with superimposed occlusive thrombosis.",
            "Universal Definition of MI requires detection of a rise and/or fall of cardiac biomarkers (preferably Cardiac Troponin I or T) with at least one value above the 99th percentile upper reference limit, alongside evidence of acute myocardial ischemia (symptoms, new ECG changes, or imaging proof).",
            "ECG evolution of STEMI: Hyperacute tall peaked T-waves (minutes) ──► ST-segment elevation (hours) ──► Pathological Q-waves (>0.04s, >25% R-wave height) and T-wave inversion (hours to days).",
            "Vascular territories: Anteroseptal (LAD: V1-V4), Inferior (RCA: II, III, aVF), Lateral (LCx: I, aVL, V5-V6), Posterior (circumflex/RCA: reciprocal ST depression in V1-V3).",
            "Immediate MONA emergency resuscitation: Morphine (2-4 mg IV), Oxygen (only if SpO2 < 90%), Nitroglycerin (0.4 mg SL), Aspirin (300 mg chewed) + Clopidogrel (300-600 mg loading).",
            "Reperfusion: Primary Percutaneous Coronary Intervention (PCI) is the gold standard (door-to-balloon time < 90 minutes); if PCI unavailable within 120 minutes, administer fibrinolytic therapy (Tenecteplase / Alteplase; door-to-needle time < 30 minutes).",
            "Dental considerations: Elective dental care contraindicated within 6 months of an uncomplicated MI; epinephrine strictly restricted (maximum 0.04 mg = 2 cartridges of 1:100,000); dual antiplatelet therapy (DAPT) must NOT be discontinued for routine extractions."
        ],
        "clinical_pearl": "Never administer nitrates to a patient presenting with an INFERIOR wall myocardial infarction (leads II, III, aVF) before checking lead V4R for RIGHT VENTRICULAR infarction! In RV infarction, right ventricular output depends entirely on preload; nitrates induce venodilation, causing a catastrophic, life-threatening plunge in cardiac output and profound shock.",
        "sections": [
            {
                "title": "1. Definition, Classification & Pathophysiology",
                "content": """**Definition**: Myocardial Infarction (MI) is defined pathologically as myocardial cell death (coagulative necrosis) attributable to prolonged, severe ischemia.

### Universal Classification of Myocardial Infarction (Fourth Universal Definition)
* **Type 1 MI**: Spontaneous MI related to atherosclerotic plaque rupture, ulceration, fissure, or dissection with intraluminal coronary thrombosis.
* **Type 2 MI**: MI secondary to an ischemic imbalance (mismatch between oxygen demand and supply without plaque rupture: e.g., coronary spasm, severe anemia, tachyarrhythmias, shock).
* **Type 3 MI**: Cardiac death resulting from suspected myocardial ischemia with symptoms before cardiac biomarker results could be obtained.
* **Type 4a/4b MI**: MI associated with Percutaneous Coronary Intervention (PCI) / stent thrombosis.
* **Type 5 MI**: MI associated with Coronary Artery Bypass Graft (CABG) surgery.

### Plaque Rupture & Thrombosis Cascade
```
Atheromatous Plaque with thin fibrous cap & lipid core
               │
               ▼
Hemodynamic shear stress or macrophage metalloproteinases rupture fibrous cap
               │
               ▼
Subendothelial von Willebrand Factor (vWF) & tissue factor exposed to blood
               │
               ▼
Platelet Adhesion (via GP Ib-IX-V) & Platelet Activation (release of TXA2, ADP)
               │
               ▼
Platelet Aggregation via conformational activation of Glycoprotein IIb/IIIa receptors
               │
               ▼
Activation of extrinsic coagulation cascade ──► Thrombin burst ──► Fibrin Meshwork
               │
               ▼
COMPLETE CORONARY OCCLUSION ──► Transmural Ischemia (ST-Elevation MI)
```

**Temporal Progression of Ischemic Cell Death**:
* Reversible injury: 0 to 20 minutes (depletion of ATP, switch to anaerobic glycolysis, lactic acidosis).
* Irreversible injury: Begins at 20–30 minutes in the vulnerable **subendocardium**, spreading wave-like to become transmural over 6 to 12 hours ('Time is Myocardium!')."""
            },
            {
                "title": "2. Clinical Presentation & Physical Examination",
                "content": """### Classical Symptoms
* **Chest Pain**: Severe, crushing, heavy, retrosternal pain described as an elephant sitting on the chest, squeezing, or tight band. Lasts > 20–30 minutes, **unrelieved by rest or sublingual nitroglycerin**.
* **Radiation**: Radiates characteristically to the left arm, inner forearm, shoulder, neck, jaw, interscapular region, or epigastrium.
* **Autonomic Sympathetic Activation**: Profuse cold sweating (diaphoresis), pallor, restlessness, sense of impending doom (*angor animi*).
* **Autonomic Parasympathetic Activation** (especially in inferior MI): Nausea, vomiting, hiccoughs, bradycardia.
* **Silent Myocardial Infarction**: Completely painless or presenting only with sudden dyspnea, confusion, or syncope; occurs in elderly patients and **diabetics** (due to autonomic neuropathy).

### Physical Findings
* Pulse: Tachycardia (anterior MI) or Bradycardia (inferior MI with AV nodal ischemia).
* Blood Pressure: May be elevated (sympathetic drive) or hypotensive (cardiogenic shock / RV infarction).
* Auscultation: Soft S1, paradoxically split S2, prominent S4 gallop (reflecting stiff, non-compliant ischemic ventricle), new apical pansystolic murmur (suggesting acute mitral regurgitation secondary to papillary muscle dysfunction or rupture)."""
            },
            {
                "title": "3. Diagnostic Workup: ECG Localization & Cardiac Biomarkers",
                "content": """### A. Electrocardiographic (ECG) Evolution
1. **Hyperacute Phase (Minutes)**: Tall, peaked, symmetrical T-waves.
2. **Acute Phase (Hours)**: Convex-upward **ST-segment elevation** (J-point elevation ≥ 1 mm in limb leads, ≥ 2 mm in precordial leads V2-V3) with reciprocal ST-depression in opposing leads.
3. **Subacute Phase (Days)**: Development of pathological **Q-waves** (width > 0.04 sec, depth > 25% of following R-wave), loss of R-wave amplitude, and symmetrical **T-wave inversion**.
4. **Chronic / Old MI Phase (Weeks to Months)**: ST-segment returns to baseline; pathological Q-waves persist permanently as an electrical scar.

### Anatomical Localization & Culprit Arteries
| Leads with ST Elevation | Reciprocal ST Depression | Infarcted Anatomical Wall | Culprit Coronary Artery |
| :--- | :--- | :--- | :--- |
| **V1, V2** | None | Interventricular Septum | Left Anterior Descending (LAD) |
| **V3, V4** | None | Anterior Wall | Left Anterior Descending (LAD) |
| **V1 to V4 (or V6)** | II, III, aVF | Extensive Anteroseptal | Proximal LAD ('Widowmaker') |
| **I, aVL, V5, V6** | II, III, aVF | Anterolateral Wall | Left Circumflex (LCx) or Diagonal LAD |
| **II, III, aVF** | I, aVL | Inferior Wall (Diaphragmatic) | Right Coronary Artery (RCA: 85%) or LCx |
| **V4R, V5R** | — | Right Ventricle | Proximal Right Coronary Artery (RCA) |
| **V7, V8, V9** | Tall R & ST depression V1-V3 | True Posterior Wall | Distal LCx or Posterior Descending RCA |

### B. Serum Cardiac Biomarkers
* **Cardiac Troponin I (cTnI) and Troponin T (cTnT)**:
  * Gold standard biomarkers of myocardial necrosis; virtually 100% tissue specific.
  * Rises within **3 to 4 hours**, peaks at **12 to 24 hours**, and remains elevated for **10 to 14 days** (troponin T) or **7 to 10 days** (troponin I).
* **CK-MB (Creatine Kinase-MB isoenzyme)**:
  * Rises in 4–6 hours, peaks at 18–24 hours, normalizes within **48 to 72 hours**.
  * Clinically invaluable for diagnosing **early re-infarction** (since troponins remain elevated for weeks)."""
            },
            {
                "title": "4. Emergency Resuscitation & Reperfusion Strategies",
                "content": """### Initial Emergency Protocol: The 'MONA-B' Bundle
1. **Aspirin**: **300 mg orally CHEWED immediately** (rapid buccal absorption; inhibits thromboxane A2).
2. **P2Y12 Receptor Inhibitor (Dual Antiplatelet Therapy - DAPT)**: **Ticagrelor 180 mg loading dose** (or Prasugrel 60 mg, or Clopidogrel 600 mg).
3. **Nitrates**: **Sublingual Nitroglycerin (0.4 mg)** every 5 minutes (up to 3 doses) for ischemic pain. *Contraindications: Systolic BP < 90 mmHg, suspected Right Ventricular MI, or recent use of Phosphodiesterase-5 inhibitors (Sildenafil within 24h)*.
4. **Analgesia**: **IV Morphine Sulfate (2 to 4 mg IV)** with antiemetic (Metoclopramide 10 mg) for intractable chest pain and anxiety.
5. **Oxygen**: Supplemental $O_2$ indicated **ONLY if oxygen saturation ($SpO_2$) < 90%** (hyperoxia causes reactive coronary vasoconstriction and free radical generation!).
6. **Beta-Blockers**: Oral Metoprolol (25–50 mg) started within 24 hours if hemodynamically stable.
7. **High-Intensity Statin**: **Atorvastatin 80 mg orally OD** immediately.

### Definitive Coronary Reperfusion Therapy
```
                               STEMI CONFIRMED ON ECG
                                         │
        ┌────────────────────────────────┴────────────────────────────────┐
        ▼                                                                 ▼
PCI-Capable Center Available?                                  Non-PCI Capable Center
(Can achieve Door-to-Balloon in < 90-120 min)                             │
        │                                                                 ▼
        ▼                                                   Can transfer to PCI center < 120 min?
PRIMARY PERCUTANEOUS CORONARY                                             │
INTERVENTION (Primary PCI)                                    ┌───────────┴───────────┐
(Catheterization + Balloon + Stent)                           ▼                       ▼
GOLD STANDARD                                                YES                      NO
                                                              │                       │
                                                      Transfer for PCI       IMMEDIATE FIBRINOLYSIS
                                                                             (Door-to-Needle < 30 min)
                                                                             • Tenecteplase (TNK-tPA) IV
                                                                             • IV Unfractionated Heparin
```"""
            },
            {
                "title": "5. Complications of Myocardial Infarction",
                "content": """1. **Arrhythmias (Most common cause of pre-hospital death)**:
   * **Ventricular Fibrillation (VF) / Ventricular Tachycardia (VT)**: Highest risk within first 1–2 hours. Treated with immediate unsynchronized defibrillation.
   * **Bradyarrhythmias & Complete Heart Block (CHB)**: RCA occlusion causes AV nodal ischemia.
2. **Cardiogenic Shock**: Systolic BP < 90 mmHg with hypoperfusion; requires inotropes (Dobutamine), vasopressors (Norepinephrine), and intra-aortic balloon pump (IABP).
3. **Mechanical Complications (Days 3 to 7: Macrophage lysis of necrotic myocardium)**:
   * **Papillary Muscle Rupture**: Acute mitral regurgitation producing catastrophic pulmonary edema.
   * **Ventricular Septal Defect (VSD)**: Harsh holosystolic murmur with thrill at left lower sternal border.
   * **Free Wall Rupture**: Acute cardiac tamponade and electromechanical dissociation (rapidly fatal).
4. **Pericarditis**:
   * Early post-MI pericarditis (Days 2 to 3): Localized friction rub.
   * **Dressler's Syndrome** (Weeks 2 to 10): Autoimmune pericarditis, pleuritis, fever, and leukocytosis."""
            },
            {
                "title": "6. Dental & Maxillofacial Considerations",
                "content": """1. **Elective Treatment Timing**: Postpone all elective dental surgical procedures for **at least 6 months** following an acute myocardial infarction. The risk of re-infarction and perioperative death drops substantially after 6 months.
2. **Local Anesthetic Epinephrine Limits**: Endogenous catecholamines from dental pain/anxiety are far more dangerous than controlled local anesthetic. However, restrict exogenous Epinephrine to a maximum of **0.04 mg per appointment** (equivalent to **2 cartridges of 2% Lignocaine with 1:100,000 epinephrine**). Avoid epinephrine-impregnated gingival retraction cords!
3. **Dual Antiplatelet Therapy (DAPT)**: Patients post-PCI are on lifelong Aspirin (75–100 mg) and 6–12 months of P2Y12 inhibitors (Clopidogrel / Ticagrelor). **DO NOT STOP DAPT FOR DENTAL EXTRACTIONS**; premature discontinuation risks acute, fatal in-stent thrombosis. Minor dental surgical procedures can be safely performed using local hemostatics (Surgicel, tranexamic acid mouthwash, sutures).
4. **Chairside Angina Management Protocol**:
   * Immediately discontinue dental treatment.
   * Place patient in comfortable upright sitting position.
   * Administer sublingual Nitroglycerin spray/tablet (0.4 mg) every 5 minutes (max 3 doses).
   * Check blood pressure and pulse. If pain persists > 10–15 minutes or is accompanied by sweating and vomiting, treat as acute MI: chew 300 mg Aspirin and call emergency ambulance immediately."""
            }
        ],
        "comparisons": [
            {
                "title": "STEMI vs NSTEMI vs Unstable Angina",
                "headers": ["Parameter", "STEMI", "NSTEMI", "Unstable Angina"],
                "rows": [
                    ["Coronary Thrombosis", "Completely Occlusive thrombus", "Partially Occlusive / Microemboli", "Partially Occlusive thrombus"],
                    ["ECG Hallmarks", "ST-segment elevation + Q-waves", "ST-depression or T-wave inversion", "ST-depression or T-inversion or Normal"],
                    ["Cardiac Troponins", "**Markedly Elevated**", "**Elevated above 99th percentile**", "**Normal** (No necrosis)"],
                    ["Transmural Involvement", "Transmural (Full thickness necrosis)", "Subendocardial (Inner 1/3 to 1/2)", "None (Reversible ischemia)"],
                    ["Emergency Fibrinolysis", "Indicated if Primary PCI unavailable", "**Contraindicated / Harmful**", "**Contraindicated**"],
                    ["Emergency Reperfusion", "Immediate emergent PCI (<90 min)", "Early invasive coronary angiogram (<24h)", "Medical stabilization, risk stratification"]
                ]
            }
        ],
        "must_draw": "ECG wave evolution diagram showing the progression: normal baseline ──► hyperacute peaked T-wave ──► marked ST elevation ──► pathological deep Q-wave with inverted T-wave.",
        "viva_questions": [
            "Why is Sublingual Nitroglycerin contraindicated in inferior wall myocardial infarction? (Answer: Inferior MI often involves the right ventricle, which is dependent on preload; nitrates induce venous pooling, collapsing RV stroke volume and precipitating fatal hypotension).",
            "What is the maximum safe dose of epinephrine in a dental patient with ischemic heart disease? (Answer: 0.04 mg of epinephrine, which equals 2 cartridges of 1:100,000 epinephrine).",
            "Why is Troponin preferred over CK-MB for diagnosing acute MI? (Answer: Troponins are cardio-specific with zero skeletal muscle cross-reactivity and remain elevated for 10–14 days, providing a wider diagnostic window).",
            "Should a patient stop taking Aspirin and Clopidogrel before a routine tooth extraction? (Answer: NO. Stopping DAPT dramatically increases the risk of fatal coronary stent thrombosis; minor oral bleeding can be readily controlled with local hemostatics).",
            "What is Dressler's syndrome? (Answer: A secondary autoimmune pericarditis occurring 2 to 10 weeks following a myocardial infarction, presenting with fever, pleuritic chest pain, and pericardial friction rub)."
        ]
    },
    {
        "id": "chap9_heart_failure_and_htn",
        "title": "Heart Failure & Systemic Hypertension",
        "badge": "15-Mark Essay Model",
        "category": "Cardiovascular Medicine",
        "reading_time": "15 min read",
        "key_points": [
            "Heart Failure is a complex clinical syndrome resulting from structural or functional cardiac disorders that impair the ability of the ventricles to fill (diastolic failure) or eject blood (systolic failure).",
            "Physiological Determinants: Cardiac Output (CO) = Stroke Volume x Heart Rate. Stroke volume is governed by Preload (Frank-Starling law), Afterload (systemic vascular resistance), and Myocardial Contractility.",
            "Neurohormonal Compensation: Hypoperfusion triggers the Renin-Angiotensin-Aldosterone System (RAAS) and Sympathetic Nervous System (SNS), initially maintaining blood pressure via salt retention and vasoconstriction, but driving maladaptive ventricular remodeling, myocyte hypertrophy, and progressive fibrosis long-term.",
            "Left Heart Failure causes pulmonary venous congestion (dyspnea, orthopnea, paroxysmal nocturnal dyspnea, basal pulmonary crackles); Right Heart Failure causes systemic venous congestion (elevated JVP, hepatojugular reflux, tender hepatomegaly, bilateral pitting ankle edema).",
            "Systemic Hypertension Classification (JNC-7/8): Normal (<120/<80), Prehypertension (120-139/80-89), Stage 1 (140-159/90-99), Stage 2 (≥160/≥100 mmHg). Hypertensive Crisis: BP >180/120 mmHg (Urgency: no target organ damage; Emergency: active target organ damage like encephalopathy or aortic dissection).",
            "Dental considerations: Patient positioning (avoid supine in orthopnea; treat in semi-fowler position); manage orthostatic hypotension caused by anti-hypertensives; monitor for gingival hyperplasia induced by Calcium Channel Blockers (Amlodipine, Nifedipine)."
        ],
        "clinical_pearl": "Orthopnea (shortness of breath on lying flat) is caused by the gravitational redistribution of peripheral blood from the lower extremities and splanchnic circulation back into the central thoracic circulation when recumbent. In a failing left ventricle, this sudden increase in preload overwhelms the heart, abruptly elevating pulmonary capillary wedge pressure (>20-25 mmHg) and causing alveolar pulmonary edema. Always ask cardiac patients: 'How many pillows do you sleep on at night?'",
        "sections": [
            {
                "title": "1. Heart Failure: Definition, Classifications & Hemodynamics",
                "content": """**Definition**: Heart Failure (HF) is a pathophysiological state in which an abnormality of cardiac function is responsible for the failure of the heart to pump blood at a rate commensurate with the requirements of the metabolizing tissues, or can do so only from an abnormally elevated filling pressure.

### Classification Systems
1. **By Ejection Fraction (European Society of Cardiology - ESC)**:
   * **HFrEF (Heart Failure with Reduced Ejection Fraction)**: Left Ventricular Ejection Fraction (**LVEF < 40%**); true systolic pump failure.
   * **HFmrEF (HF with Mildly Reduced EF)**: LVEF **41% to 49%**.
   * **HFpEF (HF with Preserved Ejection Fraction)**: **LVEF ≥ 50%**; diastolic failure characterized by stiff, non-compliant ventricles with impaired relaxation and elevated filling pressures.
2. **By Anatomical Ventricle**:
   * **Left Heart Failure (LHF)**: Primary backward failure leads to pulmonary congestion; forward failure leads to reduced systemic perfusion.
   * **Right Heart Failure (RHF)**: Most commonly caused by pre-existing Left Heart Failure. Pure RHF without LHF (*Cor Pulmonale*) is caused by severe pulmonary hypertension or chronic lung disease (COPD).
3. **NYHA Functional Classification**:
   * **Class I**: No limitation of physical activity; ordinary physical activity does not cause fatigue or dyspnea.
   * **Class II**: Slight limitation of physical activity; comfortable at rest, but ordinary activity causes symptoms.
   * **Class III**: Marked limitation of physical activity; comfortable at rest, but less than ordinary activity causes fatigue.
   * **Class IV**: Inability to carry on any physical activity without discomfort; symptoms present even at rest."""
            },
            {
                "title": "2. Pathophysiological Cascades & Neurohormonal Compensation",
                "content": """```
Myocardial Injury (MI / Longstanding Hypertension / Cardiomyopathy)
               │
               ▼
Impaired Ventricular Contractility ──► FALL IN CARDIAC OUTPUT (CO)
               │
               ▼
Baroreceptors & Renal Juxtaglomerular Apparatus detect hypoperfusion
               │
        ┌──────┴────────────────────────────────┐
        ▼                                       ▼
SYMPATHETIC NERVOUS SYSTEM (SNS)        RENIN-ANGIOTENSIN-ALDOSTERONE (RAAS)
• Noradrenaline release                 • Renin cleaves Angiotensinogen ──► Angiotensin I
• Beta-1: Tachycardia, contractility    • ACE converts Ang I ──► Angiotensin II
• Alpha-1: Peripheral vasoconstriction  • AT1 Receptor activation: intense vasoconstriction
                                        • Aldosterone release: Sodium & Water Retention
        │                                       │
        └───────────────────────┬───────────────┘
                                ▼
SHORT-TERM: Restores blood pressure & preserves cerebral/coronary perfusion
LONG-TERM: Catastrophic Ventricular Maladaptation:
• Increased Afterload + Preload overload
• Myocyte hypertrophy, apoptosis, interstitial fibrosis
• Downregulation of Beta-1 receptors
• PROGRESSIVE PUMP FAILURE & DILATATION
```

**B-Type Natriuretic Peptide (BNP)**:
Secreted by ventricular cardiomyocytes in response to excessive wall stretch and volume overload. Induces natriuresis, diuresis, and vasodilation, serving as a counter-regulatory brake on RAAS. Serum **BNP > 100 pg/mL** or **NT-proBNP > 300 pg/mL** has >95% negative predictive value for diagnosing acute heart failure in emergency dyspnea."""
            },
            {
                "title": "3. Clinical Presentation: Left vs Right Heart Failure",
                "content": """| Feature | Left-Sided Heart Failure (Pulmonary Congestion) | Right-Sided Heart Failure (Systemic Venous Congestion) |
| :--- | :--- | :--- |
| **Primary Etiologies** | Ischemic Heart Disease, Systemic Hypertension, Aortic/Mitral Valvular Disease | Pre-existing Left Heart Failure (commonest), Cor Pulmonale (COPD, PE), Pulmonary Stenosis |
| **Respiratory Signs** | **Exertional Dyspnea**, **Orthopnea** (worse lying flat), **Paroxysmal Nocturnal Dyspnea (PND)** (wakes gasping at night) | Dyspnea less prominent; fatigue, abdominal fullness, right upper quadrant discomfort |
| **Auscultation** | **Bilateral fine crepitations (crackles)** at lung bases that do not clear with coughing; wheezing (*cardiac asthma*) | Clear lung fields (unless concurrent left failure) |
| **Venous System** | Normal Jugular Venous Pressure (JVP) | **Elevated JVP** with prominent V waves; **Positive Hepatojugular Reflux** |
| **Peripheral Edema** | Absent initially | **Bilateral dependent pitting pedal/ankle edema** (ascends to pretibial, thighs, and presacral area in bedridden patients) |
| **Abdominal Exam** | Normal | **Tender, smooth congestive hepatomegaly**; ascites; splenomegaly |
| **Cardiac Auscultation** | **S3 Gallop** (rapid ventricular filling into dilated ventricle), displaced hyperdynamic apex beat | Right ventricular heave at left sternal edge, S3 gallop, pansystolic murmur of tricuspid regurgitation |"""
            },
            {
                "title": "4. Systemic Hypertension: Definition, JNC Classification & Crisis",
                "content": """**Definition**: Systemic hypertension is a chronic, persistent elevation of systemic arterial blood pressure requiring therapeutic intervention to mitigate cardiovascular, cerebrovascular, and renal morbidity.

### JNC-7 / WHO Blood Pressure Classification (Adults ≥ 18 Years)
| Category | Systolic Blood Pressure (mmHg) | Diastolic Blood Pressure (mmHg) |
| :--- | :---: | :---: |
| **Normal** | < 120 | and < 80 |
| **Prehypertension** | 120 – 139 | or 80 – 89 |
| **Stage 1 Hypertension** | 140 – 159 | or 90 – 99 |
| **Stage 2 Hypertension** | ≥ 160 | or ≥ 100 |

*Etiology*:
* **Primary (Essential) Hypertension (90–95%)**: Multifactorial etiology (genetic susceptibility, high dietary sodium, sympathetic hyperactivity, obesity, insulin resistance).
* **Secondary Hypertension (5–10%)**: Renal parenchymal disease (glomerulonephritis, polycystic kidney), Renovascular (renal artery stenosis), Endocrine (Cushing's syndrome, Conn's syndrome / primary hyperaldosteronism, Pheochromocytoma, Acromegaly), Coarctation of the aorta, Obstructive Sleep Apnea.

### Hypertensive Crisis: Urgency vs Emergency
* **Blood Pressure Threshold**: Systolic BP > 180 mmHg and/or Diastolic BP > 120 mmHg.
* **Hypertensive Urgency**: Severe elevation of BP **WITHOUT acute target organ damage**. Managed outpatient with oral antihypertensives (e.g., Captopril, Labetalol, Amlodipine) over 24 to 48 hours. Rapid IV reduction is contraindicated!
* **Hypertensive Emergency**: Severe elevation of BP **WITH acute, progressive target organ damage** (Hypertensive encephalopathy, acute aortic dissection, acute pulmonary edema, acute MI, or acute renal failure). Requires immediate ICU admission and controlled parenteral therapy (**IV Labetalol, Nicardipine, or Sodium Nitroprusside**) to lower MAP by 20–25% in the first hour."""
            },
            {
                "title": "5. Evidence-Based Management Protocols",
                "content": """### A. Pharmacotherapy for Heart Failure with Reduced Ejection Fraction (The 4 Pillars of Guideline-Directed Medical Therapy - GDMT)
1. **ARNI (Angiotensin Receptor-Neprilysin Inhibitor)**: **Sacubitril / Valsartan** (replaces traditional ACE inhibitors; reduces mortality by 20%).
2. **Beta-Blockers**: **Bisoprolol, Carvedilol, or Metoprolol Succinate** (titrated slowly from low doses; counteracts sympathetic cardiotoxicity).
3. **MRA (Mineralocorticoid Receptor Antagonists)**: **Spironolactone** (25–50 mg OD) or Eplerenone (blocks aldosterone-mediated cardiac fibrosis).
4. **SGLT2 Inhibitors**: **Dapagliflozin (10 mg OD)** or **Empagliflozin (10 mg OD)** (promotes osmotic diuresis, improves myocardial energetics).
* **Symptomatic Congestion Control**: Loop diuretics (**Furosemide 40–80 mg IV/oral**) titrated to achieve euvolemia.

### B. First-Line Antihypertensive Classes (The 'A-C-D' Rule)
* **A**: ACE Inhibitors (Ramipril, Enalapril) or ARBs (Telmisartan, Losartan) — Drug of choice in Diabetics and Chronic Kidney Disease with proteinuria.
* **C**: Calcium Channel Blockers (Amlodipine 5–10 mg OD) — Highly effective in elderly and black populations.
* **D**: Thiazide-like Diuretics (Chlorthalidone 12.5–25 mg OD, Indapamide)."""
            },
            {
                "title": "6. Dental & Maxillofacial Considerations",
                "content": """1. **Patient Positioning**: NEVER place a patient with congestive heart failure into a flat supine position. The sudden increase in venous return precipitates acute orthopnea and pulmonary edema. Always treat in a **semi-reclined (Semi-Fowler: 45 degrees)** position.
2. **Chairside Blood Pressure Cutoffs**:
   * BP < 140/90 mmHg: Routine dental treatment.
   * BP 140–159 / 90–99 mmHg: Recheck BP; routine treatment with stress-reduction protocol.
   * BP 160–179 / 100–109 mmHg: Defer elective surgical treatment; urgent palliative dental care with minimal local anesthetic.
   * **BP ≥ 180 / ≥ 110 mmHg: STRICT CONTRAINDICATION TO DENTAL CARE**. Refer immediately to physician or emergency room.
3. **Drug-Induced Gingival Enlargement**: **Calcium Channel Blockers** (especially **Nifedipine**, and less frequently **Amlodipine**) induce fibrous gingival hyperplasia. Starts in interdental papillae; exacerbated by local plaque accumulation. Management includes meticulous plaque control and physician consultation to substitute with an ACE inhibitor or ARB.
4. **Postural (Orthostatic) Hypotension**: Antihypertensives (alpha-blockers, ACEi, diuretics) predispose patients to orthostatic pooling. Raise the dental chair slowly and have the patient sit for 2 minutes before standing to prevent syncope."""
            }
        ],
        "comparisons": [
            {
                "title": "Left Heart Failure vs Right Heart Failure",
                "headers": ["Clinical Parameter", "Left-Sided Heart Failure", "Right-Sided Heart Failure"],
                "rows": [
                    ["Predominant Congestion", "Pulmonary Venous Congestion", "Systemic Venous (Caval) Congestion"],
                    ["Primary Symptoms", "Dyspnea, Orthopnea, Paroxysmal Nocturnal Dyspnea", "Ankle swelling, Abdominal fullness, Anorexia"],
                    ["Lung Examination", "Bilateral basal crepitations, Cardiac asthma", "Clear lung fields (unless secondary to LHF)"],
                    ["Jugular Venous Pressure", "Normal", "Markedly Elevated with positive Hepatojugular Reflux"],
                    ["Liver & Abdomen", "Normal liver size", "Congestive hepatomegaly ('Nutmeg liver'), Ascites"],
                    ["Peripheral Edema", "Absent in isolated LHF", "Prominent bilateral dependent pitting pedal edema"]
                ]
            }
        ],
        "must_draw": "Hemodynamic Frank-Starling curve comparing the normal myocardium against the depressed, flattened curve of Heart Failure, indicating the shift following diuretic and inotropic therapy.",
        "viva_questions": [
            "Why is the semi-supine position mandatory when treating heart failure patients in the dental chair? (Answer: Placing the patient supine increases venous return, overloading the failing left ventricle and triggering acute pulmonary edema and severe orthopnea).",
            "Which class of antihypertensive medications classically produces drug-induced gingival hyperplasia? (Answer: Dihydropyridine Calcium Channel Blockers, most notably Nifedipine and Amlodipine).",
            "What is the difference between Hypertensive Urgency and Hypertensive Emergency? (Answer: Both feature severe BP elevation >180/120 mmHg, but Hypertensive Emergency is defined by the presence of acute, progressive target organ damage like encephalopathy, dissection, or pulmonary edema).",
            "What is the significance of serum BNP in emergency dyspnea? (Answer: BNP is released by ventricular stretch; a normal level (<100 pg/mL) reliably rules out heart failure with >95% negative predictive value, pointing to pulmonary causes like COPD or asthma)."
        ]
    },
    {
        "id": "chap10_congenital_heart_diseases",
        "title": "Congenital Heart Diseases: ASD, VSD, PDA & Tetralogy of Fallot",
        "badge": "15-Mark Essay Model",
        "category": "Cardiovascular Medicine",
        "reading_time": "15 min read",
        "key_points": [
            "Congenital Heart Diseases (CHD) are structural cardiac malformations present at birth, broadly classified into Acyanotic (Left-to-Right shunts: ASD, VSD, PDA) and Cyanotic (Right-to-Left shunts: Tetralogy of Fallot, Transposition of Great Arteries).",
            "Ventricular Septal Defect (VSD) is the most common congenital cardiac malformation overall (~30-40%); classified into Perimembranous (75-80%) and Muscular.",
            "Eisenmenger Syndrome represents the irreversible reversal of an uncorrected long-standing left-to-right shunt into a right-to-left shunt secondary to severe, fixed pulmonary arterial hypertension and vascular remodeling.",
            "Atrial Septal Defect (ASD) features the pathognomonic physical finding: Fixed, widely split second heart sound (S2) with an ejection systolic murmur at the pulmonary area.",
            "Tetralogy of Fallot (TOF) is the most common cyanotic congenital heart disease in children surviving infancy, characterized by a tetrad: Pulmonary Stenosis (infundibular), Ventricular Septal Defect, Overriding of the Aorta, and Right Ventricular Hypertrophy (RVH).",
            "Classic 'tet spell' (hypercyanotic paroxysm): Triggered by crying/exertion; managed by placing the child in the **Knee-Chest position** (increases systemic vascular resistance, reducing right-to-left shunting).",
            "Dental considerations: High risk of Infective Endocarditis and brain abscesses in cyanotic CHD; strict AHA antibiotic prophylaxis mandatory."
        ],
        "clinical_pearl": "Children with Tetralogy of Fallot characteristically SQUAT during physical exertion or crying spells. Squatting kinks the femoral arteries, instantly increasing Systemic Vascular Resistance (SVR / afterload). By Ohm's law, higher left ventricular pressure forces less desaturated blood across the VSD into the aorta and drives more blood through the stenotic pulmonary outflow tract into the lungs, rapidly relieving hypoxia!",
        "sections": [
            {
                "title": "1. Definition, Classifications & Hemodynamic Principles",
                "content": """**Definition**: Congenital Heart Disease (CHD) refers to any structural abnormality of the heart or intrathoracic great vessels that develops during embryological cardiogenesis and is present at birth.

### Major Hemodynamic Classification
```
                           CONGENITAL HEART DISEASES
                                      │
        ┌─────────────────────────────┴─────────────────────────────┐
        ▼                                                           ▼
ACYANOTIC CONGENITAL HEART DISEASE                          CYANOTIC CONGENITAL HEART DISEASE
(Left-to-Right Shunt: Pulmonary Plethora)                   (Right-to-Left Shunt: Systemic Desaturation)
(Acyanotic initially; late reversal)                        (Early Central Cyanosis, Clubbing, Polycythemia)
        │                                                           │
  ┌─────┴────────────────────────┐                            ┌─────┴────────────────────────┐
  ▼                              ▼                            ▼                              ▼
INCREASED PULMONARY FLOW       OBSTRUCTIVE (No shunt)       DECREASED PULMONARY FLOW       INCREASED PULMONARY FLOW
• Ventricular Septal Defect    • Coarctation of Aorta       • Tetralogy of Fallot (TOF)    • Transposition of Great
• Atrial Septal Defect         • Aortic Stenosis            • Tricuspid Atresia              Arteries (TGA)
• Patent Ductus Arteriosus     • Pulmonary Stenosis                                        • Truncus Arteriosus
```

### The Eisenmenger Phenomenon
When a large, uncorrected left-to-right shunt (VSD, PDA, ASD) persists, chronic hyperperfusion and high pressure induce irreversible remodeling of the pulmonary arterial bed (plexiform lesions, medial hypertrophy). Once Pulmonary Vascular Resistance (PVR) exceeds Systemic Vascular Resistance (SVR), **the shunt reverses from Right-to-Left**, causing intractable cyanosis, polycythemia, clubbing, and biventricular failure. At this stage, surgical closure of the defect is **strictly contraindicated** because the defect acts as a pressure-relief pop-off valve."""
            },
            {
                "title": "2. Atrial Septal Defect (ASD)",
                "content": """* **Pathology**: Defect in the interatrial septum allowing oxygenated blood to shunt from the left atrium into the right atrium.
* **Anatomical Types**:
  1. **Ostium Secundum (75%)**: Mid-septal defect at fossa ovalis (commonest; female predominance 2:1).
  2. **Ostium Primum (15%)**: Low septal defect adjacent to AV valves (part of endocardial cushion defect).
  3. **Sinus Venosus (5–10%)**: Near junction of SVC or IVC; associated with anomalous pulmonary venous drainage.
* **Hemodynamics**: Left atrial pressure (8–10 mmHg) > Right atrial pressure (3–5 mmHg). Diastolic volume overload of the right ventricle leads to pulmonary plethora.
* **Physical Findings**:
  * **Fixed, Wide Splitting of S2**: Pathognomonic finding. S2 remains widely split and does NOT change with inspiration/expiration (the continuous left-to-right shunt keeps the right ventricle filled, delaying pulmonary valve closure fixedly).
  * **Pulmonary Ejection Systolic Murmur**: Soft (Grade 2–3/6) murmur at left 2nd intercostal space caused by **increased flow volume across the normal pulmonary valve** (NOT flow across the defect itself, as ASD is low-velocity and silent!)."""
            },
            {
                "title": "3. Ventricular Septal Defect (VSD)",
                "content": """* **Epidemiology**: Most common congenital heart lesion (30–40% of all CHD).
* **Anatomical Types**:
  1. **Perimembranous (75–80%)**: Located in membranous septum beneath aortic valve; high tendency to spontaneously close in infancy.
  2. **Muscular (Trabecular: 15–20%)**: Located in thick muscular septum; often multiple (*'Swiss-cheese VSD'*).
  3. **Infundibular (Supracristal / Outlet: 5%)**: Beneath pulmonary valve; high risk of aortic valve prolapse and regurgitation.
* **Hemodynamics & Clinical Signs**:
  * **Small VSD (Maladie de Roger)**: Hemodynamically trivial, normal pulmonary pressures, but produces a **loud, harsh, high-pitched Holosystolic Murmur with systolic thrill** at the left 3rd/4th intercostal space. (Counter-intuitive rule: Small defect = high velocity jet = loud murmur; Large defect = low resistance = soft murmur!).
  * **Large VSD**: High flow leads to left ventricular volume overload, congestive heart failure in infancy (tachypnea, failure to thrive), and early Eisenmenger transformation."""
            },
            {
                "title": "4. Patent Ductus Arteriosus (PDA)",
                "content": """* **Pathology**: Failure of the embryonic ductus arteriosus (connecting proximal descending aorta to left pulmonary artery) to functionally close within 48 hours after birth. Strongly associated with **prematurity** and congenital rubella infection.
* **Physical Findings**:
  * **Continuous 'Machinery' Murmur (Gibson Murmur)**: Best heard at left 1st and 2nd intercostal space infraclavicular area. Murmur begins after S1, builds up to a peak at S2, and envelopes S2 into diastole.
  * **Collapsing / Water-Hammer Pulse** with wide pulse pressure (aortic diastolic runoff into pulmonary artery).
* **Medical Management in Premature Infants**: Pharmacological closure using IV **Indomethacin** or **Ibuprofen** (potent prostaglandin synthesis inhibitors; prostaglandins maintain patency of ductus)."""
            },
            {
                "title": "5. Tetralogy of Fallot (TOF)",
                "content": """TOF results from a single developmental error: **Anterior and cephalad deviation of the infundibular (outlet) septum**.

### The Anatomical Tetrad
1. **Pulmonary Stenosis (Subvalvular Infundibular Stenosis)**: Determines the clinical severity and degree of cyanosis.
2. **Ventricular Septal Defect (VSD)**: Large, unrestrictive perimembranous defect.
3. **Overriding of the Aorta**: Aorta straddles the VSD, receiving blood directly from both ventricles.
4. **Right Ventricular Hypertrophy (RVH)**: Develops secondary to the high resistance offered by the pulmonary infundibular stenosis.

```
Infundibular Spasm / Crying / Stress
               │
               ▼
Increased Pulmonary Vascular Outflow Obstruction
               │
               ▼
Massive Right-to-Left Shunting across VSD into Aorta
               │
               ▼
PROFOUND SYSTEMIC HYPOXEMIA ──► 'TET SPELL' (Hypercyanotic Paroxysm)
               │
               ▼
Squatting / Knee-Chest Position ──► Kinks Femoral Arteries ──► INCREASES SVR
               │
               ▼
Reverses Shunt ──► Forces blood into Pulmonary Artery ──► RELIEF OF SPELL
```

* **Physical Findings & Imaging**:
  * Central cyanosis of lips and tongue, digital clubbing (*drumstick fingers*), polycythemia.
  * Single S2 with an ejection systolic murmur across the pulmonary outflow tract (murmur softens during a tet spell due to complete outflow occlusion).
  * **Chest X-Ray**: Classic **'Coeur en sabot' (Boot-shaped heart)**: Upturned cardiac apex due to right ventricular hypertrophy with a concave pulmonary artery segment."""
            },
            {
                "title": "6. Dental & Maxillofacial Considerations",
                "content": """1. **Infective Endocarditis Risk**: Patients with unrepaired cyanotic CHD (TOF) or patients with repaired defects with residual shunts represent the **Highest Risk Group** under AHA guidelines. **Prophylactic Amoxicillin 2.0 g orally** 30–60 minutes before any invasive dental procedure is mandatory!
2. **Paradoxical Emboli & Brain Abscess**: In right-to-left shunts (TOF, Eisenmenger), venous micro-thrombi or oral bacteremia completely bypass the pulmonary capillary filtration bed and enter the systemic circulation directly, lodging in cerebral microvessels and causing **cryptogenic cerebral abscesses**.
3. **Secondary Polycythemia & Coagulopathy**: Chronic hypoxemia triggers massive erythropoietin release, elevating hematocrit (>60%). This produces severe blood hyperviscosity and secondary platelet dysfunction with bleeding tendencies. Order pre-op CBC and coagulation screen prior to exodontia."""
            }
        ],
        "comparisons": [
            {
                "title": "Tetralogy of Fallot vs Ventricular Septal Defect",
                "headers": ["Clinical Feature", "Tetralogy of Fallot (TOF)", "Ventricular Septal Defect (VSD)"],
                "rows": [
                    ["Shunt Direction", "Right-to-Left Shunt (Cyanotic)", "Left-to-Right Shunt (Acyanotic)"],
                    ["Cyanosis at Birth/Infancy", "**Prominent Central Cyanosis Present**", "**Strictly Absent** (Pink baby)"],
                    ["Pulmonary Blood Flow", "**Decreased** (Oligemic lung fields)", "**Increased** (Pulmonary plethora)"],
                    ["Classical Physical Sign", "Squatting relief, Hypercyanotic tet spells", "Failure to thrive, recurrent pneumonia"],
                    ["Chest X-Ray Silhouette", "'Boot-shaped heart' (*Coeur en sabot*)", "Cardiomegaly with prominent pulmonary artery"],
                    ["Endocarditis Prophylaxis", "**Mandatory for Life** (Cyanotic)", "Only if residual defect adjacent to patch"]
                ]
            }
        ],
        "must_draw": "Schematic of the 4 anatomical defects of Tetralogy of Fallot (infundibular PS, perimembranous VSD, overriding aorta, RVH) alongside the classic 'boot-shaped' heart silhouette on chest radiography.",
        "viva_questions": [
            "Why does a child with Tetralogy of Fallot squat during distress? (Answer: Squatting compresses the femoral arteries, increasing systemic vascular resistance (SVR), which forces more blood across the pulmonary artery to be oxygenated rather than shunting right-to-left).",
            "What is the characteristic murmur of Patent Ductus Arteriosus? (Answer: A continuous, rough, machinery-like murmur (Gibson murmur) heard in the left 1st and 2nd intercostal space, peaking at S2).",
            "What is Eisenmenger syndrome? (Answer: Reversal of an uncorrected long-standing left-to-right shunt into a right-to-left shunt secondary to irreversible pulmonary vascular remodeling and fixed pulmonary arterial hypertension).",
            "Why is the second heart sound (S2) fixed and widely split in Atrial Septal Defect? (Answer: The persistent left-to-right shunt continuously overloads the right ventricle, delaying pulmonic valve closure equally during both inspiration and expiration).",
            "What drug is used to medically close a PDA in premature infants? (Answer: Intravenous Indomethacin or Ibuprofen, which inhibit prostaglandin synthesis)."
        ]
    }
]
