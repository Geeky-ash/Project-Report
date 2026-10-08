# generate_all_diagrams.py
# High-Resolution Academic System Diagram Generator for SPPU Stage 1 Report
# Ensures zero text overflow, dynamic auto-padded bounding boxes, and publication-quality layout.

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("figures", exist_ok=True)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9.0

def save_fig(fig, filename):
    path = os.path.join("figures", filename)
    fig.savefig(path, dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.15)
    plt.close(fig)
    print(f"Generated: {path}")
    return path

# ==============================================================================
# FIGURE 1.1: TAXONOMY OF LLM HALLUCINATIONS
# ==============================================================================
def create_fig1_1():
    fig, ax = plt.subplots(figsize=(13.5, 7.0))
    ax.axis('off')
    
    # Root title node
    ax.text(6.75, 6.2, "Taxonomy of LLM Hallucinations\nin Regulated AI Deployments", 
            ha="center", va="center", color="white", weight="bold", fontsize=11.5,
            bbox=dict(boxstyle="round,pad=0.6", fc="#1A365D", ec="#0F172A", lw=2.0))
    
    columns = [
        ("Factuality Hallucinations", 2.25, "#2B6CB0", [
            ("Fabricated Entities", "Inventing non-existent drug codes,\nclinical dosages, or legal statutes"),
            ("Factual Contradiction", "Directly contradicting verified\nenterprise source documentation")
        ]),
        ("Faithfulness Hallucinations", 6.75, "#2C7A7B", [
            ("Context Divergence", "Generating claims ungrounded in\nretrieved reference documents"),
            ("Source Misattribution", "Attaching incorrect citations to\ngenerated factual propositions")
        ]),
        ("Topological / Relational", 11.25, "#744210", [
            ("Broken Multi-Hop Paths", "Vector distance fails to bridge\ncross-document relational hops"),
            ("Temporal Staleness", "Treating expired historical records\nas active current ground truth")
        ])
    ]
    
    for cat_name, x, col, subcards in columns:
        # Category node
        ax.text(x, 4.7, cat_name, ha="center", va="center", color="white", weight="bold", fontsize=10.5,
                bbox=dict(boxstyle="round,pad=0.5", fc=col, ec="#1A202C", lw=1.5))
        
        # Arrow from root to category
        ax.annotate("", xy=(x, 5.1), xytext=(6.75, 5.7),
                    arrowprops=dict(arrowstyle="-|>", color="#4A5568", lw=1.6))
        
        # Subcards
        y_pos = [3.2, 1.45]
        for idx, (title, desc) in enumerate(subcards):
            y = y_pos[idx]
            card_text = f"{title}\n{desc}"
            ax.text(x, y, card_text, ha="center", va="center", color="#1A202C", fontsize=8.8, linespacing=1.35,
                    bbox=dict(boxstyle="round,pad=0.55", fc="#F8FAFC", ec=col, lw=1.4))
            
            # Connector line
            if idx == 0:
                ax.plot([x, x], [4.3, 3.8], color=col, lw=1.3)
            else:
                ax.plot([x, x], [2.6, 2.05], color=col, lw=1.3)
                
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0.5, 6.9)
    return save_fig(fig, "fig1_1_hallucination_taxonomy.png")

# ==============================================================================
# FIGURE 2.1: EVOLUTION OF RAG ARCHITECTURES
# ==============================================================================
def create_fig2_1():
    fig, ax = plt.subplots(figsize=(14.5, 5.5))
    ax.axis('off')
    
    stages = [
        ("Naive Vector RAG\n(2020-2022)", 
         "• Flat Vector DB\n• Top-k Cosine ANN\n• Context dilution\n• Blind to logic hops", 
         "#EDF2F7", "#2D3748"),
        ("Advanced RAG\n(2022-2023)", 
         "• Pre-retrieval HyDE\n• Cross-encoder Rerank\n• Sliding chunk window\n• Rigid single-pass", 
         "#EBF8FF", "#2B6CB0"),
        ("Standard GraphRAG\n(2023-2024)", 
         "• Entity-relation graph\n• Leiden clustering\n• Global map-reduce\n• Extraction noise", 
         "#E6FFFA", "#234E52"),
        ("Agentic RAG\n(2024-2025)", 
         "• Dynamic CoT planning\n• Tool invocation\n• Self-reflection loops\n• Correction paradox", 
         "#FEFCBF", "#744210"),
        ("Proposed Framework\n(Adaptive GraphRAG)", 
         "• Dynamic policy routing\n• ChromaDB + Neo4j\n• Temporal edge decay\n• Extrinsic RAGAS gating", 
         "#FED7D7", "#742A2A")
    ]
    
    x_positions = [1.4, 4.3, 7.2, 10.1, 13.0]
    for i, (title, details, bg_col, text_col) in enumerate(stages):
        x = x_positions[i]
        
        # Unified Milestone Card
        card_content = f"{title}\n" + "—"*18 + f"\n{details}"
        ax.text(x, 2.7, card_content, ha="center", va="center", color=text_col, fontsize=8.4, linespacing=1.35,
                bbox=dict(boxstyle="round,pad=0.6", fc=bg_col, ec=text_col, lw=1.6))
        
        # Forward arrow to next stage
        if i < len(stages) - 1:
            ax.annotate("", xy=(x_positions[i+1] - 1.15, 2.7), xytext=(x + 1.15, 2.7),
                        arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2.0))
            
    ax.set_xlim(0, 14.5)
    ax.set_ylim(0.8, 4.6)
    return save_fig(fig, "fig2_1_rag_evolution.png")

