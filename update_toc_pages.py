# update_toc_pages.py
with open("generate_final_report_docx.py", "r", encoding="utf-8") as f:
    text = f.read()

new_toc_items = """    toc_items = [
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
    ]"""

start_str = "    toc_items = ["
start_idx = text.find(start_str)
end_str = "    toc_tbl = doc.add_table(rows=len(toc_items), cols=2)"
end_idx = text.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + new_toc_items + "\n\n" + text[end_idx:]
    with open("generate_final_report_docx.py", "w", encoding="utf-8") as f:
        f.write(new_text)
    print("SUCCESS: Updated Table of Contents with exact page numbers!")
else:
    print("ERROR: TOC block not found.")
