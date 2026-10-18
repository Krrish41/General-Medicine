# -*- coding: utf-8 -*-
"""
Master Builder for General Medicine University Exam Preparation Suite
Generates:
1. General_Medicine_Master_Notes.md (Cleaned Markdown with tables and rubrics)
2. General_Medicine_Master_Notes.html (Print-ready document with embedded schematics)
3. General_Medicine_Master_Notes.pdf (Headless Edge compiled PDF)
4. index.html (Responsive, Interactive Study Dashboard & Clinical Topic Explorer)
"""

import os
import sys
import base64
import json
import subprocess
import re

from content.gastrointestinal_and_hepato import CHAPTERS as c1
from content.cardiovascular import CHAPTERS as c2
from content.infections_and_endocrine import CHAPTERS as c3
from content.hematology_renal_neuro import CHAPTERS as c4
from content.cheat_sheet import CHAPTERS as c5
from content.formatter import ICONS, FAVICON_SVG, clean_latex, parse_markdown_to_html
from content.interactive_data import CLASSIFICATION_PRESETS, SPOTTER_HOTSPOTS, COMPARISON_PAIRS, EXAM_RUBRIC_CRITERIA
from content.diagrams_data import generate_svg_schematic, LAYMAN_ANALOGIES, FLASHCARDS

ALL_CHAPTERS = c1 + c2 + c3 + c4 + c5

def generate_markdown(chapters):
    md_lines = []
    md_lines.append("# Master Compendium of General Medicine: 15-Mark University Examination Monograph")
    md_lines.append("\n*Comprehensive Clinical Internal Medicine Study Guide for BDS (3rd Year) & MBBS Examinations based on Davidson, Harrison & Clinical Lecture Blueprints*\n")
    md_lines.append("## Curriculum Table of Contents")
    for i, ch in enumerate(chapters, 1):
        md_lines.append(f"{i}. [{ch['title']}](#{ch['id']}) - *{ch['category']}*")
    md_lines.append("\n---\n")

    for ch in chapters:
        md_lines.append(f"<a id='{ch['id']}'></a>")
        md_lines.append(f"## {ch['title']}")
        md_lines.append(f"**Category:** {ch['category']} | **Standard:** {ch['badge']} | **Reading Time:** {ch['reading_time']}\n")
        
        md_lines.append("### High-Yield Key Points")
        for kp in ch["key_points"]:
            md_lines.append(f"- {clean_latex(kp)}")
        md_lines.append("")

        md_lines.append(f"> [!TIP]\n> **Clinical Pearl:** {clean_latex(ch['clinical_pearl'])}\n")

        layman = LAYMAN_ANALOGIES.get(ch["id"])
        if layman:
            md_lines.append(f"> [!NOTE]\n> **Layman's Intuition — {layman['title']}:**\n> {layman['analogy']}\n")

        md_lines.append("### Comprehensive 15-Mark Structural Monograph")
        for sec in ch["sections"]:
            md_lines.append(f"\n#### {sec['title']}\n")
            md_lines.append(clean_latex(sec["content"].strip()))
            md_lines.append("")

        if ch.get("comparisons"):
            md_lines.append("\n### Structured Differential Diagnosis & Comparisons")
            for comp in ch["comparisons"]:
                md_lines.append(f"\n##### {comp['title']}\n")
                header_line = "| " + " | ".join(comp["headers"]) + " |"
                sep_line = "| " + " | ".join(["---"] * len(comp["headers"])) + " |"
                md_lines.append(header_line)
                md_lines.append(sep_line)
                for row in comp["rows"]:
                    md_lines.append("| " + " | ".join([clean_latex(cell) for cell in row]) + " |")
                md_lines.append("")

        if ch.get("must_draw"):
            md_lines.append(f"\n> [!IMPORTANT]\n> **Must-Draw Diagram / Flowchart:** {clean_latex(ch['must_draw'])}\n")

        if ch.get("viva_questions"):
            md_lines.append("\n### High-Yield Viva Voce Pearls")
            for q in ch["viva_questions"]:
                md_lines.append(f"- {clean_latex(q)}")
            md_lines.append("")

        md_lines.append("\n---\n")

    return "\n".join(md_lines)

def generate_print_html(chapters):
    html_parts = []
    html_parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/svg+xml" href="{FAVICON_SVG}">
<title>General Medicine Master Compendium - 15-Mark University Examination Monograph</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap');

@page {{
    size: A4;
    margin: 18mm 15mm 20mm 15mm;
    @bottom-right {{
        content: counter(page);
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 8.5pt;
        color: #64748b;
    }}
    @bottom-left {{
        content: "General Medicine Master Monograph | University Exam Preparation";
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 8.5pt;
        color: #64748b;
    }}
}}

body {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #1e293b;
    background: #ffffff;
    line-height: 1.6;
    font-size: 9.5pt;
}}

.cover-page {{
    page-break-after: always;
    height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 40px;
    border-left: 8px solid #059669;
    background: #fafaf9;
}}

.cover-title {{
    font-family: 'Newsreader', serif;
    font-size: 32pt;
    font-weight: 700;
    color: #064e3b;
    line-height: 1.15;
    margin-bottom: 8px;
}}

.cover-subtitle {{
    font-size: 13pt;
    color: #047857;
    font-weight: 600;
    margin-bottom: 24px;
}}

.cover-meta {{
    font-size: 9.5pt;
    color: #475569;
    line-height: 1.8;
}}

.chapter-container {{
    page-break-before: always;
    margin-bottom: 25px;
}}

.chapter-badge {{
    display: inline-block;
    background: #ecfdf5;
    color: #065f46;
    border: 1px solid #a7f3d0;
    font-size: 7.5pt;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}}

.chapter-title {{
    font-family: 'Newsreader', serif;
    font-size: 20pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 0;
    margin-bottom: 12px;
    border-bottom: 2px solid #059669;
    padding-bottom: 6px;
}}

.pearl-box {{
    background: #f0fdf4;
    border-left: 4px solid #10b981;
    padding: 10px 14px;
    margin: 14px 0;
    font-size: 9pt;
    color: #064e3b;
    border-radius: 0 6px 6px 0;
}}

.layman-box {{
    background: #f8fafc;
    border-left: 4px solid #0284c7;
    padding: 10px 14px;
    margin: 14px 0;
    font-size: 8.8pt;
    color: #0f172a;
    border-radius: 0 6px 6px 0;
}}

.section-title {{
    font-size: 11.5pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 18px;
    margin-bottom: 8px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 8.8pt;
    page-break-inside: avoid;
}}

th, td {{
    border: 1px solid #cbd5e1;
    padding: 7px 10px;
    text-align: left;
    vertical-align: top;
}}

th {{
    background-color: #f8fafc;
    color: #0f172a;
    font-weight: 700;
}}

tr:nth-child(even) {{
    background-color: #f1f5f9;
}}

code, pre {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5pt;
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 2px 6px;
}}

pre {{
    padding: 12px;
    overflow-x: auto;
    white-space: pre-wrap;
    line-height: 1.4;
    page-break-inside: avoid;
    break-inside: avoid;
}}

.clinical-flowchart-card, .formula-card, .pearl-box, .layman-box, table, tr, pre, code {{
    page-break-inside: avoid !important;
    break-inside: avoid !important;
}}

ul, ol {{
    padding-left: 20px;
    margin-top: 6px;
    margin-bottom: 10px;
}}

li {{
    margin-bottom: 4px;
}}
</style>
</head>
<body>
<div class="cover-page">
    <div style="width: 50px; height: 50px; background: #059669; border-radius: 12px; margin-bottom: 20px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 24pt; font-weight: 800;">M</div>
    <div class="cover-title">General Medicine</div>
    <div class="cover-subtitle">15-Mark University Examination Master Monograph</div>
    <div class="cover-meta">
        <strong>Curriculum:</strong> BDS 3rd Year &amp; MBBS Clinical Medicine<br>
        <strong>Primary References:</strong> Davidson's Principles and Practice of Medicine, Harrison's Principles of Internal Medicine, Chugh Clinical Medicine<br>
        <strong>Core Inclusions:</strong> Diagnostic Criteria (Duke, Jones, ADA), Emergency Protocols, Hepatology, Hematology, Chairside Dental Safety Guidelines
    </div>
