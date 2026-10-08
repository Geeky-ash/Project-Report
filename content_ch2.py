# content_ch2.py
# Chapter 2: Literature Survey text, tables, and structure

CH2_TITLE = ("CHAPTER 2", "LITERATURE SURVEY")

CH2_TABLE1_DATA = {
    "caption": "Table 2.1: Retrieval Architecture and Scalability Profile Comparison Across Existing Paradigms",
    "headers": ["Approach", "Knowledge Representation", "Multi-Hop Capability", "Retrieval Adaptivity", "Computational Cost", "Scalability Profile", "Primary Strength", "Primary Limitation"],
    "widths": [1.1, 1.1, 0.9, 0.9, 0.9, 0.9, 1.4, 1.4],
    "rows": [
        ["Traditional RAG [7]", "Dense Embeddings (Vector DB)", "Weak (Fails on unlinked hops)", "None (Static single-pass)", "Low (O(1) ANN search)", "High (Sub-second vector lookup)", "Low latency, simple operational stack", "Fails on cross-document associative reasoning"],
        ["Advanced RAG [11]", "Dense Vectors + Chunk Metadata", "Moderate (Reranking dependent)", "Pre-retrieval Query Rewrite / HyDE", "Medium (Reranker overhead)", "High (Parallel ANN execution)", "Improved chunk contextual precision", "Remains an inflexible, single-pass pipeline"],
        ["GraphRAG [8]", "Knowledge Graph Triplets + Leiden Clusters", "Strong (Explicit multi-hop paths)", "None (Rigid corpus-wide map-reduce)", "High (Heavy LLM graph compilation)", "Moderate (High query token footprint)", "Excels at global corpus summarization", "Vulnerable to LLM extraction noise and stale edges"],
        ["Self-RAG [28]", "Dense Vectors + Reflection Tokens", "Moderate (Token triggered)", "Token-triggered iterative retrieval", "Medium-High (Multi-step generation)", "High (Model internal reflection)", "Dynamic retrieval triggering during synthesis", "Relies heavily on specialized fine-tuned model weights"],
        ["CRAG [29]", "Dense Vectors + External Web Search", "Moderate (Fallback dependent)", "Binary confidence threshold switching", "Medium (External web calls)", "High (Heuristic evaluator)", "Recovers from poor local vector retrieval", "Injects uncontrolled, non-deterministic web noise"],
        ["IRCoT [14]", "Dense Vectors + Chain-of-Thought Steps", "Strong (Reasoning-guided search)", "Reasoning-guided step-wise retrieval", "Medium-High (Multi-turn LLM calls)", "Moderate (Sequential query turns)", "High precision on multi-hop question answering", "Cascading error propagation from early flawed reasoning"],
        ["Agentic RAG [1], [31]", "Flexible / Dual Multi-Tool Stores", "Strong (Autonomous tool orchestration)", "Dynamic multi-agent planning", "Very High (Unbounded conversation turns)", "Low-Moderate (Token runaway risks)", "Highly adaptive and autonomous planning", "High latency, expensive coordination, loop divergence"],
        ["Proposed Framework", "Hybrid: Vectors (ChromaDB) + Neo4j Property KG", "Superior (Automated Cypher + Dense fusion)", "Continuous Query Complexity Routing Model", "Optimized (Dynamic modality gating)", "High (Strict state machine bounds)", "Eliminates hallucination via extrinsic gating", "Initial knowledge graph cold-start compilation"]
    ]
}

