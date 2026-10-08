# generate_final_report_docx.py
# Compiles all front matter, chapters, tables, algorithms, and figures into the final 40-45 page docx document

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

import report_meta
import content_frontmatter
import content_ch1
import content_ch2
import content_ch3
import content_ch4
import content_ch5
import content_ch6_7_8

def create_element(name):
    return OxmlElement(name)

def set_cell_margins(cell, top=100, bottom=100, left=160, right=160):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="777777", sz="6", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideH w:val="{val}" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def add_page_number_field(run):
    for t in ['begin', 'separate', 'end']:
        c = OxmlElement('w:fldChar')
        c.set(qn('w:fldCharType'), t)
        if t == 'separate':
            it = OxmlElement('w:instrText')
            it.set(qn('xml:space'), 'preserve')
            it.text = 'PAGE'
            run._r.append(it)
        run._r.append(c)

def format_run(run, font_name="Times New Roman", size_pt=12, bold=False, italic=False, color_rgb=(0x22, 0x22, 0x22)):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)

def add_chapter_header(doc, line1, line2):
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(20)
    p1.paragraph_format.space_after = Pt(4)
    run1 = p1.add_run(line1)
    format_run(run1, size_pt=16, bold=True)
    
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(16)
    run2 = p2.add_run(line2)
    format_run(run2, size_pt=16, bold=True)

def add_primary_heading(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(5)
    run = p.add_run(text.upper())
    format_run(run, size_pt=13, bold=True)

def add_secondary_heading(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run(text)
    format_run(run, size_pt=12, bold=True)

def add_tertiary_heading(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text)
    format_run(run, size_pt=12, bold=True, italic=True)

def add_body_p(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(3.5)
    run = p.add_run(text)
    format_run(run, size_pt=12)


DIAGRAM_MAP = {
    "Taxonomy of LLM Hallucinations and Grounding Mechanisms": "figures/fig1_1_hallucination_taxonomy.png",
    "Literature Architecture Evolution and Taxonomy": "figures/fig2_1_rag_evolution.png",
    "Agentic GraphRAG Interaction and Verification Cycle": "figures/fig2_2_agentic_workflow.png",
    "Research Gap to Proposed Framework Solution Mapping": "figures/fig2_3_gap_mapping.png",
    "Multi-Agent Adaptive GraphRAG System Architecture": "figures/fig4_1_system_architecture.png",
    "DFD Level 0 Context Diagram": "figures/fig4_2_dfd_level0.png",
    "DFD Level 1 Macro Data Flow": "figures/fig4_3_dfd_level1.png",
    "DFD Level 2 Sub-Process Decomposition": "figures/fig4_4_dfd_level2.png",
    "Entity Relationship Diagram": "figures/fig4_5_erd.png",
    "UML Use Case Diagram": "figures/fig4_6_use_case.png",
    "UML Class Diagram": "figures/fig4_7_class_diagram.png",
    "UML Activity Diagram": "figures/fig4_8_activity_diagram.png",
    "UML Sequence Diagram": "figures/fig4_9_sequence_diagram.png",
    "UML Component Diagram": "figures/fig4_10_component_diagram.png",
    "LangGraph Stateful Execution Graph": "figures/fig5_1_langgraph_execution.png"
}

def add_nano_banana_placeholder(doc, name, caption):
    clean_name = name.replace("Insert Diagram generated by Nano Banana here:", "").strip()
    img_path = DIAGRAM_MAP.get(clean_name)
    
    if img_path and os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(3)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(5.4))
    else:
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.0)
        set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
        set_cell_shading(cell, "F4F6F9")
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml('<w:tcBorders ' + nsdecls('w') + '><w:top w:val="single" w:sz="6" w:color="336699"/><w:bottom w:val="single" w:sz="6" w:color="336699"/><w:left w:val="single" w:sz="6" w:color="336699"/><w:right w:val="single" w:sz="6" w:color="336699"/></w:tcBorders>')
        tcPr.append(borders)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        run1 = p.add_run("[" + name.strip() + "]\n")
        format_run(run1, size_pt=11, bold=True, color_rgb=(0x1A, 0x44, 0x80))
        run2 = p.add_run("High-Resolution Vector Architecture & System Modeling Asset")
        format_run(run2, size_pt=9.5, italic=True, color_rgb=(0x66, 0x66, 0x66))
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(3)
    p_cap.paragraph_format.space_after = Pt(10)
    run_cap = p_cap.add_run(caption)
    format_run(run_cap, size_pt=10.5, bold=True)

def add_equation_box(doc, label, formula, explanation):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.0)
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    set_cell_shading(cell, "FBFBFC")
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:color="AAAAAA"/>
            <w:bottom w:val="single" w:sz="4" w:color="AAAAAA"/>
            <w:left w:val="single" w:sz="12" w:color="2B579A"/>
            <w:right w:val="single" w:sz="4" w:color="AAAAAA"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p_eq = cell.paragraphs[0]
    p_eq.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_eq.paragraph_format.space_after = Pt(2)
    run_formula = p_eq.add_run(formula)
    format_run(run_formula, font_name="Cambria Math", size_pt=12, bold=True)
    
    run_lbl = p_eq.add_run(f"    ({label})")
    format_run(run_lbl, size_pt=11, bold=True, color_rgb=(0x55, 0x55, 0x55))
    
    if explanation:
        p_exp = doc.add_paragraph()
        p_exp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_exp.paragraph_format.line_spacing = 1.15
        p_exp.paragraph_format.space_before = Pt(2)
        p_exp.paragraph_format.space_after = Pt(5)
        run_exp = p_exp.add_run(explanation)
        format_run(run_exp, size_pt=10.5, italic=False)

