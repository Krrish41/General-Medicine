# -*- coding: utf-8 -*-
"""
High-resolution medical SVG schematics, Layman analogies, and Flashcards for General Medicine.
"""

def generate_svg_schematic(ch_id, title):
    """Generates clean, responsive inline SVG medical schematics with crisp typography and clinical styling."""
    
    # Custom high-yield SVGs based on condition
    if "hepatitis" in ch_id:
        return f'''<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="420" fill="#0b1329" rx="12"/>
            <text x="400" y="36" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">ACUTE HEPATITIS B: SEROLOGICAL TIMELINE &amp; CORE WINDOW PERIOD</text>
            <line x1="80" y1="340" x2="740" y2="340" stroke="#334155" stroke-width="2"/>
            <line x1="80" y1="340" x2="80" y2="70" stroke="#334155" stroke-width="2"/>
            <text x="80" y="365" fill="#94a3b8" font-size="11" text-anchor="middle">0 Wks (Infection)</text>
            <text x="200" y="365" fill="#94a3b8" font-size="11" text-anchor="middle">4 Wks</text>
            <text x="320" y="365" fill="#94a3b8" font-size="11" text-anchor="middle">12 Wks</text>
            <text x="440" y="365" fill="#94a3b8" font-size="11" text-anchor="middle">20 Wks</text>
            <text x="560" y="365" fill="#94a3b8" font-size="11" text-anchor="middle">28 Wks</text>
            <text x="680" y="365" fill="#94a3b8" font-size="11" text-anchor="middle">36 Wks</text>
            
            <!-- Window Period shaded zone -->
            <rect x="360" y="80" width="120" height="260" fill="rgba(239, 68, 68, 0.12)" stroke="#ef4444" stroke-dasharray="4,4"/>
            <text x="420" y="105" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">CORE WINDOW PERIOD</text>
            <text x="420" y="122" fill="#fca5a5" font-size="10" text-anchor="middle">HBsAg (-) | Anti-HBs (-)</text>
            <text x="420" y="137" fill="#f87171" font-size="10" font-weight="700" text-anchor="middle">Anti-HBc IgM (+) ONLY</text>

            <!-- Curves -->
            <!-- HBsAg Curve -->
            <path d="M 100 340 Q 220 80 370 340" fill="none" stroke="#38bdf8" stroke-width="3.5"/>
            <text x="215" y="160" fill="#38bdf8" font-size="12" font-weight="700">HBsAg</text>

            <!-- HBeAg Curve -->
            <path d="M 120 340 Q 200 160 300 340" fill="none" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="3,3"/>
            <text x="180" y="240" fill="#c084fc" font-size="11">HBeAg (Replication)</text>

            <!-- Anti-HBc IgM Curve -->
            <path d="M 160 340 Q 300 90 520 340" fill="none" stroke="#f59e0b" stroke-width="3"/>
            <text x="310" y="195" fill="#f59e0b" font-size="12" font-weight="700">Anti-HBc IgM</text>

            <!-- Anti-HBs Curve -->
            <path d="M 470 340 Q 560 140 730 150" fill="none" stroke="#22c55e" stroke-width="3.5"/>
            <text x="600" y="180" fill="#4ade80" font-size="12" font-weight="700">Anti-HBs (Immunity)</text>

            <!-- Anti-HBc Total/IgG -->
            <path d="M 180 340 Q 320 180 730 200" fill="none" stroke="#94a3b8" stroke-width="2"/>
            <text x="640" y="225" fill="#cbd5e1" font-size="11">Anti-HBc IgG (Life)</text>
            
            <rect x="80" y="380" width="640" height="28" fill="#1e293b" rx="6"/>
            <text x="400" y="398" fill="#94a3b8" font-size="10.5" text-anchor="middle">Clinical Rule: If HBsAg is negative but acute viral hepatitis is suspected, ALWAYS order Anti-HBc IgM to detect the Window Period.</text>
        </svg>'''

    elif "liver_failure" in ch_id:
        return f'''<svg viewBox="0 0 800 380" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="380" fill="#0b1329" rx="12"/>
            <text x="400" y="36" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">HEPATIC ENCEPHALOPATHY: WEST-HAVEN STAGING &amp; AMMONIA TOXICITY</text>
            
            <g transform="translate(40, 70)">
                <rect x="0" y="0" width="160" height="230" fill="#1e293b" stroke="#38bdf8" rx="8"/>
                <rect x="0" y="0" width="160" height="36" fill="#0369a1" rx="8"/>
                <text x="80" y="23" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">GRADE 1 (Trivial)</text>
                <text x="12" y="65" fill="#cbd5e1" font-size="11">• Inverted sleep rhythm</text>
                <text x="12" y="90" fill="#cbd5e1" font-size="11">• Euphoria / Anxiety</text>
                <text x="12" y="115" fill="#cbd5e1" font-size="11">• Impaired math (serial 7s)</text>
                <text x="12" y="140" fill="#94a3b8" font-size="11">• Asterixis absent / subtle</text>
                <text x="12" y="180" fill="#38bdf8" font-size="10" font-weight="600">Bedside Test:</text>
                <text x="12" y="200" fill="#bae6fd" font-size="10">Construction apraxia (star)</text>
            </g>

            <g transform="translate(225, 70)">
                <rect x="0" y="0" width="160" height="230" fill="#1e293b" stroke="#f59e0b" rx="8"/>
                <rect x="0" y="0" width="160" height="36" fill="#b45309" rx="8"/>
                <text x="80" y="23" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">GRADE 2 (Lethargy)</text>
                <text x="12" y="65" fill="#cbd5e1" font-size="11">• Marked drowsiness</text>
                <text x="12" y="90" fill="#cbd5e1" font-size="11">• Temporal disorientation</text>
                <text x="12" y="115" fill="#cbd5e1" font-size="11">• Inappropriate behavior</text>
                <text x="12" y="140" fill="#f59e0b" font-size="11" font-weight="700">• ASTERIXIS PRESENT</text>
                <text x="12" y="180" fill="#f59e0b" font-size="10" font-weight="600">Characteristic Sign:</text>
                <text x="12" y="200" fill="#fde68a" font-size="10">Flapping hand tremor</text>
            </g>

            <g transform="translate(410, 70)">
                <rect x="0" y="0" width="160" height="230" fill="#1e293b" stroke="#f97316" rx="8"/>
                <rect x="0" y="0" width="160" height="36" fill="#c2410c" rx="8"/>
                <text x="80" y="23" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">GRADE 3 (Somnolence)</text>
                <text x="12" y="65" fill="#cbd5e1" font-size="11">• Stupor but arousable</text>
                <text x="12" y="90" fill="#cbd5e1" font-size="11">• Marked confusion</text>
                <text x="12" y="115" fill="#cbd5e1" font-size="11">• Incoherent speech</text>
                <text x="12" y="140" fill="#cbd5e1" font-size="11">• Hyperreflexia &amp; clonus</text>
                <text x="12" y="180" fill="#f97316" font-size="10" font-weight="600">Airway Warning:</text>
                <text x="12" y="200" fill="#fed7aa" font-size="10">High risk of aspiration</text>
            </g>

            <g transform="translate(595, 70)">
                <rect x="0" y="0" width="160" height="230" fill="#1e293b" stroke="#ef4444" rx="8"/>
                <rect x="0" y="0" width="160" height="36" fill="#b91c1c" rx="8"/>
                <text x="80" y="23" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">GRADE 4 (Coma)</text>
                <text x="12" y="65" fill="#cbd5e1" font-size="11">• Completely unarousable</text>
                <text x="12" y="90" fill="#cbd5e1" font-size="11">• Decerebrate posturing</text>
                <text x="12" y="115" fill="#cbd5e1" font-size="11">• Loss of corneal reflex</text>
                <text x="12" y="140" fill="#ef4444" font-size="11" font-weight="700">• Flaccid paralysis</text>
                <text x="12" y="180" fill="#ef4444" font-size="10" font-weight="600">Immediate Action:</text>
                <text x="12" y="200" fill="#fecaca" font-size="10">Endotracheal intubation</text>
            </g>

            <rect x="40" y="325" width="715" height="36" fill="#1e293b" rx="6"/>
            <text x="400" y="347" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Core Pharmacotherapy: Lactulose (titrated to 2-3 soft stools/day) + Rifaximin (550 mg BD) to suppress colonic ammoniagenic flora.</text>
        </svg>'''

    elif "cirrhosis" in ch_id:
        return f'''<svg viewBox="0 0 800 380" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="380" fill="#0b1329" rx="12"/>
            <text x="400" y="36" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">PORTAL HYPERTENSION: PORTOSYSTEMIC COLLATERAL SITES &amp; COMPLICATIONS</text>
            
            <circle cx="400" cy="180" r="65" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
            <text x="400" y="175" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">CIRRHOTIC</text>
            <text x="400" y="195" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">LIVER</text>
            <text x="400" y="215" fill="#94a3b8" font-size="9" text-anchor="middle">HVPG &gt; 10-12 mmHg</text>

            <!-- 4 Collateral Branches -->
            <!-- 1. Gastroesophageal -->
            <path d="M 370 125 L 200 80" stroke="#ef4444" stroke-width="3"/>
            <rect x="40" y="50" width="180" height="65" fill="#1e293b" stroke="#ef4444" rx="8"/>
            <text x="130" y="72" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">1. GASTROESOPHAGEAL</text>
            <text x="130" y="90" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Left Gastric ↔ Azygos Vein</text>
            <text x="130" y="105" fill="#fca5a5" font-size="9.5" font-weight="700" text-anchor="middle">ESOPHAGEAL VARICES</text>

            <!-- 2. Umbilical / Anterior Abdominal Wall -->
            <path d="M 360 225 L 200 270" stroke="#f59e0b" stroke-width="3"/>
            <rect x="40" y="245" width="180" height="65" fill="#1e293b" stroke="#f59e0b" rx="8"/>
            <text x="130" y="267" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">2. ANTERIOR ABDOMEN</text>
            <text x="130" y="285" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Paraumbilical ↔ Epigastric</text>
            <text x="130" y="300" fill="#fde68a" font-size="9.5" font-weight="700" text-anchor="middle">CAPUT MEDUSAE</text>

            <!-- 3. Rectal / Anal Canal -->
            <path d="M 430 225 L 600 270" stroke="#a855f7" stroke-width="3"/>
            <rect x="580" y="245" width="180" height="65" fill="#1e293b" stroke="#a855f7" rx="8"/>
            <text x="670" y="267" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle">3. ANORECTAL JUNCTION</text>
            <text x="670" y="285" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Superior Rectal ↔ Middle/Inferior</text>
            <text x="670" y="300" fill="#e9d5ff" font-size="9.5" font-weight="700" text-anchor="middle">RECTAL VARICES (Piles)</text>

            <!-- 4. Retroperitoneal -->
            <path d="M 430 125 L 600 80" stroke="#10b981" stroke-width="3"/>
            <rect x="580" y="50" width="180" height="65" fill="#1e293b" stroke="#10b981" rx="8"/>
            <text x="670" y="72" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">4. RETROPERITONEAL</text>
            <text x="670" y="90" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Colic/Splenic ↔ Renal/Lumbar</text>
            <text x="670" y="105" fill="#a7f3d0" font-size="9.5" font-weight="700" text-anchor="middle">VEINS OF RETZIUS</text>

            <rect x="40" y="335" width="720" height="30" fill="#1e293b" rx="6"/>
            <text x="400" y="354" fill="#94a3b8" font-size="10.5" text-anchor="middle">Bleeding Prophylaxis: Non-selective beta-blockers (Propranolol / Carvedilol) + Endoscopic Variceal Ligation (EVL).</text>
        </svg>'''

    elif "rheumatic" in ch_id:
        return f'''<svg viewBox="0 0 800 390" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="390" fill="#0b1329" rx="12"/>
            <text x="400" y="36" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">ACUTE RHEUMATIC FEVER: MODIFIED JONES CRITERIA (JONES ACRONYM)</text>
            
            <!-- Major Criteria -->
            <rect x="40" y="65" width="345" height="250" fill="#1e293b" stroke="#ef4444" rx="10"/>
            <rect x="40" y="65" width="345" height="38" fill="#991b1b" rx="10"/>
            <text x="212" y="90" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">5 MAJOR CRITERIA (J•O•N•E•S)</text>
            <text x="60" y="130" fill="#fca5a5" font-size="12" font-weight="700">J</text>
            <text x="80" y="130" fill="#cbd5e1" font-size="11.5">— Joint Involvement (Migratory Polyarthritis)</text>
            <text x="60" y="165" fill="#fca5a5" font-size="12" font-weight="700">O</text>
            <text x="80" y="165" fill="#cbd5e1" font-size="11.5">— &hearts; Carditis &amp; Valvulitis (Pancarditis / Carey-Coombs)</text>
            <text x="60" y="200" fill="#fca5a5" font-size="12" font-weight="700">N</text>
            <text x="80" y="200" fill="#cbd5e1" font-size="11.5">— Nodules (Painless Subcutaneous Extensor Nodules)</text>
            <text x="60" y="235" fill="#fca5a5" font-size="12" font-weight="700">E</text>
            <text x="80" y="235" fill="#cbd5e1" font-size="11.5">— Erythema Marginatum (Serpentine evanescent rash)</text>
            <text x="60" y="270" fill="#fca5a5" font-size="12" font-weight="700">S</text>
            <text x="80" y="270" fill="#cbd5e1" font-size="11.5">— Sydenham Chorea (St. Vitus dance, rapid purposeless)</text>

            <!-- Minor Criteria & Evidence -->
            <rect x="415" y="65" width="345" height="250" fill="#1e293b" stroke="#38bdf8" rx="10"/>
            <rect x="415" y="65" width="345" height="38" fill="#0369a1" rx="10"/>
            <text x="587" y="90" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">MINOR CRITERIA + ESSENTIAL EVIDENCE</text>
            <text x="435" y="125" fill="#38bdf8" font-size="11" font-weight="700">Clinical Minor:</text>
            <text x="445" y="145" fill="#cbd5e1" font-size="11">• Arthralgia (if arthritis not used as major)</text>
            <text x="445" y="165" fill="#cbd5e1" font-size="11">• Fever (≥38.5°C in moderate/low risk)</text>
            <text x="435" y="195" fill="#38bdf8" font-size="11" font-weight="700">Laboratory Minor:</text>
            <text x="445" y="215" fill="#cbd5e1" font-size="11">• Elevated acute phase reactants: ESR ≥60 mm/hr, CRP</text>
            <text x="445" y="235" fill="#cbd5e1" font-size="11">• Prolonged PR interval on ECG (unless carditis major)</text>
            <rect x="430" y="255" width="315" height="45" fill="#0f172a" stroke="#22c55e" rx="6"/>
            <text x="587" y="273" fill="#4ade80" font-size="10.5" font-weight="700" text-anchor="middle">MANDATORY ESSENTIAL REQUIREMENT:</text>
            <text x="587" y="290" fill="#cbd5e1" font-size="10" text-anchor="middle">Proof of preceding GAS infection (ASO titer &gt; 200 IU or Anti-DNase B)</text>

            <rect x="40" y="330" width="720" height="40" fill="#1e293b" rx="6"/>
            <text x="400" y="354" fill="#fbbf24" font-size="11.5" font-weight="700" text-anchor="middle">Diagnostic Formula: (2 Major) OR (1 Major + 2 Minor) + Positive Evidence of Preceding GAS Pharyngitis</text>
        </svg>'''

    elif "endocarditis" in ch_id:
        return f'''<svg viewBox="0 0 800 390" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="390" fill="#0b1329" rx="12"/>
            <text x="400" y="34" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">INFECTIVE ENDOCARDITIS: AHA DENTAL PROPHYLAXIS PROTOCOL</text>
            
            <g transform="translate(40, 60)">
                <rect x="0" y="0" width="350" height="250" fill="#1e293b" stroke="#f59e0b" rx="8"/>
                <rect x="0" y="0" width="350" height="36" fill="#b45309" rx="8"/>
                <text x="175" y="23" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">WHO REQUIRES DENTAL ANTIBIOTIC PROPHYLAXIS?</text>
                <text x="14" y="60" fill="#fde68a" font-size="11" font-weight="600">Strict AHA High-Risk Cardiac Indications Only:</text>
                <text x="14" y="85" fill="#cbd5e1" font-size="10.5">• 1. Prosthetic heart valves (mechanical or tissue)</text>
                <text x="14" y="110" fill="#cbd5e1" font-size="10.5">• 2. Prosthetic material used for cardiac valve repair</text>
                <text x="14" y="135" fill="#cbd5e1" font-size="10.5">• 3. Previous episode of Infective Endocarditis</text>
                <text x="14" y="160" fill="#cbd5e1" font-size="10.5">• 4. Unrepaired cyanotic congenital heart disease</text>
                <text x="14" y="185" fill="#cbd5e1" font-size="10.5">• 5. Repaired CHD with residual defects at/near patch</text>
                <text x="14" y="210" fill="#cbd5e1" font-size="10.5">• 6. Cardiac transplant recipients with valvulopathy</text>
                <text x="14" y="235" fill="#ef4444" font-size="10" font-weight="700">NOT indicated: Routine MVP, bicuspid aortic valve, ASD.</text>
            </g>

            <g transform="translate(410, 60)">
                <rect x="0" y="0" width="350" height="250" fill="#1e293b" stroke="#10b981" rx="8"/>
                <rect x="0" y="0" width="350" height="36" fill="#047857" rx="8"/>
                <text x="175" y="23" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">STANDARD AHA REGIMEN (30-60 MIN PRE-OP)</text>
                
                <rect x="14" y="50" width="322" height="55" fill="#0f172a" stroke="#38bdf8" rx="6"/>
                <text x="24" y="70" fill="#38bdf8" font-size="11" font-weight="700">Oral Standard (First Line):</text>
                <text x="24" y="90" fill="#fff" font-size="12" font-weight="700">AMOXICILLIN 2.0 g PO (Pediatric: 50 mg/kg)</text>

                <rect x="14" y="115" width="322" height="60" fill="#0f172a" stroke="#f97316" rx="6"/>
                <text x="24" y="133" fill="#fb923c" font-size="11" font-weight="700">Penicillin Allergy (Oral):</text>
                <text x="24" y="150" fill="#fff" font-size="11" font-weight="600">CEPHALEXIN 2.0 g PO OR</text>
                <text x="24" y="167" fill="#fff" font-size="11" font-weight="600">AZITHROMYCIN / CLARITHROMYCIN 500 mg PO</text>

                <rect x="14" y="185" width="322" height="55" fill="#0f172a" stroke="#a855f7" rx="6"/>
                <text x="24" y="203" fill="#c084fc" font-size="11" font-weight="700">Unable to Take Oral Medication:</text>
                <text x="24" y="222" fill="#fff" font-size="11" font-weight="600">AMPICILLIN 2.0 g IV/IM or CEFAZOLIN 1.0 g IV</text>
            </g>

            <rect x="40" y="325" width="720" height="48" fill="#1e293b" rx="6"/>
            <text x="400" y="345" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">High-Risk Dental Procedures: Manipulation of gingival tissue, periapical region of teeth, or perforation of oral mucosa.</text>
            <text x="400" y="362" fill="#94a3b8" font-size="10" text-anchor="middle">No prophylaxis required for: Routine dental anesthetic injection through non-infected tissue, radiographs, or shed deciduous teeth.</text>
        </svg>'''

    else:
        # Universal clinical algorithm schematic
        return f'''<svg viewBox="0 0 800 360" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Plus Jakarta Sans',sans-serif; background:#0f172a; border-radius:12px;">
            <rect width="800" height="360" fill="#0b1329" rx="12"/>
            <text x="400" y="36" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">{title.upper()}: CLINICAL DECISION &amp; MANAGEMENT ALGORITHM</text>
            
            <!-- Step 1: Presentation -->
            <rect x="50" y="70" width="200" height="90" fill="#1e293b" stroke="#38bdf8" rx="8"/>
            <text x="150" y="95" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">1. CLINICAL PRESENTATION</text>
            <text x="150" y="118" fill="#cbd5e1" font-size="10" text-anchor="middle">Bedside Physical Examination</text>
            <text x="150" y="136" fill="#94a3b8" font-size="9.5" text-anchor="middle">Vital Signs, Symptoms, Signs</text>

            <line x1="250" y1="115" x2="300" y2="115" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

            <!-- Step 2: Workup -->
            <rect x="300" y="70" width="200" height="90" fill="#1e293b" stroke="#f59e0b" rx="8"/>
            <text x="400" y="95" fill="#f59e0b" font-size="11.5" font-weight="700" text-anchor="middle">2. DIAGNOSTIC WORKUP</text>
            <text x="400" y="118" fill="#cbd5e1" font-size="10" text-anchor="middle">Confirmatory Lab Panels</text>
            <text x="400" y="136" fill="#94a3b8" font-size="9.5" text-anchor="middle">Imaging &amp; Gold Standard Criteria</text>

            <line x1="500" y1="115" x2="550" y2="115" stroke="#f59e0b" stroke-width="2.5"/>

            <!-- Step 3: Stratification -->
            <rect x="550" y="70" width="200" height="90" fill="#1e293b" stroke="#ef4444" rx="8"/>
            <text x="650" y="95" fill="#ef4444" font-size="11.5" font-weight="700" text-anchor="middle">3. SEVERITY STAGING</text>
            <text x="650" y="118" fill="#cbd5e1" font-size="10" text-anchor="middle">Risk Stratification Criteria</text>
            <text x="650" y="136" fill="#94a3b8" font-size="9.5" text-anchor="middle">Acute vs Chronic / Outpatient vs ICU</text>

            <line x1="650" y1="160" x2="650" y2="210" stroke="#ef4444" stroke-width="2.5"/>

            <!-- Step 4: Resuscitation & Therapeutics -->
            <rect x="50" y="210" width="700" height="110" fill="#1e293b" stroke="#10b981" rx="8"/>
            <text x="400" y="238" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">4. DEFINITIVE PHARMACOTHERAPY &amp; CHAIRSIDE DENTAL MANAGEMENT</text>
            
            <g transform="translate(70, 255)">
                <rect x="0" y="0" width="200" height="48" fill="#0f172a" rx="6"/>
                <text x="100" y="20" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle">EMERGENCY ABCs</text>
                <text x="100" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">IV access, oxygen, vitals stabilization</text>
            </g>

            <g transform="translate(300, 255)">
                <rect x="0" y="0" width="200" height="48" fill="#0f172a" rx="6"/>
                <text x="100" y="20" fill="#a7f3d0" font-size="10.5" font-weight="700" text-anchor="middle">FIRST-LINE MEDICAL DRUGS</text>
                <text x="100" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">Evidence-based dosage regimens</text>
            </g>

            <g transform="translate(530, 255)">
                <rect x="0" y="0" width="200" height="48" fill="#0f172a" rx="6"/>
                <text x="100" y="20" fill="#fde68a" font-size="10.5" font-weight="700" text-anchor="middle">DENTAL CONSIDERATIONS</text>
                <text x="100" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">Bleeding cutoffs &amp; precautions</text>
            </g>
        </svg>'''