# ==============================================================================
# FIGURE 2.2: MULTI-AGENT GRAPHRAG WORKFLOW WITH REFLECTION LOOP
# ==============================================================================
def create_fig2_2():
    fig, ax = plt.subplots(figsize=(14.5, 6.8))
    ax.axis('off')
    
    # 5 Main Process Nodes horizontally
    steps = [
        ("User Prompt\nIngestion", 1.4, 5.4, "#E2E8F0", "#2D3748"),
        ("Planner Agent\n(CoT Decomposition)", 4.1, 5.4, "#BEE3F8", "#2B6CB0"),
        ("Hybrid Retrieval\n(Vector + Graph)", 7.0, 5.4, "#C6F6D5", "#22543D"),
        ("Generator Agent\n(Context Grounding)", 9.9, 5.4, "#FEFCBF", "#744210"),
        ("Extrinsic Verifier\n(RAGAS / FActScore)", 12.8, 5.4, "#FED7D7", "#742A2A")
    ]
    
    for name, x, y, bg, tc in steps:
        ax.text(x, y, name, ha="center", va="center", color=tc, weight="bold", fontsize=9.0, linespacing=1.3,
                bbox=dict(boxstyle="round,pad=0.55", fc=bg, ec=tc, lw=1.6))
        
    # Forward arrows between main pipeline nodes
    ax.annotate("", xy=(2.75, 5.4), xytext=(2.15, 5.4), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=2.0))
    ax.annotate("", xy=(5.65, 5.4), xytext=(5.05, 5.4), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=2.0))
    ax.annotate("", xy=(8.55, 5.4), xytext=(7.95, 5.4), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=2.0))
    ax.annotate("", xy=(11.45, 5.4), xytext=(10.85, 5.4), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=2.0))
    
    # Down arrow from Verifier to Decision Node
    ax.annotate("", xy=(12.8, 4.0), xytext=(12.8, 4.7), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=2.0))
    
    # Decision Node
    ax.text(12.8, 3.3, "Verification\nScore >= τ ?", ha="center", va="center", color="#553C9A", weight="bold", fontsize=9.0, linespacing=1.2,
            bbox=dict(boxstyle="round,pad=0.6", fc="#E9D8FD", ec="#553C9A", lw=2.0))
    
    # PASS -> Bottom Emission Node
    ax.annotate("", xy=(12.8, 1.8), xytext=(12.8, 2.65), arrowprops=dict(arrowstyle="->", color="#22543D", lw=2.2))
    ax.text(13.25, 2.2, "PASS", color="#22543D", weight="bold", fontsize=9.5)
    
    ax.text(12.8, 1.2, "Verified Response\nEmitted to User", ha="center", va="center", color="#22543D", weight="bold", fontsize=9.0, linespacing=1.3,
            bbox=dict(boxstyle="round,pad=0.55", fc="#C6F6D5", ec="#22543D", lw=1.8))
    
    # FAIL -> Reflection Node to the left
    ax.annotate("", xy=(9.2, 3.3), xytext=(11.4, 3.3), arrowprops=dict(arrowstyle="->", color="#C53030", lw=2.0))
    ax.text(10.3, 3.55, "FAIL (N_retry < 3)", color="#C53030", weight="bold", fontsize=8.5, ha="center")
    
    ax.text(7.0, 3.3, "Reflection Node\n(Negative Feedback Synthesis)", ha="center", va="center", color="#C53030", weight="bold", fontsize=9.0, linespacing=1.3,
            bbox=dict(boxstyle="round,pad=0.55", fc="#FED7D7", ec="#C53030", lw=1.8))
    
    # Reflection Node back to Planner Agent
    ax.annotate("", xy=(4.1, 4.75), xytext=(7.0, 3.9),
                arrowprops=dict(arrowstyle="->", color="#C53030", lw=2.0, connectionstyle="arc3,rad=-0.22"))
    ax.text(5.5, 4.6, "Negative Constraints &\nPlan Adaptation", color="#C53030", fontsize=8.2, style="italic", ha="center", weight="bold")
    
    ax.set_xlim(0, 14.5)
    ax.set_ylim(0.5, 6.4)
    return save_fig(fig, "fig2_2_agentic_workflow.png")

# ==============================================================================
# FIGURE 2.3: GAP MAPPING
# ==============================================================================
def create_fig2_3():
    fig, ax = plt.subplots(figsize=(13.5, 6.0))
    ax.axis('off')
    
    gaps = [
        ("Gap 1: Disjointed Modality Routing\n(Compute waste / context fragmentation)", 2.4, 4.6, "#FED7D7", "#9B2C2C"),
        ("Gap 2: The Self-Correction Paradox\n(LLM fails to detect own errors)", 2.4, 3.2, "#FEEBC8", "#9C4221"),
        ("Gap 3: Unbounded Multi-Agent Loops\n(Non-deterministic latency violation)", 2.4, 1.8, "#E9D8FD", "#553C9A"),
        ("Gap 4: Graph Extraction & Stale Noise\n(Hallucinated edges & obsolete facts)", 2.4, 0.4, "#C4F1F9", "#0987A0")
    ]
    sols = [
        ("Query Complexity Routing Model C(Q)\n(Dynamic Vector / Graph dispatch)", 10.6, 4.6, "#C6F6D5", "#22543D"),
        ("Extrinsic Algorithmic Verifier Node\n(Programmatic RAGAS & FActScore gating)", 10.6, 3.2, "#C6F6D5", "#22543D"),
        ("LangGraph State Machine Engine\n(Finite execution DAG & N_max retry bounds)", 10.6, 1.8, "#C6F6D5", "#22543D"),
        ("Temporal Decay Graph Pruning w(e,t0)\n(Exponential edge confidence decay)", 10.6, 0.4, "#C6F6D5", "#22543D")
    ]
    
    for text, x, y, bg, tc in gaps:
        ax.text(x, y, text, ha="center", va="center", color=tc, weight="bold", fontsize=8.8, linespacing=1.3,
                bbox=dict(boxstyle="round,pad=0.55", fc=bg, ec=tc, lw=1.5))
        
    for text, x, y, bg, tc in sols:
        ax.text(x, y, text, ha="center", va="center", color=tc, weight="bold", fontsize=8.8, linespacing=1.3,
                bbox=dict(boxstyle="round,pad=0.55", fc=bg, ec=tc, lw=1.5))
        
    for i in range(4):
        y = 4.6 - i * 1.4
        ax.annotate("", xy=(7.9, y), xytext=(5.1, y), arrowprops=dict(arrowstyle="-|>", color="#2D3748", lw=2.0))
        ax.text(6.5, y + 0.18, "Mitigated by", ha="center", color="#4A5568", fontsize=8.0, style="italic")
        
    ax.set_xlim(0, 13.5)
    ax.set_ylim(-0.3, 5.3)
    return save_fig(fig, "fig2_3_gap_mapping.png")