def add_algorithm_box(doc, num, title, code):
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(3)
    run_t = p_title.add_run(f"Algorithm {num}: {title}")
    format_run(run_t, size_pt=11.5, bold=True)
    
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.0)
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    set_cell_shading(cell, "F9FAFB")
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="8" w:color="333333"/>
            <w:bottom w:val="single" w:sz="8" w:color="333333"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.1
    p.paragraph_format.space_after = Pt(0)
    
    lines = code.split("\n")
    if lines and "Algorithm" in lines[0]:
        lines = lines[1:]
    
    run_code = p.add_run("\n".join(lines).strip())
    format_run(run_code, font_name="Courier New", size_pt=9.5)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_custom_table(doc, data):
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(8)
    p_cap.paragraph_format.space_after = Pt(3)
    run_cap = p_cap.add_run(data["caption"])
    format_run(run_cap, size_pt=11, bold=True)
    
    headers = data["headers"]
    rows = data["rows"]
    widths = data["widths"]
    
    tbl = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl)
    
    # Header Row
    hdr_cells = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].width = Inches(widths[i])
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=80, right=80)
        set_cell_shading(hdr_cells[i], "EAECEF")
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.1
        run = p.add_run(h)
        format_run(run, size_pt=10, bold=True)
        
    # Data Rows
    for r_idx, row_data in enumerate(rows):
        row_cells = tbl.rows[r_idx + 1].cells
        bg_color = "FFFFFF" if r_idx % 2 == 0 else "FDFDFE"
        for c_idx, cell_value in enumerate(row_data):
            row_cells[c_idx].width = Inches(widths[c_idx])
            set_cell_margins(row_cells[c_idx], top=60, bottom=60, left=80, right=80)
            if bg_color != "FFFFFF":
                set_cell_shading(row_cells[c_idx], bg_color)
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx != 0 else WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            run = p.add_run(str(cell_value))
            format_run(run, size_pt=9.5)
            
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def render_section_content(doc, sections):
    for sec in sections:
        s_type = sec["type"]
        if s_type == "heading1":
            add_primary_heading(doc, sec["text"])
        elif s_type == "heading2":
            add_secondary_heading(doc, sec["text"])
        elif s_type == "heading3":
            add_tertiary_heading(doc, sec["text"])
        elif s_type == "paragraph":
            add_body_p(doc, sec["text"])
        elif s_type == "nano_banana":
            add_nano_banana_placeholder(doc, f"Insert Diagram generated by Nano Banana here: {sec['name']}", sec["caption"])
        elif s_type == "equation_box":
            add_equation_box(doc, sec["label"], sec["formula"], sec["explanation"])
        elif s_type == "algorithm_box":
            add_algorithm_box(doc, sec["number"], sec["title"], sec["code"])
        elif s_type == "table":
            add_custom_table(doc, sec["data"])