CH2_TABLE2_DATA = {
    "caption": "Table 2.2: Hallucination Mitigation and Verification Mechanisms Across Existing Paradigms",
    "headers": ["Approach", "Verification Method", "Self-Correction Paradigm", "Error Memory & State", "Explainability Level", "Key Vulnerability & Failure Mode"],
    "widths": [1.2, 1.2, 1.2, 1.2, 1.2, 1.8],
    "rows": [
        ["Traditional RAG [7]", "None (Direct prompt conditioning)", "None (Immutable feedforward generation)", "None (Stateless execution)", "None (Black-box neural attention)", "Blind to retrieval irrelevance; hallucinates missing facts"],
        ["GraphRAG [8]", "Implicit (Sub-graph community summary)", "None (Single-pass map-reduce synthesis)", "None (Stateless summarization)", "Moderate (Inspectable graph traversal)", "Extraction hallucinations become permanent ground truth"],
        ["CRAG [29]", "Lightweight Confidence Scorer", "Partial (Rule-based web fallback trigger)", "None (Single evaluation point)", "Moderate (Scorer threshold logged)", "Same-model evaluation bias; web source unreliability"],
        ["DSPy [23]", "Compiler Loss / Metric Optimizer", "Algorithmic Prompt Optimization", "Compilation trace memory", "High (Declarative prompt log)", "Overfits prompt instructions to training evaluation set"],
        ["Agentic RAG [28], [31]", "Intrinsic LLM Self-Reflection", "Cyclic Iterative Critique Loop", "State-based conversation memory", "High (Full agent conversation log)", "Susceptible to Self-Correction Paradox [34]; loops"],
        ["Proposed Framework", "Extrinsic Algorithmic Gating (RAGAS + FActScore)", "Constrained Cyclic State Machine Loop", "Global State Schema S with Feedback Memory", "Full Auditability (Every routing & Cypher logged)", "Cold-start entity extraction requires manual oversight"]
    ]
}

CH2_TABLE3_DATA = {
    "caption": "Table 2.3: Summary of Research Gaps, Impact, and Proposed Mitigation Strategies",
    "headers": ["Identified Research Gap", "Foundational Literature Citations", "Operational & Technical Impact", "Proposed Architectural Mitigation", "Target Verification Metric"],
    "widths": [1.4, 1.3, 1.7, 1.7, 1.4],
    "rows": [
        ["Gap 1: Disjointed Modality Routing", "Trivedi et al. [14], Singh et al. [1], Lewis et al. [7]", "Simple queries waste massive compute on graphs; complex queries fail due to vector context fragmentation.", "Intelligent Policy Selection Module executing a mathematical Query Complexity Routing Model C(Q).", "Modality classification accuracy; P95 query latency reduction (>= 40%)."],
        ["Gap 2: The Self-Correction Paradox", "Huang et al. [34], Madaan et al. [33], Es et al. [9]", "Autonomous LLM reflection fails to catch reasoning errors, rubber-stamping its own hallucinations.", "Extrinsic Verifier Agent computing composite metric Stotal (RAGAS faithfulness + FActScore atomic precision).", "RAGAS Faithfulness (>= 0.92); FActScore Precision (>= 0.95)."],
        ["Gap 3: Unbounded Multi-Agent Non-Determinism", "Chase et al. [12], Wu et al. [31], Moura [32]", "Conversational agents derail into infinite reasoning cycles, violating enterprise latency SLAs.", "LangGraph state machine enforcing strict Directed Acyclic cycles and deterministic retry threshold (N_max <= 3).", "SLA compliance rate (100%); Zero runaway token divergence."],
        ["Gap 4: Graph Construction Noise & Stale Edges", "Edge et al. [8], Cai et al. [30], Pan et al. [20]", "LLM triplet extraction introduces hallucinated edges; static graphs encode chronologically obsolete facts.", "Continuous Temporal Decay Graph Pruning Model w(e,t0) filtering edges below confidence threshold tau_decay.", "Temporal precision; Noise edge pruning rate (>= 25%)."]
    ]
}

