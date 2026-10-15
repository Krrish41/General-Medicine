# -*- coding: utf-8 -*-
"""
General Medicine: Gastroenterology, Hepatology & Nutrition
Chapters:
1. Acute Viral Hepatitis & Chronic Hepatitis (Hepatitis A, B, C, D, E)
2. Acute Liver Failure & Hepatic Encephalopathy
3. Cirrhosis of the Liver & Portal Hypertension
4. Protein Energy Malnutrition (Kwashiorkor vs Marasmus)
5. Dysphagia & Peptic Ulcer Disease
"""

CHAPTERS = [
    {
        "id": "chap1_viral_hepatitis",
        "title": "Acute Viral Hepatitis & Chronic Viral Hepatitis",
        "badge": "15-Mark Essay Model",
        "category": "Gastroenterology & Hepatology",
        "reading_time": "14 min read",
        "key_points": [
            "Hepatitis B virus (Hepadnavirus) is a 42 nm double-shelled Dane particle with outer HBsAg, inner HBcAg, and soluble HBeAg indicating active viral replication.",
            "Incubation periods: HAV (15-45 days), HBV (30-180 days), HCV (15-150 days), HDV (30-50 days), HEV (15-60 days).",
            "Chronic hepatitis is defined as sustained hepatic necroinflammation persisting for ≥ 6 months; primary etiologies are HBV, HCV, HDV, and autoimmune hepatitis.",
            "Serological window period in HBV: HBsAg has cleared but anti-HBs is not yet detectable; anti-HBc IgM is the sole serological marker of acute infection.",
            "First-line antiviral therapies: Tenofovir disoproxil fumarate (TDF 300 mg OD) or Entecavir (ETV 0.5 mg OD); Direct-Acting Antivirals (DAAs: Sofosbuvir + Velpatasvir) achieve >95% sustained virological response (SVR) in HCV.",
            "Dental considerations: High risk of cross-infection via saliva and blood; universal barrier precautions mandatory; post-exposure prophylaxis with Hepatitis B Immune Globulin (HBIG 0.06 mL/kg within 24h) plus accelerated vaccination."
        ],
        "clinical_pearl": "During the 'window period' of acute Hepatitis B infection, HBsAg is negative and anti-HBs has not yet appeared. The ONLY diagnostic marker present is IgM anti-HBc. Always order anti-HBc IgM when acute viral hepatitis is clinically suspected despite negative HBsAg.",
        "sections": [
            {
                "title": "1. Definition, Classification & Viral Taxonomy",
                "content": """**Definition**: Acute viral hepatitis is a systemic infection predominantly affecting the liver parenchyma, caused by hepatotropic viruses leading to hepatocellular necrosis, inflammation, and clinical jaundice.

### Hepatotropic Viruses Classification
| Virus | Family | Genome | Transmission | Incubation | Carrier State / Chronicity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **HAV** | Picornaviridae | ssRNA | Feco-oral (water/food) | 15–45 days | None (0%) |
| **HBV** | Hepadnaviridae | dsDNA (circular) | Parenteral, Sexual, Perinatal | 30–180 days | Adults: 5–10%; Neonates: 90% |
| **HCV** | Flaviviridae | ssRNA | Parenteral (blood/IVDU), Sexual | 15–150 days | High (75–85% chronicity) |
| **HDV** | Deltaviridae | Defective circular RNA | Parenteral (Requires HBsAg) | 30–50 days | Co-infection: <5%; Superinfection: >80% |
| **HEV** | Hepeviridae | ssRNA | Feco-oral (waterborne) | 15–60 days | None (Fulminant in pregnancy: 20%) |

**Structure of HBV (The Dane Particle)**:
* 42 nm intact virion with an outer lipoprotein envelope containing **HBsAg** (surface antigen).
* Inner 27 nm icosahedral nucleocapsid core containing **HBcAg** (core antigen), partially double-stranded circular DNA genome, and viral DNA polymerase (reverse transcriptase).
* **HBeAg** is a soluble secretory protein cleaved from pre-core protein; acts as a quantitative surrogate marker for active viral replication, high infectivity, and transmission risk."""
            },
            {
                "title": "2. Etiopathogenesis & Immunopathology",
                "content": """The hepatitis B and C viruses are **non-cytopathic**. Hepatocellular destruction is mediated entirely by the host's cellular immune response.

```
HBV Virion enters hepatocyte via NTCP receptor
               │
               ▼
Uncoating & transport of relaxed circular DNA to nucleus
               │
               ▼
Conversion to Covalently Closed Circular DNA (cccDNA) — persistent nuclear reservoir
               │
               ▼
Transcription of pre-genomic RNA & viral translation
               │
               ▼
Viral peptides (HBcAg, HBeAg) presented on MHC Class I molecules
               │
               ▼
Host Cytotoxic CD8+ T-Lymphocytes recognize viral epitopes
               │
               ├── Robust Immune Response (Adults) ──► Rapid viral clearance + Acute Self-limiting Hepatitis
               └── Impaired Immune Response (Neonates/Immunocompromised) ──► Incomplete clearance + Chronic Persistent Inflammation + Fibrogenesis
```

**Layman's Explanation**: The Hepatitis B virus itself does not poison the liver cell. Instead, it hides inside the liver cells to make copies of itself. The body's immune police (T-cells) spot the viral fingerprints on the outside of the cell and fire upon the infected liver cells to destroy the viral hideouts. If the immune response is strong, the virus is wiped out, but the liver takes temporary damage (acute hepatitis). If the immune system is weak or tolerates the virus, low-grade fighting continues for decades, eventually causing scar tissue (cirrhosis) and cancer."""
            },
            {
                "title": "3. Clinical Presentation & Phases of Illness",
                "content": """Acute viral hepatitis evolves through four distinct clinical stages:

1. **Incubation Period**: Asymptomatic viral replication; variable duration based on viral agent.
2. **Prodromal (Pre-icteric) Phase (3 to 14 days)**:
   * Constitutional symptoms: malaise, profound fatigue, anorexia, nausea, vomiting, low-grade fever.
   * **Serum sickness-like syndrome**: Seen in 10–20% of acute HBV (type III immune-complex hypersensitivity): urticaria, maculopapular rash, arthralgias, and polyarthritis.
   * Right upper quadrant dull aching pain due to stretching of Glisson's capsule.
   * Alteration in taste and smell; classic revulsion to cigarette smoke (*aversio a fumo*).
3. **Icteric Phase (1 to 4 weeks)**:
   * Jaundice: yellowish discoloration first detected in sclera (elastin affinity for bilirubin) when serum bilirubin exceeds 2.5–3.0 mg/dL.
   * Dark, tea-colored urine (conjugated bilirubinuria) preceding overt jaundice.
   * Pale, clay-colored stools (temporary intrahepatic canalicular cholestasis).
   * Hepatomegaly (smooth, tender liver edge palpable 2–3 cm below right costal margin).
   * Mild splenomegaly (10–15% of cases) and cervical lymphadenopathy.
4. **Convalescent (Post-icteric) Phase (2 to 12 weeks)**:
   * Resolution of jaundice, return of appetite, biochemical normalization."""
            },
            {
                "title": "4. Diagnostic Serology & Laboratory Workup",
                "content": """### HBV Serological Marker Interpretation Guide
| HBsAg | Anti-HBs | Anti-HBc IgM | Anti-HBc IgG | HBeAg | Anti-HBe | Interpretation |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **+** | – | **+** | – | **+** | – | **Acute Hepatitis B (Early, High Infectivity)** |
| – | – | **+** | – / + | – | + / – | **Window Period (Core window)** |
| **+** | – | – | **+** | **+** | – | **Chronic Hepatitis B (High replication, Wild-type)** |
| **+** | – | – | **+** | – | **+** | **Chronic Hepatitis B (Low replication or Pre-core mutant)** |
| – | **+** | – | **+** | – | + / – | **Natural Immunity (Resolved prior HBV infection)** |
| – | **+** | – | – | – | – | **Vaccine-Induced Immunity (Recombinant HBsAg only)** |

* **Liver Function Tests (LFTs)**:
  * Serum Transaminases (ALT & AST): Markedly elevated (>1,000–3,000 IU/L); ALT typically exceeds AST (ALT > AST ratio), reflecting diffuse hepatocellular lysis.
  * Serum Bilirubin: Both conjugated and unconjugated fractions elevated (typically 5–20 mg/dL).
  * Alkaline Phosphatase (ALP): Mildly elevated (< 3x upper limit of normal).
  * **Prothrombin Time (PT / INR)**: The most sensitive and critical prognostic marker of synthetic liver function. A prolonged PT (INR > 1.5) heralds acute liver failure!"""
            },
            {
                "title": "5. Comprehensive Medical Management & Prevention",
                "content": """### A. Acute Viral Hepatitis Management
* **Conservative Supportive Care**:
  * Physical rest titrated to fatigue; prolonged bed rest is unnecessary once symptoms improve.
  * Nutritional support: High-carbohydrate, moderate-protein diet (1.0–1.2 g/kg); small frequent meals to combat morning nausea.
  * Complete avoidance of hepatotoxic drugs (acetaminophen, NSAIDs, erythromycin) and alcohol for at least 6 months.
* **Hospitalization Criteria**:
  * Prolonged PT / INR > 1.5.
  * Inability to maintain oral hydration due to intractable vomiting.
  * Any signs of hepatic encephalopathy (altered sleep, asterixis, confusion).
  * Serum bilirubin > 20 mg/dL.

### B. Chronic Hepatitis B Pharmacotherapy
* **Indications**: Serum HBV DNA > 2,000 IU/mL, elevated ALT (>2x ULN), or evidence of moderate-to-severe histological fibrosis on elastography/biopsy.
* **First-Line Nucleos(t)ide Analogs (High barrier to resistance)**:
  * **Tenofovir Disoproxil Fumarate (TDF)**: 300 mg orally once daily. Monitor renal function and bone mineral density.
  * **Tenofovir Alafenamide (TAF)**: 25 mg orally once daily (preferable in patients with renal impairment or osteoporosis).
  * **Entecavir (ETV)**: 0.5 mg orally once daily (1.0 mg in decompensated cirrhosis).
* **Pegylated Interferon-alpha (PEG-IFN-α-2a)**: 180 mcg subcutaneously weekly for 48 weeks (in young patients with well-compensated liver disease, high ALT, and low HBV DNA wishing to avoid lifelong therapy).

### C. Immunoprophylaxis Protocols
* **Active Immunization**: Recombinant Hepatitis B Vaccine (containing HBsAg):
  * Dosing schedule: 0, 1, and 6 months (20 mcg IM into deltoid muscle).
  * Protective anti-HBs titer: ≥ 10 mIU/mL confirmed 1–2 months post-series.
* **Passive Immunization**: Hepatitis B Immune Globulin (HBIG):
  * Prepared from hyperimmune human plasma containing high titers of anti-HBs.
  * Dosing: 0.06 mL/kg IM administered within 24 hours of exposure."""
            },
            {
                "title": "6. Dental & Maxillofacial Considerations",
                "content": """1. **Infection Control**: HBV is 100x more infectious than HIV; can survive on dried operatory surfaces for >7 days. Universal precautions, autoclave validation, and sharps safety are legally and clinically mandatory.
2. **Dental Healthcare Personnel (DHCP) Immunization**: All clinical dental personnel must complete the 3-dose HBV vaccination series and demonstrate anti-HBs seroconversion (>10 mIU/mL).
3. **Bleeding Risk Assessment**: In patients with chronic hepatitis or liver dysfunction, request pre-op CBC (platelets), PT/INR, and LFTs. If INR > 2.0 or platelets < 50,000/mm³, defer elective exodontia or arrange hospital-based correction (Vitamin K 10 mg IV or Fresh Frozen Plasma).
4. **Analgesic & Sedative Prescriptions**: Avoid paracetamol doses > 2 g/day; completely avoid NSAIDs in cirrhotic patients due to precipitating acute renal failure (hepatorenal syndrome) and upper GI hemorrhage."""
            }
        ],
        "comparisons": [
            {
                "title": "Hepatitis A vs Hepatitis B vs Hepatitis C",
                "headers": ["Feature", "Hepatitis A (HAV)", "Hepatitis B (HBV)", "Hepatitis C (HCV)"],
                "rows": [
                    ["Viral Family", "Picornavirus (RNA)", "Hepadnavirus (DNA)", "Flavivirus (RNA)"],
                    ["Primary Transmission", "Feco-oral (Water/Food)", "Parenteral, Sexual, Perinatal", "Parenteral (Blood/IVDU)"],
                    ["Chronicity Rate", "0% (Never chronic)", "5–10% adults (90% infants)", "75–85% (High chronicity)"],
                    ["Diagnostic Hallmarks", "Anti-HAV IgM", "HBsAg, Anti-HBc IgM", "Anti-HCV, HCV RNA PCR"],
                    ["Vaccine Availability", "Inactivated virus vaccine", "Recombinant HBsAg vaccine", "No vaccine currently available"],
                    ["Primary Complication", "Rare fulminant in elderly", "Cirrhosis, Hepatocellular CA", "Cirrhosis, Hepatocellular CA"]
                ]
            }
        ],
        "must_draw": "Schematic of the 42 nm HBV Dane particle showing outer HBsAg envelope, inner HBcAg nucleocapsid, dsDNA circle, and DNA polymerase; accompanied by the serological time-course curve indicating HBsAg, Anti-HBc IgM, Anti-HBc IgG, and the Core Window Period.",
        "viva_questions": [
            "What is the 'window period' in acute Hepatitis B, and which marker proves infection during it? (Answer: Time between disappearance of HBsAg and appearance of Anti-HBs; Anti-HBc IgM is the sole marker).",
            "What is the difference between HBeAg and anti-HBe? (Answer: HBeAg indicates active viral replication and high infectivity; anti-HBe indicates low viral replication and lower transmission risk).",
            "Why is Hepatitis D called a defective virus? (Answer: HDV requires the outer HBsAg envelope of HBV to assemble virions and infect hepatocytes).",
            "What is the dental post-exposure protocol following an accidental needle-stick from an HBsAg-positive patient in an unvaccinated operator? (Answer: Administer HBIG 0.06 mL/kg IM within 24 hours AND initiate the accelerated Hepatitis B vaccination series at 0, 1, and 2 months)."
        ]
    },
    {
        "id": "chap2_acute_liver_failure",
        "title": "Acute Liver Failure & Hepatic Encephalopathy",
        "badge": "15-Mark Essay Model",
        "category": "Gastroenterology & Hepatology",
        "reading_time": "15 min read",
        "key_points": [
            "Acute Liver Failure (ALF) is defined as acute liver injury with coagulopathy (INR ≥ 1.5) and hepatic encephalopathy in a patient without pre-existing cirrhosis, evolving within 26 weeks.",
            "Sub-classification based on jaundice-to-encephalopathy interval: Hyperacute (< 7 days, paracetamol), Acute (8–28 days, viral), Subacute (5–26 weeks, drug-induced non-paracetamol).",
            "Pathophysiology: Massive hepatocyte necrosis leads to loss of metabolic clearance of ammonia, neurotoxins, and false neurotransmitters (octopamine), driving astrocyte swelling and cytotoxic cerebral edema.",
            "West Haven Criteria grades encephalopathy from Grade 1 (inverted sleep cycle, mild confusion) to Grade 4 (deep coma, decerebrate posturing).",
            "Definitive four-pillar management: Gut sterilization (Rifaximin 550 mg BD or Neomycin 1g QID), nitrogen flushing via Lactulose (30–60 mL titrating to 2–3 soft stools/day), cerebral edema control (20% Mannitol 0.5–1.0 g/kg or 3% hypertonic saline), and N-acetylcysteine (NAC) infusion.",
            "King's College Hospital Criteria define urgent criteria for emergency orthotopic liver transplantation."
        ],
        "clinical_pearl": "Asterixis (flapping tremor) is elicited by asking the patient to extend their arms with wrists dorsiflexed and fingers spread with eyes closed. It is NOT specific to hepatic encephalopathy; it also occurs in uremia, severe hypercapnia (CO2 narcosis), and hypomagnesemia.",
        "sections": [
            {
                "title": "1. Definition, Classification & Etiology",
                "content": """**Definition**: Acute Liver Failure (ALF) is a rapid deterioration of liver function resulting in altered mental status (hepatic encephalopathy) and coagulopathy (INR ≥ 1.5) in an individual with no prior history of liver disease or underlying cirrhosis.

### O'Grady Classification of Acute Liver Failure
| Category | Jaundice to Encephalopathy Onset | Common Etiologies | Cerebral Edema Risk | Prognosis without Transplant |
| :--- | :--- | :--- | :--- | :--- |
| **Hyperacute** | < 7 days | Paracetamol toxicity, HAV, HEV, Ischemia | High | Moderate (Best survival: 35%) |
| **Acute** | 8 to 28 days | HBV, Wilson's disease, Autoimmune hepatitis | High | Poor (~20% survival) |
| **Subacute** | 5 to 26 weeks | Idiosyncratic drug-induced liver injury (DILI) | Low | Very Poor (<15% survival) |

### Etiological Spectrum
1. **Dose-Dependent Hepatotoxins**:
   * **Paracetamol (Acetaminophen)**: Leading cause in the Western world. Toxic metabolite **NAPQI** (N-acetyl-p-benzoquinone imine) depletes glutathione stores, inducing centrilobular (Zone 3) hepatic necrosis.
2. **Idiosyncratic Drug Reactions**: Isoniazid, Rifampicin, Pyrazinamide, Phenytoin, Valproate, NSAIDs.
3. **Infectious**: Viral hepatitis (HBV, HBV+HDV superinfection, HAV, HEV especially in pregnancy, HSV, CMV).
4. **Vascular & Hemodynamic**: Budd-Chiari syndrome (acute hepatic vein thrombosis), ischemic hepatitis ('shock liver').
5. **Metabolic & Miscellaneous**: Wilson's disease (acute fulminant presentation with Coombs-negative hemolytic anemia), Acute Fatty Liver of Pregnancy (AFLP), Amanita phalloides mushroom poisoning."""
            },
            {
                "title": "2. Pathophysiology of Hepatic Encephalopathy & Cerebral Edema",
                "content": """Hepatic encephalopathy (HE) is a neuropsychiatric syndrome caused by biochemical failure of the liver to clear gut-derived neurotoxins:

```
Gut microbiota deaminate proteins & urea
               │
               ▼
Production of Ammonia (NH3) absorbed into portal circulation
               │
               ▼
Failing liver cannot detoxify NH3 via Urea Cycle (Krebs-Henseleit)
               │
               ▼
Systemic Hyperammonemia crosses Blood-Brain Barrier (BBB)
               │
               ▼
Astrocyte Glutamine Synthetase converts Ammonia + Glutamate ──► Glutamine
               │
               ▼
Excessive intracellular Glutamine exerts potent Osmotic Effect
               │
               ▼
Astrocyte Swelling & Cytotoxic Cerebral Edema
               │
               ▼
Increased Intracranial Pressure (ICP) ──► Brainstem Herniation (Leading cause of death!)
```

**Additional Pathophysiological Contributors**:
* **GABA-Benzodiazepine Neurotransmission**: Increased endogenous neurosteroids enhancing inhibitory GABAergic tone.
* **False Neurotransmitters**: Impaired hepatic amino acid metabolism leads to elevated Aromatic Amino Acids (AAA: phenylalanine, tyrosine) relative to Branched-Chain Amino Acids (BCAA: leucine, isoleucine, valine). AAAs cross the BBB and synthesize weak false neurotransmitters (**octopamine**, **phenylethylamine**), displacing true dopamine and norepinephrine."""
            },
            {
                "title": "3. Clinical Staging: The West Haven Criteria",
                "content": """| Grade | Consciousness & Alertness | Intellectual Function & Behavior | Neurological & Motor Signs |
| :---: | :--- | :--- | :--- |
| **Grade 1** | Inverted sleep pattern (daytime somnolence, nocturnal insomnia); mild restlessness | Shortened attention span, impaired arithmetic (serial 7s), mild euphoria/anxiety | Slight tremor, impaired handwriting / constructional apraxia |
| **Grade 2** | Lethargy, apathy, slow response to commands | Obvious personality changes, inappropriate behavior, spatial disorientation | **Asterixis (flapping tremor)** clearly elicited; hypoactive reflexes |
| **Grade 3** | Somnolent but arousable to verbal stimuli; marked confusion | Gross disorientation to time/place, incomprehensible speech, bizarre behavior | Marked asterixis, hyperreflexia, muscle rigidity, positive Babinski sign |
| **Grade 4** | **Deep Coma**: Unresponsive to voice; variable response to noxious/painful stimuli | Absent intellectual function | Decerebrate / decorticate posturing; dilated, sluggish pupils (herniation risk) |"""
            },
            {
                "title": "4. Diagnostic Workup & Prognostic Criteria",
                "content": """### Laboratory Investigations
* **Coagulation Profile**: PT / INR (hallmark of synthetic failure; INR ≥ 1.5 required for diagnosis), factor V levels (< 20–30% indicates grave prognosis).
* **Arterial Ammonia**: Elevated (> 100–150 mcmol/L correlates with high risk of herniation).
* **Arterial Blood Gas (ABG)**: Metabolic acidosis (lactic acidosis due to impaired clearance and tissue hypoperfusion).
* **Metabolic Screen**: Hypoglycemia (impaired gluconeogenesis and glycogenolysis; check capillary glucose hourly!).
* **Infectious & Toxic Screen**: Paracetamol serum levels, viral hepatitis serologies (IgM anti-HAV, HBsAg, IgM anti-HBc, IgM anti-HEV), ceruloplasmin/urinary copper.

### King's College Hospital Criteria for Emergency Liver Transplantation
* **Paracetamol-Induced ALF**:
  * Arterial pH < 7.30 (irrespective of encephalopathy grade), **OR**
  * All three of: PT > 100 seconds (INR > 6.5) + Serum Creatinine > 3.4 mg/dL (300 mcmol/L) + Grade 3/4 Encephalopathy.
* **Non-Paracetamol ALF**:
  * PT > 100 seconds (INR > 6.5), **OR**
  * Any three of the following five:
    1. Etiology: idiosyncratic drug reaction, seronegative hepatitis.
    2. Age < 10 or > 40 years.
    3. Jaundice-to-encephalopathy interval > 7 days.
    4. PT > 50 seconds (INR > 3.5).
    5. Serum Bilirubin > 17.5 mg/dL (300 mcmol/L)."""
            },
            {
                "title": "5. Comprehensive Intensive Care & Medical Management",
                "content": """### A. General Intensive Care Resuscitation
1. **Airway Management**: Elective endotracheal intubation for Grade 3 or 4 encephalopathy to prevent pulmonary aspiration and control hypercapnia.
2. **Hemodynamics**: Maintain Mean Arterial Pressure (MAP) ≥ 75 mmHg and Cerebral Perfusion Pressure (CPP) 60–80 mmHg. Fluid resuscitation with balanced crystalloids; first-line vasopressor is **Noradrenaline** (Norepinephrine).
3. **Glycemic Control**: Continuous IV infusion of 10% or 20% Dextrose to maintain blood glucose 140–180 mg/dL.
4. **Stress Ulcer Prophylaxis**: IV PPI (Pantoprazole 40 mg OD).

### B. Specific Pharmacotherapy for Hepatic Encephalopathy
1. **Lactulose (Non-absorbable Synthetic Disaccharide)**:
   * Dose: 30–60 mL orally or via NG tube every 2–4 hours initially, titrated to achieve **2 to 3 soft bowel movements per day**.
   * Mechanisms of Action:
     * *Osmotic Laxative*: Flushes nitrogenous waste and bacteria out of the colon.
     * *Colonic Acidification*: Gut colonic bacteria ferment lactulose into lactic and acetic acids, dropping colonic pH below 5.0. This converts diffusible ammonia ($NH_3$) into non-absorbable ammonium ions ($NH_4^+$), trapping them in the stool (**ion trapping**).
     * *Inhibition of Urease-producing Bacteria*.
2. **Gut-Targeted Non-absorbable Antibiotics**:
   * **Rifaximin**: 550 mg orally twice daily. Minimally absorbed (<0.4%) rifamycin derivative that eradicates ammoniagenic gut bacteria with minimal systemic toxicity.
   * **Neomycin**: 1 g orally every 6 hours (alternative, monitor for ototoxicity and nephrotoxicity).
3. **L-Ornithine L-Aspartate (LOLA)**: 20–30 g/day IV infusion; provides substrates for hepatic urea synthesis and skeletal muscle glutamine synthesis.

### C. Management of Raised Intracranial Pressure & Cerebral Edema
* Elevate head of the bed to 30 degrees (promotes jugular venous drainage).
* Target Serum Sodium: 145–150 mEq/L using **3% Hypertonic Saline** infusion.
* **Osmotic Diuretics**: **Mannitol 20%** (0.5 to 1.0 g/kg IV bolus over 15 minutes), repeatable if serum osmolality remains < 320 mOsm/kg.
* Avoid hypothermia, fever, and violent agitation (judicious sedation with Propofol).

### D. Specific Antidote Therapy
* **N-Acetylcysteine (NAC)**:
  * For paracetamol overdose: IV loading dose 150 mg/kg over 1 hour, followed by 50 mg/kg over 4 hours, then 100 mg/kg over 16 hours. Replenishes hepatic glutathione.
  * Also proven beneficial in non-paracetamol ALF by improving systemic microcirculatory hemodynamics."""
            }
        ],
        "comparisons": [
            {
                "title": "Hyperacute vs Acute vs Subacute Liver Failure",
                "headers": ["Parameter", "Hyperacute ALF", "Acute ALF", "Subacute ALF"],
                "rows": [
                    ["Timeframe", "< 7 days", "8 to 28 days", "5 to 26 weeks"],
                    ["Primary Cause", "Paracetamol, HAV, HEV", "Hepatitis B", "Idiosyncratic DILI"],
                    ["Jaundice Severity", "Mild to Moderate", "Marked", "Severe"],
                    ["Coagulopathy", "Very Marked (High INR)", "Marked", "Variable"],
                    ["Cerebral Edema", "High Frequency (~70%)", "High Frequency (~60%)", "Low Frequency (<15%)"],
                    ["Transplant-Free Survival", "Favorable (~35–40%)", "Poor (~20%)", "Extremely Poor (<15%)"]
                ]
            }
        ],
        "must_draw": "Biochemical flowchart of colonic ammonia production, hepatic urea cycle bypass, blood-brain barrier transit, astrocyte glutamine swelling, and the ion-trapping mechanism of Lactulose.",
        "viva_questions": [
            "Why is protein NOT permanently restricted in hepatic encephalopathy today? (Answer: Protein-calorie malnutrition accelerates muscle wasting; skeletal muscle is crucial for peripheral ammonia detoxification. Provide 1.2–1.5 g/kg/day of protein once acute crisis stabilizes).",
            "What is the difference between asterixis and tremors? (Answer: Asterixis is negative myoclonus—a sudden brief loss of postural tone followed by a rapid compensatory recovery flick—not a rhythmic oscillation).",
            "Why must sedatives and benzodiazepines be strictly avoided in patients with liver failure? (Answer: Impaired hepatic clearance leads to drug accumulation, and baseline up-regulated cerebral GABA receptors cause catastrophic coma).",
            "What is the role of Rifaximin in HE? (Answer: Eradicates ammoniagenic bacterial flora in the colon with negligible systemic absorption)."
        ]
    },
    {
        "id": "chap3_cirrhosis_portal_htn",
        "title": "Cirrhosis of the Liver & Portal Hypertension",
        "badge": "15-Mark Essay Model",
        "category": "Gastroenterology & Hepatology",
        "reading_time": "16 min read",
        "key_points": [
            "Cirrhosis is the irreversible end-stage histological alteration of the liver characterized by diffuse parenchymal extinction, hepatic fibrosis, and conversion of normal vascular architecture into structurally abnormal regenerative nodules.",
            "Morphological classification: Micronodular (< 3 mm nodules, Laennec's, alcoholic), Macronodular (> 3 mm nodules, viral post-necrotic), Mixed.",
            "Portal hypertension is defined as a hepatic venous pressure gradient (HVPG) > 5 mmHg; clinically significant portal hypertension (CSPH) occurs when HVPG ≥ 10 mmHg.",
            "Child-Pugh Score stratifies surgical risk and cirrhosis prognosis based on 5 parameters: Bilirubin, Albumin, INR, Ascites, and Encephalopathy (Class A: 5-6, Class B: 7-9, Class C: 10-15).",
            "Complications triad: Ascites (SAAG ≥ 1.1 g/dL indicates portal hypertension), Bleeding Esophageal Varices (EVBL + Terlipressin), and Hepatorenal Syndrome.",
            "Dental considerations: Severe coagulopathy, thrombocytopenia secondary to hypersplenism, high risk of acute bacteremia requiring antibiotic prophylaxis, and altered drug metabolism."
        ],
        "clinical_pearl": "The Serum-Ascites Albumin Gradient (SAAG) is calculated as: [Serum Albumin] - [Ascitic Fluid Albumin]. A SAAG ≥ 1.1 g/dL reliably indicates Portal Hypertension (hydrostatic transudate with >97% accuracy), distinguishing cirrhosis or heart failure from peritoneal tuberculosis or peritoneal carcinomatosis (SAAG < 1.1 g/dL).",
        "sections": [
            {
                "title": "1. Definition, Classification & Etiological Spectrum",
                "content": """**Definition**: Cirrhosis is a chronic, diffuse, progressive pathological entity defined by a pathological triad:
1. Diffuse hepatocellular degeneration and necrosis.
2. Extensive collagenous interstitial **fibrosis** (bridging portoportal and portocentral septa).
3. Parenchymal nodular regeneration replacing normal lobular architecture.

### Morphological Classification
* **Micronodular Cirrhosis (Laennec's)**: Nodules uniform and small (< 3 mm in diameter). Classically seen in chronic alcohol abuse, hemochromatosis, and biliary obstruction.
* **Macronodular Cirrhosis (Post-necrotic)**: Nodules of variable size (> 3 mm to several centimeters), separated by broad fibrous scars. Classically seen in chronic viral hepatitis (HBV, HCV) and alpha-1 antitrypsin deficiency.
* **Mixed Cirrhosis**: Features of both micro and macronodules present simultaneously.

### Major Etiological Categories
1. **Alcoholic Liver Disease (ALD)**: Chronic ethanol consumption exceeding 30–40 g/day.
2. **Chronic Viral Hepatitis**: Persistent Hepatitis B, C, and D infections.
3. **Non-Alcoholic Fatty Liver Disease (NAFLD / MASH)**: Metabolic dysfunction-associated steatohepatitis driven by insulin resistance, type 2 diabetes, and obesity.
4. **Autoimmune & Cholestatic**: Primary Biliary Cholangitis (PBC), Primary Sclerosing Cholangitis (PSC), Autoimmune Hepatitis.
5. **Inherited & Metabolic**: Hereditary Hemochromatosis (HFE mutation), Wilson's disease (ATP7B mutation), Alpha-1 Antitrypsin deficiency, Glycogen storage diseases.
6. **Vascular**: Budd-Chiari syndrome, severe chronic right heart failure (*cardiac cirrhosis*)."""
            },
            {
                "title": "2. Pathogenesis of Fibrogenesis & Portal Hypertension",
                "content": """The central driver of hepatic fibrosis is the activation of **Hepatic Stellate Cells (Ito cells)** residing in the subendothelial space of Disse:

```
Chronic Hepatic Injury (Alcohol / Viral / Steatosis)
               │
               ▼
Damaged hepatocytes & activated Kupffer cells release TGF-beta1, PDGF, TNF-alpha
               │
               ▼
Quiescent Stellate Cells (Vitamin A storing) transdifferentiate into Myofibroblasts
               │
               ▼
Massive synthesis of Collagen Types I & III in Space of Disse
               │
               ▼
Loss of sinusoidal endothelial fenestrations ('Capillarization of sinusoids')
               │
               ▼
Marked Increase in Sinusoidal Resistance (Ohm's Law: Delta P = Q x R)
               │
               ▼
Splanchnic Arteriolar Vasodilation (Nitric Oxide overproduction) ──► Hyperdynamic Circulation
               │
               ▼
PORTAL HYPERTENSION (HVPG > 10 mmHg)
```

**Portosystemic Collateral Pathways**:
1. **Gastroesophageal Junction**: Left gastric (coronary) vein anastomoses with azygos veins ──► **Esophageal Varices**.
2. **Anterior Abdominal Wall**: Paraumbilical veins within falciform ligament communicate with superior and inferior epigastric veins ──► **Caput Medusae**.
3. **Rectal Submucosa**: Superior rectal vein (portal) communicates with middle and inferior rectal veins (internal iliac) ──► **Rectal Varices**.
4. **Retroperitoneal**: Veins of Retzius communicate with lumbar veins."""
            },
            {
                "title": "3. Clinical Manifestations: Stigmata of Chronic Liver Disease",
                "content": """Clinical features reflect two fundamental mechanisms: **Hepatocellular Failure** and **Portal Hypertension**.

### Cutaneous & Peripheral Stigmata (Hyperestrogenism & Vasodilation)
* **Spider Telangiectasia (Spider Naevi)**: Central pulsating arteriole with radiating blanching capillaries, located in vascular territory of SVC (face, neck, upper chest).
* **Palmar Erythema**: Symmetrical mottling and redness over thenar and hypothenar eminences.
* **Gynecomastia, Testicular Atrophy, and Loss of Body Hair** in males (impaired hepatic clearance of androstenedione with peripheral conversion to estrogens).
* **Dupuytren's Contracture**: Palmar fascial thickening, strongly associated with alcoholic etiology.
* **Nail Signs**: Terry's nails (white proximal nailbed with narrow pink distal band), Muehrcke's lines (paired horizontal white bands indicating hypoalbuminemia), clubbing.

### Manifestations of Portal Hypertension
* **Ascites**: Shifting dullness (> 500 mL fluid), fluid thrill (> 1500–2000 mL fluid), abdominal distension, everted umbilicus.
* **Splenomegaly**: Congestive enlargement causing **Hypersplenism** (pancytopenia: thrombocytopenia, leukopenia, anemia).
* **Caput Medusae**: Radiating tortuous veins around the umbilicus."""
            },
            {
                "title": "4. Clinical Staging: The Child-Pugh & MELD Scores",
                "content": """### Child-Turcotte-Pugh (CTP) Scoring System
| Assessment Parameter | 1 Point | 2 Points | 3 Points |
| :--- | :---: | :---: | :---: |
| **Serum Bilirubin (mg/dL)** | < 2.0 | 2.0 – 3.0 | > 3.0 |
| **Serum Albumin (g/dL)** | > 3.5 | 2.8 – 3.5 | < 2.8 |
| **Prothrombin Time (INR)** | < 1.7 | 1.7 – 2.3 | > 2.3 |
| **Ascites** | None | Mild / Medically Controlled | Moderate to Severe / Refractory |
| **Hepatic Encephalopathy** | None | Grade 1 or 2 | Grade 3 or 4 |

**Classification & Perioperative Mortality**:
* **Class A (Score 5–6)**: Well-compensated cirrhosis; 1-year survival 100%; elective surgery well tolerated (operative mortality ~10%).
* **Class B (Score 7–9)**: Significant functional compromise; 1-year survival 80%; elective surgery carries substantial risk (operative mortality ~30%).
* **Class C (Score 10–15)**: Decompensated cirrhosis; 1-year survival 45%; elective surgery is strictly contraindicated (operative mortality >70–80%).

**MELD Score (Model for End-Stage Liver Disease)**:
Calculated using a logarithmic formula incorporating: **Serum Bilirubin, Serum Creatinine, INR, and Serum Sodium**. Used universally for donor liver allocation prioritization."""
            },
            {
                "title": "5. Evidence-Based Management of Major Complications",
                "content": """### A. Management of Acute Variceal Bleeding
1. **Initial Resuscitation**: Hemodynamic stabilization with packed RBCs; target restrictive hemoglobin of **7 to 8 g/dL** (over-transfusion increases portal pressure and precipitates rebleeding!).
2. **Vasoactive Drug Therapy**: Start immediately upon suspicion before endoscopy:
   * **Terlipressin**: 2 mg IV bolus every 4 hours (splanchnic vasoconstrictor), OR **Octreotide** (50 mcg IV bolus followed by 50 mcg/hr continuous infusion).
3. **Endoscopic Therapy**: Urgent upper GI endoscopy within 12 hours:
   * **Endoscopic Variceal Band Ligation (EVBL)** is the gold standard definitive therapy.
4. **Prophylactic Antibiotics**: IV **Ceftriaxone 1g/day** for 7 days (prevents spontaneous bacterial peritonitis and bacteremia).
5. **Refractory Bleeding**: Balloon tamponade (Sengstaken-Blakemore tube) as a temporary bridge (<24h) to **TIPS (Transjugular Intrahepatic Portosystemic Shunt)**.
6. **Secondary Prophylaxis**: Combination of repeat EVBL every 2–4 weeks until eradication PLUS non-selective beta-blockers (**Carvedilol 6.25–12.5 mg OD** or **Propranolol 20–40 mg BD**).

### B. Management of Ascites
* **Dietary Sodium Restriction**: Restrict dietary sodium to **2 g/day (88 mmol/day)**.
* **Dual Diuretic Therapy**:
  * **Spironolactone** (Aldosterone antagonist): 100 mg orally OD, titrated up to 400 mg OD.
  * **Furosemide** (Loop diuretic): 40 mg orally OD, titrated up to 160 mg OD.
  * Maintain the classic 100:40 ratio to preserve normokalemia.
* **Large-Volume Paracentesis (LVP)**: For tense ascites; administer **IV Albumin (6 to 8 g per liter of fluid removed)** if > 5 liters are drained to prevent paracentesis-induced circulatory dysfunction (PICD).

### C. Spontaneous Bacterial Peritonitis (SBP)**:
* Diagnostic paracentesis showing ascitic neutrophil count **≥ 250 PMNs/mm³**.
* Drug of choice: IV **Ceftriaxone 2 g OD** for 5 days."""
            },
            {
                "title": "6. Dental & Maxillofacial Management in Cirrhosis",
                "content": """1. **Bleeding Risk**: Impaired synthesis of clotting factors (II, VII, IX, X) and thrombocytopenia (<50,000/mm³ from hypersplenism). Pre-op PT/INR and platelets mandatory. Minor extractions can proceed if INR ≤ 2.5 and platelets ≥ 50,000/mm³ using local hemostatics (oxidized cellulose, tranexamic acid 5% mouthwash, figure-of-8 sutures).
2. **Analgesic Prescriptions**: Avoid paracetamol > 2 g/day. Completely avoid all NSAIDs (Ibuprofen, Diclofenac) because they inhibit renal prostaglandins, precipitating acute renal failure (Hepatorenal Syndrome) and blunting diuretic efficacy.
3. **Antibiotic Cover**: Cirrhotic patients are severely immunocompromised (impaired reticuloendothelial clearance); provide prophylactic antibiotic cover for invasive dental procedures to prevent bacteremic seeding of ascites (SBP) or heart valves."""
            }
        ],
        "comparisons": [
            {
                "title": "High SAAG vs Low SAAG Ascites",
                "headers": ["Parameter", "High SAAG (≥ 1.1 g/dL)", "Low SAAG (< 1.1 g/dL)"],
                "rows": [
                    ["Pathophysiology", "Portal Hypertension (Increased hydrostatic capillary pressure)", "Peritoneal Inflammation / Malignancy (Increased vascular permeability)"],
                    ["Ascitic Protein", "Usually low (< 2.5 g/dL in cirrhosis; > 2.5 g/dL in cardiac)", "High (> 2.5 g/dL)"],
                    ["Primary Causes", "Cirrhosis, Congestive Heart Failure, Budd-Chiari syndrome", "Peritoneal Carcinomatosis, Tubercular Peritonitis, Nephrotic syndrome"],
                    ["Response to Diuretics", "Good response (Sodium restriction + Spironolactone)", "Poor response (Requires specific etiology treatment)"]
                ]
            }
        ],
        "must_draw": "Anatomical diagram of portal venous circulation showing the 4 portosystemic collateral sites: gastroesophageal varices, caput medusae, rectal hemorrhoidal plexus, and retroperitoneal veins.",
        "viva_questions": [
            "Why is Carvedilol preferred over Propranolol for portal hypertension? (Answer: Carvedilol combines non-selective beta-blockade (beta-1 and beta-2) with alpha-1 receptor blockade, reducing intrahepatic vascular resistance as well as splanchnic inflow, achieving greater HVPG reduction).",
            "Why does splenomegaly cause thrombocytopenia in cirrhosis? (Answer: Portal hypertension causes passive splenic venous congestion; the enlarged spleen sequesters up to 90% of circulating platelets (hypersplenism)).",
            "What is the mechanism of Spider Naevi? (Answer: Impaired hepatic metabolism of circulating estrogens leads to arteriolar dilation; pressing on the central arteriole blanches the radiating capillaries).",
            "What is the minimum platelet count required for routine dental extraction in a cirrhotic patient? (Answer: 50,000 /mm³, accompanied by local hemostatic measures)."
        ]
    },
    {
        "id": "chap4_protein_energy_malnutrition",
        "title": "Protein Energy Malnutrition: Kwashiorkor vs Marasmus",
        "badge": "15-Mark Essay Model",
        "category": "Nutrition & Pediatrics",
        "reading_time": "12 min read",
        "key_points": [
            "Protein-Energy Malnutrition (PEM) represents a spectrum of clinical conditions ranging from pure protein deficiency (Kwashiorkor) to severe caloric-energy deprivation (Marasmus).",
            "Wellcome Trust Classification: Body weight calculated as % of expected 50th percentile: Marasmus (<60% weight without edema), Kwashiorkor (60-80% weight with edema), Marasmic-Kwashiorkor (<60% weight with edema).",
            "Pathophysiology of Kwashiorkor edema: Inadequate dietary protein with preserved carbohydrate intake stimulates insulin, suppressing lipolysis. Severe hypoalbuminemia (< 2.0 g/dL) causes loss of plasma oncotic pressure, driving generalized extracellular fluid extravasation.",
            "Pathophysiology of Marasmus: Chronic total starvation leads to low insulin and elevated cortisol, driving massive mobilization of subcutaneous fat and skeletal muscle proteolysis for gluconeogenesis, producing the classical 'skin and bones' appearance.",
            "Key clinical signs of Kwashiorkor: 'Moon face', 'flaky paint' dermatosis, 'flag sign' alternating hair pigmentation, hepatomegaly due to fatty infiltration.",
            "WHO 10-Step 3-Phase Management Protocol: Phase 1: Stabilization (Days 1–7: hypoglycemia, hypothermia, dehydration with ReSoMal, F-75 milk), Phase 2: Transition (Days 8–14: F-100 milk), Phase 3: Rehabilitation (Weeks 2–6: catch-up growth)."
        ],
        "clinical_pearl": "NEVER refeed a child with severe acute malnutrition aggressively with high protein or high sodium. Sudden carbohydrate loads trigger massive intracellular shifts of phosphate, potassium, and magnesium (**Refeeding Syndrome**), causing acute fatal congestive heart failure and cardiac arrest. Always begin with low-protein, low-sodium F-75 formula.",
        "sections": [
            {
                "title": "1. Definition, Classifications & Epidemiology",
                "content": """**Definition**: Protein-Energy Malnutrition (PEM) is a pathological state of undernutrition resulting from varying degrees of deficient intake of protein and energy substrates, frequently compounded by recurrent infectious diarrheas.

### Wellcome Trust Working Party Classification
| Category | Weight for Age (% of Expected) | Bilateral Pitting Edema |
| :--- | :---: | :---: |
| **Underweight** | 60% – 80% | Absent |
| **Nutritional Marasmus** | < 60% | Absent |
| **Kwashiorkor** | 60% – 80% | **Present** |
| **Marasmic-Kwashiorkor** | < 60% | **Present** |

* **Gomez Classification**: Based on weight-for-age: Grade I (Mild: 75–90%), Grade II (Moderate: 60–74%), Grade III (Severe: < 60%).
* **Waterlow Classification**: Distinguishes **Stunting** (height-for-age: chronic malnutrition) from **Wasting** (weight-for-height: acute malnutrition)."""
            },
            {
                "title": "2. Pathophysiological Mechanisms: Why Kwashiorkor Differs from Marasmus",
                "content": """```
                        DIETARY DEPRIVATION
                                │
        ┌───────────────────────┴───────────────────────┐
        ▼                                               ▼
SEVERE ENERGY (CALORIC) DEFICIT                SELECTIVE PROTEIN DEFICIT
      (Starvation)                           (Starchy carbohydrate diet)
        │                                               │
        ▼                                               ▼
Decreased Blood Glucose                         Preserved Blood Glucose
        │                                               │
        ▼                                               ▼
Low Insulin / High Glucagon & Cortisol          Normal to High Insulin Levels
        │                                               │
        ▼                                               ▼
Maximal Lipolysis & Proteolysis                 Inhibition of Lipolysis & Proteolysis
        │                                               │
        ▼                                               ▼
Subcutaneous fat melted away                    Subcutaneous fat preserved
Gross muscle wasting                            Impaired hepatic protein synthesis
        │                                               │
        ▼                                               ▼
'Skin and Bone' Old Man Facies                  HYPOALBUMINEMIA (< 2.0 g/dL)
NO EDEMA (Marasmus)                             Marked reduction in oncotic pressure
                                                Decreased apolipoprotein synthesis (Fatty Liver)
                                                        │
                                                        ▼
                                                GENERALIZED PITTING EDEMA (Kwashiorkor)
```

**Layman's Explanation**: Imagine your body as a car. In **Marasmus**, there is no fuel of any kind coming in (total starvation). The engine has to burn whatever it has—first the fat stored in the gas tank, then the metal parts of the frame (muscles)—until only the skeletal chassis remains. In **Kwashiorkor**, you are pouring sugar water into the tank (carbohydrates) but no engine oil (protein). The engine gets fooled by the sugar into thinking everything is fine, so it does not burn fat, but the liver cannot build the vital blood proteins needed to keep fluid inside the pipes. The fluid leaks out into the body tissues, swelling the child with water like a balloon (edema)."""
            },
            {
                "title": "3. Clinical Features & Diagnostic Contrasts",
                "content": """### Clinical Signs of Kwashiorkor
* **Edema**: Cardinal feature; begins in feet and ankles (bilateral pedal pitting edema), progressing to legs, hands, and periorbital tissues.
* **Facies**: 'Moon face'—rounded, puffy, edematous cheeks.
* **Psychological State**: Apathetic, miserable, irritable, lethargic, constantly whining, unresponsive to play.
* **Cutaneous Manifestations ('Flaky Paint' Dermatosis)**: Hyperpigmented patches that crack, desquamate, and peel off like dried outdoor paint, exposing raw, weeping hypopigmented areas underneath (seen in groin, thighs, buttocks).
* **Hair Changes ('Flag Sign')**: Depigmentation; alternating horizontal bands of pale red/blonde and dark hair corresponding to alternating periods of poor and adequate protein intake. Hair is sparse, dry, and easily plucked out without pain.
* **Hepatomegaly**: Markedly enlarged, soft, smooth liver due to massive triglyceride accumulation (**fatty liver**) resulting from failure to synthesize apolipoprotein B-100.

### Clinical Signs of Marasmus
* **Severe Wasting**: Loss of subcutaneous fat and muscle mass.
* **Facies**: 'Old man' / 'Monkey facies' due to loss of buccal fat pads (**Bichat's sucking pads**—the last fat reserve to disappear).
* **Skin**: Loose, redundant, wrinkly, bag of bones appearance; prominent ribs (*rosary appearance*).
* **Abdomen**: Protuberant or scaphoid; no hepatomegaly (no fatty liver).
* **Appetite**: Voracious appetite (ravenous hunger), alert and anxious."""
            },
            {
                "title": "4. WHO 10-Step 3-Phase Management Protocol",
                "content": """The World Health Organization (WHO) establishes three precise therapeutic phases:

### Phase 1: Initial Stabilization (Days 1 to 7)
Focuses on reversing immediate life threats without overwhelming metabolic reserves:
1. **Treat / Prevent Hypoglycemia**: Feed immediately with 10% Dextrose (50 mL bolus) or starter formula; feed every 2 hours day and night.
2. **Treat / Prevent Hypothermia**: Keep warm (target rectal temp ≥ 36.5°C); 'kangaroo mother care' (skin-to-skin contact).
3. **Treat / Prevent Dehydration**: **DO NOT USE STANDARD IV FLUIDS** (risk of acute congestive heart failure). Use specialized oral rehydration solution: **ReSoMal** (Rehydration Solution for Malnutrition: low sodium 45 mmol/L, high potassium 40 mmol/L, magnesium 3 mmol/L). Dosing: 5 mL/kg every 30 minutes for the first 2 hours, then 5–10 mL/kg/hr for 4–10 hours.
4. **Correct Electrolyte Imbalances**: All severely malnourished children have excess total body sodium with severe intracellular **Potassium and Magnesium depletion**. Supplements added to feeds (Potassium 3–4 mmol/kg/day, Magnesium 0.4–0.6 mmol/kg/day).
5. **Treat / Prevent Infections**: Routine broad-spectrum antibiotics even in the absence of fever: Oral Amoxicillin (15 mg/kg 8-hourly) for 5 days or IV Ampicillin + Gentamicin if lethargic.
6. **Correct Micronutrient Deficiencies**: High-dose **Vitamin A** on Day 1, Day 2, and Day 14. Daily Folic Acid (5 mg Day 1, then 1 mg/day), Zinc (2 mg/kg/day), Copper. **Do NOT give Iron in Phase 1** (free iron promotes bacterial sepsis and oxidative cellular death).
7. **Initiate Starter Feeds (F-75 Milk)**: Low-protein, low-energy formula (75 kcal/100 mL, 0.9 g protein/100 mL) administered at 100 mL/kg/day in 8 to 12 feeds.

### Phase 2: Transition (Days 8 to 14)
* Switch from F-75 to **F-100 Formula** (100 kcal/100 mL, 2.9 g protein/100 mL).
* Increase volume gradually by 10 mL per feed until the child reaches 150–200 kcal/kg/day.

### Phase 3: Rehabilitation & Catch-Up Growth (Weeks 2 to 6)
* Readiness criteria: Good appetite, complete loss of edema.
* Transition to **Ready-to-Use Therapeutic Food (RUTF)** (peanut-butter paste fortified with milk powder, vitamins, and minerals).
* **Start Iron Therapy**: Ferrous sulfate (3 mg elemental iron/kg/day) to treat nutritional anemia.
* Sensory stimulation, maternal education, and immunization."""
            },
            {
                "title": "5. Oral & Dental Manifestations of Malnutrition",
                "content": """1. **Enamel Hypoplasia**: Severe nutritional insult during amelogenesis (first 3 years of life) results in linear enamel hypoplasia, pitted defective enamel, and heightened vulnerability to rapid dental caries.
2. **Delayed Tooth Eruption**: Significant chronological delay in the eruption of deciduous and permanent dentition.
3. **Atrophic Glossitis & Angular Cheilitis**: Smooth, beefy red, depapillated tongue secondary to concurrent B-complex and iron deficiencies.
4. **Noma (Cancrum Oris)**: Rapidly progressive, gangrenous stomatitis of the orofacial tissues occurring almost exclusively in severely malnourished children (Kwashiorkor) with concurrent measles or malaria. Driven by anaerobic fusospirochetal bacteria (*Fusobacterium necrophorum* and *Prevotella intermedia*), causing extensive ischemic destruction of the cheek, lips, and facial bones."""
            }
        ],
        "comparisons": [
            {
                "title": "Kwashiorkor vs Nutritional Marasmus",
                "headers": ["Clinical Feature", "Kwashiorkor", "Nutritional Marasmus"],
                "rows": [
                    ["Deficiency", "Severe Protein deficiency with preserved calories", "Total Starvation (Both Protein and Caloric deficiency)"],
                    ["Typical Age", "1 to 3 years (After weaning)", "< 1 year (Infancy)"],
                    ["Subcutaneous Fat", "Preserved", "Completely absent / melted away"],
                    ["Muscle Wasting", "Mild to moderate (masked by edema)", "Gross and severe"],
                    ["Bilateral Pitting Edema", "**Mandatory Hallmark Present**", "**Strictly Absent**"],
                    ["Facial Appearance", "'Moon face' (puffy, edematous)", "'Old man / Monkey facies' (sunken, dry)"],
                    ["Liver", "Enlarged, soft fatty liver (Hepatomegaly)", "Normal size, no fatty changes"],
                    ["Dermatosis & Hair", "'Flaky paint' skin, 'Flag sign' hair", "Skin dry, thin, loose; hair normal"],
                    ["Serum Albumin", "Severely Reduced (< 2.0 g/dL)", "Normal or slightly reduced (> 2.8 g/dL)"],
                    ["Appetite & Mood", "Anorexic, miserable, irritable, apathetic", "Ravenously hungry, alert"]
                ]
            }
        ],
        "must_draw": "Hand-drawn comparison diagram displaying the 'Moon face', pedal edema, and flaky paint dermatosis of Kwashiorkor alongside the 'Monkey face', prominent ribs, and muscle wasting of Marasmus.",
        "viva_questions": [
            "Why is iron contraindicated in Phase 1 of severe malnutrition management? (Answer: Free iron is a bacterial growth nutrient that precipitates overwhelming sepsis, and it generates toxic free radicals via the Fenton reaction in tissues lacking antioxidant proteins).",
            "What is ReSoMal and how does it differ from standard WHO ORS? (Answer: ReSoMal has lower sodium (45 vs 75 mmol/L) to prevent heart failure, higher potassium (40 vs 20 mmol/L) to treat hypokalemia, and added magnesium).",
            "What is the pathophysiology of fatty liver in Kwashiorkor? (Answer: Inability of the liver to synthesize Apolipoprotein B-100 prevents the export of triglycerides as VLDL, causing intracellular fat accumulation).",
            "What is Cancrum Oris (Noma)? (Answer: A severe gangrenous orofacial necrotizing infection seen in malnourished children driven by Fusobacterium necrophorum)."
        ]
    },
    {
        "id": "chap5_dysphagia_and_pud",
        "title": "Dysphagia & Peptic Ulcer Disease",
        "badge": "15-Mark Essay Model",
        "category": "Gastroenterology",
        "reading_time": "14 min read",
        "key_points": [
            "Dysphagia is the subjective sensation of difficulty in swallowing or the obstruction of the passage of food through the mouth, pharynx, or esophagus.",
            "Classification: Mechanical (luminal narrowing: food bolus hangs up; solids > liquids initially) vs Motor (neuromuscular incoordination: liquids and solids equally from onset).",
            "Plummer-Vinson (Paterson-Kelly) Syndrome triad: Middle-aged women, Microcytic hypochromic iron deficiency anemia, and Upper esophageal web; high malignant potential for post-cricoid carcinoma.",
            "Peptic Ulcer Disease (PUD) results from an imbalance between aggressive mucosal factors (acid, pepsin, H. pylori, NSAIDs) and protective mucosal defenses (mucus-bicarbonate barrier, blood flow, prostaglandins).",
            "H. pylori eradication: 14-day Bismuth Quadruple Therapy (PPI BD + Bismuth subsalicylate + Metronidazole + Tetracycline) or Clarithromycin Triple Therapy (PPI + Clarithromycin + Amoxicillin).",
            "Upper GI bleeding risk stratification via Forrest Classification guides endoscopic intervention (hemoclips, thermal coagulation, epinephrine injection)."
        ],
        "clinical_pearl": "In mechanical esophageal obstruction (such as esophageal carcinoma or benign peptic stricture), dysphagia begins with SOLIDS and progresses gradually to LIQUIDS. In motor / neuromuscular dysphagia (such as Achalasia cardia or Diffuse Esophageal Spasm), dysphagia affects BOTH LIQUIDS AND SOLIDS right from the onset of the disease.",
        "sections": [
            {
                "title": "1. Dysphagia: Definition, Terminology & Classification",
                "content": """**Definition**: Dysphagia is the sensation of sticking, impedance, or obstruction to the normal transit of food or liquids from the mouth into the stomach.

### Clinical Terminology
* **Odynophagia**: Painful swallowing, classically associated with severe mucosal ulceration (Candida, HSV, CMV esophagitis, or radiation).
* **Phagophobia**: Fear of swallowing (observed in Rabies, Tetanus, and severe pharyngeal paralysis).
* **Globus Hystericus**: Sensation of a lump in the throat unrelated to swallowing, without organic esophageal pathology.

### Etiological Classification of Dysphagia
```
                                DYSPHAGIA
                                    │
        ┌───────────────────────────┴───────────────────────────┐
        ▼                                                       ▼
MECHANICAL DYSPHAGIA                                    MOTOR (NEUROMUSCULAR)
(Structural Luminal Obstruction)                        (Incoordinate / Weak Peristalsis)
(Solids >> Liquids initially)                           (Liquids & Solids equally from onset)
        │                                                       │
  ┌─────┴─────┐                                           ┌─────┴─────┐
  ▼           ▼                                           ▼           ▼
INTRINSIC   EXTRINSIC                                   OROPHARYNGEAL ESOPHAGEAL
LUMINAL     COMPRESSION                                 (Transfer)    (Transit)
  │           │                                           │           │
  • Carcinoma • Retropharyngeal abscess                   • Bulbar /  • Achalasia cardia
  • Stricture • Retrovisceral Goitre                        pseudobulbar • Diffuse spasm
  • Rings/Webs• Left Atrial Enlargement                     palsy     • Scleroderma
  • Atresia     (Mitral Stenosis / Ortner sign)           • Myasthenia• Chagas disease
              • Bronchial Carcinoma                         gravis
              • Aortic Aneurysm
```

**Plummer-Vinson (Paterson-Kelly) Syndrome**:
* Classical triad: **Middle-aged females + Severe Iron Deficiency Anemia + Post-cricoid Upper Esophageal Web**.
* Associated features: Koilonychia (spoon-shaped nails), atrophic glossitis, angular stomatitis, and splenomegaly.
* Clinical significance: Pre-malignant condition predisposing to squamous cell carcinoma of the hypopharynx / post-cricoid region."""
            },
            {
                "title": "2. Peptic Ulcer Disease: Etiopathogenesis & Pathophysiology",
                "content": """PUD is a chronic excoriation of the gastroduodenal mucosa extending through the muscularis mucosae into deeper layers, caused by an imbalance between aggressive luminal factors and defensive mucosal barriers.

### Aggressive vs Defensive Factors (Shay's Balance Concept)
* **Aggressive Forces**: Gastric acid ($HCl$), Pepsin, *Helicobacter pylori* infection, NSAIDs, cigarette smoking, alcohol, bile reflux, ischemia.
* **Defensive Forces**: Mucus-bicarbonate gel layer (secreted by surface foveolar cells), mucosal blood flow (clears back-diffused acid), apical epithelial tight junctions, epithelial restitution, endogenous prostaglandins ($PGE_2$ and $PGI_2$).

### Role of Helicobacter pylori
* Gram-negative, microaerophilic, flagellated spiral bacillus colonizing gastric antrum.
* **Virulence Factors**:
  * **Urease Enzyme**: Converts urea into ammonia ($NH_3$) and $CO_2$, creating a protective alkaline micro-cloud buffering against gastric acid.
  * **VacA (Vacuolating cytotoxin A)**: Induces epithelial vacuolation and apoptosis.
  * **CagA (Cytotoxin-associated gene A)**: Injected via Type IV secretion system into host epithelial cells, disrupting cytoskeleton and inducing IL-8 cytokine release, driving intense neutrophil recruitment.
  * Antral-predominant gastritis inhibits somatostatin secretion from D-cells ──► uninhibited Gastrin release from G-cells ──► hyperchlorhydria ──► duodenal gastric metaplasia ──► **Duodenal Ulceration**.

### Role of NSAIDs
* Systemic inhibition of Cyclooxygenase-1 (**COX-1**) blocks protective mucosal prostaglandin ($PGE_2$) synthesis, decreasing bicarbonate and mucus secretion and reducing mucosal microvascular blood flow."""
            },
            {
                "title": "3. Clinical Presentation: Gastric vs Duodenal Ulcers",
                "content": """| Feature | Gastric Ulcer (GU) | Duodenal Ulcer (DU) |
| :--- | :--- | :--- |
| **Peak Age & Gender** | 50–70 years; Equal M:F | 30–55 years; Male predominance (3:1) |
| **Acid Secretion** | Normal to Low | **Hyperchlorhydria** (Markedly elevated) |
| **Pain-Food Timing** | Pain occurs **immediately or within 30 min** after food | Pain occurs **2 to 3 hours after food** or on empty stomach |
| **Food Effect** | Food **aggravates pain** (leads to food fear) | Food and antacids **relieve pain** |
| **Nocturnal Pain** | Uncommon | Very common (wakes patient at 1–2 AM) |
| **Body Weight** | **Weight Loss** (afraid to eat) | **Weight Gain** (eats frequently to relieve pain) |
| **Location** | Lesser curvature (incisura angularis) | First part of duodenum (duodenal bulb: 95%) |
| **Malignant Potential** | 2–5% malignant transformation (biopsy mandatory!) | **Strictly Benign** (virtually zero malignant risk) |"""
            },
            {
                "title": "4. Diagnostic Workup & Forrest Classification",
                "content": """1. **Upper Gastrointestinal Endoscopy (Esophagogastroduodenoscopy - OGD)**:
   * Investigation of choice. Visualizes location, size, and depth.
   * **Mandatory rule**: Always take at least 6–8 radial mucosal biopsies from the margins of every **gastric ulcer** to exclude adenocarcinoma.
2. **Helicobacter pylori Diagnostics**:
   * *Invasive (Endoscopic)*: Rapid Urease Test (RUT / CLO test: turns pink within 1 hour), histology (Warthin-Starry silver stain), culture.
   * *Non-Invasive*: $^{13}C$ or $^{14}C$ **Urea Breath Test (UBT)** (gold standard for confirming post-treatment eradication), Stool Antigen Test (HpSA), serology.

### Forrest Classification of Upper GI Bleeding
* **Forrest Ia**: Spurting arterial hemorrhage (Rebleed risk: 90%; Immediate endoscopic therapy).
* **Forrest Ib**: Oozing venous hemorrhage (Rebleed risk: 50%; Immediate endoscopic therapy).
* **Forrest IIa**: Non-bleeding visible vessel (Rebleed risk: 40%; Endoscopic therapy required).
* **Forrest IIb**: Adherent clot (Rebleed risk: 20%; Endoscopic clot removal + treatment).
* **Forrest IIc**: Flat pigmented hematin spot (Rebleed risk: 10%; Medical therapy only).
* **Forrest III**: Clean-based ulcer bed (Rebleed risk: <5%; Early hospital discharge)."""
            },
            {
                "title": "5. Comprehensive Medical Management Protocols",
                "content": """### A. Helicobacter pylori Eradication Regimens (14 Days)
* **First-Line: Bismuth Quadruple Therapy** (Recommended in areas of high clarithromycin resistance):
  1. **Proton Pump Inhibitor (PPI)**: Esomeprazole 40 mg orally BD (or Omeprazole 20 mg BD).
  2. **Bismuth Subsalicylate**: 524 mg orally QID (or Bismuth Subcitrate 120 mg QID).
  3. **Metronidazole**: 500 mg orally TID or QID.
  4. **Tetracycline**: 500 mg orally QID.
* **Alternative: Clarithromycin Triple Therapy** (Only if local clarithromycin resistance < 15%):
  1. **PPI**: Esomeprazole 40 mg BD.
  2. **Clarithromycin**: 500 mg BD.
  3. **Amoxicillin**: 1,000 mg BD (replace with Metronidazole 500 mg BD if penicillin-allergic).

### B. Management of Acute Peptic Ulcer Bleeding
* **IV PPI Infusion**: High-dose **Pantoprazole 80 mg IV bolus**, followed by **8 mg/hour continuous infusion for 72 hours**. Neutralizes gastric pH (> 6.0), stabilizing the fibrin platelet plug over the ruptured vessel.
* **Dual Endoscopic Hemostasis**: Epinephrine injection (1:10,000 to induce local vasospasm) COMBINED WITH mechanical hemoclips or thermal contact coagulation (bipolar probe / heater probe).

### C. Surgical Indications in PUD
* Perforation (acute abdomen with pneumoperitoneum: Graham patch repair).
* Uncontrolled refractory hemorrhage despite repeat endoscopic interventions.
* Gastric Outlet Obstruction (fibrotic cicatricial stenosis of pylorus)."""
            }
        ],
        "comparisons": [
            {
                "title": "Mechanical vs Motor Dysphagia",
                "headers": ["Diagnostic Feature", "Mechanical Dysphagia", "Motor (Neuromuscular) Dysphagia"],
                "rows": [
                    ["Onset of Symptoms", "Solids first, progresses to liquids later", "Liquids and solids concurrently from onset"],
                    ["Course", "Gradual, predictable, continuous worsening", "Intermittent, variable, aggravated by stress/cold"],
                    ["Impact of Cold Liquids", "No significant effect", "Often triggers or worsens spasm"],
                    ["Physical Maneuvers", "Regurgitation of undigested food", "Uses Valsalva or neck extension to clear food"],
                    ["Key Causes", "Esophageal Carcinoma, Peptic Stricture, Rings", "Achalasia Cardia, Diffuse Esophageal Spasm, Scleroderma"],
                    ["Barium Swallow Sign", "Irregular 'Apple-core' or smooth tapered shelf", "'Bird's beak' / 'Rat-tail' appearance (Achalasia)"]
                ]
            }
        ],
        "must_draw": "Schematic of the Barium Swallow showing the smooth 'Bird-beak' tapering of Achalasia cardia versus the irregular, ragged 'Apple-core' shelf of esophageal carcinoma.",
        "viva_questions": [
            "What is the classical triad of Plummer-Vinson syndrome? (Answer: Middle-aged females, severe iron deficiency anemia, and post-cricoid esophageal web).",
            "Why must every gastric ulcer be biopsied while duodenal ulcers rarely require biopsy? (Answer: Gastric ulcers have a 2–5% risk of harboring malignancy (adenocarcinoma); duodenal ulcers are almost universally benign).",
            "What is the mechanism of the Urea Breath Test? (Answer: The patient drinks 13C or 14C labeled urea. If H. pylori is present, its urease splits the urea into ammonia and labeled CO2, which is absorbed, exhaled, and quantified in breath).",
            "Why do NSAIDs cause gastric ulceration? (Answer: Systemic inhibition of COX-1 enzymes halts mucosal prostaglandin synthesis (PGE2), impairing the bicarbonate-mucus barrier and mucosal blood supply)."
        ]
    }
]