def generate_report():
    print("Beginning comprehensive Stage 1 report generation...")
    doc = docx.Document()
    
    # Configure initial section (Front Matter)
    s1 = doc.sections[0]
    s1.page_width = Inches(8.27)
    s1.page_height = Inches(11.69)
    s1.top_margin = Inches(1.0)
    s1.bottom_margin = Inches(1.0)
    s1.left_margin = Inches(1.25)
    s1.right_margin = Inches(1.0)
    s1.different_first_page_header_footer = True
    
    # ------------------ COVER PAGE ------------------
    print("Generating Cover Page...")
    p_cov_top = doc.add_paragraph()
    p_cov_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cov_top.paragraph_format.space_before = Pt(12)
    p_cov_top.paragraph_format.space_after = Pt(8)
    run = p_cov_top.add_run("A PROJECT REPORT ON\n")
    format_run(run, size_pt=14, bold=True)
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(16)
    p_title.paragraph_format.line_spacing = 1.3
    run_title = p_title.add_run(content_frontmatter.COVER_PAGE_DATA["report_title"])
    format_run(run_title, size_pt=15, bold=True)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(6)
    p_sub.paragraph_format.space_after = Pt(16)
    p_sub.paragraph_format.line_spacing = 1.2
    run_sub = p_sub.add_run(content_frontmatter.COVER_PAGE_DATA["submission_statement"])
    format_run(run_sub, size_pt=11.5, bold=True)
    
    p_by = doc.add_paragraph()
    p_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_by.paragraph_format.space_before = Pt(6)
    p_by.paragraph_format.space_after = Pt(6)
    run_by = p_by.add_run("SUBMITTED BY\n")
    format_run(run_by, size_pt=12, bold=True)
    
    p_students = doc.add_paragraph()
    p_students.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_students.paragraph_format.space_before = Pt(0)
    p_students.paragraph_format.space_after = Pt(16)
    p_students.paragraph_format.line_spacing = 1.25
    for s_name, s_exam in content_frontmatter.COVER_PAGE_DATA["students"]:
        run_st = p_students.add_run(f"{s_name}    {s_exam}\n")
        format_run(run_st, size_pt=11.5, bold=True)
        
    p_guide = doc.add_paragraph()
    p_guide.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_guide.paragraph_format.space_before = Pt(6)
    p_guide.paragraph_format.space_after = Pt(16)
    run_g_hdr = p_guide.add_run("UNDER THE GUIDANCE OF\n")
    format_run(run_g_hdr, size_pt=12, bold=True)
    run_g_name = p_guide.add_run(f"{content_frontmatter.COVER_PAGE_DATA['guide']}\n")
    format_run(run_g_name, size_pt=13, bold=True)
    
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(12)
    p_inst.paragraph_format.space_after = Pt(0)
    p_inst.paragraph_format.line_spacing = 1.25
    run_dept = p_inst.add_run(f"{content_frontmatter.COVER_PAGE_DATA['department']}\n")
    format_run(run_dept, size_pt=12, bold=True)
    run_clg = p_inst.add_run(f"{content_frontmatter.COVER_PAGE_DATA['college']}\n{content_frontmatter.COVER_PAGE_DATA['location']}\n")
    format_run(run_clg, size_pt=11.5, bold=True)
    run_uni = p_inst.add_run(f"{content_frontmatter.COVER_PAGE_DATA['university']}\n{content_frontmatter.COVER_PAGE_DATA['academic_year']}")
    format_run(run_uni, size_pt=12, bold=True)
    
    # ------------------ FRONT MATTER SECTION ------------------
    s_fm = doc.add_section(docx.enum.section.WD_SECTION.NEW_PAGE)
    s_fm.different_first_page_header_footer = False
    s_fm.footer.is_linked_to_previous = False
    
    p_fm_foot = s_fm.footer.paragraphs[0]
    p_fm_foot.text = f"{report_meta.FOOTER_TEXT}\t\t"
    run_pg_fm = p_fm_foot.add_run()
    add_page_number_field(run_pg_fm)
    
    pgNumType_fm = OxmlElement('w:pgNumType')
    pgNumType_fm.set(qn('w:fmt'), 'roman')
    pgNumType_fm.set(qn('w:start'), '1')
    s_fm._sectPr.append(pgNumType_fm)
    
    # ------------------ CERTIFICATE PAGE ------------------
    print("Generating Certificate Page...")
    p_cert_hdr = doc.add_paragraph()
    p_cert_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_hdr.paragraph_format.space_before = Pt(10)
    p_cert_hdr.paragraph_format.space_after = Pt(14)
    run = p_cert_hdr.add_run("CERTIFICATE")
    format_run(run, size_pt=16, bold=True)
    
    p_cert_intro = doc.add_paragraph()
    p_cert_intro.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_intro.paragraph_format.space_before = Pt(0)
    p_cert_intro.paragraph_format.space_after = Pt(6)
    run = p_cert_intro.add_run("This is to certify that the project report entitled")
    format_run(run, size_pt=12)
    
    p_cert_title = doc.add_paragraph()
    p_cert_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_title.paragraph_format.space_before = Pt(4)
    p_cert_title.paragraph_format.space_after = Pt(12)
    p_cert_title.paragraph_format.line_spacing = 1.25
    run = p_cert_title.add_run(f'"{content_frontmatter.CERTIFICATE_DATA["title"]}"')
    format_run(run, size_pt=13, bold=True)
    
    p_cert_subby = doc.add_paragraph()
    p_cert_subby.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_subby.paragraph_format.space_after = Pt(6)
    run = p_cert_subby.add_run("Submitted by")
    format_run(run, size_pt=12)
    
    p_cert_sts = doc.add_paragraph()
    p_cert_sts.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_sts.paragraph_format.line_spacing = 1.2
    p_cert_sts.paragraph_format.space_after = Pt(12)
    for s_name, s_exam in content_frontmatter.CERTIFICATE_DATA["students"]:
        run = p_cert_sts.add_run(f"{s_name}    {s_exam}\n")
        format_run(run, size_pt=11.5, bold=True)
        
    p_cert_body = doc.add_paragraph()
    p_cert_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_cert_body.paragraph_format.line_spacing = 1.5
    p_cert_body.paragraph_format.space_after = Pt(28)
    run = p_cert_body.add_run(content_frontmatter.CERTIFICATE_DATA["guide_text"])
    format_run(run, size_pt=12)
    
    # Signature Table
    sig_tbl = doc.add_table(rows=2, cols=3)
    sig_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    sig_tbl.rows[0].cells[0].width = Inches(2.2)
    sig_tbl.rows[0].cells[1].width = Inches(2.2)
    sig_tbl.rows[0].cells[2].width = Inches(2.0)
    
    c0 = sig_tbl.rows[0].cells[0].paragraphs[0]
    c0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c0.paragraph_format.line_spacing = 1.15
    run0 = c0.add_run(f"{content_frontmatter.CERTIFICATE_DATA['guide_name']}\n{content_frontmatter.CERTIFICATE_DATA['guide_designation']}")
    format_run(run0, size_pt=11, bold=True)
    
    c1 = sig_tbl.rows[0].cells[1].paragraphs[0]
    c1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c1.paragraph_format.line_spacing = 1.15
    run1 = c1.add_run(f"{content_frontmatter.CERTIFICATE_DATA['principal_name']}\n{content_frontmatter.CERTIFICATE_DATA['principal_designation']}")
    format_run(run1, size_pt=11, bold=True)
    
    c2 = sig_tbl.rows[0].cells[2].paragraphs[0]
    c2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c2.paragraph_format.line_spacing = 1.15
    run2 = c2.add_run(f"\n{content_frontmatter.CERTIFICATE_DATA['external_designation']}")
    format_run(run2, size_pt=11, bold=True)
    
    p_cert_btm = doc.add_paragraph()
    p_cert_btm.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_btm.paragraph_format.space_before = Pt(24)
    p_cert_btm.paragraph_format.line_spacing = 1.2
    run = p_cert_btm.add_run(f"{content_frontmatter.CERTIFICATE_DATA['college_full']}\n{content_frontmatter.CERTIFICATE_DATA['university_year']}")
    format_run(run, size_pt=11.5, bold=True)
    
    doc.add_page_break()
    
    # ------------------ ACKNOWLEDGEMENT PAGE ------------------
    print("Generating Acknowledgement Page...")
    p_ack_hdr = doc.add_paragraph()
    p_ack_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ack_hdr.paragraph_format.space_before = Pt(12)
    p_ack_hdr.paragraph_format.space_after = Pt(16)
    run = p_ack_hdr.add_run("ACKNOWLEDGEMENT")
    format_run(run, size_pt=16, bold=True)
    
    for para in content_frontmatter.ACKNOWLEDGEMENT_TEXT.split("\n\n"):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.35
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(para)
        format_run(run, size_pt=12)
        
    doc.add_page_break()
    
    # ------------------ EXECUTIVE ABSTRACT PAGE ------------------
    print("Generating Abstract Page...")
    p_abs_hdr = doc.add_paragraph()
    p_abs_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_abs_hdr.paragraph_format.space_before = Pt(12)
    p_abs_hdr.paragraph_format.space_after = Pt(16)
    run = p_abs_hdr.add_run("ABSTRACT")
    format_run(run, size_pt=16, bold=True)
    
    for para in content_frontmatter.ABSTRACT_TEXT.split("\n\n"):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.35
        p.paragraph_format.space_after = Pt(6)
        if para.startswith("Keywords:"):
            run_lbl = p.add_run("Keywords: ")
            format_run(run_lbl, size_pt=12, bold=True)
            run_kw = p.add_run(para.replace("Keywords: ", ""))
            format_run(run_kw, size_pt=12, italic=True)
        else:
            run = p.add_run(para)
            format_run(run, size_pt=12)
            
    doc.add_page_break()
    
    # ------------------ TABLE OF CONTENTS (Exact Page Numbers) ------------------
    print("Generating Table of Contents with exact scanned page numbers...")
    p_toc_hdr = doc.add_paragraph()
    p_toc_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_toc_hdr.paragraph_format.space_before = Pt(12)
    p_toc_hdr.paragraph_format.space_after = Pt(16)
    run = p_toc_hdr.add_run("TABLE OF CONTENTS")
    format_run(run, size_pt=16, bold=True)
    
    toc_items = [
        ("CERTIFICATE", "i", True),
        ("ACKNOWLEDGEMENT", "ii", True),
        ("ABSTRACT", "iii", True),
        ("LIST OF ABBREVIATIONS", "v", True),
        ("LIST OF FIGURES", "vi", True),
        ("LIST OF TABLES", "vii", True),
        ("CHAPTER 1: INTRODUCTION", "1", True),
        ("    1.1 Background and Motivation", "1", False),
        ("    1.2 Problem Definition", "3", False),
        ("    1.3 Objectives of the Project", "4", False),
        ("    1.4 Scope of Work", "5", False),
        ("    1.5 Organization of the Report", "6", False),
        ("CHAPTER 2: LITERATURE SURVEY", "7", True),
        ("    2.1 Current Trends in Research", "7", False),
        ("        2.1.1 Traditional and Advanced Vector RAG Pipelines", "7", False),
        ("        2.1.2 Structural Knowledge Retrieval and GraphRAG", "8", False),
        ("        2.1.3 Agentic Orchestration and Iterative Reasoning", "9", False),
        ("        2.1.4 Verification Paradigms and the Self-Correction Paradox", "10", False),
        ("    2.2 Comparative Analysis", "11", False),
        ("    2.3 Critical Analysis of Existing Literature", "13", False),
        ("    2.4 Research Gap Identification", "14", False),
        ("CHAPTER 3: SOFTWARE REQUIREMENTS SPECIFICATION (SRS)", "18", True),
        ("    3.1 Introduction & System Overview", "18", False),
        ("    3.2 Functional Requirements", "19", False),
        ("    3.3 External Interface Requirements", "21", False),
        ("    3.4 Non-Functional Requirements", "21", False),
        ("    3.5 System Requirements", "22", False),
        ("    3.6 Analysis Models & SDLC Implementation Plan", "23", False),
        ("CHAPTER 4: SYSTEM DESIGN", "25", True),
        ("    4.1 System Architecture", "25", False),
        ("    4.2 Data Flow Diagrams (DFD)", "27", False),
        ("    4.3 Entity Relationship Diagram (ERD)", "29", False),
        ("    4.4 UML Diagrams", "30", False),
        ("CHAPTER 5: MATHEMATICAL MODEL & ALGORITHMIC MECHANICS", "35", True),
        ("    5.1 Mathematical Formulations", "35", False),
        ("    5.2 Algorithmic Pseudocode & Execution Strategy", "38", False),
        ("CHAPTER 6: EXPECTED OUTCOMES & APPLICATIONS", "43", True),
        ("    6.1 Expected Outcomes & Performance Benchmarks", "43", False),
        ("    6.2 Edge-Case Handling and System Resilience", "43", False),
        ("    6.3 Enterprise Applications & Domain Impact", "44", False),
        ("    6.4 Limitations of Stage 1", "45", False),
        ("CHAPTER 7: CONCLUSION & FUTURE SCOPE", "46", True),
        ("    7.1 Conclusion", "46", False),
        ("    7.2 Future Scope & Semester VIII Milestones", "46", False),
        ("CHAPTER 8: REFERENCES", "48", True)
    ]

    toc_tbl = doc.add_table(rows=len(toc_items), cols=2)
    toc_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    toc_tbl.rows[0].cells[0].width = Inches(5.2)
    toc_tbl.rows[0].cells[1].width = Inches(0.8)
    
    for idx, (title_str, pg_str, is_bold) in enumerate(toc_items):
        r_cells = toc_tbl.rows[idx].cells
        r_cells[0].width = Inches(5.2)
        r_cells[1].width = Inches(0.8)
        set_cell_margins(r_cells[0], top=20, bottom=20, left=30, right=30)
        set_cell_margins(r_cells[1], top=20, bottom=20, left=30, right=30)
        
        p0 = r_cells[0].paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        p0.paragraph_format.line_spacing = 1.1
        run0 = p0.add_run(title_str)
        format_run(run0, size_pt=10.5, bold=is_bold)
        
        p1 = r_cells[1].paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.space_after = Pt(0)
        p1.paragraph_format.line_spacing = 1.1
        run1 = p1.add_run(pg_str)
        format_run(run1, size_pt=10.5, bold=is_bold)
        
    doc.add_page_break()
    
    # ------------------ LIST OF ABBREVIATIONS ------------------
    print("Generating List of Abbreviations...")
    p_abbr_hdr = doc.add_paragraph()
    p_abbr_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_abbr_hdr.paragraph_format.space_before = Pt(12)
    p_abbr_hdr.paragraph_format.space_after = Pt(16)
    run = p_abbr_hdr.add_run("LIST OF ABBREVIATIONS")
    format_run(run, size_pt=16, bold=True)
    
    abbr_tbl = doc.add_table(rows=len(report_meta.ABBREVIATIONS) + 1, cols=2)
    abbr_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(abbr_tbl)
    
    h0 = abbr_tbl.rows[0].cells[0]
    h1 = abbr_tbl.rows[0].cells[1]
    h0.width = Inches(1.8)
    h1.width = Inches(4.2)
    set_cell_shading(h0, "EAECEF")
    set_cell_shading(h1, "EAECEF")
    set_cell_margins(h0, top=80, bottom=80, left=100, right=100)
    set_cell_margins(h1, top=80, bottom=80, left=100, right=100)
    
    p = h0.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run("Abbreviation")
    format_run(run, size_pt=11, bold=True)
    
    p = h1.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run("Full Form / Standard Illustration")
    format_run(run, size_pt=11, bold=True)
    
    for idx, (abbr, full) in enumerate(report_meta.ABBREVIATIONS):
        r_cells = abbr_tbl.rows[idx + 1].cells
        r_cells[0].width = Inches(1.8)
        r_cells[1].width = Inches(4.2)
        set_cell_margins(r_cells[0], top=40, bottom=40, left=100, right=100)
        set_cell_margins(r_cells[1], top=40, bottom=40, left=100, right=100)
        
        p = r_cells[0].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(abbr)
        format_run(run, size_pt=10, bold=True)
        
        p = r_cells[1].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(full)
        format_run(run, size_pt=10)
        
    doc.add_page_break()
    
    # ------------------ LIST OF FIGURES & TABLES ------------------
    print("Generating List of Figures and Tables...")
    p_fig_hdr = doc.add_paragraph()
    p_fig_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_fig_hdr.paragraph_format.space_before = Pt(12)
    p_fig_hdr.paragraph_format.space_after = Pt(14)
    run = p_fig_hdr.add_run("LIST OF FIGURES")
    format_run(run, size_pt=16, bold=True)
    
    for fig_id, fig_title, _ in report_meta.FIGURES:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        run1 = p.add_run(f"{fig_id}: ")
        format_run(run1, size_pt=10.5, bold=True)
        run2 = p.add_run(fig_title)
        format_run(run2, size_pt=10.5)
        
    doc.add_paragraph().paragraph_format.space_before = Pt(14)
    
    p_tbl_hdr = doc.add_paragraph()
    p_tbl_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tbl_hdr.paragraph_format.space_before = Pt(10)
    p_tbl_hdr.paragraph_format.space_after = Pt(14)
    run = p_tbl_hdr.add_run("LIST OF TABLES")
    format_run(run, size_pt=16, bold=True)
    
    for tbl_id, tbl_title in report_meta.TABLES:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        run1 = p.add_run(f"{tbl_id}: ")
        format_run(run1, size_pt=10.5, bold=True)
        run2 = p.add_run(tbl_title)
        format_run(run2, size_pt=10.5)
        
    doc.add_page_break()
    
    # ------------------ CHAPTERS SECTION (Arabic Numerals starting at 1) ------------------
    s_ch = doc.add_section(docx.enum.section.WD_SECTION.NEW_PAGE)
    s_ch.different_first_page_header_footer = False
    s_ch.footer.is_linked_to_previous = False
    
    p_ch_foot = s_ch.footer.paragraphs[0]
    p_ch_foot.text = f"{report_meta.FOOTER_TEXT}\t\t"
    run_pg_ch = p_ch_foot.add_run()
    add_page_number_field(run_pg_ch)
    
    pgNumType_ch = OxmlElement('w:pgNumType')
    pgNumType_ch.set(qn('w:fmt'), 'decimal')
    pgNumType_ch.set(qn('w:start'), '1')
    s_ch._sectPr.append(pgNumType_ch)
    
    # CHAPTER 1: INTRODUCTION
    print("Writing Chapter 1: Introduction...")
    add_chapter_header(doc, content_ch1.CH1_TITLE[0], content_ch1.CH1_TITLE[1])
    render_section_content(doc, content_ch1.CH1_SECTIONS)
    doc.add_page_break()
    
    # CHAPTER 2: LITERATURE SURVEY
    print("Writing Chapter 2: Literature Survey...")
    add_chapter_header(doc, content_ch2.CH2_TITLE[0], content_ch2.CH2_TITLE[1])
    render_section_content(doc, content_ch2.CH2_SECTIONS)
    doc.add_page_break()
    
    # CHAPTER 3: SOFTWARE REQUIREMENTS SPECIFICATION
    print("Writing Chapter 3: Software Requirements Specification...")
    add_chapter_header(doc, content_ch3.CH3_TITLE[0], content_ch3.CH3_TITLE[1])
    render_section_content(doc, content_ch3.CH3_SECTIONS)
    doc.add_page_break()
    
    # CHAPTER 4: SYSTEM DESIGN
    print("Writing Chapter 4: System Design...")
    add_chapter_header(doc, content_ch4.CH4_TITLE[0], content_ch4.CH4_TITLE[1])
    render_section_content(doc, content_ch4.CH4_SECTIONS)
    doc.add_page_break()
    
    # CHAPTER 5: MATHEMATICAL MODEL & ALGORITHMIC MECHANICS
    print("Writing Chapter 5: Mathematical Model & Algorithmic Mechanics...")
    add_chapter_header(doc, content_ch5.CH5_TITLE[0], content_ch5.CH5_TITLE[1])
    render_section_content(doc, content_ch5.CH5_SECTIONS)
    doc.add_page_break()
    
    # CHAPTER 6: EXPECTED OUTCOMES & APPLICATIONS
    print("Writing Chapter 6: Expected Outcomes & Applications...")
    add_chapter_header(doc, content_ch6_7_8.CH6_TITLE[0], content_ch6_7_8.CH6_TITLE[1])
    render_section_content(doc, content_ch6_7_8.CH6_SECTIONS)
    doc.add_page_break()
    
    # CHAPTER 7: CONCLUSION & FUTURE SCOPE
    print("Writing Chapter 7: Conclusion & Future Scope...")
    add_chapter_header(doc, content_ch6_7_8.CH7_TITLE[0], content_ch6_7_8.CH7_TITLE[1])
    render_section_content(doc, content_ch6_7_8.CH7_SECTIONS)
    doc.add_page_break()
    
    # CHAPTER 8: REFERENCES
    print("Writing Chapter 8: References...")
    add_chapter_header(doc, content_ch6_7_8.CH8_TITLE[0], content_ch6_7_8.CH8_TITLE[1])
    for ref in content_ch6_7_8.REFERENCES_LIST:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.2
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.first_line_indent = Inches(-0.4)
        run = p.add_run(ref)
        format_run(run, size_pt=10.5)
        
    out_path = os.path.join(os.getcwd(), "Adaptive_MultiAgent_GraphRAG_Project_Report_Stage1.docx")
    print(f"Saving compiled document to: {out_path}")
    doc.save(out_path)
    print("Report generation successfully completed!")
    return out_path

if __name__ == "__main__":
    generate_report()