LAYMAN_ANALOGIES = {
    "chap1_viral_hepatitis": {
        "title": "The City Waterworks and the Infiltration Agent",
        "analogy": "Think of your liver as the central chemical purification plant of a mega-city. Hepatitis viruses are like sabotaging hackers that sneak into the plant. Intriguingly, the viruses themselves don't dynamite the machinery; instead, your body's own over-zealous security guards (killer T-cells) spot the infected factory workers (hepatocytes) and blow up the entire assembly line to contain the breach. The 'window period' is like when the intruder's original fingerprints have been wiped clean, but the city's specialized detectives haven't finished forging the permanent neutralizing handcuff antibodies yet — during this blackout, only the temporary crime-scene tape (IgM antibodies) reveals that a break-in occurred."
    },
    "chap2_acute_liver_failure": {
        "title": "The Chemical Waste Spill and the Clouded Brain",
        "analogy": "When severe liver failure strikes, it is as though the city's massive sewage treatment facility suffers a total blackout overnight. Industrial ammonia, normally detoxified into harmless urea, bypasses the shutdown plant and pours into the brain's bloodstream. The brain's star-shaped support cells (astrocytes) attempt to soak up the poison, swelling until intracranial pressure spikes dangerously like an over-inflated tire, causing erratic sleep, flapping hands, and deep coma."
    },
    "chap3_cirrhosis_portal_htn": {
        "title": "The Sclerotic Dam and the Bursting Overflow Pipes",
        "analogy": "Healthy liver tissue is soft and porous like a natural sponge. Cirrhosis turns that sponge into tough, scarred gristle. Blood arriving from the stomach and intestines through the portal vein hits this solid dam and cannot pass. The backed-up pressure forces blood into fragile, paper-thin detour veins around the esophagus and stomach. These veins swell like overstretched water balloons (varices) that can rupture catastrophically under ordinary coughing or food swallowing."
    },
    "chap4_pem_kwashiorkor_marasmus": {
        "title": "The Leaking Water Tanks vs The Completely Burned Fuel Tank",
        "analogy": "Imagine a house running out of supplies. In Marasmus, there is no food at all — both coal and bricks are missing. The body methodically burns every drop of fat and muscle to stay alive, resulting in a skeletal 'old man' appearance. In Kwashiorkor, the diet has rice or starch (calories) but zero protein (bricks). Because there is no albumin in the bloodstream to act as a molecular sponge, fluid leaks out of capillaries into tissues, producing swollen, bloated legs and a deceptive 'moon face' on a starving toddler."
    },
    "chap5_dysphagia_pud": {
        "title": "The Over-Acidic Furnace and the Protective Clay Lining",
        "analogy": "The stomach is like a brick oven burning pure battery acid to dissolve food. A thick coating of mucus and bicarbonate is the fireproof clay lining. Peptic ulcer disease happens either when the fire burns too hot (excess acid) or when a tenacious bacterium named H. pylori or NSAID painkillers strip off the protective clay, allowing the furnace's own acid to eat raw holes into the muscle wall."
    },
    "chap6_rheumatic_fever_rhd": {
        "title": "The Case of Mistaken Identity and Friendly Fire",
        "analogy": "Streptococcus pyogenes (strep throat) wears a specific protein coat (M protein) that closely resembles the molecular structure of human heart valves and joint cartilage. When the immune system manufactures missile antibodies to wipe out the strep throat, those antibodies mistake the patient's own mitral valve for the bacterial invader, hammering the heart leaflets with chronic inflammatory scarring."
    },
    "chap7_infective_endocarditis": {
        "title": "Barnacles on the Damaged Propeller",
        "analogy": "Imagine a heart valve that is slightly roughened or artificial — like a pitted ship propeller. When a dental extraction releases oral bacteria (Viridans streptococci) into the bloodstream, they stick to the rough valve surface, forming slimy, infected vegetations like barnacles. These vegetations chew through valve leaflets and throw off septic emboli like shrapnel into the brain and kidneys."
    },
    "chap8_ischemic_heart_disease": {
        "title": "The Clogged Fuel Line and the Stalling Engine",
        "analogy": "The heart muscle is a high-performance engine that works 24/7 without rest. The coronary arteries are its dedicated fuel lines. Cholesterol plaque gradually narrows the fuel line. In a heart attack (STEMI), an unstable plaque ruptures, forming a sudden blood clot that shuts the fuel line completely. Deprived of oxygen, engine cylinders begin dying within 20 minutes unless the blockage is cracked open by an emergency balloon."
    },
    "chap9_heart_failure_hypertension": {
        "title": "The Exhausted Sump Pump and the Overloaded Pipes",
        "analogy": "In hypertension, the pipes in the house are under constant extreme pressure, forcing the central sump pump (the left ventricle) to work against heavy resistance. Over years, the pump walls thicken and eventually tire out. When the pump can no longer push blood forward, fluid backs up into the lungs like water pooling in the basement, causing nighttime breathlessness and swollen ankles."
    },
    "chap10_congenital_heart_disease": {
        "title": "The Plumber's Mismatch in Blue Babies",
        "analogy": "In Tetralogy of Fallot, the plumbing of the newborn heart has four simultaneous flaws: a hole between ventricles (VSD), a pinched pulmonary artery, a thickened right pump, and a misaligned aorta. Because the route to the lungs is choked, unoxygenated blue blood takes the path of least resistance through the hole directly into the main artery, starving the baby's fingers and lips of oxygen."
    },
    "chap11_enteric_fever": {
        "title": "The Trojan Horse in the Intestinal Barracks",
        "analogy": "Salmonella typhi does not cause immediate explosive diarrhea. Instead, it behaves like a silent spy, penetrating the intestinal lining and multiplying silently inside the body's immune macrophages for 10 to 14 days before bursting into the bloodstream in a step-ladder fever wave, targeting the gut's Peyer's patches with risk of perforation."
    },
    "chap12_syphilis_stds": {
        "title": "The Great Masquerader's Three Acts",
        "analogy": "Treponema pallidum is a corkscrew spirochete that acts like a dramatic villain across three acts: Act 1 is a clean, painless sore (chancre) that deceptively heals on its own; Act 2 is a body-wide rash and snail-track ulcers teeming with spirochetes; Act 3, arriving decades later, creates destructive rubbery gummas that hollow out the palate, bone, and spinal cord."
    },
    "chap13_diphtheria_tetanus": {
        "title": "The Choking Leathery Curtain and the Locked Brakes",
        "analogy": "Diphtheria produces an exotoxin that freezes cell protein synthesis, forming a gray leathery false membrane across the throat that can suffocate a child. Tetanus, on the other hand, produces tetanospasmin, which cuts the inhibitory brake wires in the spinal cord, sending motor nerves into uncontrollable, agonizing spasms that lock the jaw shut (trismus)."
    },
    "chap14_viral_exanthems_hiv": {
        "title": "The Early Salt Grains and the Slow Defense Hijack",
        "analogy": "In measles, tiny grains of salt on a red background (Koplik spots) appear inside the mouth days before the fever breaks out onto the skin. In HIV, the virus targets the commander generals of the immune military (CD4 T-cells), slowly whittling their numbers down from 1,000 to below 200, allowing ordinary fungal and viral opportunists to run riot in the mouth."
    },
    "chap15_diabetes_mellitus": {
        "title": "Starving in a Sea of Sugar and the Acidic Fire",
        "analogy": "Insulin is the molecular key that unlocks cell doors so blood sugar can enter and be used for energy. Without insulin (Type 1 DM), cells are starving despite swimming in an ocean of glucose. In desperation, the body burns fats at a furious pace, generating acidic ketone byproducts that sour the bloodstream into life-threatening Diabetic Ketoacidosis (DKA)."
    },
    "chap16_leukemias_oral": {
        "title": "The Mutinous Clone Army and the Bleeding Gums",
        "analogy": "In leukemia, the bone marrow factory is overrun by mutinous, immature blast cells that refuse to grow up or perform defense duties. As they choke the assembly line, red blood cells and platelets plummet. In the mouth, neoplastic myeloblasts physically invade the gum tissue, making the gums swell into purple, boggy pillows that bleed spontaneously at the touch of a dental mirror."
    },
    "chap17_nephrotic_nephritic_ckd": {
        "title": "The Torn Kitchen Sieve vs The Inflamed Clogged Filter",
        "analogy": "The kidney's glomerulus is like an ultra-fine kitchen sieve. In Nephrotic Syndrome, the podocyte sieve holes are stretched wide open, dumping precious albumin into the urine and causing full-body swelling (anasarca). In Nephritic Syndrome, the filter is violently inflamed and bleeding, producing dark cola-colored urine, high blood pressure, and swollen eyelids."
    },
    "chap18_facial_palsy_headaches": {
        "title": "The Swollen Cable in the Bone Tunnel",
        "analogy": "The facial nerve (CN VII) is a high-density fiber-optic cable that controls every facial expression. On its way to the face, it passes through an unyielding, narrow bony tunnel. In Bell's palsy, viral inflammation causes the cable to swell. Trapped against hard bone, the nerve loses blood supply, causing the entire half of the face to droop helplessly with inability to close the eye."
    },
    "chap19_meningitis_neuro_infections": {
        "title": "The Infected Fortress Wall and the Stiff Neck",
        "analogy": "The meninges are the three-layered protective envelope wrapped around the brain and spinal cord. When virulent bacteria breach this sanctuary, the envelope becomes red-hot and acutely inflamed. Stretching the inflamed spinal envelope by bending the neck forward creates agonizing resistance (neck stiffness and Brudzinski's sign)."
    },
    "chap20_shock_cpr": {
        "title": "The Collapsed Electrical Grid and the Mechanical Reset",
        "analogy": "Shock is not just low blood pressure; it is a profound failure of oxygen delivery to cellular powerhouses (mitochondria). In cardiac arrest, the heart's rhythm degenerates into chaotic quivering (Ventricular Fibrillation). CPR acts as an artificial mechanical pump to keep the brain alive until an electrical defibrillator can reboot the heart's pacemaker back into synchronized rhythm."
    }
}

