# content_frontmatter.py
# Contains front matter content and formatting instructions

COVER_PAGE_DATA = {
    "report_title": "AN ADAPTIVE MULTI-AGENT GRAPHRAG FRAMEWORK FOR CONTEXTUAL HALLUCINATION MITIGATION USING AUTOMATED POLICY SWITCHING AND SELF-CORRECTION LOOPS",
    "submission_statement": "SUBMITTED TO THE SAVITRIBAI PHULE PUNE UNIVERSITY, PUNE\nIN PARTIAL FULFILLMENT OF THE REQUIREMENTS\nFOR THE AWARD OF THE DEGREE OF\nBACHELOR OF ENGINEERING\n(COMPUTER ENGINEERING)",
    "students": [
        ("Student Name: Aryan Yadav", "Exam No: 112023204"),
        ("Student Name: Ashirwad Sharma", "Exam No: 112023220"),
        ("Student Name: Hari Darade", "Exam No: 112023168"),
        ("Student Name: Gaurav Malviya", "Exam No: 112023")
    ],
    "guide": "Dr. Ankita V. Karale",
    "department": "DEPARTMENT OF COMPUTER ENGINEERING",
    "college": "Sandip Institute of Technology and Research Centre, Nashik",
    "location": "Nashik - 422213",
    "university": "SAVITRIBAI PHULE PUNE UNIVERSITY",
    "academic_year": "2026 – 2027"
}

CERTIFICATE_DATA = {
    "title": "AN ADAPTIVE MULTI-AGENT GRAPHRAG FRAMEWORK FOR CONTEXTUAL HALLUCINATION MITIGATION USING AUTOMATED POLICY SWITCHING AND SELF-CORRECTION LOOPS",
    "students": [
        ("Student Name: Aryan Yadav", "Exam No: 112023204"),
        ("Student Name: Ashirwad Sharma", "Exam No: 112023220"),
        ("Student Name: Hari Darade", "Exam No: 112023168"),
        ("Student Name: Gaurav Malviya", "Exam No: 112023")
    ],
    "guide_text": "are bonafide students of this institute and the work has been carried out by them under the supervision of Dr. Ankita V. Karale. It is approved for the partial fulfillment of the requirement of Savitribai Phule Pune University, for the award of the degree of Bachelor of Engineering (Computer Engineering).",
    "guide_name": "Dr. Ankita V. Karale",
    "guide_designation": "Guide & Head\nDepartment of Computer Engineering",
    "principal_name": "Dr. Amol D. Potgantwar",
    "principal_designation": "Principal\nSandip Institute of Technology and Research Centre",
    "external_designation": "Project External",
    "college_full": "DEPARTMENT OF COMPUTER ENGINEERING\nSandip Institute of Technology and Research Centre, Nashik\nNashik - 422213",
    "university_year": "SAVITRIBAI PHULE PUNE UNIVERSITY\n2026 – 2027"
}

ACKNOWLEDGEMENT_TEXT = """It gives us immense pleasure to present this preliminary Stage 1 project report titled "AN ADAPTIVE MULTI-AGENT GRAPHRAG FRAMEWORK FOR CONTEXTUAL HALLUCINATION MITIGATION USING AUTOMATED POLICY SWITCHING AND SELF-CORRECTION LOOPS." We take this opportunity to express our profound gratitude to our project guide and Head of the Department, Dr. Ankita V. Karale, for her invaluable guidance, insightful technical recommendations, continuous encouragement, and intellectual leadership throughout the conceptualization and formulation of this project. Her extensive expertise in artificial intelligence, clinical decision support architectures, and machine learning systems has been instrumental in shaping our research vision and establishing rigorous academic standards.

We are deeply grateful to Dr. Amol D. Potgantwar, Principal of Sandip Institute of Technology and Research Centre, Nashik, for providing world-class infrastructure, access to advanced high-performance computational facilities, and an institutional environment that actively fosters cutting-edge innovation and academic inquiry. 

We extend our sincere thanks to Prof. Anmol Budhewar, Project Coordinator, Department of Computer Engineering, for his structured coordination, meticulous timeline reviews, and persistent encouragement. We also express our appreciation to all the faculty members, technical laboratory assistants, and administrative staff of the Department of Computer Engineering for their cooperative assistance throughout this academic phase.

Finally, we express our heartfelt appreciation to our parents, family members, and peers for their continuous moral support, patience, and unwavering belief in our endeavors.

Project Group Members:
Aryan Yadav (Exam No: 112023204)
Ashirwad Sharma (Exam No: 112023220)
Hari Darade (Exam No: 112023168)
Gaurav Malviya (Exam No: 112023)
Department of Computer Engineering,
Sandip Institute of Technology and Research Centre, Nashik"""

ABSTRACT_TEXT = """Large Language Models (LLMs) have emerged as pivotal engines for enterprise automation, analytical reasoning, and synthesized intelligence across mission-critical domains including clinical decision support, regulatory compliance, and statutory legal auditing. However, the stochastic nature of auto-regressive generation exposes these models to factual hallucinations—generating plausible yet ungrounded and logically corrupt claims—which poses severe operational and legal risks in regulated environments. Retrieval-Augmented Generation (RAG) seeks to anchor model responses in verifiable external knowledge bases. Nonetheless, conventional vector-based RAG architectures exhibit fundamental failure modes: dense semantic embeddings operate within unlinked geometric latent spaces, suffering from semantic dilution, chunk fragmentation, and an inherent inability to execute multi-hop relational reasoning across dispersed documents.

To overcome the relational blindness of latent vector embeddings, recent research has explored Knowledge Graph-Augmented RAG (GraphRAG) and Agentic RAG. However, current deployments deploy these paradigms in isolation, exposing fatal limitations: standard GraphRAG introduces heavy computational overhead for simple queries and remains vulnerable to LLM extraction noise and temporal invalidation, while agentic self-reflection frameworks succumb to the "Self-Correction Paradox" wherein an LLM cannot reliably identify its own logical or factual reasoning errors without deterministic extrinsic feedback.

This report presents Stage 1 of the design and implementation of an Adaptive Multi-Agent GraphRAG Framework for Contextual Hallucination Mitigation Using Automated Policy Switching and Self-Correction Loops. The framework is architected upon a deterministic LangGraph state machine orchestrating specialized autonomous agents over a hybrid dual-backend knowledge repository (ChromaDB vector store and Neo4j property knowledge graph). A dynamic Query Complexity and Topology Routing Model evaluates semantic embedding vectors, entity depth, and subgraph density to dynamically route sub-queries to vector, graph, or hybrid modalities, optimizing computational cost. A continuous Temporal Decay Graph Pruning Model mitigates extraction noise by exponentially down-weighting stale factual edges. Crucially, the framework resolves the self-correction paradox by instituting an Extrinsic Verifier Agent that computes a composite factual verification score incorporating RAGAS faithfulness, FActScore atomic claim precision, and temporal validity. Failed verification triggers bounded reflection loops with negative feedback constraints, terminating deterministically to satisfy enterprise Service Level Agreements. This document establishes the Software Requirements Specification (SRS), formal mathematical models, multi-agent system design, and algorithmic execution mechanics for the system.

Keywords: Retrieval-Augmented Generation (RAG), GraphRAG, Multi-Agent Systems, Knowledge Graphs, Hallucination Mitigation, Self-Correction Paradox, Automated Policy Switching, LangGraph, Extrinsic Verification."""

print("Front matter content prepared successfully.")