CH2_SECTIONS = [
    {
        "type": "heading1",
        "text": "2.1 CURRENT TRENDS IN RESEARCH"
    },
    {
        "type": "paragraph",
        "text": "The rapid intersection of neural language modeling, information retrieval, structural knowledge engineering, and multi-agent systems has established Retrieval-Augmented Generation (RAG) as one of the most prolific frontiers in modern artificial intelligence. Over the past five years, the research community has witnessed four distinct evolutionary phases: (1) Traditional and Advanced Vector-based Pipelines, (2) Structural Knowledge Retrieval via Knowledge Graphs (GraphRAG), (3) Autonomous Multi-Agent Orchestration, and (4) Algorithmic Verification and Self-Correction. This literature survey provides a comprehensive, rigorous examination of the seminal publications, structural paradigms, and unresolved tensions across these four domains."
    },
    {
        "type": "nano_banana",
        "name": "Literature Architecture Evolution and Taxonomy",
        "caption": "Figure 2.1: Evolution of Retrieval-Augmented Generation Architectures: From Naive Vector Pipelines to Adaptive Agentic GraphRAG."
    },
    {
        "type": "heading2",
        "text": "2.1.1 Traditional and Advanced Vector RAG Pipelines"
    },
    {
        "type": "paragraph",
        "text": "The foundational blueprint of Retrieval-Augmented Generation was established by Lewis et al. [7] and Borgeaud et al. [17]. In their seminal formulation, Lewis et al. combined a pre-trained sequence-to-sequence neural model (BART) with a Dense Passage Retriever (DPR) utilizing dual-encoder architectures. Unstructured textual passages were mapped into a continuous latent vector space, enabling non-parametric factual retrieval via maximum inner product search. Borgeaud et al. [17] scaled this concept to trillion-token corpora with the RETRO architecture, demonstrating that retrieval-enhanced models achieve competitive perplexity compared to massive dense models an order of magnitude larger."
    },
    {
        "type": "paragraph",
        "text": "Gao et al. [11] systematically categorized the progression of retrieval-augmented architectures into Naive, Advanced, and Modular RAG. Naive RAG operates as a static, feed-forward three-stage pipeline: chunking, indexing, and retrieve-then-generate. However, empirical studies rapidly identified severe precision bottlenecks in Naive RAG. Because dense vector embeddings compress complex textual semantics into fixed-dimensional vectors, they suffer from semantic dilution—loss of fine-grained numeric, relational, and contextual nuances. Furthermore, when documents are split into static token chunks (e.g., 256 or 512 tokens), interconnected concepts spanning adjacent paragraphs or distinct corporate documents are severed."
    },
    {
        "type": "paragraph",
        "text": "To alleviate these limitations, researchers formulated Advanced RAG paradigms [11]. Gao et al. [27] developed Hypothetical Document Embeddings (HyDE), which prompts an LLM to generate a hypothetical answer passage prior to retrieval, utilizing the embedding of the hypothetical text to locate authentic documents in vector space. Other advanced enhancements introduced sliding-window chunking with sentence-window retrieval, bi-encoder cross-encoder re-ranking hierarchies (e.g., Cohere Rerank, BGE-Reranker), and metadata filtering. In parallel, Liu et al. [26] exposed the critical 'Lost in the Middle' failure mode, proving that when long candidate passages are injected into transformer context windows, the model's multi-head attention mechanism systematically prioritizes tokens located at the extreme beginning and end of the context, while failing to retrieve critical facts positioned in the middle. While Advanced RAG significantly elevates single-hop lookup precision, it remains structurally constrained: its rigid, single-pass pipeline is incapable of dynamic query reformulation or multi-hop logical reasoning [14]."
    },
    {
        "type": "heading2",
        "text": "2.1.2 Structural Knowledge Retrieval and GraphRAG"
    },
    {
        "type": "paragraph",
        "text": "Recognizing that unlinked geometric vector spaces cannot represent explicit relational dependencies, researchers turned to Knowledge Graphs (KGs) [10], [13] to impart deterministic structural topology to retrieval architectures. Robinson, Webber, and Eifrem [13] established the computational advantages of labeled property graphs for multi-hop traversals, demonstrating that graph databases (e.g., Neo4j) achieve index-free adjacency, allowing relationship traversal at O(1) complexity per edge hop regardless of the global database size. Ji et al. [10] surveyed knowledge graph representations, detailing how knowledge triplets (u, r, v)—consisting of head entity, relation predicate, and tail entity—provide formal, explainable knowledge substrates."
    },
    {
        "type": "paragraph",
        "text": "The integration of knowledge graphs into generative AI achieved a major breakthrough with Edge et al.'s [8] Microsoft GraphRAG. Edge et al. identified that vector RAG fails completely on global sensemaking queries that require synthesizing thematic concepts across entire corpora (e.g., 'What are the main systemic fraud indicators across all auditing transcripts?'). Microsoft GraphRAG constructs a corpus-wide knowledge graph by prompting an LLM to extract all entity-relationship triplets, creates a hierarchical community structure using the Leiden community detection algorithm, and generates pre-computed community summaries. During retrieval, the system performs a map-reduce summarization across relevant community levels to produce comprehensive responses. In parallel, Yasunaga et al. [18] developed QA-GNN, which bridges language models and knowledge graphs through joint reasoning, using Graph Neural Networks (GNNs) with message-passing mechanisms to score graph connectivity. Pan et al. [20] and Wu et al. [24] formulated comprehensive roadmaps for unifying LLMs and KGs, proving that structural graphs ground LLMs in formal logic while LLMs enhance graph completeness."
    },
    {
        "type": "paragraph",
        "text": "Despite these compelling advantages, a critical review of the GraphRAG literature reveals profound operational bottlenecks. Primary among these is the 'Knowledge Graph Extraction Bottleneck' [8], [20]. Because automated knowledge graph compilation relies on prompting LLMs to identify entities and relationships across raw text, the initial extraction step is itself highly prone to factual hallucinations. Hallucinated relationships are encoded directly as permanent edges in the property graph, fundamentally poisoning downstream graph traversals. Furthermore, as Cai et al. [30] noted in their survey of temporal knowledge graphs, facts are inherently time-dependent (e.g., corporate executive appointments or clinical drug guidelines change over time). Standard GraphRAG systems treat all extracted triplets as timeless truths, lacking mathematical mechanisms to prune obsolete or temporally invalid edges."
    },
    {
        "type": "heading2",
        "text": "2.1.3 Agentic Orchestration and Iterative Reasoning"
    },
    {
        "type": "paragraph",
        "text": "To liberate RAG from rigid single-pass feedforward execution, recent literature has championed the paradigm of Agentic RAG [1]. Agentic architectures endow language models with executive agency: the capacity to analyze queries, formulate multi-step plans, autonomously invoke retrieval and calculation tools, evaluate intermediate outputs, and iterate until the objective is satisfied. Singh et al. [1] provided a comprehensive taxonomy of Agentic RAG, highlighting how multi-agent coordination transforms retrieval from a passive data-fetching operation into a proactive reasoning strategy."
    },
    {
        "type": "paragraph",
        "text": "Seminal works in this domain include Self-RAG by Asai et al. [28], who trained an open-weight LLM to generate special reflection tokens ([Retrieve], [IsRel], [IsSup], [IsUse]) that trigger retrieval dynamically during generation and critique context relevance. Yan et al. [29] proposed Corrective RAG (CRAG), which evaluates retrieved document confidence using a lightweight heuristic scorer; if confidence is low, CRAG automatically falls back to public web search (e.g., Google or Tavily) to recover missing context. Trivedi et al. [14] introduced Interleaving Retrieval with Chain-of-Thought (IRCoT), demonstrating that complex multi-hop question answering requires interleaving reasoning steps with retrieval steps—using intermediate Chain-of-Thought [21] sentences as targeted search queries for subsequent retrieval rounds."
    },
    {
        "type": "nano_banana",
        "name": "Agentic GraphRAG Interaction and Verification Cycle",
        "caption": "Figure 2.2: Multi-Agent GraphRAG Workflow with Integrated Verification and Reflection Loop."
    },
    {
        "type": "paragraph",
        "text": "To enable multi-agent collaboration, generalized orchestration frameworks have proliferated. Wu et al. [31] introduced AutoGen, demonstrating that complex software engineering and analytical tasks can be solved through multi-agent conversational dialogues between specialized agent personas (e.g., Planner, UserProxy, Assistant). Moura [32] developed CrewAI, which coordinates role-playing autonomous agents via sequential and hierarchical processes. Most significantly, Chase et al. [12] introduced LangGraph, a graph-based orchestration framework that models multi-agent workflows as stateful computational state machines. LangGraph structures interactions using Directed Acyclic Graphs (DAGs) and cyclic state graphs, defining individual nodes as agent actions and edges as conditional routing functions. In parallel, Khattab et al. [23] introduced DSPy, a programming framework that compiles declarative LM pipelines into optimized prompt configurations and parameter weights, eliminating heuristic prompt trial-and-error."
    },
    {
        "type": "heading2",
        "text": "2.1.4 Verification Paradigms and the Self-Correction Paradox"
    },
    {
        "type": "paragraph",
        "text": "In mission-critical, regulated deployments, ensuring factual truthfulness requires rigorous post-generation verification mechanisms [6], [15]. To establish objective standards for grounding, the academic community developed quantitative benchmark suites. Es et al. [9] developed RAGAS (Retrieval Augmented Generation Assessment System), formulating reference-free evaluation metrics including Context Precision, Context Recall, Faithfulness (measuring whether the generated response is strictly derived from retrieved context), and Answer Relevance. In parallel, Min et al. [25] introduced FActScore, an automated evaluation protocol that decomposes long-form text into atomic factual propositions and evaluates the precision of each proposition against authoritative sources."
    },
    {
        "type": "paragraph",
        "text": "To automate verification, modern agentic systems initially relied on iterative self-reflection, exemplified by Madaan et al.'s [33] Self-Refine and Wang et al.'s [19] Self-Consistency. These systems prompt the generator LLM to critique its own response and refine errors iteratively. However, this foundational premise was fundamentally invalidated by Huang et al. [34] in their landmark study, 'Large Language Models Cannot Self-Correct Reasoning Yet.' Huang et al. proved empirically that without an external ground-truth feedback signal, LLMs systematically fail to identify their own logical and factual errors. When prompted to self-correct, transformers frequently degrade their answers, change correct assertions to incorrect ones, or hallucinate justifications for their initial mistakes. The root cause of this 'Self-Correction Paradox' is that the LLM evaluating the response shares the identical statistical distributions, training biases, and blind spots as the LLM that generated the error. Consequently, self-reflection without extrinsic, non-LLM algorithmic verification constitutes an illusion of reliability."
    },
    {
        "type": "heading1",
        "text": "2.2 COMPARATIVE ANALYSIS"
    },
    {
        "type": "paragraph",
        "text": "To establish a rigorous technical baseline, Table 2.1 presents a comprehensive comparative evaluation of existing retrieval architectures regarding knowledge representation, reasoning capabilities, computational cost, and scalability profiles. Furthermore, Table 2.2 analyzes hallucination mitigation and verification mechanisms across these paradigms, exposing their primary architectural vulnerabilities."
    },
    {
        "type": "table",
        "data": CH2_TABLE1_DATA
    },
    {
        "type": "table",
        "data": CH2_TABLE2_DATA
    },
    {
        "type": "paragraph",
        "text": "Analytical Discussion of Comparative Findings:\nAs synthesized in Tables 2.1 and 2.2, existing retrieval architectures exhibit a fundamental, polarizing dichotomy. Traditional and Advanced Vector RAG architectures [7], [11] deliver outstanding sub-second operational latency and simple infrastructure management; however, they are mathematically blind to relational logic, resulting in severe factual hallucinations whenever an enterprise query demands multi-hop synthesis across distinct documents. Conversely, Knowledge Graph architectures (GraphRAG) [8] excel at structural reasoning and corpus-wide sensemaking, but impose immense computational and financial costs during graph construction, while lacking mechanisms to handle extraction hallucinations and chronological staleness. Agentic frameworks [1], [31] offer unprecedented adaptivity, but their reliance on intrinsic self-reflection falls victim to the Self-Correction Paradox [34], and their unconstrained conversational loops introduce dangerous latency and token runaway risks that violate enterprise Service Level Agreements (SLAs). Therefore, the literature indicates an urgent imperative for an architecture that combines the topological precision of KGs with the adaptive routing of agents, strictly bounded by a state machine and gated by extrinsic algorithmic verification."
    },
    {
        "type": "heading1",
        "text": "2.3 CRITICAL ANALYSIS OF EXISTING LITERATURE"
    },
    {
        "type": "paragraph",
        "text": "A rigorous critical analysis of the surveyed literature reveals four fundamental technical contradictions that prevent current RAG systems from achieving production reliability in high-stakes enterprise applications:"
    },
    {
        "type": "paragraph",
        "text": "1. The Failure of Static Geometric Retrieval: The foundational assumption of vector-based RAG [7], [11] is that semantic proximity in latent embedding space correlates directly with factual and logical relevance. This assumption is mathematically flawed. Cosine similarity evaluates the angular alignment of dense vectors, which captures topical congruence but is agnostic to directional relationships, logical negation, and temporal causality. In regulated enterprise scenarios—such as verifying whether a specific pharmaceutical drug interacts adversely with another compound [39], [40]—two passages describing completely opposite clinical outcomes share near-identical dense vector embeddings. Furthermore, dense similarity search cannot perform iterative relational traversal without multiple disjointed queries, resulting in context fragmentation."
    },
    {
        "type": "paragraph",
        "text": "2. The Knowledge Graph Extraction and Temporal Stagnation Bottleneck: While GraphRAG [8] successfully imposes topological order over unstructured text, its construction pipeline introduces a systemic vulnerability. Edge et al. rely exclusively on prompting generative LLMs to perform automated Named Entity Recognition and Relation Extraction. Because base LLMs are inherently stochastic, they frequently hallucinate non-existent relations or misclassify entity types during extraction. Because these false triplets are codified permanently into the graph database, the graph itself becomes an authoritative source of corrupted knowledge. Compounding this failure is the complete lack of temporal decay mechanics in modern property graphs [30]. In fast-moving corporate environments, outdated policies, expired contracts, and superseded clinical guidelines remain fully active in the graph, overriding current documentation."
    },
    {
        "type": "paragraph",
        "text": "3. Unbounded Non-Determinism in Autonomous Multi-Agent Orchestration: Frameworks such as AutoGen [31] and CrewAI [32] demonstrate impressive emergent reasoning capabilities by enabling free-form conversational exchanges between specialized agent personas. However, from an enterprise software engineering standpoint, free-form multi-agent interaction is fundamentally non-deterministic. Without rigid mathematical state transitions and finite execution boundaries, agents easily enter recursive clarification loops, context window bloat, and infinite token expenditure [1], [12]. In an enterprise environment governed by strict millisecond SLAs and cost quotas, unconstrained agentic orchestration represents an unacceptable operational and financial risk."
    },
    {
        "type": "paragraph",
        "text": "4. The Verification Deficit: The Fallacy of Intrinsic LLM Self-Correction: The most glaring vulnerability across modern agentic RAG literature is the pervasive reliance on intrinsic self-reflection [28], [33]. Systems that instruct an LLM to 'review your previous response and fix any hallucinations' operate on the mathematically disproven premise that an autoregressive model can act as an impartial judge of its own output. As Huang et al. [34] empirically proved across rigorous mathematical and factual reasoning benchmarks, an LLM evaluating its own flawed reasoning will reliably re-confirm its hallucinated assumptions because the generative error originated from the model's own statistical weights. Relying on intrinsic self-critique in clinical, legal, or financial applications creates a dangerous illusion of safety while leaving factual vulnerabilities unmitigated."
    },
    {
        "type": "heading1",
        "text": "2.4 RESEARCH GAP IDENTIFICATION"
    },
    {
        "type": "paragraph",
        "text": "Synthesizing the critical analysis, this project identifies four major, unresolved research gaps in contemporary literature, as visually mapped in Figure 2.3 and detailed in Table 2.3:"
    },
    {
        "type": "nano_banana",
        "name": "Research Gap to Proposed Framework Solution Mapping",
        "caption": "Figure 2.3: Systematic Mapping of Identified Research Gaps to the Architectural Modules of the Proposed Adaptive Multi-Agent GraphRAG Framework."
    },
    {
        "type": "paragraph",
        "text": "Research Gap 1: Disjointed Modality Routing (Single-Backend Inefficiency)\n• Literature Origin: Identified by Trivedi et al. [14], Singh et al. [1], and Lewis et al. [7].\n• Problem Description: Current enterprise architectures treat knowledge retrieval as a monolithic, static modality. Systems either route all queries through flat vector search (which fails on complex multi-hop queries) or execute comprehensive graph traversals and community summarizations (which wastes massive computational resources and incurs excessive latency for simple factual queries).\n• Research Opportunity: Development of an automated, complexity-aware Policy Selection Module that computes a continuous mathematical routing score C(Q) across semantic embeddings, entity counts, traversal depth, and subgraph density, dynamically dispatching queries to Vector, Knowledge Graph, or Hybrid backends."
    },
    {
        "type": "paragraph",
        "text": "Research Gap 2: The Self-Correction Paradox in Autonomous Agent Workflows\n• Literature Origin: Empirically exposed by Huang et al. [34] and Madaan et al. [33].\n• Problem Description: Agentic RAG frameworks rely on intrinsic LLM self-reflection to verify outputs. Because the evaluator LLM shares the identical generative blind spots as the generator agent, contextual hallucinations reliably bypass the reflection stage and are emitted to users.\n• Research Opportunity: Engineering an extrinsic, non-LLM algorithmic verification gating mechanism that computes composite factual verification scores Stotal based on programmatic RAGAS faithfulness [9] and FActScore atomic claim decomposition [25], directly conditioning cyclic self-correction loops with negative feedback constraints."
    },
    {
        "type": "paragraph",
        "text": "Research Gap 3: Unbounded Non-Determinism and Latency in Multi-Agent Systems\n• Literature Origin: Discussed by Chase et al. [12], Wu et al. [31], and Moura [32].\n• Problem Description: Free-form conversational multi-agent dialogue lacks formal state constraints, leading to runaway execution cycles, unbounded latency, exponential token costs, and catastrophic violations of enterprise Service Level Agreements.\n• Research Opportunity: Implementing a deterministic LangGraph state machine orchestrating agent operations within rigid Directed Acyclic Graphs and bounded cyclic transitions, enforcing hard retry limits (N_max <= 3) and deterministic fallback responses."
    },
    {
        "type": "paragraph",
        "text": "Research Gap 4: Knowledge Graph Construction Noise and Temporal Invalidation\n• Literature Origin: Identified by Edge et al. [8], Cai et al. [30], and Pan et al. [20].\n• Problem Description: Automated knowledge graph extraction codifies LLM hallucinations directly into structural triplets, and existing property graphs lack mathematical mechanisms to account for fact expiration, leading to temporal hallucinations where obsolete data overrides current records.\n• Research Opportunity: Formulating and implementing a continuous Temporal Decay Graph Pruning Model w(e,t0) that exponentially down-weights structural edges based on factual age and extraction confidence, dynamically filtering noisy and stale triplets prior to retrieval."
    },
    {
        "type": "table",
        "data": CH2_TABLE3_DATA
    }
]

print("Chapter 2 content prepared successfully.")