FLASHCARDS = {
    "chap1_viral_hepatitis": [
        {"q": "What is the sole serological marker present during the Hepatitis B 'Window Period'?", "a": "Anti-HBc IgM. HBsAg has cleared and Anti-HBs has not yet reached detectable levels."},
        {"q": "Which hepatitis virus has a 20% mortality rate in pregnant women?", "a": "Hepatitis E Virus (HEV) — due to acute fulminant hepatic necrosis in the 3rd trimester."},
        {"q": "What is the recommended post-exposure prophylaxis for an unvaccinated dental student after an HBV needlestick?", "a": "Hepatitis B Immune Globulin (HBIG 0.06 mL/kg) within 24 hours + complete 3-dose HBV vaccine series."}
    ],
    "chap2_acute_liver_failure": [
        {"q": "What is the clinical definition of Asterixis in Hepatic Encephalopathy?", "a": "A sudden, non-rhythmic, flapping cessation of voluntary muscle contraction when hands are dorsiflexed with arms outstretched."},
        {"q": "What is the first-line medication to eliminate intestinal ammonia in encephalopathy?", "a": "Lactulose (acidifies colon, traps NH4+, produces 2-3 soft stools/day) + Rifaximin (550 mg BD)."},
        {"q": "What is the single most sensitive prognostic indicator in Acute Liver Failure?", "a": "Prothrombin Time / INR (INR > 6.5 in King's College Criteria mandates urgent liver transplantation)."}
    ],
    "chap3_cirrhosis_portal_htn": [
        {"q": "What threshold of Hepatic Venous Pressure Gradient (HVPG) defines clinically significant portal hypertension?", "a": "HVPG ≥ 10 mmHg (esophageal varices form at ≥10 mmHg; risk of variceal bleeding rises steeply at ≥12 mmHg)."},
        {"q": "Name the 4 anatomical sites of portosystemic collateral circulation.", "a": "1. Gastroesophageal junction, 2. Umbilicus (Caput medusae), 3. Anorectal junction, 4. Retroperitoneum (Veins of Retzius)."},
        {"q": "What class of medication is used for primary prophylaxis of variceal hemorrhage?", "a": "Non-selective beta-blockers: Propranolol or Carvedilol (reduce cardiac output and induce splanchnic vasoconstriction)."}
    ],
    "chap4_pem_kwashiorkor_marasmus": [
        {"q": "What is the mandatory hallmark sign that distinguishes Kwashiorkor from Marasmus?", "a": "Bilateral pitting edema (caused by severe hypoalbuminemia due to selective protein deficiency)."},
        {"q": "Why does fatty liver develop in Kwashiorkor but not Marasmus?", "a": "Impaired synthesis of apolipoprotein B-100 prevents export of triglycerides from hepatocytes."},
        {"q": "What is the 'Flag sign' of hair in protein-energy malnutrition?", "a": "Alternating light and dark bands in hair corresponding to periods of nutritional deficiency and sufficiency."}
    ],
    "chap5_dysphagia_pud": [
        {"q": "What is the classic first-line Triple Therapy for H. pylori eradication?", "a": "Proton Pump Inhibitor (Omeprazole 20 mg BD) + Clarithromycin (500 mg BD) + Amoxicillin (1000 mg BD) for 14 days."},
        {"q": "What is Plummer-Vinson (Paterson-Kelly) Syndrome triad?", "a": "1. Iron deficiency anemia, 2. Post-cricoid dysphagia (esophageal webs), 3. Glossitis / Koilonychia. High risk of squamous cell carcinoma."},
        {"q": "What distinguishes gastric ulcer pain from duodenal ulcer pain?", "a": "Gastric ulcer pain worsens shortly after food intake; duodenal ulcer pain is relieved by food and wakes the patient at 2 AM."}
    ],
    "chap6_rheumatic_fever_rhd": [
        {"q": "What are the 5 Major Jones criteria for Acute Rheumatic Fever?", "a": "J•O•N•E•S: Joint (Migratory Polyarthritis), &hearts; Carditis, Nodules (Subcutaneous), Erythema Marginatum, Sydenham Chorea."},
        {"q": "What is the pathognomonic myocardial histopathological finding in Rheumatic Carditis?", "a": "Aschoff bodies containing plump Anitschkow cells ('caterpillar cells') and multinucleated Aschoff giant cells."},
        {"q": "What is the duration of secondary penicillin prophylaxis for RHD with persistent valvular disease?", "a": "Until age 40 years or 10 years after last attack (whichever is longer), sometimes lifelong."}
    ],
    "chap7_infective_endocarditis": [
        {"q": "What is the standard oral antibiotic prophylaxis regimen for high-risk dental procedures?", "a": "Amoxicillin 2.0 g orally (50 mg/kg in children) taken 30 to 60 minutes prior to the procedure."},
        {"q": "What are Janeway lesions vs Osler nodes in Infective Endocarditis?", "a": "Janeway lesions: Painless, erythematous macules on palms/soles (septic microemboli). Osler nodes: Tender, painful violaceous nodules on finger pulps (immune complexes)."},
        {"q": "What are the 2 Major Duke Criteria for Infective Endocarditis?", "a": "1. Positive blood cultures for typical microorganisms from 2 separate blood samples. 2. Evidence of endocardial involvement on echocardiography (vegetation, abscess, new valve regurgitation)."}
    ],
    "chap8_ischemic_heart_disease": [
        {"q": "What is the definitive ECG criterion for acute STEMI in male patients under 40?", "a": "ST-segment elevation ≥ 2.5 mm in leads V2-V3 (≥ 2 mm in men ≥ 40, ≥ 1.5 mm in women), or ≥ 1 mm in any other contiguous leads."},
        {"q": "What is the golden time window for Primary Percutaneous Coronary Intervention (PCI)?", "a": "Door-to-balloon time < 90 minutes (or fibrinolysis door-to-needle time < 30 minutes if PCI not available within 120 min)."},
        {"q": "What is the MONA-B initial emergency protocol for acute MI?", "a": "Morphine, Oxygen (if SaO2 < 90%), Nitroglycerin sublingual, Aspirin 325 mg chewed, and Beta-blocker."}
    ],
    "chap9_heart_failure_hypertension": [
        {"q": "What serum biomarker confirms the diagnosis of acute decompensated heart failure?", "a": "B-type Natriuretic Peptide (BNP > 100 pg/mL) or NT-proBNP (> 300 pg/mL)."},
        {"q": "What are the 4 guideline-directed medical therapy (GDMT) pillars for HFrEF?", "a": "1. ARNI (Sacubitril/Valsartan) or ACEi, 2. Beta-blocker (Bisoprolol/Carvedilol), 3. MRA (Spironolactone), 4. SGLT2 inhibitor (Empagliflozin)."},
        {"q": "What defines a Hypertensive Emergency vs Hypertensive Urgency?", "a": "Hypertensive Emergency: BP > 180/120 mmHg WITH acute target organ damage (encephalopathy, acute MI, pulmonary edema)."}
    ],
    "chap10_congenital_heart_disease": [
        {"q": "What are the 4 anatomical defects in Tetralogy of Fallot?", "a": "PROV: Pulmonary stenosis, Right ventricular hypertrophy, Overriding aorta, Ventricular septal defect."},
        {"q": "Why do children with Tetralogy of Fallot instinctively squat during hypercyanotic 'tet' spells?", "a": "Squatting kinks the femoral arteries, increasing systemic vascular resistance (SVR), which forces blood from RV into the pulmonary artery instead of the aorta."},
        {"q": "What is the classic cardiac murmur heard in Patent Ductus Arteriosus (PDA)?", "a": "Continuous 'machinery' murmur heard loudest in the left infraclavicular area."}
    ],
    "chap11_enteric_fever": [
        {"q": "What is the diagnostic timeline acronym 'BASU' for Enteric Fever?", "a": "Week 1: Blood culture (90% positive); Week 2: Agglutination (Widal test); Week 3: Stool culture; Week 4: Urine culture."},
        {"q": "What is Faget's sign in Typhoid Fever?", "a": "Sphygmothermic dissociation (relative bradycardia despite high spiking step-ladder fever)."},
        {"q": "What is the major surgical emergency that occurs in the 3rd week of Typhoid?", "a": "Intestinal perforation of necrotic Peyer's patches in the terminal ileum."}
    ],
    "chap12_syphilis_stds": [
        {"q": "What is the drug of choice for all stages of Syphilis?", "a": "Benzathine Penicillin G (2.4 million units IM single dose for primary/secondary; weekly for 3 weeks for latent/tertiary)."},
        {"q": "What are the components of Hutchinson's Triad in Congenital Syphilis?", "a": "1. Hutchinson's teeth (screwdriver incisors & mulberry molars), 2. Interstitial keratitis, 3. Eighth nerve sensorineural deafness."},
        {"q": "What is the Jarisch-Herxheimer reaction?", "a": "An acute febrile inflammatory reaction with chills and hypotension occurring within 24 hours of initiating penicillin, due to massive spirochetal endotoxin release."}
    ],
    "chap13_diphtheria_tetanus": [
        {"q": "Why should you NEVER forcibly scrape off a Diphtheritic pseudomembrane?", "a": "It leaves a raw, actively bleeding surface and accelerates fatal systemic absorption of diphtheria exotoxin."},
        {"q": "What is Risus Sardonicus in Tetanus?", "a": "Sardonic grin produced by sustained involuntary spasm of the facial muscles (frontalis and orbicularis oris)."},
        {"q": "What is the mechanism of action of Tetanospasmin?", "a": "Cleaves synaptobrevin, blocking presynaptic release of inhibitory neurotransmitters (GABA and glycine) at motor synapses."}
    ],
    "chap14_viral_exanthems_hiv": [
        {"q": "What are Koplik's spots and when do they appear?", "a": "Pathognomonic bluish-white salt-like specks on an erythematous base opposite lower molars; appear 1-2 days before the generalized measles rash."},
        {"q": "What CD4 count defines the transition from HIV infection to clinical AIDS?", "a": "CD4 T-lymphocyte count < 200 cells/mm³ (or presence of an AIDS-defining condition such as PCP or Kaposi sarcoma)."},
        {"q": "Name 3 high-yield oral manifestations that raise clinical suspicion of undiagnosed HIV.", "a": "1. Pseudomembranous Oral Candidiasis (thrush), 2. Oral Hairy Leukoplakia (EBV on lateral tongue), 3. Kaposi Sarcoma (HHV-8 purplish palate lesions)."}
    ],
    "chap15_diabetes_mellitus": [
        {"q": "What diagnostic triad defines Diabetic Ketoacidosis (DKA)?", "a": "1. Hyperglycemia (blood glucose > 250 mg/dL), 2. Ketosis (ketonemia / ketonuria), 3. Metabolic acidosis (arterial pH < 7.30, serum bicarbonate < 18 mEq/L)."},
        {"q": "What is the first and most critical resuscitation step in managing DKA?", "a": "Aggressive IV fluid rehydration with 0.9% Normal Saline (1.0 to 1.5 L in the first hour) before starting insulin."},
        {"q": "At what serum potassium level must insulin infusion be withheld in DKA?", "a": "If K⁺ < 3.3 mEq/L, withhold insulin and administer IV potassium immediately to prevent fatal cardiac arrhythmias."}
    ],
    "chap16_leukemias_oral": [
        {"q": "What is the pathognomonic cytological inclusion seen in Acute Myeloid Leukemia (AML)?", "a": "Auer rods (fused crystalline lysosomal granules in the cytoplasm of myeloblasts)."},
        {"q": "Which AML subtypes are notorious for massive leukemic gingival enlargement?", "a": "Acute Myelomonocytic (FAB M4) and Acute Monocytic Leukemia (FAB M5)."},
        {"q": "What chromosomal translocation is the hallmark of Chronic Myelogenous Leukemia (CML)?", "a": "Philadelphia chromosome: t(9;22)(q34;q11) creating the chimeric BCR-ABL1 oncogenic tyrosine kinase."}
    ],
    "chap17_nephrotic_nephritic_ckd": [
        {"q": "What defines the nephrotic range proteinuria threshold in a 24-hour urine collection?", "a": "Protein excretion > 3.5 grams per 24 hours (or spot urine protein-to-creatinine ratio > 3.0 mg/mg)."},
        {"q": "What are the pathognomonic urine microscopy findings in Nephritic Syndrome?", "a": "Dysmorphic red blood cells (RBCs) and Red Blood Cell Casts indicating active glomerulonephritis."},
        {"q": "At what GFR threshold does Chronic Kidney Disease enter Stage 5 (End-Stage Renal Disease)?", "a": "eGFR < 15 mL/min/1.73m² (indicates urgent need for renal replacement therapy: hemodialysis or renal transplant)."}
    ],
    "chap18_facial_palsy_headaches": [
        {"q": "How do you clinically differentiate UMN from LMN facial nerve paralysis?", "a": "LMN (Bell's palsy): Entire half of face is paralyzed including forehead wrinkling. UMN (stroke): Forehead wrinkling is preserved due to bilateral cortical innervation."},
        {"q": "What is Bell's phenomenon?", "a": "Upward and outward deviation of the eyeball when the patient attempts to close the paralyzed eyelid."},
        {"q": "What is the first-line medication for Trigeminal Neuralgia?", "a": "Carbamazepine (100–200 mg BD initially, titrated up to 800–1200 mg/day)."}
    ],
    "chap19_meningitis_neuro_infections": [
        {"q": "What are the classic CSF findings in Acute Bacterial Meningitis?", "a": "Marked neutrophilic pleocytosis (>1,000 WBCs/mm³), severely low glucose (<40 mg/dL or CSF/serum ratio < 0.4), and markedly elevated protein (>100 mg/dL)."},
        {"q": "What is Kernig's sign and Brudzinski's sign?", "a": "Kernig's: Resistance or pain on extending the knee when the hip is flexed at 90°. Brudzinski's: Involuntary flexion of hips and knees upon passive flexion of the patient's neck."},
        {"q": "What antibiotic combination is recommended as empirical therapy for bacterial meningitis in adults?", "a": "Ceftriaxone (2 g IV 12-hourly) + Vancomycin (15-20 mg/kg IV 12-hourly) + Dexamethasone (10 mg IV before or with the first antibiotic dose)."}
    ],
    "chap20_shock_cpr": [
        {"q": "What are the 2 shockable rhythms in Cardiopulmonary Resuscitation (ACLS)?", "a": "Ventricular Fibrillation (VF) and Pulseless Ventricular Tachycardia (pVT)."},
        {"q": "What are the chest compression metrics for high-quality adult CPR?", "a": "Rate of 100–120 compressions per minute; Depth of 5 to 6 cm (2 to 2.4 inches); Allow complete chest recoil; Compression-to-ventilation ratio of 30:2."},
        {"q": "What is the drug and dosage of choice for Anaphylactic Shock?", "a": "Intramuscular Adrenaline (Epinephrine): 0.5 mg (0.5 mL of 1:1,000 dilution) injected into the anterolateral thigh."}
    ]
}