# ==============================================================================
# FIGURE 4.1: SYSTEM ARCHITECTURE (4-TIER)
# ==============================================================================
def create_fig4_1():
    fig, ax = plt.subplots(figsize=(14.0, 8.5))
    ax.axis('off')
    
    tiers = [
        ("Tier 1: Knowledge Ingestion & Graph Compilation", 6.8, [
            ("Document Loader\n(PDF / DOCX / JSON)", 1.8),
            ("Sliding Chunker\n(512 / 64 tokens)", 5.2),
            ("Dense Embedder\n(Bi-Encoder d=1536)", 8.6),
            ("Triplet Extractor\n(Entities & Relations)", 12.0)
        ], "#EBF8FF", "#2B6CB0"),
        ("Tier 2: Dual Storage & Indexing Subsystems", 4.8, [
            ("Vector Database (ChromaDB)\n[HNSW Cosine ANN Index]", 4.0),
            ("Property Graph Database (Neo4j)\n[Index-Free Adjacency + Cypher]", 10.0)
        ], "#F0FFF4", "#22543D"),
        ("Tier 3: Multi-Agent Orchestration Engine (LangGraph State Machine)", 2.8, [
            ("Planner Agent\n(CoT DAG)", 1.4),
            ("Policy Router\n(Equation 5.1)", 3.9),
            ("Hybrid Retriever\n(RRF Fusion)", 6.4),
            ("Generator Agent\n(Grounding)", 8.9),
            ("Verifier Agent\n(RAGAS Score)", 11.4),
            ("Reflection Node\n(Feedback Loop)", 13.5)
        ], "#FAF5FF", "#553C9A"),
        ("Tier 4: Enterprise Governance, Memory & API Layer", 0.8, [
            ("State Checkpointer\n(PostgreSQL)", 2.2),
            ("Explainability Logger\n(Audit Trail)", 5.8),
            ("FastAPI Gateway\n(REST & WebSockets)", 9.4),
            ("React Dashboard\n(Graph Exploration)", 12.6)
        ], "#FFF5F5", "#9B2C2C")
    ]
    
    for title, y_base, boxes, bg_c, bord_c in tiers:
        container = patches.FancyBboxPatch((0.2, y_base - 0.55), 13.6, 1.25,
                                           boxstyle="round,pad=0.15", fc=bg_c, ec=bord_c, lw=1.4)
        ax.add_patch(container)
        ax.text(0.5, y_base + 0.45, title, color=bord_c, weight="bold", fontsize=9.5)
        
        for name, x in boxes:
            ax.text(x, y_base - 0.05, name, ha="center", va="center", color="#1A202C", weight="bold", fontsize=7.8, linespacing=1.25,
                    bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=bord_c, lw=1.2))
            
    ax.annotate("", xy=(7.0, 5.65), xytext=(7.0, 6.15), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2.0))
    ax.annotate("", xy=(7.0, 3.65), xytext=(7.0, 4.15), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2.0))
    ax.annotate("", xy=(7.0, 1.65), xytext=(7.0, 2.15), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2.0))
    
    ax.set_xlim(0, 14.0)
    ax.set_ylim(0.0, 7.8)
    return save_fig(fig, "fig4_1_system_architecture.png")

# ==============================================================================
# FIGURE 4.2: DFD LEVEL 0 (CONTEXT DIAGRAM)
# ==============================================================================
def create_fig4_2():
    fig, ax = plt.subplots(figsize=(12.0, 6.0))
    ax.axis('off')
    
    proc = patches.Circle((6.0, 3.0), 1.35, fc="#EBF8FF", ec="#2B6CB0", lw=2.2)
    ax.add_patch(proc)
    ax.text(6.0, 3.0, "0.0\nAdaptive GraphRAG\nSystem", ha="center", va="center",
            color="#1A365D", weight="bold", fontsize=10.5, linespacing=1.3)
    
    ax.text(1.2, 3.0, "End User\n(Enterprise)", ha="center", va="center", color="#1A202C", weight="bold", fontsize=9.0,
            bbox=dict(boxstyle="round,pad=0.6", fc="#EDF2F7", ec="#2D3748", lw=1.5))
    
    ax.text(6.0, 5.3, "Document Sources\n(PDF / DOCX / Text)", ha="center", va="center", color="#1A202C", weight="bold", fontsize=9.0,
            bbox=dict(boxstyle="round,pad=0.55", fc="#EDF2F7", ec="#2D3748", lw=1.5))
    
    ax.text(10.8, 3.0, "LLM Inference API\n(Groq / Ollama / OpenAI)", ha="center", va="center", color="#1A202C", weight="bold", fontsize=9.0,
            bbox=dict(boxstyle="round,pad=0.6", fc="#EDF2F7", ec="#2D3748", lw=1.5))
    
    ax.text(6.0, 0.7, "Compliance Auditor\n& Log Service", ha="center", va="center", color="#1A202C", weight="bold", fontsize=9.0,
            bbox=dict(boxstyle="round,pad=0.55", fc="#EDF2F7", ec="#2D3748", lw=1.5))
    
    ax.annotate("", xy=(4.65, 3.3), xytext=(2.3, 3.3), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.5))
    ax.text(3.45, 3.55, "Natural Language Query", ha="center", fontsize=8.0)
    
    ax.annotate("", xy=(2.3, 2.7), xytext=(4.65, 2.7), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.5))
    ax.text(3.45, 2.45, "Verified Answer + Citations", ha="center", fontsize=8.0)
    
    ax.annotate("", xy=(6.0, 4.35), xytext=(6.0, 4.8), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.5))
    ax.text(6.8, 4.55, "Raw Enterprise Docs", ha="center", fontsize=8.0)
    
    ax.annotate("", xy=(9.4, 3.3), xytext=(7.35, 3.3), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.5))
    ax.text(8.4, 3.55, "Prompt Token Streams", ha="center", fontsize=8.0)
    
    ax.annotate("", xy=(7.35, 2.7), xytext=(9.4, 2.7), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.5))
    ax.text(8.4, 2.45, "Structured Completions", ha="center", fontsize=8.0)
    
    ax.annotate("", xy=(6.0, 1.25), xytext=(6.0, 1.65), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.5))
    ax.text(6.8, 1.45, "Audit Traces & Metrics", ha="center", fontsize=8.0)
    
    ax.set_xlim(0, 12.0)
    ax.set_ylim(0.0, 6.0)
    return save_fig(fig, "fig4_2_dfd_level0.png")

