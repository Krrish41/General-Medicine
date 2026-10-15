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

from content.gastrointestinal_and_hepato import CHAPTERS as c1
from content.cardiovascular import CHAPTERS as c2
from content.infections_and_endocrine import CHAPTERS as c3
from content.hematology_renal_neuro import CHAPTERS as c4
from content.formatter import ICONS, FAVICON_SVG, clean_latex, parse_markdown_to_html
from content.interactive_data import CLASSIFICATION_PRESETS, SPOTTER_HOTSPOTS, COMPARISON_PAIRS, EXAM_RUBRIC_CRITERIA

ALL_CHAPTERS = c1 + c2 + c3 + c4

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
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

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
        font-size: 8pt;
        color: #94a3b8;
    }}
}}

body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.6;
    color: #1e293b;
    background-color: #ffffff;
    font-size: 9.8pt;
    margin: 0;
    padding: 0;
}}

.cover-page {{
    page-break-after: always;
    min-height: 85vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 40px 20px;
    border: 3px double #059669;
    margin: 20px;
}}

.cover-title {{
    font-size: 26pt;
    font-weight: 800;
    color: #065f46;
    letter-spacing: -0.02em;
    margin-bottom: 12px;
    text-transform: uppercase;
}}

.cover-subtitle {{
    font-size: 13pt;
    color: #047857;
    margin-bottom: 30px;
    font-weight: 600;
}}

.cover-meta {{
    font-size: 10pt;
    color: #64748b;
    line-height: 1.8;
    border-top: 1px solid #e2e8f0;
    padding-top: 20px;
    max-width: 500px;
}}

.chapter-container {{
    page-break-before: always;
    margin-bottom: 30px;
}}

h1.chapter-title {{
    font-size: 18pt;
    font-weight: 800;
    color: #065f46;
    border-bottom: 2.5px solid #10b981;
    padding-bottom: 8px;
    margin-top: 20px;
    margin-bottom: 14px;
}}

.chapter-badge {{
    display: inline-block;
    background: #ecfdf5;
    color: #047857;
    border: 1px solid #a7f3d0;
    border-radius: 4px;
    padding: 2px 8px;
    font-size: 8pt;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 12px;
}}

.pearl-box {{
    background: #f0fdf4;
    border-left: 4px solid #10b981;
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
    margin: 16px 0;
    font-size: 9.5pt;
}}

.pearl-box strong {{
    color: #065f46;
}}

