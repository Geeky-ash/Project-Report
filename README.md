# AN ADAPTIVE MULTI-AGENT GRAPHRAG FRAMEWORK FOR CONTEXTUAL HALLUCINATION MITIGATION USING AUTOMATED POLICY SWITCHING AND SELF-CORRECTION LOOPS

**Bachelor of Engineering (Stage 1) Project Report (2026-2027)**  
*Department of Computer Engineering, Sandip Institute of Technology and Research Centre (SITRC), Nashik*  
*Affiliated to Savitribai Phule Pune University (SPPU), Pune*

---

## 👥 Project Team
- **Aryan Yadav** (Roll No: 112023204)
- **Ashirwad Sharma** (Roll No: 112023207)
- **Hari Darade** (Roll No: 112023214)
- **Gaurav Malviya** (Roll No: 112023220)

### 🎓 Project Guide
- **Dr. Ankita V. Karale** (Associate Professor, Department of Computer Engineering, SITRC)

---

## 📌 Abstract
Large Language Models (LLMs) deployed in mission-critical domains (healthcare, legal informatics, regulatory compliance) face severe reliability bottlenecks due to contextual and factuality hallucinations. Existing Retrieval-Augmented Generation (RAG) paradigms either suffer from context dilution and vector similarity blindness (Dense Vector RAG) or incur prohibitive computational latency and graph extraction noise (GraphRAG).

This project presents an **Adaptive Multi-Agent GraphRAG Framework** that bridges structural topology and dense semantics:
1. **Dynamic Complexity Policy Switching ($C(Q)$)**: Categorizes incoming user queries and dynamically dispatches retrieval across ChromaDB (dense vector ANN) and Neo4j (property knowledge graph).
2. **Temporal Edge Decay Pruning**: Incorporates half-life temporal confidence weights $w(e, t_0)$ on knowledge graph edges to prevent historical fact hallucination.
3. **LangGraph Stateful Orchestration**: Implements finite DAG execution with bounded self-correction loops ($N_{max} \le 3$) to eliminate unbounded agent execution latency.
4. **Extrinsic Programmatic Verification**: Utilizes non-parametric, programmatic gating using RAGAS Faithfulness and FActScore atomic fact decomposition before response emission.

---

## 📊 Publication-Quality Architecture & System Diagrams
All 15 system models are located in [`figures/`](./figures) rendered at 300 DPI:
- **Figure 1.1**: Taxonomy of LLM Hallucinations and Grounding Mechanisms in Regulated Deployments
- **Figure 2.1**: Evolutionary Progression of Retrieval-Augmented Generation Paradigms (2020–2025)
- **Figure 2.2**: Multi-Agent GraphRAG Workflow with Integrated Verification and Reflection Loop
- **Figure 2.3**: Research Gap to Proposed Framework Solution Mapping Matrix
- **Figure 4.1**: Multi-Agent Adaptive GraphRAG 4-Tier Architectural Blueprint
- **Figure 4.2**: DFD Level 0 Context Flow Model
- **Figure 4.3**: DFD Level 1 Functional Data Flow Decomposition
- **Figure 4.4**: DFD Level 2 Modality Routing and Verification Sub-Decompositions
- **Figure 4.5**: Entity-Relationship Diagram (ERD) with Primary/Foreign Keys and Cardinalities
- **Figure 4.6**: UML Use Case Behavioral Interaction Model
- **Figure 4.7**: UML Class Diagram with Attribute Types and Operation Signatures
- **Figure 4.8**: UML Activity Workflow Diagram with Decision Diamond Branching
- **Figure 4.9**: UML Sequence Diagram for Distributed Async Token-Streaming Invocations
- **Figure 4.10**: UML Component Deployment Blueprint with Port Mapping
- **Figure 5.1**: LangGraph Stateful Execution Graph with Cyclic Reflection Fallback

---

## 📁 Repository Structure
```
├── Adaptive_MultiAgent_GraphRAG_Project_Report_Stage1.docx  # Full 59-page SPPU Stage 1 Report
├── figures/                                                 # 15 high-res publication figures (300 DPI)
├── generate_all_diagrams.py                                 # Automated figure generator
├── generate_final_report_docx.py                            # Report builder & DOCX compiler
├── content_frontmatter.py                                   # Cover, Certificate, Abstract, TOC
├── content_ch1.py                                           # Chapter 1: Introduction
├── content_ch2.py                                           # Chapter 2: Literature Survey
├── content_ch3.py                                           # Chapter 3: Software Requirements Specification
├── content_ch4.py                                           # Chapter 4: System Design
├── content_ch5.py                                           # Chapter 5: Mathematical Model & Algorithms
├── content_ch6_7_8.py                                       # Chapters 6, 7 & 8: Outcomes, Conclusion, References
├── report_helpers.py                                        # DOCX styling and XML utilities
├── report_meta.py                                           # Project metadata definitions
└── README.md                                                # Project documentation
```

---

## 🚀 Re-compiling the Report & Regenerating Figures
To regenerate all figures:
```bash
python generate_all_diagrams.py
```

To recompile the full 59-page Microsoft Word project report:
```bash
python generate_final_report_docx.py
```