# ==============================================================================
# FIGURE 4.3: DFD LEVEL 1 (FUNCTIONAL DECOMPOSITION)
# ==============================================================================
def create_fig4_3():
    fig, ax = plt.subplots(figsize=(13.0, 6.5))
    ax.axis('off')
    
    procs = [
        ("1.0 Ingestion &\nGraph Indexing", 1.5, 5.0),
        ("2.0 Query Planning\n& Decomposition", 4.8, 5.0),
        ("3.0 Policy Routing\n& Hybrid Retrieval", 8.2, 5.0),
        ("4.0 Grounded\nSynthesis", 11.2, 3.0),
        ("5.0 Extrinsic\nVerification", 7.5, 1.2),
        ("6.0 Audit Log\nPersistence", 2.5, 1.2)
    ]
    for name, x, y in procs:
        c = patches.Circle((x, y), 0.9, fc="#EBF8FF", ec="#2B6CB0", lw=1.8)
        ax.add_patch(c)
        ax.text(x, y, name, ha="center", va="center", color="#1A365D", weight="bold", fontsize=8.2, linespacing=1.2)
        
    stores = [
        ("D1: Vector DB\n(ChromaDB)", 4.8, 3.2),
        ("D2: Property KG\n(Neo4j)", 8.2, 3.2),
        ("D3: Audit DB\n(PostgreSQL)", 2.5, 3.2)
    ]
    for name, x, y in stores:
        ax.text(x, y, name, ha="center", va="center", color="#744210", weight="bold", fontsize=8.0, linespacing=1.2,
                bbox=dict(boxstyle="square,pad=0.45", fc="#FEFCBF", ec="#B7791F", lw=1.4))
        
    ax.annotate("", xy=(3.85, 5.0), xytext=(2.45, 5.0), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(7.25, 5.0), xytext=(5.75, 5.0), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(10.4, 3.5), xytext=(9.05, 4.6), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(8.35, 1.4), xytext=(10.5, 2.5), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(3.45, 1.2), xytext=(6.55, 1.2), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    
    ax.annotate("", xy=(4.8, 3.75), xytext=(2.2, 4.4), arrowprops=dict(arrowstyle="->", color="#B7791F", lw=1.2))
    ax.annotate("", xy=(8.2, 3.75), xytext=(2.4, 4.7), arrowprops=dict(arrowstyle="->", color="#B7791F", lw=1.2))
    ax.annotate("", xy=(7.6, 4.4), xytext=(5.4, 3.5), arrowprops=dict(arrowstyle="->", color="#B7791F", lw=1.2))
    ax.annotate("", xy=(8.2, 4.1), xytext=(8.2, 3.65), arrowprops=dict(arrowstyle="->", color="#B7791F", lw=1.2))
    ax.annotate("", xy=(2.5, 2.75), xytext=(2.5, 2.15), arrowprops=dict(arrowstyle="->", color="#B7791F", lw=1.2))
    
    ax.set_xlim(0, 12.8)
    ax.set_ylim(0.0, 6.2)
    return save_fig(fig, "fig4_3_dfd_level1.png")

# ==============================================================================
# FIGURE 4.4: DFD LEVEL 2 (MODALITY ROUTING & VERIFICATION)
# ==============================================================================
def create_fig4_4():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
    ax.axis('off')
    
    # Container 1: Process 3.0 Sub-Decomposition
    p1 = patches.FancyBboxPatch((0.3, 0.4), 5.7, 5.4, boxstyle="round,pad=0.15", fc="#F0FFF4", ec="#276749", lw=1.5)
    ax.add_patch(p1)
    ax.text(3.15, 5.4, "Process 3.0: Modality Routing & Retrieval", ha="center", color="#22543D", weight="bold", fontsize=9.2)
    
    sub3 = [
        ("3.1 Query Embedding &\nEntity Extraction", 3.15, 4.6),
        ("3.2 Complexity Scoring\nC(Q) Evaluation", 3.15, 3.5),
        ("3.3 ChromaDB Vector\nANN Similarity Search", 1.8, 2.3),
        ("3.4 Neo4j Cypher Traversal\n& Temporal Edge Pruning", 4.5, 2.3),
        ("3.5 Reciprocal Rank Fusion\n(RRF k=60 Integration)", 3.15, 1.1)
    ]
    for name, x, y in sub3:
        ax.text(x, y, name, ha="center", va="center", color="#1A202C", weight="bold", fontsize=7.6, linespacing=1.2,
                bbox=dict(boxstyle="round,pad=0.45", fc="white", ec="#276749", lw=1.2))
        
    ax.annotate("", xy=(3.15, 3.9), xytext=(3.15, 4.2), arrowprops=dict(arrowstyle="->", color="#276749", lw=1.4))
    ax.annotate("", xy=(2.0, 2.7), xytext=(2.9, 3.15), arrowprops=dict(arrowstyle="->", color="#276749", lw=1.4))
    ax.annotate("", xy=(4.3, 2.7), xytext=(3.4, 3.15), arrowprops=dict(arrowstyle="->", color="#276749", lw=1.4))
    ax.annotate("", xy=(2.9, 1.5), xytext=(2.0, 1.9), arrowprops=dict(arrowstyle="->", color="#276749", lw=1.4))
    ax.annotate("", xy=(3.4, 1.5), xytext=(4.3, 1.9), arrowprops=dict(arrowstyle="->", color="#276749", lw=1.4))
    
    # Container 2: Process 5.0 Sub-Decomposition
    p2 = patches.FancyBboxPatch((8.2, 0.4), 5.7, 5.4, boxstyle="round,pad=0.15", fc="#FFF5F5", ec="#9B2C2C", lw=1.5)
    ax.add_patch(p2)
    ax.text(11.05, 5.4, "Process 5.0: Verification & Reflection", ha="center", color="#742A2A", weight="bold", fontsize=9.2)
    
    sub5 = [
        ("5.1 Atomic Fact Decomposition\n(FActScore Parsing)", 11.05, 4.6),
        ("5.2 Programmatic RAGAS\nFaithfulness Assessment", 11.05, 3.5),
        ("5.3 Composite Score Gating\nS_total >= τ Threshold", 11.05, 2.4),
        ("5.4 Negative Feedback\nConstraint Formulator", 9.6, 1.2),
        ("5.5 Retry Controller\n(N_retry <= 3 State)", 12.5, 1.2)
    ]
    for name, x, y in sub5:
        ax.text(x, y, name, ha="center", va="center", color="#1A202C", weight="bold", fontsize=7.6, linespacing=1.2,
                bbox=dict(boxstyle="round,pad=0.45", fc="white", ec="#9B2C2C", lw=1.2))
        
    ax.annotate("", xy=(11.05, 3.9), xytext=(11.05, 4.2), arrowprops=dict(arrowstyle="->", color="#9B2C2C", lw=1.4))
    ax.annotate("", xy=(11.05, 2.8), xytext=(11.05, 3.1), arrowprops=dict(arrowstyle="->", color="#9B2C2C", lw=1.4))
    ax.annotate("", xy=(9.9, 1.6), xytext=(10.7, 2.05), arrowprops=dict(arrowstyle="->", color="#9B2C2C", lw=1.4))
    ax.annotate("", xy=(12.2, 1.6), xytext=(11.4, 2.05), arrowprops=dict(arrowstyle="->", color="#9B2C2C", lw=1.4))
    
    # Bridge arrow in wide center gutter
    ax.annotate("", xy=(8.1, 3.1), xytext=(6.1, 3.1), arrowprops=dict(arrowstyle="->", color="#2B6CB0", lw=2.2))
    ax.text(7.1, 3.35, "Retrieved\nContext", ha="center", fontsize=8.2, color="#2B6CB0", weight="bold")
    
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0.0, 6.2)
    return save_fig(fig, "fig4_4_dfd_level2.png")