.section-title {{
    font-size: 12pt;
    font-weight: 700;
    color: #1e293b;
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
    <div style="width: 50px; height: 50px; background: #10b981; border-radius: 12px; margin-bottom: 20px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 24pt; font-weight: 800;">M</div>
    <div class="cover-title">General Medicine</div>
    <div class="cover-subtitle">15-Mark University Examination Master Monograph</div>
    <div class="cover-meta">
        <strong>Curriculum:</strong> BDS 3rd Year & MBBS Clinical Medicine<br>
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
            <strong style="color: #0f172a; font-size: 9pt; text-transform: uppercase; letter-spacing: 0.05em;">High-Yield Viva Pearls</strong><ul>""")
            for q in ch["viva_questions"]:
                html_parts.append(f"<li>{clean_latex(q)}</li>")
            html_parts.append("</ul></div>")

        html_parts.append("</div>")

    html_parts.append("</body></html>")
    return "\n".join(html_parts)

def generate_interactive_dashboard(chapters):
    # Serialized chapters data for client-side search & filtering
    chapters_json = json.dumps([
        {
            "id": ch["id"],
            "title": ch["title"],
            "category": ch["category"],
            "badge": ch["badge"],
            "reading_time": ch["reading_time"],
            "clinical_pearl": ch["clinical_pearl"],
            "sections": ch["sections"],
            "comparisons": ch.get("comparisons", []),
            "must_draw": ch.get("must_draw", ""),
            "viva_questions": ch.get("viva_questions", [])
        }
        for ch in chapters
    ])

    presets_json = json.dumps(CLASSIFICATION_PRESETS)
    comparisons_json = json.dumps(COMPARISON_PAIRS)
    rubric_json = json.dumps(EXAM_RUBRIC_CRITERIA)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/svg+xml" href="{FAVICON_SVG}">
    <title>General Medicine — Interactive Clinical Study Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #0a0f1d;
            --bg-surface: #111827;
            --bg-card: #182235;
            --bg-card-hover: #1f2b42;
            --border-color: rgba(255, 255, 255, 0.08);
            --border-active: rgba(16, 185, 129, 0.4);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --accent-primary: #10b981;
            --accent-glow: rgba(16, 185, 129, 0.15);
            --radius-md: 10px;
            --radius-lg: 16px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-base);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}

        .navbar {{
            position: sticky;
            top: 0;
            backdrop-filter: blur(16px);
            background: rgba(10, 15, 29, 0.85);
            border-bottom: 1px solid var(--border-color);
            padding: 0.9rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 50;
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: inherit;
        }}

        .brand-badge {{
            width: 34px;
            height: 34px;
            background: linear-gradient(135deg, #10b981, #059669);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1.1rem;
            color: #fff;
        }}

        .brand-title h1 {{
            font-size: 1.05rem;
            font-weight: 700;
        }}

        .brand-title span {{
            font-size: 0.72rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 600;
        }}

        .nav-actions {{
            display: flex;
            gap: 10px;
        }}

        .btn-nav {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .btn-nav:hover {{
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.2);
        }}

        .container {{
            max-width: 1380px;
            margin: 0 auto;
            padding: 2rem 1.5rem;
            flex: 1;
            width: 100%;
        }}

        .header-search {{
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }}

        .search-box {{
            flex: 1;
            min-width: 300px;
            position: relative;
        }}

        .search-input {{
            width: 100%;
            padding: 12px 18px 12px 42px;
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            color: var(--text-primary);
            font-size: 0.92rem;
            outline: none;
        }}

        .search-input:focus {{
            border-color: var(--accent-primary);
            box-shadow: 0 0 0 2px var(--accent-glow);
        }}

        .category-filter {{
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 4px;
        }}

        .filter-chip {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--text-secondary);
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s ease;
        }}

        .filter-chip.active {{
            background: rgba(16, 185, 129, 0.15);
            border-color: var(--accent-primary);
            color: #34d399;
        }}

        .layout-grid {{
            display: grid;
            grid-template-columns: 360px 1fr;
            gap: 2rem;
        }}

        .topic-list {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 1.25rem;
            max-height: calc(100vh - 180px);
            overflow-y: auto;
        }}

        .topic-item {{
            padding: 12px 14px;
            border-radius: var(--radius-md);
            cursor: pointer;
            margin-bottom: 6px;
            border: 1px solid transparent;
            transition: all 0.2s ease;
        }}

        .topic-item:hover {{
            background: var(--bg-card);
        }}

        .topic-item.active {{
            background: var(--bg-card);
            border-color: var(--border-active);
        }}

        .topic-item-title {{
            font-size: 0.9rem;
            font-weight: 700;
            margin-bottom: 4px;
        }}

        .topic-item-meta {{
            font-size: 0.75rem;
            color: var(--text-muted);
            display: flex;
            justify-content: space-between;
        }}

        .viewer-panel {{
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 2.5rem;
            max-height: calc(100vh - 180px);
            overflow-y: auto;
        }}

        .viewer-header {{
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1.5rem;
            margin-bottom: 2rem;
        }}

        .viewer-category {{
            font-size: 0.8rem;
            font-weight: 700;
            color: #34d399;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 6px;
        }}

        .viewer-title {{
            font-size: 1.85rem;
            font-weight: 800;
            margin-bottom: 1rem;
            letter-spacing: -0.02em;
        }}

        .clinical-pearl-card {{
            background: rgba(16, 185, 129, 0.08);
            border-left: 4px solid var(--accent-primary);
            padding: 14px 18px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 2rem;
            font-size: 0.92rem;
        }}

        .clinical-pearl-card strong {{
            color: #34d399;
        }}

        .viewer-section {{
            margin-bottom: 2.5rem;
        }}

        .viewer-section-title {{
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 12px;
            color: #fff;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            padding-bottom: 6px;
        }}

        .viewer-body {{
            font-size: 0.95rem;
            color: #cbd5e1;
            line-height: 1.7;
        }}

        .viewer-body p {{
            margin-bottom: 1rem;
        }}

        .viewer-body table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
            font-size: 0.88rem;
        }}

        .viewer-body th, .viewer-body td {{
            padding: 10px 14px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}

        .viewer-body th {{
            background: rgba(255, 255, 255, 0.04);
            color: #fff;
            font-weight: 600;
        }}

        .viewer-body tr:nth-child(even) {{
            background: rgba(255, 255, 255, 0.02);
        }}

        .viewer-body pre {{
            background: #060913;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 14px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            overflow-x: auto;
            margin: 1.5rem 0;
            color: #a7f3d0;
        }}

        .viva-box {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            margin-top: 2rem;
        }}

        .viva-title {{
            font-size: 0.85rem;
            font-weight: 700;
            color: #34d399;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 12px;
        }}

        .viva-list {{
            list-style: none;
        }}

        .viva-list li {{
            margin-bottom: 10px;
            padding-left: 20px;
            position: relative;
            font-size: 0.9rem;
            color: #e2e8f0;
        }}

        .viva-list li::before {{
            content: "•";
            position: absolute;
            left: 6px;
            color: #34d399;
            font-weight: bold;
        }}

        @media (max-width: 900px) {{
            .layout-grid {{
                grid-template-columns: 1fr;
            }}
            .topic-list {{
                max-height: 350px;
            }}
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <a href="#" class="brand">
            <div class="brand-badge">M</div>
            <div class="brand-title">
                <h1>GENERAL MEDICINE</h1>
                <span>Clinical Monograph Suite</span>
            </div>
        </a>
        <div class="nav-actions">
            <a href="General_Medicine_Master_Notes.pdf" class="btn-nav" target="_blank">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/></svg>
                Download Master PDF
            </a>
            <a href="https://krrish41.github.io/bds-vault/" class="btn-nav" target="_blank">
                Clinical Vault Hub
            </a>
        </div>
    </nav>

    <main class="container">
        <div class="header-search">
            <div class="search-box">
                <input type="text" id="topicSearch" class="search-input" placeholder="Search conditions, clinical signs, or drug doses..." oninput="filterTopics()">
            </div>
            <div class="category-filter" id="categoryBar">
                <button class="filter-chip active" onclick="setCategory('All')">All Topics</button>
                <button class="filter-chip" onclick="setCategory('Gastroenterology')">Gastro & Hepato</button>
                <button class="filter-chip" onclick="setCategory('Cardiovascular')">Cardiovascular</button>
                <button class="filter-chip" onclick="setCategory('Infectious')">Infections & STDs</button>
                <button class="filter-chip" onclick="setCategory('Endocrinology')">Endocrine / DM</button>
                <button class="filter-chip" onclick="setCategory('Hematology')">Hematology & Oncology</button>
                <button class="filter-chip" onclick="setCategory('Nephrology')">Nephrology</button>
                <button class="filter-chip" onclick="setCategory('Neurology')">Neurology & Emergency</button>
            </div>
        </div>

        <div class="layout-grid">
            <aside class="topic-list" id="topicListContainer">
                <!-- Injected via JavaScript -->
            </aside>
            <section class="viewer-panel" id="viewerContainer">
                <!-- Injected via JavaScript -->
            </section>
        </div>
    </main>

    <script>
        const CHAPTERS = {chapters_json};
        let currentCategory = 'All';
        let activeChapterId = CHAPTERS[0].id;

        function setCategory(cat) {{
            currentCategory = cat;
            document.querySelectorAll('.filter-chip').forEach(btn => {{
                if (btn.innerText.toLowerCase().includes(cat.toLowerCase()) || (cat === 'All' && btn.innerText.includes('All'))) {{
                    btn.classList.add('active');
                }} else {{
                    btn.classList.remove('active');
                }}
            }});
            renderTopicList();
        }}

        function filterTopics() {{
            renderTopicList();
        }}

        function renderTopicList() {{
            const query = document.getElementById('topicSearch').value.toLowerCase();
            const listEl = document.getElementById('topicListContainer');
            listEl.innerHTML = '';

            const filtered = CHAPTERS.filter(ch => {{
                const matchesCat = (currentCategory === 'All') || ch.category.toLowerCase().includes(currentCategory.toLowerCase());
                const matchesQuery = !query || ch.title.toLowerCase().includes(query) || ch.sections.some(s => s.content.toLowerCase().includes(query));
                return matchesCat && matchesQuery;
            }});

            if (filtered.length === 0) {{
                listEl.innerHTML = '<div style=\"padding:20px; color:#64748b; text-align:center;\">No matching topics found.</div>';
                return;
            }}

            filtered.forEach(ch => {{
                const item = document.createElement('div');
                item.className = 'topic-item' + (ch.id === activeChapterId ? ' active' : '');
                item.onclick = () => selectChapter(ch.id);
                item.innerHTML = `
                    <div class=\"topic-item-title\">${{ch.title}}</div>
                    <div class=\"topic-item-meta\">
                        <span>${{ch.category}}</span>
                        <span>${{ch.reading_time}}</span>
                    </div>
                `;
                listEl.appendChild(item);
            }});
        }}

        function selectChapter(id) {{
            activeChapterId = id;
            renderTopicList();
            renderViewer();
        }}

        function renderViewer() {{
            const ch = CHAPTERS.find(c => c.id === activeChapterId) || CHAPTERS[0];
            const viewerEl = document.getElementById('viewerContainer');

            let sectionsHtml = '';
            ch.sections.forEach(sec => {{
                sectionsHtml += `
                    <div class=\"viewer-section\">
                        <h3 class=\"viewer-section-title\">${{sec.title}}</h3>
                        <div class=\"viewer-body\">${{markdownToHtml(sec.content)}}</div>
                    </div>
                `;
            }});

            let comparisonsHtml = '';
            if (ch.comparisons && ch.comparisons.length > 0) {{
                ch.comparisons.forEach(comp => {{
                    let tableRows = '';
                    comp.rows.forEach(r => {{
                        tableRows += '<tr>' + r.map(c => `<td>${{c}}</td>`).join('') + '</tr>';
                    }});
                    comparisonsHtml += `
                        <div class=\"viewer-section\">
                            <h3 class=\"viewer-section-title\">${{comp.title}}</h3>
                            <div class=\"viewer-body\">
                                <table>
                                    <thead><tr>${{comp.headers.map(h => `<th>${{h}}</th>`).join('')}}</tr></thead>
                                    <tbody>${{tableRows}}</tbody>
                                </table>
                            </div>
                        </div>
                    `;
                }});
            }}

            let vivaHtml = '';
            if (ch.viva_questions && ch.viva_questions.length > 0) {{
                vivaHtml = `
                    <div class=\"viva-box\">
                        <div class=\"viva-title\">High-Yield Clinical & Viva Voce Pearls</div>
                        <ul class=\"viva-list\">
                            ${{ch.viva_questions.map(q => `<li>${{q}}</li>`).join('')}}
                        </ul>
                    </div>
                `;
            }}

            viewerEl.innerHTML = `
                <div class=\"viewer-header\">
                    <div class=\"viewer-category\">${{ch.category}} • ${{ch.badge}}</div>
                    <h2 class=\"viewer-title\">${{ch.title}}</h2>
                    <div class=\"clinical-pearl-card\">
                        <strong>Clinical Pearl:</strong> ${{ch.clinical_pearl}}
                    </div>
                </div>
                ${{sectionsHtml}}
                ${{comparisonsHtml}}
                ${{vivaHtml}}
            `;
            viewerEl.scrollTop = 0;
        }}

        function markdownToHtml(md) {{
            if (!md) return '';
            let html = md
                .replace(/^### (.*$)/gim, '<h4 style=\"font-size:1.05rem; font-weight:700; margin:1rem 0 0.5rem 0; color:#e2e8f0;\">$1</h4>')
                .replace(/^## (.*$)/gim, '<h3 style=\"font-size:1.15rem; font-weight:700; margin:1.2rem 0 0.6rem 0; color:#fff;\">$1</h3>')
                .replace(/^# (.*$)/gim, '<h2 style=\"font-size:1.3rem; font-weight:800; margin:1.5rem 0 0.8rem 0; color:#fff;\">$1</h2>')
                .replace(/\\*\\*(.*?)\\*\\*/gim, '<strong style=\"color:#f8fafc;\">$1</strong>')
                .replace(/\\*(.*?)\\*/gim, '<em>$1</em>')
                .replace(/```([\\s\\S]*?)```/gim, '<pre>$1</pre>')
                .replace(/^\\* (.*$)/gim, '<li>$1</li>')
                .replace(/\\n/gim, '<br>');
            return html;
        }}

        // Initial render
        renderTopicList();
        renderViewer();
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