</div>
""")

    for ch in chapters:
        html_parts.append(f"""<div class="chapter-container" id="{ch['id']}">
        <span class="chapter-badge">{ch['category']} • {ch['badge']}</span>
        <h1 class="chapter-title">{ch['title']}</h1>
        
        <div class="pearl-box">
            <strong>Clinical Pearl:</strong> {clean_latex(ch['clinical_pearl'])}
        </div>
        """)

        layman = LAYMAN_ANALOGIES.get(ch["id"])
        if layman:
            html_parts.append(f"""<div class="layman-box">
                <strong style="color: #0369a1;">Layman's Intuition — {layman['title']}:</strong><br>
                {layman['analogy']}
            </div>""")

        for sec in ch["sections"]:
            html_parts.append(f"""<h3 class="section-title">{sec['title']}</h3>""")
            html_parts.append(parse_markdown_to_html(sec["content"]))

        if ch.get("comparisons"):
            for comp in ch["comparisons"]:
                html_parts.append(f"""<h4 style="margin-top: 14px; font-weight: 700; color: #065f46;">{comp['title']}</h4>""")
                html_parts.append("<table><thead><tr>")
                for h in comp["headers"]:
                    html_parts.append(f"<th>{h}</th>")
                html_parts.append("</tr></thead><tbody>")
                for row in comp["rows"]:
                    html_parts.append("<tr>")
                    for cell in row:
                        html_parts.append(f"<td>{clean_latex(cell)}</td>")
                    html_parts.append("</tr>")
                html_parts.append("</tbody></table>")

        if ch.get("viva_questions"):
            html_parts.append("""<div style="background: #fafafa; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; margin-top: 16px;">
                <h4 style="margin: 0 0 8px 0; color: #047857; font-size: 9.5pt; text-transform: uppercase;">High-Yield Clinical &amp; Viva Voce Pearls</h4>
                <ul style="margin: 0; padding-left: 20px;">""")
            for q in ch["viva_questions"]:
                html_parts.append(f"""<li style="margin-bottom: 4px; font-size: 8.8pt;">{clean_latex(q)}</li>""")
            html_parts.append("</ul></div>")

        html_parts.append("</div>")

    html_parts.append("</body></html>")
    return "\n".join(html_parts)

def generate_interactive_dashboard(chapters):
    # Pre-bundle chapters data with diagrams, analogies, flashcards and classifications
    enriched_chapters = []
    for ch in chapters:
        ch_id = ch["id"]
        svg_diagram = generate_svg_schematic(ch_id, ch["title"])
        analogy = LAYMAN_ANALOGIES.get(ch_id, {
            "title": "Clinical Intuition",
            "analogy": ch["clinical_pearl"]
        })
        cards = FLASHCARDS.get(ch_id, [
            {"q": f"What is the clinical hallmark of {ch['title']}?", "a": ch['clinical_pearl']}
        ])
        
        # Check classification presets or extract from sections
        custom_types = CLASSIFICATION_PRESETS.get(ch_id)
        if not custom_types:
            # Fallback types based on sections
            type_list = []
            for sec in ch["sections"][:4]:
                clean_lines = [l.strip() for l in clean_latex(sec["content"]).split('\n') if not l.strip().startswith('|') and not l.strip().startswith('#') and l.strip()]
                clean_text = ' '.join(clean_lines)
                if len(clean_text) > 220:
                    clean_text = clean_text[:220].rsplit(' ', 1)[0] + '...'
                if clean_text.count('**') % 2 != 0:
                    clean_text = clean_text.rsplit('**', 1)[0] + '...'
                type_list.append({
                    "name": sec["title"],
                    "badge": "Core Monograph Section",
                    "hemodynamics": "High-Yield Clinical Standard",
                    "summary": clean_text
                })
            custom_types = {
                "title": f"Classification & Subtypes: {ch['title']}",
                "types": type_list
            }

        word_count = sum(len(sec["content"].split()) for sec in ch["sections"])
        word_count += len(ch.get("clinical_pearl", "").split())
        read_minutes = max(5, round(word_count / 180))

        clean_title = re.sub(r'^(Chapter\s*\d+[:.]*|\d+[\.:\s]+)', '', ch["title"], flags=re.IGNORECASE).strip()
        slug = re.sub(r'[^a-zA-Z0-9]+', '-', clean_title).strip('-').lower()

        enriched_chapters.append({
            "id": ch["id"],
            "slug": slug,
            "title": ch["title"],
            "category": ch["category"],
            "badge": ch["badge"],
            "readMinutes": read_minutes,
            "readingTime": f"{read_minutes} min read",
            "reading_time": f"{read_minutes} min read",
            "clinical_pearl": ch["clinical_pearl"],
            "key_points": ch.get("key_points", []),
            "sections": ch["sections"],
            "comparisons": ch.get("comparisons", []),
            "must_draw": ch.get("must_draw", ""),
            "viva_questions": ch.get("viva_questions", []),
            "schematic_svg": svg_diagram,
            "analogy": analogy,
            "flashcards": cards,
            "classification": custom_types,
            "tags": [ch["category"], "medicine", slug, ch["id"]]
        })

    chapters_json = json.dumps(enriched_chapters)
    comparisons_json = json.dumps(COMPARISON_PAIRS)
    rubric_json = json.dumps(EXAM_RUBRIC_CRITERIA)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/svg+xml" href="favicon.svg?v=2">
    <link rel="alternate icon" href="favicon.ico?v=2">
    <link rel="apple-touch-icon" href="apple-touch-icon.png?v=2">
    <link rel="manifest" href="manifest.json?v=2">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Medicine Pro">
    <meta name="color-scheme" content="light dark">
    <meta name="theme-color" content="#090a12" id="metaThemeColor">
    <title>Medicine Pro — University Exam Monograph | BDS Clinical Vault</title>
    <script>
    (function() {{
        try {{
            var t = localStorage.getItem('bds.theme') || localStorage.getItem('bds.medicine.theme') || localStorage.getItem('medicine_theme');
            if (t === 'light') {{
                document.documentElement.setAttribute('data-theme', 'light');
                document.documentElement.classList.remove('dark');
                document.documentElement.classList.add('light');
                document.documentElement.style.colorScheme = 'light';
            }} else {{
                document.documentElement.setAttribute('data-theme', 'dark');
                document.documentElement.classList.remove('light');
                document.documentElement.classList.add('dark');
                document.documentElement.style.colorScheme = 'dark';
            }}
        }} catch(e) {{}}
    }})();
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="portal-core/core-shell.css">
    <script src="portal-core/core-engine.js"></script>
    <style>
        :root {{
            color-scheme: dark;

            /* Per-portal Accent: Medicine Diagnostic Sky Blue */
            --accent-primary: #38bdf8;
            --accent-primary-dark: #0369a1;
            --accent-btn-bg: #0369a1;
            --accent-btn-hover: #0284c7;
            --accent-btn-border: rgba(56, 189, 248, 0.55);
            --accent-light: rgba(56, 189, 248, 0.12);
            --accent-glow: rgba(56, 189, 248, 0.18);
            --border-accent: rgba(56, 189, 248, 0.28);
            --accent-text: #7dd3fc;
            --accent-contrast: #082f49;
            --primary: #38bdf8;
            --primary-dark: #0284c7;
            --sidebar-w: 304px;

            /* Shared Neutral Tokens (Obsidian Dark Default) */
            --bg-base: #090a12;
            --bg-surface: #101322;
            --bg-card: #101322;
            --bg-card-hover: #171b30;
            --border-color: rgba(255, 255, 255, 0.09);
            --border-strong: rgba(255, 255, 255, 0.18);
            --border-active: #38bdf8;
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --header-bg: rgba(9, 10, 18, 0.94);
            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.4);
            --shadow-md: 0 4px 14px rgba(0, 0, 0, 0.5);
            --shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.7);
        }}

        html[data-theme="light"], body.light {{
            color-scheme: light;
            --bg-base: #f8fafc;
            --bg-surface: #ffffff;
            --bg-card: #ffffff;
            --bg-card-hover: #f1f5f9;
            --border-color: #e2e8f0;
            --border-strong: #cbd5e1;
            --border-active: #38bdf8;
            --text-primary: #0f172a;
            --text-secondary: #334155;
            --text-muted: #64748b;
            --header-bg: rgba(255, 255, 255, 0.94);
            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.06);
            --shadow-md: 0 4px 14px rgba(0, 0, 0, 0.08);
            --shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.12);
        }}

        html[data-theme="dark"], body.dark {{
            color-scheme: dark;
            --bg-base: #090a12;
            --bg-surface: #101322;
            --bg-card: #101322;
            --bg-card-hover: #171b30;
            --border-color: rgba(255, 255, 255, 0.09);
            --border-strong: rgba(255, 255, 255, 0.18);
            --border-active: #38bdf8;
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --accent-primary: #38bdf8;
            --accent-primary-dark: #0284c7;
            --accent-light: rgba(56, 189, 248, 0.12);
            --accent-glow: rgba(56, 189, 248, 0.18);
            --header-bg: rgba(9, 10, 18, 0.94);
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.4);
            --shadow-md: 0 4px 14px rgba(0,0,0,0.5);
            --shadow-lg: 0 10px 30px rgba(0,0,0,0.7);
        }}

        /* Ultra-thin surgical scrollbar */
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: transparent;
        }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(148, 163, 184, 0.35);
            border-radius: 999px;
            border: 1px solid transparent;
            background-clip: content-box;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(100, 116, 139, 0.6);
        }}
        body.dark ::-webkit-scrollbar-thumb {{
            background: rgba(148, 163, 184, 0.25);
        }}
        body.dark ::-webkit-scrollbar-thumb:hover {{
            background: rgba(148, 163, 184, 0.45);
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            scrollbar-width: thin;
            scrollbar-color: rgba(148, 163, 184, 0.35) transparent;
        }}

        /* Tactile button feedback */
        .btn:active, .nav-btn:active, .speed-pill:active, .mobile-bottom-tab:active, .filter-chip:active {{
            transform: scale(0.96) translateY(1px);
        }}

        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-base);
            color: var(--text-primary);
            line-height: 1.6;
            height: 100vh;
            display: flex;
            flex-direction: row;
            overflow: hidden;
            font-size: 14px;
        }}

        #sidebar-backdrop {{
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(4px);
            z-index: 95;
        }}
        #sidebar-backdrop.active {{
            display: block;
        }}

        /* Sidebar - Docked 304px (Spec 2.6) */
        .sidebar {{
            width: 304px;
            min-width: 304px;
            max-width: 304px;
            flex-shrink: 0;
            border-right: 1px solid var(--border-color);
            background: var(--bg-surface);
            display: flex;
            flex-direction: column;
            height: 100vh;
            position: sticky;
            top: 0;
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 100;
        }}

        /* Main View / Main Column */
        .main-column {{
            flex: 1;
            min-width: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
            overflow-y: auto;
            position: relative;
            background: var(--bg-base);
        }}

        /* 64px Topbar */
        .top-bar {{
            height: 64px;
            min-height: 64px;
            padding: 0 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--border-color);
            background: var(--bg-surface);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            position: sticky;
            top: 0;
            z-index: 90;
            gap: 12px;
            flex-shrink: 0;
        }}

        .top-bar-left {{
            display: flex;
            align-items: center;
            gap: 12px;
            min-width: 0;
        }}

        .top-right-tools {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-shrink: 0;
        }}

        @media (max-width: 1150px) {{
            .top-right-tools .btn-label {{
                display: none;
            }}
        }}

        .mobile-menu-btn {{
            display: none;
            background: none;
            border: none;
            cursor: pointer;
            color: var(--text-primary);
            padding: 6px;
            border-radius: var(--radius-sm);
        }}

        @media (max-width: 1024px) {{
            .mobile-menu-btn {{
                display: inline-flex;
            }}
            .sidebar {{
                position: fixed;
                left: -320px;
                top: 0;
                bottom: 0;
                width: 290px;
                min-width: 290px;
            }}
            .sidebar.open, .sidebar.active {{
                transform: translateX(320px);
            }}
        }}

        .nav-btn {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 7px 14px;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            display: inline-flex;
            align-items: center;
            gap: 6px;
            box-shadow: var(--shadow-sm);
        }}

        .nav-btn:hover {{
            background: var(--accent-light);
            border-color: var(--accent-primary);
            color: var(--accent-primary);
        }}

        .nav-btn-primary {{
            background: var(--accent-btn-bg);
            color: #ffffff !important;
            border: 1px solid var(--accent-btn-border);
            font-weight: 700;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.35);
        }}
        .nav-btn-primary:hover {{
            background: var(--accent-btn-hover);
            border-color: var(--accent-primary);
            color: #ffffff !important;
            box-shadow: 0 0 14px var(--accent-glow);
        }}

        .sidebar-header {{
            padding: 14px 16px;
            border-bottom: 1px solid var(--border-color);
        }}

        .search-box {{
            position: relative;
            margin-bottom: 10px;
        }}

        .search-input {{
            width: 100%;
            padding: 9px 36px 9px 12px;
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            color: var(--text-primary);
            font-size: 0.85rem;
            font-family: inherit;
            outline: none;
            transition: border-color 0.2s ease;
        }}
        .search-input:focus {{
            border-color: var(--accent-primary);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }}

        .search-kbd {{
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 4px;
            font-size: 0.7rem;
            padding: 1px 5px;
            color: var(--text-muted);
            pointer-events: none;
        }}

        .category-scroll {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            padding-bottom: 4px;
        }}

        .filter-chip {{
            white-space: nowrap;
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.72rem;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 999px;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .filter-chip:hover:not(.active) {{
            background: var(--accent-light);
            color: var(--text-primary);
            border-color: var(--border-accent);
        }}
        .filter-chip.active {{
            background: var(--accent-btn-bg);
            color: #ffffff !important;
            border-color: var(--accent-btn-border);
            box-shadow: 0 0 10px var(--accent-glow);
            font-weight: 700;
        }}
        .filter-chip.active:hover {{
            background: var(--accent-btn-hover);
            border-color: var(--accent-primary);
            color: #ffffff !important;
        }}

        .topic-list {{
            flex: 1;
            overflow-y: auto;
            padding: 8px;
        }}

        .topic-item {{
            display: flex;
            align-items: flex-start;
            gap: 10px;
            padding: 10px 12px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.15s ease;
            margin-bottom: 4px;
            border: 1px solid transparent;
        }}
        .topic-item:hover {{
            background: var(--bg-card-hover);
        }}
        .topic-item.active {{
            background: var(--accent-light);
            border-color: var(--accent-primary);
        }}
        .topic-check {{
            margin-top: 2px;
            color: var(--text-muted);
            cursor: pointer;
            flex-shrink: 0;
        }}
        .topic-check.completed {{
            color: var(--accent-primary);
        }}
        .topic-info {{
            flex: 1;
            min-width: 0;
        }}
        .topic-title {{
            font-size: 0.86rem;
            font-weight: 600;
            color: var(--text-primary);
            line-height: 1.35;
        }}
        .topic-meta {{
            font-size: 0.72rem;
            color: var(--text-secondary);
            font-weight: 500;
            margin-top: 2px;
        }}

        /* Content Area */
        .content-area {{
            flex: 1;
            min-width: 0;
            padding: 24px 32px 120px 32px;
            overflow-y: auto;
        }}

        /* Dashboard Hero */
        .dash-hero {{
            background: linear-gradient(135deg, rgba(5, 150, 105, 0.08), rgba(4, 120, 87, 0.03));
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 24px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            flex-wrap: wrap;
        }}
        .dash-badge {{
            display: inline-block;
            background: var(--accent-light);
            color: var(--accent-primary);
            font-size: 0.75rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }}
        .dash-title {{
            font-family: 'Newsreader', serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--text-primary);
        }}
        .dash-subtitle {{
            font-size: 0.88rem;
            color: var(--text-secondary);
            margin-top: 4px;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 12px;
            margin-bottom: 28px;
        }}
        .stat-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 14px 18px;
            box-shadow: var(--shadow-sm);
        }}
        .stat-val {{
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--accent-primary);
            line-height: 1.1;
        }}
        .stat-lbl {{
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 600;
            margin-top: 4px;
        }}

        /* Chapter View Header & Tabs */
        .chapter-header {{
            margin-bottom: 20px;
        }}
        .chapter-top-badge {{
            display: inline-block;
            background: var(--accent-light);
            color: var(--accent-primary);
            font-size: 0.75rem;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 6px;
            text-transform: uppercase;
            margin-bottom: 8px;
            border: 1px solid var(--accent-primary);
        }}
        html[data-theme="light"] .chapter-top-badge,
        body.light .chapter-top-badge {{
            background: rgba(56, 189, 248, 0.12);
            color: #0369a1;
            border-color: rgba(56, 189, 248, 0.4);
        }}
        html[data-theme="dark"] .chapter-top-badge,
        body.dark .chapter-top-badge {{
            background: rgba(56, 189, 248, 0.18);
            color: #7dd3fc;
            border-color: rgba(56, 189, 248, 0.6);
        }}
        .chapter-title-display {{
            font-family: 'Newsreader', serif;
            font-size: 2.2rem;
            font-weight: 700;
            color: var(--text-primary);
            line-height: 1.2;
            letter-spacing: -0.5px;
        }}

        .tab-bar-container {{
            position: sticky;
            top: 61px;
            background: var(--bg-base);
            z-index: 30;
            padding: 10px 0;
            margin-bottom: 20px;
            border-bottom: 1px solid var(--border-color);
        }}
        .tab-bar {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            padding-bottom: 4px;
        }}
        .tab-btn {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.82rem;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            white-space: nowrap;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: var(--shadow-sm);
        }}
        .tab-btn:hover {{
            background: var(--bg-card-hover);
            color: var(--text-primary);
        }}
        .tab-btn.active {{
            background: var(--accent-btn-bg);
            color: #ffffff !important;
            border-color: var(--accent-btn-border);
            box-shadow: 0 4px 12px var(--accent-glow);
            font-weight: 700;
        }}

        /* 15-Mark Master Essay Reading Ergonomics */
        .master-essay-content {{
            max-width: 76ch;
            margin: 0 auto;
        }}
        .pearl-card {{
            background: var(--accent-light);
            border-left: 4px solid var(--accent-primary);
            border-radius: 0 8px 8px 0;
            padding: 14px 18px;
            margin-bottom: 24px;
            font-size: 0.92rem;
            color: var(--text-primary);
        }}
        .essay-section-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px 28px;
            margin-bottom: 20px;
            box-shadow: var(--shadow-sm);
        }}
        .essay-section-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 14px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
        }}
        .essay-section-title {{
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-primary);
        }}
        .essay-body {{
            font-size: 0.96rem;
            line-height: 1.72;
            color: var(--text-secondary);
        }}
        .essay-body h4 {{
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--text-primary);
            margin: 18px 0 8px 0;
        }}
        .essay-body p {{
            margin-bottom: 14px;
        }}
        .essay-body ul, .essay-body ol {{
            padding-left: 22px;
            margin-bottom: 14px;
        }}
        .essay-body li {{
            margin-bottom: 6px;
        }}
        .essay-body table {{
            width: 100%;
            border-collapse: collapse;
            margin: 18px 0;
            font-size: 0.88rem;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            overflow: hidden;
        }}
        .essay-body th, .essay-body td {{
            padding: 10px 14px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}
        .essay-body th {{
            background: var(--bg-base);
            color: var(--text-primary);
            font-weight: 700;
        }}
        .essay-body tr:nth-child(even) {{
            background: var(--bg-card-hover);
        }}
        .essay-body pre {{
            background: #0f172a;
            color: #a7f3d0;
            border-radius: 8px;
            padding: 14px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            overflow-x: auto;
            margin: 16px 0;
        }}

        /* Layman Intuition Card */
        .layman-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 28px;
            box-shadow: var(--shadow-sm);
        }}
        .layman-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
        }}
        .layman-badge {{
            background: #e0f2fe;
            color: #0369a1;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 6px;
        }}
        .layman-title {{
            font-family: 'Newsreader', serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--text-primary);
        }}
        .layman-body {{
            font-size: 1.02rem;
            line-height: 1.8;
            color: var(--text-secondary);
        }}

        /* Classification / Types Explorer */
        .types-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 18px;
        }}
        .type-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            box-shadow: var(--shadow-sm);
            transition: all 0.2s ease;
        }}
        .type-card:hover {{
            border-color: var(--accent-primary);
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }}
        .type-card-badge {{
            display: inline-block;
            background: var(--accent-light);
            color: var(--accent-primary);
            font-size: 0.72rem;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 4px;
            margin-bottom: 8px;
        }}
        .type-card-title {{
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 8px;
        }}
        .type-card-stat {{
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 6px 10px;
            font-size: 0.78rem;
            font-family: 'JetBrains Mono', monospace;
            color: var(--accent-primary);
            margin-bottom: 10px;
        }}
        .type-card-summary {{
            font-size: 0.88rem;
            color: var(--text-secondary);
            line-height: 1.5;
        }}

        /* Diagrams Gallery */
        .diagram-container {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-sm);
        }}
        .diagram-title {{
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 14px;
        }}
        .diagram-viewer-box {{
            cursor: zoom-in;
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background: #0f172a;
        }}

        /* Examiner Viva Voce */
        .viva-item {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 18px 22px;
            margin-bottom: 14px;
            box-shadow: var(--shadow-sm);
        }}
        .viva-q {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 8px;
        }}
        .viva-speaker-btn {{
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            color: var(--accent-primary);
            width: 32px;
            height: 32px;
            border-radius: 8px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            flex-shrink: 0;
            transition: all 0.2s ease;
        }}
        .viva-speaker-btn:hover {{
            background: var(--accent-light);
            border-color: var(--accent-primary);
        }}
        .viva-reveal-btn {{
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.8rem;
            font-weight: 600;
            padding: 5px 12px;
            border-radius: 6px;
            cursor: pointer;
            margin-top: 6px;
        }}
        .viva-ans {{
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px dashed var(--border-color);
            font-size: 0.92rem;
            color: var(--text-secondary);
            display: none;
        }}
        .viva-ans.revealed {{
            display: block;
        }}

        /* Active Recall Flashcards */
        .flashcard-wrap {{
            max-width: 620px;
            margin: 20px auto;
            perspective: 1000px;
        }}
        .flashcard {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            min-height: 280px;
            padding: 36px 32px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            cursor: pointer;
            box-shadow: var(--shadow-md);
            position: relative;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}
        .flashcard:hover {{
            border-color: var(--accent-primary);
        }}
        .flashcard-tag {{
            position: absolute;
            top: 18px;
            left: 20px;
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--accent-primary);
        }}
        .flashcard-instruction {{
            position: absolute;
            bottom: 16px;
            font-size: 0.75rem;
            color: var(--text-muted);
        }}
        .flashcard-text {{
            font-size: 1.18rem;
            font-weight: 600;
            color: var(--text-primary);
            line-height: 1.6;
        }}
        .flashcard-controls {{
            display: flex;
            justify-content: center;
            gap: 14px;
            margin-top: 20px;
        }}

        /* Exam Simulator & Rubric */
        .exam-sim-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 24px;
            box-shadow: var(--shadow-sm);
        }}
        .rubric-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            padding: 12px 0;
            border-bottom: 1px solid var(--border-color);
        }}
        .rubric-info h4 {{
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--text-primary);
        }}
        .rubric-info p {{
            font-size: 0.82rem;
            color: var(--text-muted);
        }}
        .rubric-slider {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        /* Clinical Notes */
        .notes-textarea {{
            width: 100%;
            height: 380px;
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px;
            font-family: inherit;
            font-size: 0.95rem;
            color: var(--text-primary);
            line-height: 1.6;
            outline: none;
            resize: vertical;
        }}
        .notes-textarea:focus {{
            border-color: var(--accent-primary);
            box-shadow: 0 0 0 3px var(--accent-glow);
        }}

        /* Modern Floating Island Audio Player Dock */
        .audio-dock {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 48px);
            max-width: 1040px;
            z-index: 1050;
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(28px) saturate(180%);
            -webkit-backdrop-filter: blur(28px) saturate(180%);
            border: 1px solid rgba(5, 150, 105, 0.25);
            border-radius: 22px;
            box-shadow: 0 16px 42px -6px rgba(15, 23, 42, 0.25), 0 4px 16px rgba(0, 0, 0, 0.05);
            padding: 12px 22px;
            display: block;
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.35s ease;
        }}
        body.dark .audio-dock {{
            background: rgba(15, 23, 42, 0.94);
            border: 1px solid rgba(16, 185, 129, 0.25);
            box-shadow: 0 20px 50px -8px rgba(0, 0, 0, 0.75), 0 0 24px rgba(5, 150, 105, 0.18);
        }}
        .audio-dock.hidden {{
            transform: translate(-50%, 150%);
            opacity: 0;
            pointer-events: none;
        }}
        .audio-dock-inner {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 18px;
            flex-wrap: wrap;
        }}
        .audio-dock-meta {{
            display: flex;
            align-items: center;
            gap: 12px;
            min-width: 200px;
            max-width: 300px;
            flex-shrink: 0;
        }}
        .audio-dock-track-icon {{
            width: 42px;
            height: 42px;
            border-radius: 12px;
            background: linear-gradient(135deg, #059669 0%, #047857 100%);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3);
        }}
        .audio-dock.is-playing .audio-dock-track-icon {{
            animation: pulseTrackIcon 2.4s ease-in-out infinite;
        }}
        @keyframes pulseTrackIcon {{
            0%, 100% {{ transform: scale(1); box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3); }}
            50% {{ transform: scale(1.05); box-shadow: 0 6px 18px rgba(5, 150, 105, 0.45); }}
        }}
        .audio-dock-track-title {{
            font-size: 9pt;
            font-weight: 700;
            color: var(--text-primary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .audio-dock-chapter-title {{
            font-size: 7.5pt;
            color: var(--text-muted);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            margin-top: 2px;
        }}
        .audio-dock-controls-wrap {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
            flex: 1;
            min-width: 240px;
        }}
        .audio-dock-buttons {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .audio-control-btn {{
            background: transparent;
            border: none;
            color: var(--text-primary);
            cursor: pointer;
            padding: 6px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
        }}
        .audio-control-btn:hover {{
            background: var(--bg-card-hover);
            color: var(--accent-primary);
        }}
        .audio-btn-playpause {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--accent-btn-bg);
            border: 1px solid var(--accent-btn-border);
            color: #ffffff !important;
            box-shadow: 0 4px 14px var(--accent-glow);
        }}
        .audio-btn-playpause:hover {{
            background: var(--accent-btn-hover);
            transform: scale(1.04);
        }}
        .audio-dock-progress-wrap {{
            display: flex;
            align-items: center;
            gap: 10px;
            width: 100%;
            max-width: 440px;
        }}
        .audio-time-label {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 7.5pt;
            color: var(--text-muted);
            min-width: 36px;
        }}
        .audio-scrubber {{
            flex: 1;
            -webkit-appearance: none;
            appearance: none;
            height: 4px;
            border-radius: 999px;
            background: #cbd5e1;
            outline: none;
            cursor: pointer;
        }}
        body.dark .audio-scrubber {{
            background: #334155;
        }}
        .audio-scrubber::-webkit-slider-thumb {{
            -webkit-appearance: none;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--accent-primary);
            cursor: pointer;
        }}
        .audio-dock-options {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-shrink: 0;
        }}
        .audio-voice-select {{
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            font-size: 7.5pt;
            font-weight: 600;
            padding: 4px 8px;
            border-radius: 8px;
            outline: none;
            cursor: pointer;
            max-width: 160px;
        }}
        .audio-speed-selector {{
            display: flex;
            align-items: center;
            gap: 4px;
            background: var(--bg-base);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 3px 6px;
        }}
        .speed-label {{
            font-size: 7.5pt;
            color: var(--text-primary);
            font-weight: 700;
            margin-right: 2px;
        }}
        .speed-pill {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            font-size: 7.5pt;
            font-weight: 700;
            padding: 3px 6px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .speed-pill:hover {{
            color: var(--accent-primary);
        }}
        .speed-pill.active {{
            background: var(--accent-btn-bg);
            color: #ffffff !important;
            border: 1px solid var(--accent-btn-border);
            font-weight: 700;
        }}
        .audio-dock-close {{
            background: transparent;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            padding: 6px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .audio-dock-close:hover {{
            background: var(--bg-card-hover);
            color: #ef4444;
        }}

        /* Mobile Bottom Floating Bar */
        .mobile-bottom-bar {{
            display: none;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: var(--header-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-top: 1px solid var(--border-color);
            padding: 6px 12px 10px 12px;
            z-index: 90;
            justify-content: space-around;
        }}
        .mobile-bottom-tab {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            font-size: 0.74rem;
            font-weight: 700;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 3px;
            cursor: pointer;
            padding: 4px 8px;
            border-radius: 8px;
        }}
        .mobile-bottom-tab.active {{
            color: var(--accent-primary);
        }}

        /* Modals */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.82);
            backdrop-filter: blur(8px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 2000;
            padding: 20px;
        }}
        .modal-box {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            max-width: 960px;
            width: 100%;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: var(--shadow-lg);
        }}
        .modal-header {{
            padding: 14px 20px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .modal-body {{
            padding: 20px;
            overflow-y: auto;
            flex: 1;
        }}

        @media (max-width: 1024px) {{
            .audio-dock {{
                bottom: 74px !important;
                padding: 10px 16px;
            }}
            .sidebar {{
                position: fixed;
                left: 0;
                top: 61px;
                bottom: 0;
                transform: translateX(-100%);
            }}
            .sidebar.open {{
                transform: translateX(0);
            }}
            .mobile-bottom-bar {{
                display: flex;
            }}
            .content-area {{
                padding: 16px 16px 140px 16px;
            }}
        }}

        @media (max-width: 640px) {{
            .navbar {{
                padding: 0.6rem 1rem;
            }}
            .chapter-title-display {{
                font-size: 1.6rem;
            }}
            .audio-dock {{
                width: calc(100% - 24px);
                padding: 8px 12px;
            }}
            .audio-voice-wrap {{
                display: none;
            }}
        }}

        /* Responsive Data Tables */
        .table-responsive {{
            width: 100%;
            overflow-x: auto;
            margin: 18px 0 24px 0;
            border-radius: 10px;
            border: 1px solid var(--border-color);
            background: var(--bg-surface);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        }}

        .data-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
            line-height: 1.5;
            text-align: left;
            font-variant-numeric: tabular-nums;
        }}

        .data-table th, .data-table td {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
        }}

        .data-table th {{
            background: var(--bg-surface);
            color: var(--accent-primary);
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.74rem;
            letter-spacing: 0.06em;
            border-bottom: 2px solid var(--accent-primary);
        }}

        .data-table tbody tr:nth-child(even) {{
            background: rgba(99, 102, 241, 0.03);
        }}

        body.dark .data-table tbody tr:nth-child(even) {{
            background: rgba(255, 255, 255, 0.02);
        }}

        .data-table tbody tr:hover {{
            background: rgba(99, 102, 241, 0.08);
        }}

        /* Clinical Formula Callout Box */
        .formula-card {{
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(139, 92, 246, 0.04) 100%);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-left: 4px solid var(--accent-primary);
            border-radius: 10px;
            padding: 14px 18px;
            margin: 16px 0;
        }}

        .formula-header {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--accent-primary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 6px;
        }}

        .formula-equation {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-primary);
            padding: 4px 0;
        }}

        /* Callout Alerts */
        .callout-alert {{
            display: flex;
            align-items: flex-start;
            gap: 12px;
            padding: 14px 18px;
            border-radius: 10px;
            margin: 16px 0;
            font-size: 0.92rem;
            line-height: 1.55;
        }}

        .callout-alert.alert-tip {{
            background: rgba(16, 185, 129, 0.08);
            border: 1px solid rgba(16, 185, 129, 0.25);
            border-left: 4px solid #10b981;
            color: var(--text-primary);
        }}

        .callout-alert.alert-note {{
            background: rgba(99, 102, 241, 0.08);
            border: 1px solid rgba(99, 102, 241, 0.25);
            border-left: 4px solid #6366f1;
            color: var(--text-primary);
        }}

        .callout-alert.alert-important {{
            background: rgba(245, 158, 11, 0.08);
            border: 1px solid rgba(245, 158, 11, 0.25);
            border-left: 4px solid #f59e0b;
            color: var(--text-primary);
        }}

        .content-list, .content-list-ordered {{
            padding-left: 24px;
            margin: 10px 0 16px 0;
        }}

        .content-list li, .content-list-ordered li {{
            margin-bottom: 6px;
            line-height: 1.55;
            color: var(--text-secondary);
        }}

        .content-para {{
            margin-bottom: 12px;
            line-height: 1.65;
            color: var(--text-secondary);
        }}

        .algorithm-block {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 14px 16px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            overflow-x: auto;
            margin: 16px 0;
            color: var(--text-primary);
        }}

        .inline-code {{
            background: rgba(99, 102, 241, 0.1);
            color: var(--accent-primary);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85em;
        }}

        /* Dashboard Specific Styles matching Calm Obsidian Theme */
        .dash-hero-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-left: 4px solid var(--accent-primary);
            border-radius: 14px;
            padding: 26px 30px;
            margin-bottom: 22px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 24px;
            color: var(--text-primary);
            box-shadow: var(--shadow-sm);
        }}

        .dash-hero-badge {{
            display: inline-block;
            font-size: 0.74rem;
            font-weight: 700;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            background: var(--accent-light);
            color: var(--accent-primary);
            padding: 4px 12px;
            border-radius: 9999px;
            margin-bottom: 12px;
        }}

        .dash-hero-title {{
            font-size: 1.9rem;
            font-weight: 800;
            color: var(--text-primary);
            margin: 0 0 8px 0;
            letter-spacing: -0.02em;
            line-height: 1.25;
        }}

        .dash-hero-sub {{
            font-size: 0.95rem;
            color: var(--text-secondary);
            margin: 0 0 16px 0;
            line-height: 1.5;
        }}

        .dash-hero-meta {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .dash-hero-stat {{
            font-size: 0.84rem;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            padding: 5px 14px;
            border-radius: 9999px;
            color: var(--text-secondary);
            font-weight: 500;
        }}

        .dash-hero-image-box {{
            flex-shrink: 0;
            width: 260px;
            height: 140px;
            border-radius: 10px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(0, 0, 0, 0.2);
            border: 1px solid var(--border-color);
        }}

        .dash-cheat-sheet-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-left: 4px solid var(--accent-primary);
            border-radius: 14px;
            padding: 20px 24px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            color: var(--text-primary);
            box-shadow: var(--shadow-sm);
            flex-wrap: wrap;
        }}

        .cheat-sheet-badge-icon {{
            width: 44px;
            height: 44px;
            border-radius: 12px;
            background: var(--accent-light);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            color: var(--accent-primary);
        }}

        .stats-grid-dashboard {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }}

        .stat-card-box {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 18px 20px;
            box-shadow: var(--shadow-sm);
        }}

        .stat-card-label {{
            font-size: 0.76rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: var(--text-muted);
            margin-bottom: 6px;
            font-weight: 600;
        }}

        .stat-card-val {{
            font-size: 1.85rem;
            font-weight: 800;
            color: var(--accent-primary);
            line-height: 1.2;
        }}

        .progress-banner-dash {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 18px 22px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-sm);
        }}

        .progress-bar-bg-dash {{
            width: 100%;
            height: 9px;
            background-color: var(--border-color);
            border-radius: 999px;
            overflow: hidden;
            margin-top: 10px;
        }}

        .progress-bar-fill-dash {{
            height: 100%;
            background: linear-gradient(90deg, #6366f1 0%, #4f46e5 50%, #10b981 100%);
            border-radius: 999px;
            width: 0%;
            transition: width 0.4s ease;
        }}

        .dashboard-topic-cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
            gap: 16px;
        }}

        .dash-topic-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.25s ease;
            box-shadow: var(--shadow-sm);
        }}

        .dash-topic-card:hover {{
            transform: translateY(-2px);
            border-color: var(--accent-primary);
            box-shadow: var(--shadow-md);
        }}

        .dash-topic-card.completed {{
            border-color: rgba(16, 185, 129, 0.4);
            background: rgba(16, 185, 129, 0.02);
        }}

        .dash-card-header-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 8px;
        }}

        .dash-card-chapter-tag {{
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--accent-primary);
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }}

        .dash-card-title-text {{
            font-size: 1.02rem;
            font-weight: 700;
            color: var(--text-primary);
            line-height: 1.35;
            margin-bottom: 6px;
        }}

        .dash-card-source-text {{
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-bottom: 16px;
        }}

        .dash-card-footer-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-top: 12px;
            border-top: 1px solid var(--border-color);
        }}

        .toggle-complete-btn {{
            background: transparent;
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            font-size: 0.78rem;
            padding: 6px 12px;
            border-radius: 7px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-weight: 600;
            transition: all 0.2s ease;
        }}

        .toggle-complete-btn:hover {{
            border-color: var(--accent-primary);
            color: var(--accent-primary);
        }}

        .toggle-complete-btn.is-completed {{
            background: rgba(16, 185, 129, 0.1);
            border-color: #10b981;
            color: #10b981;
        }}

        /* Focus Timer Pill */
        .focus-timer-pill {{
            display: inline-flex;
            align-items: center;
        }}
        .btn-focus-timer {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            font-weight: 600;
        }}
        .btn-focus-timer.running {{
            border-color: var(--accent-primary) !important;
            color: var(--accent-primary) !important;
            box-shadow: 0 0 10px var(--accent-glow) !important;
        }}

        .search-kbd-btn {{
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            background: transparent;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            font-size: 0.72rem;
            display: flex;
            align-items: center;
            padding: 0;
            z-index: 2;
        }}
        .kbd-label {{
            background: var(--bg-surface, rgba(255, 255, 255, 0.08));
            border: 1px solid var(--border-color, rgba(255, 255, 255, 0.12));
            border-radius: 4px;
            padding: 2px 5px;
            font-size: 0.68rem;
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-muted);
            font-weight: 600;
            line-height: 1;
            pointer-events: none;
        }}
    </style>
</head>
<body class="dark">

    <aside class="portal-sidebar" id="sidebar"></aside>

    <!-- Main View Column -->
    <div class="main-column" id="mainView">
        <header class="portal-topbar" id="portalTopBar" data-testid="topbar"></header>

        <!-- Main Content Viewer -->
        <main class="content-area" id="mainContent">
            <!-- Dynamically rendered (Dashboard or Chapter View) -->
        </main>
    </div>

    <!-- Mobile Floating Bottom Navigation Bar -->
    <nav class="mobile-bottom-bar" id="mobileFloatingBottomBar">
        <button class="mobile-bottom-tab" onclick="toggleMobileSidebar()">
            {ICONS["menu"]}
            <span>Topics</span>
        </button>
        <button class="mobile-bottom-tab active" data-tab="master" onclick="switchTab('master')">
            {ICONS["master_answer"]}
            <span>15-Mark</span>
        </button>
        <button class="mobile-bottom-tab" data-tab="diagrams" onclick="switchTab('diagrams')">
            {ICONS["diagrams"]}
            <span>Diagrams</span>
        </button>
        <button class="mobile-bottom-tab" data-tab="viva" onclick="switchTab('viva')">
            {ICONS["viva"]}
            <span>Viva</span>
        </button>
        <button class="mobile-bottom-tab" onclick="togglePlayPauseAudio()">
            {ICONS["headphones"]}
            <span>Audio</span>
        </button>
    </nav>

    <!-- Floating Island Audio Dock -->
    <div id="masterAudioDock" class="audio-dock hidden">
        <div class="audio-dock-inner">
            <div class="audio-dock-meta">
                <div class="audio-dock-track-icon">{ICONS["headphones"]}</div>
                <div class="audio-dock-text">
                    <div class="audio-dock-track-title" id="audioDockTrackTitle">Section Audio</div>
                    <div class="audio-dock-chapter-title" id="audioDockChapterTitle">General Medicine Monograph</div>
                </div>
            </div>

            <div class="audio-dock-controls-wrap">
                <div class="audio-dock-buttons">
                    <button class="audio-control-btn" onclick="prevAudioTrack()" title="Previous Section">{ICONS["prev_track"]}</button>
                    <button class="audio-control-btn audio-btn-playpause" onclick="togglePlayPauseAudio()" id="audioDockPlayPauseBtn" title="Play / Pause">{ICONS["play"]}</button>
                    <button class="audio-control-btn" onclick="nextAudioTrack()" title="Next Section">{ICONS["next_track"]}</button>
                </div>
                <div class="audio-dock-progress-wrap">
                    <span class="audio-time-label" id="audioCurrentTime">0:00</span>
                    <input type="range" class="audio-scrubber" id="audioProgressScrubber" min="0" max="100" value="0" oninput="onAudioScrub(this.value)" aria-label="Audio playback progress scrubber">
                    <span class="audio-time-label" id="audioDuration">0:00</span>
                </div>
            </div>

            <div class="audio-dock-options">
                <div class="audio-voice-wrap" title="Narration Voice Engine">
                    <span class="speed-label">Voice:</span>
                    <select id="audioVoiceSelect" class="audio-voice-select" onchange="onVoiceSelected(this.value)" aria-label="Select Narration Voice">
                        <option value="">Auto (Natural Studio)</option>
                    </select>
                </div>
                <div class="audio-speed-selector">
                    <span class="speed-label">Speed:</span>
                    <button class="speed-pill active" onclick="setAudioPlaybackRate(1.0)" data-speed="1.0">1x</button>
                    <button class="speed-pill" onclick="setAudioPlaybackRate(1.25)" data-speed="1.25">1.25x</button>
                    <button class="speed-pill" onclick="setAudioPlaybackRate(1.5)" data-speed="1.5">1.5x</button>
                    <button class="speed-pill" onclick="setAudioPlaybackRate(2.0)" data-speed="2.0">2x</button>
                </div>
                <button class="audio-dock-close" onclick="closeAudioDock()" title="Stop and Close Player">{ICONS["close"]}</button>
            </div>
        </div>
    </div>

    <!-- Master PDF Modal -->
    <div class="modal-overlay" id="pdfModal" onclick="closePdfModal(event)">
        <div class="modal-box" style="height: 85vh;" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 style="font-size: 1.1rem; font-weight: 700;">General Medicine Master Compendium (PDF)</h3>
                <div style="display: flex; gap: 8px;">
                    <a href="General_Medicine_Master_Notes.pdf" download class="nav-btn nav-btn-primary" style="padding: 4px 10px; font-size: 0.78rem;">Download</a>
                    <button class="audio-dock-close" onclick="closePdfModal()">{ICONS["close"]}</button>
                </div>
            </div>
            <div class="modal-body" style="padding: 0;">
                <iframe src="General_Medicine_Master_Notes.pdf" style="width: 100%; height: 100%; border: none;"></iframe>
            </div>
        </div>
    </div>

    <!-- Spotter / Diagram Zoom Modal -->
    <div class="modal-overlay" id="modal" onclick="closeDiagramModal(event)">
        <div class="modal-box" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h3 id="modalDiagramTitle" style="font-size: 1.1rem; font-weight: 700;">Clinical Schematic</h3>
                <button class="audio-dock-close" onclick="closeDiagramModal()">{ICONS["close"]}</button>
            </div>
            <div class="modal-body" id="modalDiagramBody" style="display:flex; justify-content:center; align-items:center; background:#0f172a;">
                <!-- Injected SVG / Image -->
            </div>
        </div>
    </div>

    <script>
        // Platform detection for keyboard shortcut hints (Ctrl K vs ⌘K)
        (function() {{
            try {{
                const isMac = typeof navigator !== 'undefined' && /Mac|iPod|iPhone|iPad/.test(navigator.platform);
                const kbdString = isMac ? '⌘K' : 'Ctrl K';
                window.addEventListener('DOMContentLoaded', () => {{
                    document.querySelectorAll('.kbd-label').forEach(el => el.textContent = kbdString);
                }});
            }} catch(e) {{}}
        }})();

        const CHAPTERS = {chapters_json};
        const COMPARISONS = {comparisons_json};
        const RUBRIC = {rubric_json};

        let currentChapterIdx = -1;
        let currentDashFilter = 'all';
        let activeTab = 'master';
        let currentCategory = 'All';
        let completedTopics = JSON.parse(localStorage.getItem('bds.medicine.progress') || localStorage.getItem('medicine_completed_topics') || '{{}}');
        let currentFlashcardIdx = 0;
        let isFlashcardFlipped = false;

        // --- Audio & Neural Speech Synthesis Engine ---
        let availableVoices = [];
        let selectedVoice = null;
        let isAudioPlaying = false;
        let audioPlaybackSpeed = 1.0;
        let currentSpeechUtterance = null;
        let speechKeepaliveTimer = null;
        let speechTickerTimer = null;
        let chapterAudioQueue = [];
        let chapterQueueIdx = 0;

        function initVoiceList() {{
            if (!('speechSynthesis' in window)) return;
            const updateVoices = () => {{
                availableVoices = window.speechSynthesis.getVoices().filter(v => v.lang && v.lang.startsWith('en'));
                const select = document.getElementById('audioVoiceSelect');
                if (!select) return;

                const currentVal = select.value || localStorage.getItem('medicine_selected_voice') || '';
                select.innerHTML = '<option value="">Auto (Natural Studio)</option>';

                const sorted = [...availableVoices].sort((a, b) => {{
                    const aNat = a.name.includes('Natural') || a.name.includes('Online') || a.name.includes('Enhanced');
                    const bNat = b.name.includes('Natural') || b.name.includes('Online') || b.name.includes('Enhanced');
                    if (aNat && !bNat) return -1;
                    if (!aNat && bNat) return 1;
                    return a.name.localeCompare(b.name);
                }});

                sorted.forEach(v => {{
                    const opt = document.createElement('option');
                    opt.value = v.name;
                    opt.textContent = `${{v.name.replace(/Microsoft |Google /g, '')}} (${{v.lang}})`;
                    if (v.name === currentVal) opt.selected = true;
                    select.appendChild(opt);
                }});

                if (currentVal) {{
                    selectedVoice = availableVoices.find(v => v.name === currentVal) || null;
                }}
            }};

            updateVoices();
            if (window.speechSynthesis.onvoiceschanged !== undefined) {{
                window.speechSynthesis.onvoiceschanged = updateVoices;
            }}
        }}

        function onVoiceSelected(voiceName) {{
            if (!voiceName) {{
                selectedVoice = null;
                localStorage.removeItem('medicine_selected_voice');
            }} else {{
                selectedVoice = availableVoices.find(v => v.name === voiceName) || null;
                localStorage.setItem('medicine_selected_voice', voiceName);
            }}
            if (isAudioPlaying) {{
                speakCurrentChapterSection();
            }}
        }}

        function cleanMedicalTextForSpeech(text) {{
            if (!text) return '';
            let s = text.replace(/<[^>]+>/g, ' ');
            s = s.replace(/\|/g, ' ');
            s = s.replace(/\*\*/g, '');
            s = s.replace(/```[\s\S]*?```/g, ' ');
            s = s.replace(/`([^`]+)`/g, '$1');

            // Expand standard clinical abbreviations
            const expansions = [
                [/\\bHBV\\b/g, 'Hepatitis B Virus'],
                [/\\bHCV\\b/g, 'Hepatitis C Virus'],
                [/\\bHAV\\b/g, 'Hepatitis A Virus'],
                [/\\bHDV\\b/g, 'Hepatitis D Virus'],
                [/\\bHEV\\b/g, 'Hepatitis E Virus'],
                [/\\bHBsAg\\b/g, 'Hepatitis B Surface Antigen'],
                [/\\bHBeAg\\b/g, 'Hepatitis B E Antigen'],
                [/\\banti-HBs\\b/g, 'Antibody to Hepatitis B Surface Antigen'],
                [/\\banti-HBc\\b/g, 'Antibody to Hepatitis B Core Antigen'],
                [/\\bAML\\b/g, 'Acute Myeloid Leukemia'],
                [/\\bALL\\b/g, 'Acute Lymphoblastic Leukemia'],
                [/\\bCML\\b/g, 'Chronic Myeloid Leukemia'],
                [/\\bCLL\\b/g, 'Chronic Lymphocytic Leukemia'],
                [/\\bSTEMI\\b/g, 'S T Elevation Myocardial Infarction'],
                [/\\bNSTEMI\\b/g, 'Non S T Elevation Myocardial Infarction'],
                [/\\bDKA\\b/g, 'Diabetic Ketoacidosis'],
                [/\\bCKD\\b/g, 'Chronic Kidney Disease'],
                [/\\bESRD\\b/g, 'End Stage Renal Disease'],
                [/\\bVSD\\b/g, 'Ventricular Septal Defect'],
                [/\\bASD\\b/g, 'Atrial Septal Defect'],
                [/\\bPDA\\b/g, 'Patent Ductus Arteriosus'],
                [/\\bTOF\\b/g, 'Tetralogy of Fallot'],
                [/\\bBP\\b/g, 'Blood Pressure'],
                [/\\bHR\\b/g, 'Heart Rate'],
                [/\\bCVP\\b/g, 'Central Venous Pressure'],
                [/\\bSVR\\b/g, 'Systemic Vascular Resistance'],
                [/\\bCO\\b/g, 'Cardiac Output'],
                [/\\bIV\\b/g, 'intravenous'],
                [/\\bIM\\b/g, 'intramuscular'],
                [/\\bPO\\b/g, 'orally'],
                [/\\bBD\\b/g, 'twice daily'],
                [/\\bTDS\\b/g, 'three times daily'],
                [/\\bOD\\b/g, 'once daily'],
                [/\\bmg\\/kg\\b/g, 'milligrams per kilogram'],
                [/\\bmL\\/kg\\b/g, 'milliliters per kilogram']
            ];

            expansions.forEach(([rx, replacement]) => {{
                s = s.replace(rx, replacement);
            }});
            return s.trim();
        }}

        function togglePlayPauseAudio() {{
            const dock = document.getElementById('masterAudioDock');
            if (dock) dock.classList.remove('hidden');

            if (!('speechSynthesis' in window)) {{
                if (window.CoreEngine && CoreEngine.showToast) {{
                    CoreEngine.showToast('Speech synthesis is not supported in this browser.', 'error');
                }} else {{
                    console.warn('Speech synthesis is not supported in this browser.');
                }}
                return;
            }}

            if (currentChapterIdx < 0) {{
                selectChapter(0);
                setTimeout(speakCurrentChapterSection, 250);
                return;
            }}

            if (window.speechSynthesis.paused) {{
                window.speechSynthesis.resume();
                isAudioPlaying = true;
                updateAudioUI();
            }} else if (window.speechSynthesis.speaking) {{
                window.speechSynthesis.pause();
                isAudioPlaying = false;
                updateAudioUI();
            }} else {{
                speakCurrentChapterSection();
            }}
        }}

        function buildChapterAudioQueue(ch) {{
            const queue = [];
            if (ch.clinical_pearl) {{
                queue.push({{
                    title: 'Clinical Pearl',
                    text: `${{ch.title}}. Category: ${{ch.category}}. Clinical Pearl: ${{ch.clinical_pearl}}.`
                }});
            }}
            if (Array.isArray(ch.sections)) {{
                ch.sections.forEach(sec => {{
                    queue.push({{
                        title: sec.title,
                        text: `${{sec.title}}. ${{sec.content}}`
                    }});
                }});
            }}
            return queue;
        }}

        function speakCurrentChapterSection() {{
            if (!('speechSynthesis' in window)) return;
            window.speechSynthesis.cancel();
            clearInterval(speechTickerTimer);
            clearInterval(speechKeepaliveTimer);

            if (currentChapterIdx < 0) {{
                selectChapter(0);
                setTimeout(speakCurrentChapterSection, 250);
                return;
            }}

            const ch = CHAPTERS[currentChapterIdx];
            if (!ch) return;

            chapterAudioQueue = buildChapterAudioQueue(ch);
            chapterQueueIdx = 0;
            playQueueItem(ch);
        }}

        function playQueueItem(ch) {{
            if (!('speechSynthesis' in window)) return;
            window.speechSynthesis.cancel();
            clearInterval(speechTickerTimer);
            clearInterval(speechKeepaliveTimer);

            if (chapterQueueIdx >= chapterAudioQueue.length) {{
                if (currentChapterIdx + 1 < CHAPTERS.length) {{
                    currentChapterIdx++;
                    renderChapterView();
                    speakCurrentChapterSection();
                }} else {{
                    isAudioPlaying = false;
                    updateAudioUI();
                }}
                return;
            }}

            const item = chapterAudioQueue[chapterQueueIdx];
            const titleEl = document.getElementById('audioDockTrackTitle');
            const chTitleEl = document.getElementById('audioDockChapterTitle');
            if (titleEl) titleEl.innerText = `${{item.title}} (${{chapterQueueIdx + 1}}/${{chapterAudioQueue.length}})`;
            if (chTitleEl) chTitleEl.innerText = ch.title;

            const cleanText = cleanMedicalTextForSpeech(item.text);
            const utterance = new SpeechSynthesisUtterance(cleanText);
            utterance.rate = audioPlaybackSpeed || 1.0;

            if (selectedVoice) {{
                utterance.voice = selectedVoice;
            }} else if (availableVoices.length > 0) {{
                const best = availableVoices.find(v => v.name.includes('Natural') || v.name.includes('Online') || v.name.includes('Enhanced')) || availableVoices[0];
                if (best) utterance.voice = best;
            }}

            const words = cleanText.split(/\\s+/).length;
            const estDurationSec = Math.max(5, (words / (150 * (audioPlaybackSpeed || 1.0))) * 60);
            let elapsedSec = 0;

            const durEl = document.getElementById('audioDuration');
            const curTimeEl = document.getElementById('audioCurrentTime');
            const scrubber = document.getElementById('audioProgressScrubber');
            if (durEl) durEl.innerText = formatTime(estDurationSec);

            speechTickerTimer = setInterval(() => {{
                if (isAudioPlaying) {{
                    elapsedSec += 0.5;
                    if (curTimeEl) curTimeEl.innerText = formatTime(elapsedSec);
                    if (scrubber && estDurationSec > 0) {{
                        scrubber.value = Math.min(100, (elapsedSec / estDurationSec) * 100);
                    }}
                }}
            }}, 500);

            // Heartbeat to prevent Chromium 15s freeze
            speechKeepaliveTimer = setInterval(() => {{
                if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) {{
                    window.speechSynthesis.pause();
                    window.speechSynthesis.resume();
                }}
            }}, 12000);

            utterance.onend = () => {{
                clearInterval(speechTickerTimer);
                clearInterval(speechKeepaliveTimer);
                chapterQueueIdx++;
                playQueueItem(ch);
            }};

            utterance.onerror = () => {{
                clearInterval(speechTickerTimer);
                clearInterval(speechKeepaliveTimer);
                isAudioPlaying = false;
                updateAudioUI();
            }};

            window.speechSynthesis.speak(utterance);
            currentSpeechUtterance = utterance;
            isAudioPlaying = true;
            updateAudioUI();
        }}

        function setAudioPlaybackRate(rate) {{
            audioPlaybackSpeed = rate;
            document.querySelectorAll('.speed-pill').forEach(pill => {{
                const pSpeed = parseFloat(pill.getAttribute('data-speed'));
                if (Math.abs(pSpeed - rate) < 0.01) {{
                    pill.classList.add('active');
                }} else {{
                    pill.classList.remove('active');
                }}
            }});
            if (isAudioPlaying && CHAPTERS[currentChapterIdx]) {{
                playQueueItem(CHAPTERS[currentChapterIdx]);
            }}
        }}

        function onAudioScrub(val) {{
            // Scrubbing visual only
        }}

        function prevAudioTrack() {{
            if (chapterQueueIdx > 0) {{
                chapterQueueIdx--;
                const ch = CHAPTERS[currentChapterIdx];
                if (ch) playQueueItem(ch);
            }} else if (currentChapterIdx > 0) {{
                currentChapterIdx--;
                renderChapterView();
                if (isAudioPlaying) speakCurrentChapterSection();
            }}
        }}

        function nextAudioTrack() {{
            if (chapterQueueIdx + 1 < chapterAudioQueue.length) {{
                chapterQueueIdx++;
                const ch = CHAPTERS[currentChapterIdx];
                if (ch) playQueueItem(ch);
            }} else if (currentChapterIdx + 1 < CHAPTERS.length) {{
                currentChapterIdx++;
                renderChapterView();
                if (isAudioPlaying) speakCurrentChapterSection();
            }}
        }}

        function closeAudioDock() {{
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
            }}
            clearInterval(speechTickerTimer);
            clearInterval(speechKeepaliveTimer);
            isAudioPlaying = false;
            const dock = document.getElementById('masterAudioDock');
            if (dock) dock.classList.add('hidden');
            updateAudioUI();
        }}

        function updateAudioUI() {{
            const btn = document.getElementById('audioDockPlayPauseBtn');
            const dock = document.getElementById('masterAudioDock');
            if (btn) {{
                btn.innerHTML = isAudioPlaying ? '{ICONS["pause"]}' : '{ICONS["play"]}';
            }}
            if (dock) {{
                if (isAudioPlaying) dock.classList.add('is-playing');
                else dock.classList.remove('is-playing');
            }}
            if (window.CoreEngine && CoreEngine.setAudioPlayingState) {{
                CoreEngine.setAudioPlayingState(isAudioPlaying);
            }}
        }}

        function speakVivaPearl(btn, text) {{
            if (!('speechSynthesis' in window)) return;
            window.speechSynthesis.cancel();
            const cleanText = cleanMedicalTextForSpeech(text);
            const utterance = new SpeechSynthesisUtterance(cleanText);
            utterance.rate = audioPlaybackSpeed || 1.0;
            if (selectedVoice) utterance.voice = selectedVoice;

            btn.style.color = 'var(--accent-primary, #38bdf8)';
            utterance.onend = () => {{ btn.style.color = ''; }};
            utterance.onerror = () => {{ btn.style.color = ''; }};
            window.speechSynthesis.speak(utterance);
        }}

        function formatTime(sec) {{
            const m = Math.floor(sec / 60);
            const s = Math.floor(sec % 60);
            return `${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
        }}

        // --- View & Navigation Logic ---
        function renderSidebar(filterText = '') {{
            if (window.CoreEngine && CoreEngine.onSidebarSearch) {{
                CoreEngine.onSidebarSearch(filterText);
            }}
        }}

        function getSlugForChapter(idx) {{
            if (idx < 0 || idx >= CHAPTERS.length) return '';
            const ch = CHAPTERS[idx];
            const cleanTitle = (ch.title || '').replace(/^(chapter\s*\d+[:.]*|\d+[\.:\s]+)/i, '').trim();
            return cleanTitle.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
        }}

        function handleHashRoute() {{
            const hash = window.location.hash || '';
            if (!hash || hash === '#' || hash === '#/') {{
                if (currentChapterIdx !== -1) showDashboard(false);
                return;
            }}
            if (hash.startsWith('#/topic/')) {{
                const targetSlug = hash.replace('#/topic/', '').toLowerCase();
                const foundIdx = CHAPTERS.findIndex((ch, i) => {{
                    const s = getSlugForChapter(i);
                    return s === targetSlug || (ch.id && ch.id.toLowerCase() === targetSlug) || ('chap' + (i + 1) === targetSlug) || (String(i + 1) === targetSlug);
                }});
                if (foundIdx !== -1) {{
                    if (currentChapterIdx !== foundIdx) {{
                        selectChapter(foundIdx, false);
                    }}
                }} else {{
                    console.warn('Unknown topic slug:', targetSlug);
                    showDashboard(false);
                }}
            }} else if (hash === '#/simulator') {{
                launchExamSimFromDashboard();
            }} else if (hash === '#/spotters') {{
                openDiagramSpotterFromDashboard();
            }}
        }}

        function selectChapter(idx, updateHash = true) {{
            currentChapterIdx = idx;
            if (updateHash) {{
                const slug = getSlugForChapter(idx);
                if (slug && window.location.hash !== `#/topic/${{slug}}`) {{
                    history.pushState(null, '', `#/topic/${{slug}}`);
                }}
            }}
            if (window.CoreEngine) {{
                CoreEngine.currentTopicIndex = idx;
                CoreEngine.updateViewHeading(CHAPTERS[idx].title, CHAPTERS[idx].category, idx + 1);
                const activeRow = document.querySelector(`.topic-row[data-topic-id="${{CHAPTERS[idx].id}}"]`);
                if (activeRow) {{
                    document.querySelectorAll('.topic-row').forEach(r => r.classList.remove('active'));
                    activeRow.classList.add('active');
                }}
            }}
            renderChapterView();
            toggleMobileSidebar(false);
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function showDashboard(updateHash = true) {{
            currentChapterIdx = -1;
            if (updateHash && window.location.hash && window.location.hash !== '#/' && window.location.hash !== '#') {{
                history.pushState(null, '', '#/');
            }}
            if (window.CoreEngine) {{
                CoreEngine.currentTopicIndex = -1;
                CoreEngine.updateViewHeading('Dashboard');
                CoreEngine.toggleSidebar(false);
            }}
            renderDashboard();
            toggleMobileSidebar(false);
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function setDashFilter(filter) {{
            currentDashFilter = filter;
            renderDashboard();
        }}

        function renderDashboard() {{
            currentChapterIdx = -1;
            const main = document.getElementById('mainContent');
            const total = CHAPTERS.length;
            const completed = Object.keys(completedTopics).length;
            const remaining = total - completed;
            const pct = Math.round((completed / total) * 100);

            let notesCount = 0;
            CHAPTERS.forEach(ch => {{
                if ((localStorage.getItem('medicine_notes_' + ch.id) || '').trim().length > 0) notesCount++;
            }});

            const dashBtn = document.getElementById('sidebarDashBtn');
            if (dashBtn) dashBtn.classList.add('nav-btn-primary');
            document.querySelectorAll('.topic-item').forEach(el => el.classList.remove('active'));

            let html = `
                <div class="dash-hero-card">
                    <div style="flex: 1;">
                        <span class="dash-hero-badge">BDS 3RD YEAR &amp; MBBS GENERAL MEDICINE PORTAL</span>
                        <h1 class="dash-hero-title">General Medicine Master Exam Hub</h1>
                        <p class="dash-hero-sub">15-Mark University Essay Blueprints • Emergency Protocols • Bedside Clinical Pearls</p>
                        <div class="dash-hero-meta">
                            <span class="dash-hero-stat"><strong>${{total}}</strong> University Topics</span>
                            <span class="dash-hero-stat"><strong style="color: #4ade80;">${{completed}}</strong> Completed</span>
                            <span class="dash-hero-stat"><strong style="color: #c7d2fe;">${{pct}}%</strong> Syllabus Ready</span>
                        </div>
                    </div>
                    <div class="dash-hero-image-box">
                        <svg viewBox="0 0 260 140" width="260" height="140" xmlns="http://www.w3.org/2000/svg">
                            <rect width="260" height="140" fill="#1e1b4b" rx="8"/>
                            <path d="M20 70H60L75 40L95 100L115 55L130 85L145 70H240" stroke="#818cf8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                            <circle cx="95" cy="100" r="4" fill="#f43f5e"/>
                            <circle cx="75" cy="40" r="4" fill="#38bdf8"/>
                            <text x="130" y="125" fill="#c7d2fe" font-size="11" font-family="'Plus Jakarta Sans',sans-serif" font-weight="700" text-anchor="middle">HEMODYNAMICS &amp; CLINICAL ECG</text>
                        </svg>
                    </div>
                </div>

                <div class="dash-cheat-sheet-card">
                    <div style="display: flex; align-items: center; gap: 16px; flex: 1;">
                        <div class="cheat-sheet-badge-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>
                            </svg>
                        </div>
                        <div>
                            <div style="font-size: 0.72rem; font-weight: 700; color: var(--accent-primary); text-transform: uppercase; letter-spacing: 0.08em;">Emergency &amp; High-Yield Protocol</div>
                            <div style="font-size: 1.15rem; font-weight: 800; color: var(--text-primary);">Chapter 21: Rapid Revision Master Cheat Sheet</div>
                            <div style="font-size: 0.84rem; color: var(--text-secondary); margin-top: 2px;">
                                High-yield clinical matrices, emergency resuscitation dosages, chairside bleeding cutoffs &amp; antibiotic prophylaxis protocols.
                            </div>
                        </div>
                    </div>
                    <button class="nav-btn nav-btn-primary" onclick="selectChapter(20)" style="padding: 10px 20px; font-size: 0.88rem;">
                        Launch Master Cheat Sheet →
                    </button>
                </div>

                <div class="stats-grid-dashboard">
                    <div class="stat-card-box">
                        <div class="stat-card-label">Total University Topics</div>
                        <div class="stat-card-val">${{total}}</div>
                    </div>
                    <div class="stat-card-box">
                        <div class="stat-card-label">Topics Completed</div>
                        <div class="stat-card-val" style="color: #10b981;">${{completed}}</div>
                    </div>
                    <div class="stat-card-box">
                        <div class="stat-card-label">Topics Remaining</div>
                        <div class="stat-card-val" style="color: #f59e0b;">${{remaining}}</div>
                    </div>
                    <div class="stat-card-box">
                        <div class="stat-card-label">Topics with Notes</div>
                        <div class="stat-card-val" style="color: var(--accent-primary);">${{notesCount}}</div>
                    </div>
                </div>

                <div class="progress-banner-dash">
                    <div style="display: flex; justify-content: space-between; align-items: center; font-weight: 700; font-size: 0.92rem;">
                        <span>University Syllabus Completion</span>
                        <span style="color: var(--accent-primary);">${{pct}}%</span>
                    </div>
                    <div class="progress-bar-bg-dash" data-testid="progress">
                        <div class="progress-bar-fill-dash" style="width: ${{pct}}%;"></div>
                    </div>
                </div>

                <div style="margin-bottom: 14px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
                    <h2 style="font-size: 1.1rem; font-weight: 800; color: var(--text-primary);">Study Plan Topics</h2>
                    <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
                        <div class="category-scroll">
                            <button class="filter-chip ${{currentDashFilter === 'all' ? 'active' : ''}}" onclick="setDashFilter('all')">All Topics (${{total}})</button>
                            <button class="filter-chip ${{currentDashFilter === 'pending' ? 'active' : ''}}" onclick="setDashFilter('pending')">Pending (${{remaining}})</button>
                            <button class="filter-chip ${{currentDashFilter === 'completed' ? 'active' : ''}}" onclick="setDashFilter('completed')">Completed (${{completed}})</button>
                            <button class="filter-chip ${{currentDashFilter === 'notes' ? 'active' : ''}}" onclick="setDashFilter('notes')">Has Notes (${{notesCount}})</button>
                        </div>
                        <div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;" data-testid="modules">
                            <button class="filter-chip" data-testid="voice-walk" onclick="togglePlayPauseAudio()" style="cursor: pointer;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block; vertical-align:middle; margin-right:4px;" aria-hidden="true"><path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/></svg>Voice Walk</button>
                            <button class="filter-chip" data-testid="exam-simulator" onclick="launchExamSimFromDashboard()" style="cursor: pointer;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block; vertical-align:middle; margin-right:4px;" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>Exam Simulator</button>
                            <button class="filter-chip" data-testid="spotters" onclick="openDiagramSpotterFromDashboard()" style="cursor: pointer;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block; vertical-align:middle; margin-right:4px;" aria-hidden="true"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/></svg>Spotters</button>
                            <button class="filter-chip" data-testid="flashcards" onclick="openFlashcardsFromDashboard()" style="cursor: pointer;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block; vertical-align:middle; margin-right:4px;" aria-hidden="true"><rect width="18" height="14" x="3" y="5" rx="2"/><line x1="7" y1="15" x2="7.01" y2="15"/></svg>Flashcards</button>
                            <button class="filter-chip" data-testid="schematics" onclick="openDiagramSpotterFromDashboard()" style="cursor: pointer;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block; vertical-align:middle; margin-right:4px;" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>Schematics</button>
                            <button class="filter-chip" data-testid="cheat-sheet" onclick="selectChapter(20)" style="cursor: pointer;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block; vertical-align:middle; margin-right:4px;" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>Cheat Sheet</button>
                        </div>
                    </div>
                </div>

                <div class="dashboard-topic-cards-grid">
            `;

            CHAPTERS.forEach((ch, idx) => {{
                const isDone = !!completedTopics[ch.id];
                const hasNote = ((localStorage.getItem('medicine_notes_' + ch.id) || '').trim().length > 0);

                if (currentDashFilter === 'completed' && !isDone) return;
                if (currentDashFilter === 'pending' && isDone) return;
                if (currentDashFilter === 'notes' && !hasNote) return;

                html += `
                    <div class="dash-topic-card ${{isDone ? 'completed' : ''}}">
                        <div>
                            <div class="dash-card-header-row">
                                <span class="dash-card-chapter-tag">Chapter ${{idx + 1}}</span>
                                ${{hasNote ? '<span style="font-size: 0.72rem; background: rgba(99, 102, 241, 0.12); color: #818cf8; padding: 2px 7px; border-radius: 4px; font-weight: 600;">Note Saved</span>' : ''}}
                            </div>
                            <div class="dash-card-title-text">${{ch.title}}</div>
                            <div class="dash-card-source-text">${{ch.category}} • ${{ch.reading_time}}</div>
                        </div>
                        <div class="dash-card-footer-row">
                            <button class="toggle-complete-btn ${{isDone ? 'is-completed' : ''}}" onclick="toggleTopicComplete('${{ch.id}}')">
                                ${{isDone ? 'Completed' : 'Mark Done'}}
                            </button>
                            <button class="nav-btn nav-btn-primary" onclick="selectChapter(${{idx}})" style="padding: 6px 14px; font-size: 0.8rem;">
                                Study →
                            </button>
                        </div>
                    </div>
                `;
            }});

            html += `</div>`;
            main.innerHTML = html;
        }}

        function renderChapterView() {{
            if (currentChapterIdx < 0 || currentChapterIdx >= CHAPTERS.length) {{
                renderDashboard();
                return;
            }}

            const ch = CHAPTERS[currentChapterIdx];
            const main = document.getElementById('mainContent');

            main.innerHTML = `
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                    <button class="nav-btn" onclick="showDashboard()">
                        ← Back to Dashboard
                    </button>
                    <div style="font-size: 0.82rem; color: var(--text-muted); font-weight: 600;">
                        Chapter ${{currentChapterIdx + 1}} of ${{CHAPTERS.length}}
                    </div>
                </div>

                <div class="chapter-header">
                    <span class="chapter-top-badge">${{ch.category}} • ${{ch.badge}}</span>
                    <h2 class="chapter-title-display">${{ch.title}}</h2>
                </div>

                <div class="tab-bar-container">
                    <div class="tab-bar" role="tablist" aria-label="Curriculum Topic Sections">
                        <button class="tab-btn ${{activeTab === 'master' ? 'active' : ''}}" data-tab="master" role="tab" aria-selected="${{activeTab === 'master' ? 'true' : 'false'}}" tabindex="${{activeTab === 'master' ? '0' : '-1'}}" onclick="switchTab('master')">
                            {ICONS["master_answer"]} 15-Mark Master Answer
                        </button>
                        <button class="tab-btn ${{activeTab === 'layman' ? 'active' : ''}}" data-tab="layman" role="tab" aria-selected="${{activeTab === 'layman' ? 'true' : 'false'}}" tabindex="${{activeTab === 'layman' ? '0' : '-1'}}" onclick="switchTab('layman')">
                            {ICONS["layman"]} Layman's Intuition
                        </button>
                        <button class="tab-btn ${{activeTab === 'types' ? 'active' : ''}}" data-tab="types" role="tab" aria-selected="${{activeTab === 'types' ? 'true' : 'false'}}" tabindex="${{activeTab === 'types' ? '0' : '-1'}}" onclick="switchTab('types')">
                            {ICONS["dashboard"]} Types &amp; Classifications
                        </button>
                        <button class="tab-btn ${{activeTab === 'diagrams' ? 'active' : ''}}" data-tab="diagrams" role="tab" aria-selected="${{activeTab === 'diagrams' ? 'true' : 'false'}}" tabindex="${{activeTab === 'diagrams' ? '0' : '-1'}}" data-testid="schematics" onclick="switchTab('diagrams')">
                            {ICONS["diagrams"]} Diagrams &amp; Spotters
                        </button>
                        <button class="tab-btn ${{activeTab === 'viva' ? 'active' : ''}}" data-tab="viva" role="tab" aria-selected="${{activeTab === 'viva' ? 'true' : 'false'}}" tabindex="${{activeTab === 'viva' ? '0' : '-1'}}" onclick="switchTab('viva')">
                            {ICONS["viva"]} Examiner Viva Pearls
                        </button>
                        <button class="tab-btn ${{activeTab === 'quiz' ? 'active' : ''}}" data-tab="quiz" role="tab" aria-selected="${{activeTab === 'quiz' ? 'true' : 'false'}}" tabindex="${{activeTab === 'quiz' ? '0' : '-1'}}" data-testid="flashcards" onclick="switchTab('quiz')">
                            {ICONS["quiz"]} Active Recall Flashcards
                        </button>
                        <button class="tab-btn ${{activeTab === 'exam' ? 'active' : ''}}" data-tab="exam" role="tab" aria-selected="${{activeTab === 'exam' ? 'true' : 'false'}}" tabindex="${{activeTab === 'exam' ? '0' : '-1'}}" data-testid="exam-simulator" onclick="switchTab('exam')">
                            {ICONS["cheat_sheet"]} Exam Rubric Simulator
                        </button>
                        <button class="tab-btn ${{activeTab === 'notes' ? 'active' : ''}}" data-tab="notes" role="tab" aria-selected="${{activeTab === 'notes' ? 'true' : 'false'}}" tabindex="${{activeTab === 'notes' ? '0' : '-1'}}" onclick="switchTab('notes')">
                            {ICONS["notes"]} My Clinical Notes
                        </button>
                    </div>
                </div>

                <div id="tabContentContainer">
                    ${{getTabHTML(ch, activeTab)}}
                </div>
            `;
        }}

        function switchTab(tab) {{
            activeTab = tab;
            document.querySelectorAll('.tab-btn').forEach(btn => {{
                const bTab = btn.getAttribute('data-tab');
                const isMatch = bTab === tab;
                btn.classList.toggle('active', isMatch);
                btn.setAttribute('aria-selected', isMatch ? 'true' : 'false');
                btn.setAttribute('tabindex', isMatch ? '0' : '-1');
                if (isMatch) {{
                    btn.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
                }}
            }});
            document.querySelectorAll('.mobile-bottom-tab').forEach(btn => {{
                const bTab = btn.getAttribute('data-tab');
                btn.classList.toggle('active', bTab === tab);
            }});

            // Sync URL query (?tab=...)
            try {{
                const url = new URL(window.location.href);
                if (url.hash.includes('?')) {{
                    const parts = url.hash.split('?');
                    const params = new URLSearchParams(parts[1]);
                    params.set('tab', tab);
                    url.hash = parts[0] + '?' + params.toString();
                }} else {{
                    url.hash = url.hash + '?tab=' + tab;
                }}
                history.replaceState(null, '', url.toString());
            }} catch(e) {{}}

            const ch = CHAPTERS[currentChapterIdx];
            const container = document.getElementById('tabContentContainer');
            if (container && ch) {{
                container.innerHTML = getTabHTML(ch, tab);
                container.scrollTop = 0;
            }}

            if (tab === 'exam' && ch && window.BdsSimulator) {{
                setTimeout(() => window.BdsSimulator.renderHistoryList('medicine', ch.id), 20);
            }}
        }}

        function getTabHTML(ch, tab) {{
            if (tab === 'master') {{
                return `
                    <div class="master-essay-content">
                        <div class="pearl-card">
                            <strong style="color: var(--accent-primary);">Clinical Pearl:</strong> ${{ch.clinical_pearl}}
                        </div>
                        ${{ch.sections.map(sec => `
                            <div class="essay-section-card">
                                <div class="essay-section-header">
                                    <h3 class="essay-section-title">${{sec.title}}</h3>
                                </div>
                                <div class="essay-body">${{parseMarkdown(sec.content)}}</div>
                            </div>
                        `).join('')}}

                        ${{ch.comparisons && ch.comparisons.length > 0 ? `
                            <div class="essay-section-card">
                                <h3 class="essay-section-title">Differential Diagnosis &amp; Comparative Matrices</h3>
                                ${{ch.comparisons.map(comp => `
                                    <h4 style="margin: 16px 0 8px 0; color: var(--accent-primary); font-size: 1.05rem;">${{comp.title}}</h4>
                                    <table>
                                        <thead><tr>${{comp.headers.map(h => `<th>${{h}}</th>`).join('')}}</tr></thead>
                                        <tbody>
                                            ${{comp.rows.map(r => `<tr>${{r.map(c => `<td>${{c}}</td>`).join('')}}</tr>`).join('')}}
                                        </tbody>
                                    </table>
                                `).join('')}}
                            </div>
                        ` : ''}}
                    </div>
                `;
            }} else if (tab === 'layman') {{
                const layman = ch.analogy || {{ title: 'Clinical Intuition', analogy: ch.clinical_pearl }};
                return `
                    <div class="master-essay-content">
                        <div class="layman-card">
                            <div class="layman-header">
                                <span class="layman-badge">INTUITIVE CLINICAL ANALOGY</span>
                                <h3 class="layman-title">${{layman.title}}</h3>
                            </div>
                            <div class="layman-body">${{layman.analogy}}</div>
                        </div>
                    </div>
                `;
            }} else if (tab === 'types') {{
                const cls = ch.classification;
                return `
                    <div>
                        <h3 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 14px;">${{cls.title}}</h3>
                        <div class="types-grid">
                            ${{cls.types.map(t => `
                                <div class="type-card">
                                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                                        <span class="type-card-badge">${{t.badge || 'Diagnostic Criteria'}}</span>
                                        ${{t.hemodynamics && t.hemodynamics !== 'Pathognomonic Microscopic Sign' ? `<span class="type-card-stat">${{t.hemodynamics}}</span>` : ''}}
                                    </div>
                                    <div class="type-card-title">${{t.name}}</div>
                                    <div class="type-card-summary">${{parseMarkdown(t.summary)}}</div>
                                </div>
                            `).join('')}}
                        </div>
                    </div>
                `;
            }} else if (tab === 'diagrams') {{
                return `
                    <div>
                        <div class="diagram-container">
                            <div class="diagram-title">${{ch.title}}: Vector Clinical Algorithm &amp; Schematic</div>
                            <div class="diagram-viewer-box" onclick="openDiagramModal('${{ch.id}}')">
                                ${{ch.schematic_svg}}
                            </div>
                            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 10px; text-align: right;">Click diagram to expand to full-screen inspection mode</div>
                        </div>
                    </div>
                `;
            }} else if (tab === 'viva') {{
                return `
                    <div class="master-essay-content">
                        <h3 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 16px;">Examiner Viva Voce High-Yield Pearls</h3>
                        ${{ch.viva_questions.map((q, idx) => `
                            <div class="viva-item">
                                <div class="viva-q">
                                    <span>Q${{idx + 1}}: ${{q}}</span>
                                    <button class="viva-speaker-btn" onclick="speakVivaPearl(this, '${{q.replace(/'/g, "\\'")}}')">
                                        {ICONS["volume"]}
                                    </button>
                                </div>
                                <button class="viva-reveal-btn" onclick="toggleVivaAnswer(this)">Tap to Reveal Answer</button>
                                <div class="viva-ans">
                                    <strong>Examiner Expectation:</strong> State definitions clearly, cite pathognomonic clinical signs, and quote exact drug dosages without hesitation.
                                </div>
                            </div>
                        `).join('')}}
                    </div>
                `;
            }} else if (tab === 'quiz') {{
                currentFlashcardIdx = 0;
                isFlashcardFlipped = false;
                const card = ch.flashcards[0] || {{ q: 'No flashcard available.', a: '' }};
                return `
                    <div class="flashcard-wrap">
                        <div class="flashcard" id="activeFlashcard" onclick="flipFlashcard()">
                            <span class="flashcard-tag" id="flashcardTag">QUESTION (CARD 1 OF ${{ch.flashcards.length}})</span>
                            <div class="flashcard-text" id="flashcardText">${{card.q}}</div>
                            <span class="flashcard-instruction">Click anywhere to flip</span>
                        </div>
                        <div class="flashcard-controls">
                            <button class="nav-btn" onclick="prevFlashcard()">← Previous</button>
                            <button class="nav-btn nav-btn-primary" onclick="nextFlashcard()">Next Card →</button>
                        </div>
                    </div>
                `;
            }} else if (tab === 'exam') {{
                return `
                    <div class="master-essay-content">
                        <div class="exam-sim-card">
                            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
                                <div>
                                    <h3 style="font-size: 1.25rem; font-weight: 700; margin: 0 0 4px 0;">25-Minute Timed University Exam Simulator</h3>
                                    <p style="font-size: 0.88rem; color: var(--text-muted); margin: 0;">Evaluate your structured 15-mark essay against the university examiner 10-point scoring matrix.</p>
                                </div>
                                <div id="simSaveStatus" style="font-size: 0.78rem; font-family: 'JetBrains Mono', monospace; color: var(--text-muted);"></div>
                            </div>
                            ${{RUBRIC.map((r, i) => `
                                <div class="rubric-row">
                                    <div class="rubric-info">
                                        <h4>${{r.section}} (${{r.weight}})</h4>
                                        <p>${{r.criteria}}</p>
                                    </div>
                                    <div class="rubric-slider">
                                        <input type="range" id="rubric_range_${{i + 1}}" min="0" max="10" value="8" oninput="updateRubricScore()">
                                    </div>
                                </div>
                            `).join('')}}
                            <div style="margin-top: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; padding-top: 16px; border-top: 1px solid var(--border-color);">
                                <div style="font-size: 1.1rem; font-weight: 700;">Simulated Exam Score: <span id="examScoreTotal" style="color: var(--accent-primary);">12.5 / 15 Marks (Honors)</span></div>
                                <button class="nav-btn nav-btn-primary btn-save-evaluation" id="btnSaveEvaluation" onclick="saveMedicineEvaluation('${{ch.id}}')" style="min-height: 44px; padding: 0 18px; font-weight: 700;">Save Evaluation</button>
                            </div>
                            <div class="sim-history-pane" style="margin-top: 20px; padding: 14px; background: rgba(0,0,0,0.18); border: 1px solid var(--border-color); border-radius: var(--radius-sm);">
                                <details>
                                    <summary style="font-size: 0.82rem; font-weight: 700; color: var(--text-secondary); cursor: pointer;">
                                        Past Evaluation Attempts &amp; Score Logs
                                    </summary>
                                    <div id="simHistoryList" style="margin-top: 10px;"></div>
                                </details>
                            </div>
                        </div>
                    </div>
                `;
            }} else if (tab === 'notes') {{
                const savedNotes = localStorage.getItem('medicine_notes_' + ch.id) || '';
                return `
                    <div class="master-essay-content">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                            <h3 style="font-size: 1.2rem; font-weight: 700;">My Clinical Notes</h3>
                            <span id="notesStatus" style="font-size: 0.78rem; color: var(--accent-primary);">Auto-saved locally</span>
                        </div>
                        <textarea class="notes-textarea" id="notesTextarea" placeholder="Type chairside clinical notes, mnemonics, or revision reminders for this topic..." oninput="saveTopicNotes('${{ch.id}}', this.value)">${{savedNotes}}</textarea>
                    </div>
                `;
            }}
            return '';
        }}

        function parseMarkdown(md) {{
            if (!md) return '';

            // Clean LaTeX and medical notations
            let text = md
                .replace(/\\\\times(?![a-zA-Z])/g, '×')
                .replace(/\\\\pm(?![a-zA-Z])/g, '±')
                .replace(/\\\\ge(?![a-zA-Z])/g, '≥')
                .replace(/\\\\le(?![a-zA-Z])/g, '≤')
                .replace(/\\\\to(?![a-zA-Z])/g, '→')
                .replace(/\\\\rightarrow(?![a-zA-Z])/g, '→')
                .replace(/\\\\leftarrow(?![a-zA-Z])/g, '←')
                .replace(/\\\\uparrow(?![a-zA-Z])/g, '↑')
                .replace(/\\\\downarrow(?![a-zA-Z])/g, '↓')
                .replace(/\\\\Delta(?![a-zA-Z])/g, 'Δ')
                .replace(/\\\\circ(?![a-zA-Z])/g, '°')
                .replace(/\\\\mu(?![a-zA-Z])/g, 'µ')
                .replace(/\\\\alpha(?![a-zA-Z])/g, 'α')
                .replace(/\\\\beta(?![a-zA-Z])/g, 'β')
                .replace(/\\\\gamma(?![a-zA-Z])/g, 'γ')
                .replace(/\\\\text\\{{([^\\}}]+)\\}}/g, ' $1')
                .replace(/\\bHbA1[cC]\\b/g, 'HbA<sub>1c</sub>')
                .replace(/\\bFiO_?2\\b/g, 'FiO<sub>2</sub>')
                .replace(/\\bPaO_?2\\b/g, 'PaO<sub>2</sub>')
                .replace(/\\bPaCO_?2\\b/g, 'PaCO<sub>2</sub>')
                .replace(/\\bSpO_?2\\b/g, 'SpO<sub>2</sub>')
                .replace(/\\bCO_?2\\b/g, 'CO<sub>2</sub>')
                .replace(/\\bO_?2\\b/g, 'O<sub>2</sub>')
                .replace(/\\bH_?2O\\b/g, 'H<sub>2</sub>O')
                .replace(/\\bNa\\^\\+/g, 'Na⁺')
                .replace(/\\bK\\^\\+/g, 'K⁺')
                .replace(/\\bCa\\^2\\+/g, 'Ca²⁺');

            // Format formula blocks ($$...$$)
            text = text.replace(/\$\$([\s\S]*?)\$\$/g, (m, formula) => {{
                return `<div class="formula-card"><div class="formula-header"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"/></svg> CLINICAL FORMULA</div><div class="formula-equation">${{formula.trim()}}</div></div>`;
            }});

            // Preserve code blocks
            const codeBlocks = [];
            text = text.replace(/```([\s\S]*?)```/g, (m, code) => {{
                const id = `__CODE_BLOCK_${{codeBlocks.length}}__`;
                codeBlocks.push(`<pre class="algorithm-block"><code>${{code.trim()}}</code></pre>`);
                return id;
            }});

            const lines = text.split('\\n');
            const result = [];
            let inTable = false;
            let tableLines = [];
            let inUl = false;
            let inOl = false;

            function closeLists() {{
                if (inUl) {{ result.push('</ul>'); inUl = false; }}
                if (inOl) {{ result.push('</ol>'); inOl = false; }}
            }}

            function formatInline(str) {{
                let s = str;
                const count = (s.match(/\*\*/g) || []).length;
                if (count % 2 !== 0) {{
                    const lastIdx = s.lastIndexOf('**');
                    s = s.substring(0, lastIdx) + s.substring(lastIdx + 2);
                }}
                return s
                    .replace(/\*\*(.*?)\*\*/g, '<strong style="color:var(--text-primary); font-weight:700;">$1</strong>')
                    .replace(/(?<!\*)\*([^*]+?)\*(?!\*)/g, '<em>$1</em>')
                    .replace(/`([^`]+)`/g, '<code class="inline-code">$1</code>')
                    .replace(/\$([^$]+)\$/g, '<span class="inline-math">$1</span>');
            }}

            function flushTable() {{
                if (tableLines.length < 2) {{
                    tableLines = [];
                    return;
                }}
                const headers = tableLines[0].split('|').slice(1, -1).map(h => h.trim());
                let startRow = 1;
                if (tableLines.length > 1 && tableLines[1].includes('---')) {{
                    startRow = 2;
                }}

                let html = '<div class="table-responsive"><table class="data-table"><thead><tr>';
                headers.forEach(h => {{
                    html += `<th>${{formatInline(h)}}</th>`;
                }});
                html += '</tr></thead><tbody>';

                for (let i = startRow; i < tableLines.length; i++) {{
                    const line = tableLines[i].trim();
                    if (!line || !line.includes('|')) continue;
                    const cols = line.split('|').slice(1, -1).map(c => c.trim());
                    html += '<tr>';
                    cols.forEach(c => {{
                        html += `<td>${{formatInline(c)}}</td>`;
                    }});
                    html += '</tr>';
                }}
                html += '</tbody></table></div>';
                result.push(html);
                tableLines = [];
            }}

            for (let i = 0; i < lines.length; i++) {{
                const line = lines[i];
                const trimmed = line.trim();

                if (trimmed.startsWith('|') && trimmed.endsWith('|')) {{
                    closeLists();
                    inTable = true;
                    tableLines.push(trimmed);
                    continue;
                }} else if (inTable) {{
                    inTable = false;
                    flushTable();
                }}

                if (!trimmed) {{
                    closeLists();
                    continue;
                }}

                if (trimmed.startsWith('#### ')) {{
                    closeLists();
                    result.push(`<h5 class="essay-subheading" style="font-size:1.02rem; font-weight:700; margin:14px 0 6px 0; color:var(--text-primary);">${{formatInline(trimmed.substring(5))}}</h5>`);
                    continue;
                }}
                if (trimmed.startsWith('### ')) {{
                    closeLists();
                    result.push(`<h4 class="essay-section-title" style="font-size:1.1rem; font-weight:700; margin:18px 0 8px 0; color:var(--accent-primary);">${{formatInline(trimmed.substring(4))}}</h4>`);
                    continue;
                }}
                if (trimmed.startsWith('## ')) {{
                    closeLists();
                    result.push(`<h3 class="essay-major-title" style="font-size:1.22rem; font-weight:800; margin:22px 0 10px 0; color:var(--text-primary);">${{formatInline(trimmed.substring(3))}}</h3>`);
                    continue;
                }}

                if (trimmed.startsWith('> [!TIP]')) {{
                    closeLists();
                    const tipText = formatInline(trimmed.replace('> [!TIP]', '').replace('**Clinical Pearl:**', '').trim());
                    result.push(`<div class="callout-alert alert-tip"><div class="alert-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div><div><strong>Clinical Pearl:</strong> ${{tipText}}</div></div>`);
                    continue;
                }}
                if (trimmed.startsWith('> [!NOTE]')) {{
                    closeLists();
                    const noteText = formatInline(trimmed.replace('> [!NOTE]', '').trim());
                    result.push(`<div class="callout-alert alert-note"><div class="alert-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg></div><div>${{noteText}}</div></div>`);
                    continue;
                }}
                if (trimmed.startsWith('> [!IMPORTANT]')) {{
                    closeLists();
                    const impText = formatInline(trimmed.replace('> [!IMPORTANT]', '').trim());
                    result.push(`<div class="callout-alert alert-important"><div class="alert-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div><div>${{impText}}</div></div>`);
                    continue;
                }}
                if (trimmed.startsWith('> ')) {{
                    closeLists();
                    result.push(`<blockquote class="clinical-quote" style="border-left: 3px solid var(--accent-primary); padding-left: 14px; margin: 12px 0; color: var(--text-secondary); font-style: italic;">${{formatInline(trimmed.substring(2))}}</blockquote>`);
                    continue;
                }}

                const olMatch = trimmed.match(/^(\\d+)\\.\\s+(.*)$/);
                if (olMatch) {{
                    if (inUl) {{ result.push('</ul>'); inUl = false; }}
                    if (!inOl) {{
                        result.push(`<ol class="content-list-ordered" start="${{olMatch[1]}}">`);
                        inOl = true;
                    }}
                    result.push(`<li>${{formatInline(olMatch[2])}}</li>`);
                    continue;
                }}

                if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {{
                    if (inOl) {{ result.push('</ol>'); inOl = false; }}
                    if (!inUl) {{
                        result.push('<ul class="content-list">');
                        inUl = true;
                    }}
                    result.push(`<li>${{formatInline(trimmed.substring(2))}}</li>`);
                    continue;
                }}

                closeLists();
                result.push(`<p class="content-para">${{formatInline(trimmed)}}</p>`);
            }}

            if (inTable) flushTable();
            closeLists();

            let finalHtml = result.join('\\n');
            codeBlocks.forEach((code, idx) => {{
                finalHtml = finalHtml.replace(`__CODE_BLOCK_${{idx}}__`, code);
            }});

            return finalHtml;
        }}

        function toggleTopicComplete(chId, state) {{
            const willBeDone = (state !== undefined) ? !!state : !completedTopics[chId];
            if (willBeDone) completedTopics[chId] = true;
            else delete completedTopics[chId];
            try {{
                localStorage.setItem('bds.medicine.progress', JSON.stringify(completedTopics));
                localStorage.setItem('medicine_completed_topics', JSON.stringify(completedTopics));
            }} catch(e) {{}}
            if (window.CoreEngine && CoreEngine.updateProgressDisplays) {{
                CoreEngine.updateProgressDisplays();
            }}
            if (currentChapterIdx === -1) {{
                renderDashboard();
            }} else {{
                renderChapterView();
            }}
        }}

        function onSearchInput() {{
            renderSidebar();
        }}

        function setCategoryFilter(cat) {{
            currentCategory = cat;
            document.querySelectorAll('#categoryPillBar .filter-chip').forEach(btn => {{
                if (btn.innerText.toLowerCase().includes(cat.toLowerCase()) || (cat === 'All' && btn.innerText.includes('All'))) {{
                    btn.classList.add('active');
                }} else {{
                    btn.classList.remove('active');
                }}
            }});
            renderSidebar();
        }}

        function toggleSidebar(force) {{
            const sb = document.getElementById('sidebar');
            const bd = document.getElementById('sidebar-backdrop');
            if (!sb) return;
            if (force !== undefined) {{
                if (force) {{
                    sb.classList.add('open');
                    sb.classList.add('active');
                    if (bd) bd.classList.add('active');
                }} else {{
                    sb.classList.remove('open');
                    sb.classList.remove('active');
                    if (bd) bd.classList.remove('active');
                }}
            }} else {{
                const isOpen = sb.classList.toggle('open');
                sb.classList.toggle('active', isOpen);
                if (bd) bd.classList.toggle('active', isOpen);
            }}
        }}
        window.toggleSidebar = toggleSidebar;
        window.toggleMobileSidebar = toggleSidebar;

        function toggleVivaAnswer(btn) {{
            const ans = btn.nextElementSibling;
            if (ans) {{
                ans.classList.toggle('revealed');
                btn.innerText = ans.classList.contains('revealed') ? 'Hide Answer' : 'Tap to Reveal Answer';
            }}
        }}

        function flipFlashcard() {{
            const ch = CHAPTERS[currentChapterIdx];
            if (!ch || !ch.flashcards || ch.flashcards.length === 0) return;
            const card = ch.flashcards[currentFlashcardIdx];
            isFlashcardFlipped = !isFlashcardFlipped;

            const textEl = document.getElementById('flashcardText');
            const tagEl = document.getElementById('flashcardTag');
            if (isFlashcardFlipped) {{
                textEl.innerText = card.a;
                tagEl.innerText = `ANSWER (CARD ${{currentFlashcardIdx + 1}} OF ${{ch.flashcards.length}})`;
                tagEl.style.color = 'var(--accent-primary, #38bdf8)';
            }} else {{
                textEl.innerText = card.q;
                tagEl.innerText = `QUESTION (CARD ${{currentFlashcardIdx + 1}} OF ${{ch.flashcards.length}})`;
                tagEl.style.color = '';
            }}
        }}

        function prevFlashcard() {{
            const ch = CHAPTERS[currentChapterIdx];
            if (!ch || !ch.flashcards) return;
            if (currentFlashcardIdx > 0) {{
                currentFlashcardIdx--;
                isFlashcardFlipped = false;
                const card = ch.flashcards[currentFlashcardIdx];
                document.getElementById('flashcardText').innerText = card.q;
                document.getElementById('flashcardTag').innerText = `QUESTION (CARD ${{currentFlashcardIdx + 1}} OF ${{ch.flashcards.length}})`;
                document.getElementById('flashcardTag').style.color = '';
            }}
        }}

        function nextFlashcard() {{
            const ch = CHAPTERS[currentChapterIdx];
            if (!ch || !ch.flashcards) return;
            if (currentFlashcardIdx + 1 < ch.flashcards.length) {{
                currentFlashcardIdx++;
                isFlashcardFlipped = false;
                const card = ch.flashcards[currentFlashcardIdx];
                document.getElementById('flashcardText').innerText = card.q;
                document.getElementById('flashcardTag').innerText = `QUESTION (CARD ${{currentFlashcardIdx + 1}} OF ${{ch.flashcards.length}})`;
                document.getElementById('flashcardTag').style.color = '';
            }}
        }}

        function saveTopicNotes(chId, val) {{
            localStorage.setItem('medicine_notes_' + chId, val);
            const status = document.getElementById('notesStatus');
            if (status) status.innerText = 'Saved ' + new Date().toLocaleTimeString();
        }}

        function updateRubricScore() {{
            const sliders = document.querySelectorAll('.rubric-slider input');
            let total = 0;
            sliders.forEach(s => total += parseInt(s.value));
            const scaled = ((total / (sliders.length * 10)) * 15).toFixed(1);
            document.getElementById('examScoreTotal').innerText = `${{scaled}} / 15 Marks (${{scaled >= 11 ? 'Honors' : 'Pass'}})`;
        }}

        function saveMedicineEvaluation(topicId) {{
            const totalEl = document.getElementById('examScoreTotal');
            const totalText = totalEl ? totalEl.textContent : '12.5';
            const match = totalText.match(/([0-9.]+)\s*\/\s*15/);
            const scoreVal = match ? parseFloat(match[1]) : 12.5;

            let gradeLabel = 'Pass';
            if (scoreVal >= 12.0) gradeLabel = 'Honors / Distinction';
            else if (scoreVal >= 10.0) gradeLabel = 'First Class';
            else if (scoreVal < 7.5) gradeLabel = 'Needs Revision';

            const scores = {{}};
            const sliders = document.querySelectorAll('.rubric-slider input');
            sliders.forEach((slider, idx) => {{
                scores['criteria_' + (idx + 1)] = parseFloat(slider.value) || 0;
            }});

            if (window.BdsSimulator) {{
                window.BdsSimulator.saveEvaluation('medicine', topicId, {{
                    total: scoreVal,
                    outOf: 15,
                    gradeLabel: gradeLabel,
                    scores: scores
                }});
            }}
        }}

        window.applyLoadedEvaluationScores = function(scores) {{
            if (!scores) return;
            const sliders = document.querySelectorAll('.rubric-slider input');
            sliders.forEach((slider, idx) => {{
                if (scores['criteria_' + (idx + 1)] !== undefined) {{
                    slider.value = scores['criteria_' + (idx + 1)];
                }}
            }});
            updateRubricScore();
        }};

        function openPdfModal() {{
            document.getElementById('pdfModal').style.display = 'flex';
        }}
        function closePdfModal() {{
            document.getElementById('pdfModal').style.display = 'none';
        }}

        function openDiagramModal(chId) {{
            const ch = CHAPTERS.find(c => c.id === chId) || CHAPTERS[currentChapterIdx];
            document.getElementById('modalDiagramTitle').innerText = ch.title + ': Full Schematic';
            document.getElementById('modalDiagramBody').innerHTML = ch.schematic_svg;
            document.getElementById('modal').style.display = 'flex';
        }}
        function closeDiagramModal() {{
            document.getElementById('modal').style.display = 'none';
        }}

        function toggleStudyFocusTimer() {{
            if (window.BdsTimer) {{
                window.BdsTimer.toggle();
            }}
        }}

        function launchExamSimFromDashboard() {{
            selectChapter(0);
            setTimeout(() => {{
                switchTab('exam');
            }}, 120);
        }}

        function openDiagramSpotterFromDashboard() {{
            selectChapter(0);
            setTimeout(() => {{
                switchTab('diagrams');
            }}, 120);
        }}

        function openFlashcardsFromDashboard() {{
            selectChapter(0);
            setTimeout(() => {{
                switchTab('quiz');
            }}, 120);
        }}

        function toggleTheme() {{
            if (window.CoreEngine && typeof window.CoreEngine.toggleTheme === 'function') {{
                window.CoreEngine.toggleTheme();
            }} else {{
                const isLight = document.documentElement.getAttribute('data-theme') === 'light' || document.body.classList.contains('light');
                const next = isLight ? 'dark' : 'light';
                document.documentElement.setAttribute('data-theme', next);
                document.documentElement.classList.remove('dark', 'light');
                document.documentElement.classList.add(next);
                document.documentElement.style.colorScheme = next;
                if (document.body) {{
                    document.body.classList.remove('dark', 'light');
                    document.body.classList.add(next);
                }}
                const metaTheme = document.getElementById('metaThemeColor') || document.querySelector('meta[name="theme-color"]');
                if (metaTheme) metaTheme.setAttribute('content', next === 'light' ? '#f8fafc' : '#090a12');
                try {{
                    localStorage.setItem('medicine_theme', next);
                    localStorage.setItem('bds.medicine.theme', next);
                    localStorage.setItem('bds.theme', next);
                }} catch(e) {{}}
            }}
            const isDark = document.documentElement.getAttribute('data-theme') !== 'light' && !document.body.classList.contains('light');
            const btn = document.getElementById('themeToggleBtn');
            if (btn) btn.innerHTML = isDark ? '{ICONS["sun"]}' : '{ICONS["moon"]}';
        }}

        // Stethoscope Logo SVG for Medicine Pro
        const MEDICINE_LOGO_SVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs><linearGradient id="medBgCard" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1e3a8a"/><stop offset="100%" stop-color="#0f172a"/></linearGradient></defs><rect width="512" height="512" rx="112" fill="url(#medBgCard)" stroke="rgba(255,255,255,0.20)" stroke-width="16"/><g fill="none" stroke="#f8fafc" stroke-linecap="round" stroke-linejoin="round" stroke-width="26"><circle cx="180" cy="130" r="14" fill="#93c5fd" stroke="none"/><circle cx="332" cy="130" r="14" fill="#93c5fd" stroke="none"/><path d="M180 144 V180 C180 220 220 250 256 250 C292 250 332 220 332 180 V144"/><path d="M256 250 V290 C256 360 190 390 190 340 C190 290 290 300 290 370 C290 410 320 410 336 410"/><circle cx="356" cy="410" r="30" fill="#93c5fd" fill-opacity="0.25" stroke="#ffffff" stroke-width="24"/><circle cx="356" cy="410" r="12" fill="#38bdf8" stroke="none"/></g></svg>`;

        // Keyboard Shortcuts (Esc to close modals)
        window.addEventListener('keydown', e => {{
            if (e.key === 'Escape') {{
                closePdfModal();
                closeDiagramModal();
                toggleMobileSidebar(false);
            }}
        }});

        // Initialize Shared Core Engine
        if (window.CoreEngine) {{
            CoreEngine.init({{
                portalKey: 'medicine',
                name: 'MEDICINE PRO',
                subtitle: 'Paper II · Clinical monograph',
                logoSvg: MEDICINE_LOGO_SVG,
                hubUrl: 'https://krrish41.github.io/bds-vault/#medicine',
                pdfUrl: 'General_Medicine_Master_Notes.pdf',
                searchPlaceholder: 'Search conditions, signs, drugs...',
                topics: CHAPTERS,
                currentTopicIndex: currentChapterIdx,
                onToggleAudioWalk: () => {{
                    togglePlayPauseAudio();
                }},
                onOpenDashboard: () => {{
                    showDashboard(true);
                }},
                onSelectTopic: (idx) => {{
                    selectChapter(idx, true);
                }},
                onOpenSimulator: () => {{
                    selectChapter(currentChapterIdx >= 0 ? currentChapterIdx : 0);
                    setTimeout(() => switchTab('exam'), 120);
                }},
                onOpenSpotters: () => {{
                    selectChapter(currentChapterIdx >= 0 ? currentChapterIdx : 0);
                    setTimeout(() => switchTab('diagrams'), 120);
                }},
                onOpenFlashcards: () => {{
                    selectChapter(currentChapterIdx >= 0 ? currentChapterIdx : 0);
                    setTimeout(() => switchTab('quiz'), 120);
                }},
                onOpenCheatSheet: () => {{
                    selectChapter(20);
                }},
                onToggleComplete: (id, isDone) => {{
                    toggleTopicComplete(id, isDone);
                }},
                onResetStatusFilter: () => {{
                    setCategoryFilter('All');
                }}
            }});
        }}

        initVoiceList();
        window.addEventListener('hashchange', handleHashRoute);
        if (window.location.hash && window.location.hash.startsWith('#/topic/')) {{
            handleHashRoute();
        }} else {{
            renderDashboard();
        }}
    </script>
</body>
</html>
"""
    return html

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Loaded {len(ALL_CHAPTERS)} General Medicine chapters.")

    # 1. Generate Markdown
    md_path = os.path.join(base_dir, "General_Medicine_Master_Notes.md")
    print(f"Generating {md_path}...")
    md_content = generate_markdown(ALL_CHAPTERS)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Markdown generated: {len(md_content)} characters.")

    # 2. Generate Print-ready HTML
    print_html_path = os.path.join(base_dir, "General_Medicine_Master_Notes.html")
    print(f"Generating {print_html_path}...")
    print_html_content = generate_print_html(ALL_CHAPTERS)
    with open(print_html_path, "w", encoding="utf-8") as f:
        f.write(print_html_content)
    print(f"Print HTML generated: {len(print_html_content)} characters.")

    # 3. Generate Interactive Study App (index.html)
    app_html_path = os.path.join(base_dir, "index.html")
    print(f"Generating {app_html_path}...")
    app_html_content = generate_interactive_dashboard(ALL_CHAPTERS)
    with open(app_html_path, "w", encoding="utf-8") as f:
        f.write(app_html_content)
    print(f"Interactive App HTML generated: {len(app_html_content)} characters.")

    # 4. Emit topics.json registry
    topics_registry = []
    import re
    for idx, ch in enumerate(ALL_CHAPTERS):
        title = ch["title"]
        clean_title = re.sub(r'^(Chapter\s*\d+[:.]*|\d+[\.:\s]+)', '', title, flags=re.IGNORECASE).strip()
        slug = re.sub(r'[^a-zA-Z0-9]+', '-', clean_title).strip('-').lower()
        is_cheat_sheet = "cheat sheet" in title.lower() or "rapid revision" in title.lower()
        category = ch.get("category", "General")

        word_count = sum(len(sec["content"].split()) for sec in ch["sections"])
        word_count += len(ch.get("clinical_pearl", "").split())
        read_minutes = max(5, round(word_count / 180))

        topics_registry.append({
            "id": slug,
            "title": title,
            "category": category,
            "readMinutes": read_minutes,
            "readingTime": f"{read_minutes} min read",
            "portal": "medicine",
            "portalName": "General Medicine Pro",
            "paper": "Paper II · Medicine",
            "chapter": idx + 1,
            "type": "cheat-sheet" if is_cheat_sheet else "essay",
            "url": f"https://krrish41.github.io/General-Medicine/#/topic/{slug}",
            "order": idx + 1,
            "tags": [category, "medicine", slug]
        })
    with open(os.path.join(base_dir, "topics.json"), "w", encoding="utf-8") as f:
        json.dump(topics_registry, f, indent=2)
    print(f"Emitted topics.json ({len(topics_registry)} topics).")

    # 4. Compile PDF via Headless Edge
    pdf_path = os.path.join(base_dir, "General_Medicine_Master_Notes.pdf")
    print(f"Compiling typeset PDF to {pdf_path}...")
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "msedge"
    ]
    edge_bin = None
    for ep in edge_paths:
        if os.path.exists(ep) or ep == "msedge":
            edge_bin = ep
            break

    if edge_bin:
        cmd = [
            edge_bin,
            "--headless",
            "--disable-gpu",
            "--run-all-compositor-stages-before-draw",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            f"file:///{print_html_path.replace(os.sep, '/')}"
        ]
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
            if os.path.exists(pdf_path):
                size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
                print(f"PDF successfully compiled: {size_mb:.2f} MB")
            else:
                print("PDF compilation completed without file output.")
        except Exception as e:
            print(f"Error compiling PDF: {e}")
    else:
        print("Microsoft Edge not found for headless PDF compilation.")

if __name__ == "__main__":
    main()