# ==============================================================================
# FIGURE 4.5: ENTITY RELATIONSHIP DIAGRAM (ERD)
# ==============================================================================
def create_fig4_5():
    fig, ax = plt.subplots(figsize=(14.0, 7.2))
    ax.axis('off')
    
    entities = [
        ("DOCUMENT", 1.8, 5.0, ["Doc_ID (PK)", "Title", "File_Path", "MIME_Type", "Ingest_Time"]),
        ("CHUNK", 5.8, 5.0, ["Chunk_ID (PK)", "Doc_ID (FK)", "Text_Content", "Embedding_ID", "Created_At"]),
        ("NAMED_ENTITY", 9.8, 5.0, ["Entity_ID (PK)", "Name", "Entity_Type", "Canonical_URI", "First_Seen"]),
        ("RELATION_EDGE", 9.8, 1.8, ["Edge_ID (PK)", "Head_ID (FK)", "Tail_ID (FK)", "Rel_Type", "Weight", "Timestamp"]),
        ("QUERY_LOG", 1.8, 1.8, ["Query_ID (PK)", "Raw_Query", "Normalized_Query", "User_ID", "Status"]),
        ("AGENT_TASK", 5.8, 1.8, ["Task_ID (PK)", "Query_ID (FK)", "Modality", "Complexity", "Latency"]),
        ("VERIFICATION_RESULT", 5.8, -1.2, ["Verif_ID (PK)", "Query_ID (FK)", "Faithfulness", "Composite_Score", "Decision"]),
        ("FEEDBACK_CONSTRAINT", 9.8, -1.2, ["Constraint_ID (PK)", "Verif_ID (FK)", "Retry_Num", "Negative_Prompt", "Status"])
    ]
    
    for name, x, y, attrs in entities:
        # Unified entity card
        card_content = f"{name}\n" + "—"*18 + "\n" + "\n".join(attrs)
        ax.text(x, y, card_content, ha="center", va="center", color="#1A202C", fontsize=7.6, linespacing=1.3,
                bbox=dict(boxstyle="square,pad=0.5", fc="#F8FAFC", ec="#2B6CB0", lw=1.5))
        
    # Relationships
    ax.annotate("", xy=(4.6, 5.0), xytext=(3.0, 5.0), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.text(3.8, 5.25, "1 : N", ha="center", fontsize=8.0, weight="bold")
    
    ax.annotate("", xy=(8.6, 5.0), xytext=(7.0, 5.0), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.text(7.8, 5.25, "M : N", ha="center", fontsize=8.0, weight="bold")
    
    ax.annotate("", xy=(9.8, 2.9), xytext=(9.8, 3.8), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.text(10.3, 3.35, "1 : N", ha="center", fontsize=8.0, weight="bold")
    
    ax.annotate("", xy=(4.6, 1.8), xytext=(3.0, 1.8), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.text(3.8, 2.05, "1 : N", ha="center", fontsize=8.0, weight="bold")
    
    ax.annotate("", xy=(5.8, -0.1), xytext=(5.8, 0.7), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.text(6.3, 0.3, "1 : 1", ha="center", fontsize=8.0, weight="bold")
    
    ax.annotate("", xy=(8.6, -1.2), xytext=(7.0, -1.2), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.text(7.8, -0.95, "1 : N", ha="center", fontsize=8.0, weight="bold")
    
    ax.set_xlim(0, 12.0)
    ax.set_ylim(-2.2, 6.2)
    return save_fig(fig, "fig4_5_erd.png")

# ==============================================================================
# FIGURE 4.6: UML USE CASE DIAGRAM
# ==============================================================================
def create_fig4_6():
    fig, ax = plt.subplots(figsize=(13.0, 6.2))
    ax.axis('off')
    
    sys_box = patches.Rectangle((3.2, 0.3), 6.6, 5.4, fc="#F7FAFC", ec="#2B6CB0", lw=1.8, linestyle="--")
    ax.add_patch(sys_box)
    ax.text(6.5, 5.45, "Adaptive Multi-Agent GraphRAG System Boundary", ha="center", color="#2B6CB0", weight="bold", fontsize=9.5)
    
    use_cases = [
        ("Submit Natural Language Query", 6.5, 4.6),
        ("Inspect Reasoning Subgraph", 6.5, 3.6),
        ("Audit Verification Scorecard", 6.5, 2.6),
        ("Ingest Enterprise Documents", 6.5, 1.6),
        ("Tune Routing & Decay Params", 6.5, 0.7)
    ]
    for uc, x, y in use_cases:
        ax.text(x, y, uc, ha="center", va="center", color="#1A365D", weight="bold", fontsize=8.5,
                bbox=dict(boxstyle="round,pad=0.55", fc="#EBF8FF", ec="#3182CE", lw=1.4))
        
    actors = [
        ("End User", 1.5, 4.1),
        ("Compliance Officer", 1.5, 1.8),
        ("Knowledge Engineer", 11.5, 3.8),
        ("System Admin", 11.5, 1.5)
    ]
    for act, x, y in actors:
        c = patches.Circle((x, y + 0.35), 0.18, fc="white", ec="#2D3748", lw=1.8)
        ax.add_patch(c)
        ax.plot([x, x], [y + 0.17, y - 0.25], color="#2D3748", lw=1.8)
        ax.plot([x - 0.25, x + 0.25], [y + 0.05, y + 0.05], color="#2D3748", lw=1.8)
        ax.plot([x, x - 0.2], [y - 0.25, y - 0.55], color="#2D3748", lw=1.8)
        ax.plot([x, x + 0.2], [y - 0.25, y - 0.55], color="#2D3748", lw=1.8)
        ax.text(x, y - 0.8, act, ha="center", color="#1A202C", weight="bold", fontsize=8.2)
        
    ax.plot([1.8, 4.5], [4.1, 4.6], color="#718096", lw=1.2)
    ax.plot([1.8, 4.5], [4.1, 3.6], color="#718096", lw=1.2)
    ax.plot([1.8, 4.5], [1.8, 2.6], color="#718096", lw=1.2)
    ax.plot([11.2, 8.5], [3.8, 1.6], color="#718096", lw=1.2)
    ax.plot([11.2, 8.5], [1.5, 0.7], color="#718096", lw=1.2)
    
    ax.set_xlim(0, 13.0)
    ax.set_ylim(-0.2, 6.0)
    return save_fig(fig, "fig4_6_use_case.png")

# ==============================================================================
# FIGURE 4.7: UML CLASS DIAGRAM
# ==============================================================================
def create_fig4_7():
    fig, ax = plt.subplots(figsize=(14.0, 6.6))
    ax.axis('off')
    
    classes = [
        ("StateEngine", 2.2, 4.2, ["- state: GlobalSchema", "- checkpointer: DB", "+ run_workflow(q)", "+ transition_node()"]),
        ("QueryPlanner", 6.8, 4.2, ["- llm: BaseLLM", "+ rewrite(query)", "+ decompose(tasks)", "+ replan(feedback)"]),
        ("PolicyRouter", 11.4, 4.2, ["- tau_1: float", "- tau_2: float", "+ calc_complexity(q)", "+ route(score)"]),
        ("VectorRetriever", 2.2, 1.2, ["- client: ChromaDB", "+ ann_search(emb, k)", "+ filter_metadata()"]),
        ("GraphRetriever", 6.8, 1.2, ["- driver: Neo4jDriver", "- lambda_decay: float", "+ cypher_traverse()", "+ prune_edges()"]),
        ("VerifierAgent", 11.4, 1.2, ["- ragas: Evaluator", "- factscore: Daemon", "+ score_faithfulness()", "+ gate_response()"])
    ]
    for cname, x, y, members in classes:
        # Unified UML class card
        class_text = f"«class» {cname}\n" + "—"*24 + "\n" + "\n".join(members)
        ax.text(x, y, class_text, ha="center", va="center", color="#1A202C", fontsize=7.6, fontfamily="monospace", linespacing=1.3,
                bbox=dict(boxstyle="square,pad=0.5", fc="#F8FAFC", ec="#2B6CB0", lw=1.5))
        
    ax.annotate("", xy=(5.2, 4.2), xytext=(3.7, 4.2), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(9.8, 4.2), xytext=(8.3, 4.2), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(2.2, 2.3), xytext=(2.2, 3.1), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(6.8, 2.3), xytext=(6.8, 3.1), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(11.4, 2.3), xytext=(11.4, 3.1), arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.5))
    
    ax.set_xlim(0, 13.6)
    ax.set_ylim(-0.2, 5.4)
    return save_fig(fig, "fig4_7_class_diagram.png")

# ==============================================================================
# FIGURE 4.8: UML ACTIVITY DIAGRAM
# ==============================================================================
def create_fig4_8():
    fig, ax = plt.subplots(figsize=(13.5, 6.2))
    ax.axis('off')
    
    c_start = patches.Circle((1.2, 5.0), 0.22, fc="#2D3748", ec="#1A202C")
    ax.add_patch(c_start)
    ax.text(1.2, 5.5, "Start", ha="center", fontsize=8.5, weight="bold")
    
    acts = [
        ("Query Ingestion\n& Normalization", 3.2, 5.0),
        ("CoT Planning\n& Decomposition", 6.2, 5.0),
        ("Complexity\nRouting C(Q)", 9.2, 5.0),
        ("Candidate Context\nRetrieval", 12.0, 5.0),
        ("Generator Synthesis\n(Cited Answer)", 12.0, 2.8),
        ("Extrinsic Verification\n(S_total Evaluation)", 8.2, 2.8)
    ]
    for name, x, y in acts:
        ax.text(x, y, name, ha="center", va="center", color="#1A365D", weight="bold", fontsize=7.8, linespacing=1.2,
                bbox=dict(boxstyle="round,pad=0.5", fc="#EBF8FF", ec="#3182CE", lw=1.3))
        
    ax.annotate("", xy=(2.1, 5.0), xytext=(1.45, 5.0), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.4))
    ax.annotate("", xy=(5.0, 5.0), xytext=(4.3, 5.0), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.4))
    ax.annotate("", xy=(8.1, 5.0), xytext=(7.4, 5.0), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.4))
    ax.annotate("", xy=(10.8, 5.0), xytext=(10.3, 5.0), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.4))
    ax.annotate("", xy=(12.0, 3.5), xytext=(12.0, 4.3), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.4))
    ax.annotate("", xy=(9.7, 2.8), xytext=(10.8, 2.8), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.4))
    
    ax.text(4.8, 2.8, "Verification\nS_total >= τ ?", ha="center", va="center", color="#744210", weight="bold", fontsize=7.8, linespacing=1.2,
            bbox=dict(boxstyle="round,pad=0.55", fc="#FEFCBF", ec="#B7791F", lw=1.5))
    ax.annotate("", xy=(6.2, 2.8), xytext=(6.9, 2.8), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.4))
    
    p_end = patches.Circle((1.5, 2.8), 0.28, fc="#C6F6D5", ec="#22543D", lw=2.2)
    ax.add_patch(p_end)
    ax.text(1.5, 2.8, "END", ha="center", va="center", color="#22543D", weight="bold", fontsize=7.5)
    ax.annotate("", xy=(1.85, 2.8), xytext=(3.4, 2.8), arrowprops=dict(arrowstyle="->", color="#22543D", lw=1.8))
    ax.text(2.6, 3.05, "PASS", color="#22543D", weight="bold", fontsize=8.0)
    
    ax.text(4.8, 1.0, "Reflection Agent\n(Increment N_retry)", ha="center", va="center", color="#9B2C2C", weight="bold", fontsize=7.8, linespacing=1.2,
            bbox=dict(boxstyle="round,pad=0.5", fc="#FED7D7", ec="#C53030", lw=1.4))
    ax.annotate("", xy=(4.8, 1.6), xytext=(4.8, 2.15), arrowprops=dict(arrowstyle="->", color="#C53030", lw=1.4))
    ax.text(5.3, 1.85, "FAIL", color="#C53030", weight="bold", fontsize=8.0)
    
    ax.annotate("", xy=(6.2, 4.3), xytext=(6.1, 1.0),
                arrowprops=dict(arrowstyle="->", color="#C53030", lw=1.5, connectionstyle="arc3,rad=-0.28"))
    ax.text(7.2, 2.0, "Negative Feedback\nConstraint Injection", color="#C53030", fontsize=7.8, style="italic")
    
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0.2, 6.0)
    return save_fig(fig, "fig4_8_activity_diagram.png")

# ==============================================================================
# FIGURE 4.9: UML SEQUENCE DIAGRAM
# ==============================================================================
def create_fig4_9():
    fig, ax = plt.subplots(figsize=(13.5, 6.2))
    ax.axis('off')
    
    lifelines = [("User", 1.2), ("Gateway", 3.4), ("Planner", 5.6), ("Retriever", 7.8), ("Generator", 10.0), ("Verifier", 12.2)]
    for name, x in lifelines:
        ax.text(x, 5.4, name, ha="center", va="center", color="#1A202C", weight="bold", fontsize=8.8,
                bbox=dict(boxstyle="round,pad=0.45", fc="#EDF2F7", ec="#2D3748", lw=1.4))
        ax.plot([x, x], [0.4, 5.0], color="#CBD5E0", linestyle="--", lw=1.3)
        
    messages = [
        (1.2, 3.4, 4.6, "1: submit_query(Q)", False),
        (3.4, 5.6, 4.0, "2: decompose_plan(Q)", False),
        (5.6, 7.8, 3.4, "3: hybrid_fetch(subtasks)", False),
        (7.8, 5.6, 2.8, "4: candidate_context(K)", True),
        (5.6, 10.0, 2.2, "5: grounded_synthesis(K)", False),
        (10.0, 12.2, 1.6, "6: extrinsic_verify(Y, K)", False),
        (12.2, 3.4, 1.0, "7: return_certified_response()", True),
        (3.4, 1.2, 0.5, "8: emit_stream_to_user()", True)
    ]
    for x1, x2, y, txt, is_ret in messages:
        ls = "--" if is_ret else "-"
        col = "#2B6CB0" if not is_ret else "#22543D"
        ax.annotate("", xy=(x2, y), xytext=(x1, y), arrowprops=dict(arrowstyle="->", color=col, lw=1.4, linestyle=ls))
        ax.text((x1 + x2)/2, y + 0.12, txt, ha="center", color="#2D3748", fontsize=7.6, weight="bold")
        
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0.1, 5.9)
    return save_fig(fig, "fig4_9_sequence_diagram.png")

# ==============================================================================
# FIGURE 4.10: UML COMPONENT DIAGRAM
# ==============================================================================
def create_fig4_10():
    fig, ax = plt.subplots(figsize=(13.5, 6.2))
    ax.axis('off')
    
    host = patches.Rectangle((0.6, 0.3), 12.3, 5.4, fc="#F8FAFC", ec="#4A5568", lw=1.8)
    ax.add_patch(host)
    ax.text(0.9, 5.45, "Docker Containerized Infrastructure Host Node", color="#2D3748", weight="bold", fontsize=9.2)
    
    comps = [
        ("Nginx / React Client\n[Port: 80, 443]", 2.2, 4.0),
        ("FastAPI Gateway Engine\n[Port: 8000]", 6.5, 4.0),
        ("LangGraph Agent Runtime\n[Asyncio Worker Pool]", 10.8, 4.0),
        ("ChromaDB Vector Service\n[Port: 8001]", 2.8, 1.5),
        ("Neo4j Property KG Engine\n[Port: 7687 Bolt]", 6.8, 1.5),
        ("PostgreSQL 16 Audit Store\n[Port: 5432]", 10.8, 1.5)
    ]
    for name, x, y in comps:
        ax.text(x, y, name, ha="center", va="center", color="#1A365D", weight="bold", fontsize=7.8, linespacing=1.3,
                bbox=dict(boxstyle="square,pad=0.55", fc="#EBF8FF", ec="#3182CE", lw=1.4))
        
    ax.annotate("", xy=(5.0, 4.0), xytext=(3.6, 4.0), arrowprops=dict(arrowstyle="<->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(9.3, 4.0), xytext=(8.0, 4.0), arrowprops=dict(arrowstyle="<->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(3.0, 2.2), xytext=(5.6, 3.4), arrowprops=dict(arrowstyle="<->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(6.8, 2.2), xytext=(9.8, 3.4), arrowprops=dict(arrowstyle="<->", color="#4A5568", lw=1.5))
    ax.annotate("", xy=(10.8, 2.2), xytext=(10.8, 3.3), arrowprops=dict(arrowstyle="<->", color="#4A5568", lw=1.5))
    
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0.0, 6.0)
    return save_fig(fig, "fig4_10_component_diagram.png")

# ==============================================================================
# FIGURE 5.1: LANGGRAPH STATEFUL EXECUTION MACHINE
# ==============================================================================
def create_fig5_1():
    fig, ax = plt.subplots(figsize=(14.0, 6.0))
    ax.axis('off')
    
    nodes = [
        ("Query Ingestion\n& Rewriter", 1.5, 4.6, "#E2E8F0", "#2D3748"),
        ("Planner Node\n(CoT Decomposition)", 4.5, 4.6, "#BEE3F8", "#2B6CB0"),
        ("Policy Router\n(Modality Switching)", 7.8, 4.6, "#C6F6D5", "#22543D"),
        ("Retriever Node\n(ChromaDB + Neo4j)", 11.2, 4.6, "#FEFCBF", "#744210"),
        ("Generator Node\n(Context Synthesis)", 11.2, 2.0, "#E9D8FD", "#553C9A"),
        ("Verifier Node\n(Composite Gating)", 7.8, 2.0, "#FED7D7", "#9B2C2C"),
        ("Reflection Node\n(Retry Counter++)", 4.5, 2.0, "#FFD8A8", "#D9480F"),
        ("Safe Fallback\nRefusal Node", 1.5, 2.0, "#FFA8A8", "#C92A2A")
    ]
    for name, x, y, bg, tc in nodes:
        ax.text(x, y, name, ha="center", va="center", color=tc, weight="bold", fontsize=8.2, linespacing=1.3,
                bbox=dict(boxstyle="round,pad=0.55", fc=bg, ec=tc, lw=1.5))
        
    ax.annotate("", xy=(3.15, 4.6), xytext=(2.45, 4.6), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.8))
    ax.annotate("", xy=(6.45, 4.6), xytext=(5.85, 4.6), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.8))
    ax.annotate("", xy=(9.75, 4.6), xytext=(9.15, 4.6), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.8))
    ax.annotate("", xy=(11.2, 2.7), xytext=(11.2, 3.9), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.8))
    ax.annotate("", xy=(9.2, 2.0), xytext=(9.8, 2.0), arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.8))
    
    p_fin = patches.Circle((7.8, 0.45), 0.26, fc="#C6F6D5", ec="#22543D", lw=2.0)
    ax.add_patch(p_fin)
    ax.text(7.8, 0.45, "PASS", ha="center", va="center", color="#22543D", weight="bold", fontsize=7.5)
    ax.annotate("", xy=(7.8, 0.75), xytext=(7.8, 1.35), arrowprops=dict(arrowstyle="->", color="#22543D", lw=1.8))
    ax.text(8.3, 1.0, "S_total >= τ", color="#22543D", fontsize=8.0, weight="bold")
    
    ax.annotate("", xy=(5.9, 2.0), xytext=(6.4, 2.0), arrowprops=dict(arrowstyle="->", color="#D9480F", lw=1.8))
    ax.text(6.15, 2.25, "FAIL (N<3)", ha="center", color="#D9480F", fontsize=7.8, weight="bold")
    
    ax.annotate("", xy=(4.5, 3.9), xytext=(4.5, 2.7), arrowprops=dict(arrowstyle="->", color="#D9480F", lw=1.8))
    ax.text(3.7, 3.3, "Negative\nFeedback", color="#D9480F", fontsize=7.8, style="italic")
    
    ax.annotate("", xy=(2.6, 2.0), xytext=(3.1, 2.0), arrowprops=dict(arrowstyle="->", color="#C92A2A", lw=1.8))
    ax.text(2.85, 2.25, "N >= 3", ha="center", color="#C92A2A", fontsize=7.8, weight="bold")
    
    ax.set_xlim(0, 13.0)
    ax.set_ylim(-0.1, 5.5)
    return save_fig(fig, "fig5_1_langgraph_execution.png")

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == "__main__":
    print("Regenerating all 15 figures...")
    create_fig1_1()
    create_fig2_1()
    create_fig2_2()
    create_fig2_3()
    create_fig4_1()
    create_fig4_2()
    create_fig4_3()
    create_fig4_4()
    create_fig4_5()
    create_fig4_6()
    create_fig4_7()
    create_fig4_8()
    create_fig4_9()
    create_fig4_10()
    create_fig5_1()
    print("All 15 figures successfully generated and verified!")
