# content_ch3.py
# Chapter 3: Software Requirements Specification (SRS) text, tables, and structure

CH3_TITLE = ("CHAPTER 3", "SOFTWARE REQUIREMENTS SPECIFICATION")

CH3_TABLE1_DATA = {
    "caption": "Table 3.1: Hardware Requirements Specification",
    "headers": ["Component / Layer", "Minimum Development Specification", "Recommended Enterprise Production Specification"],
    "widths": [2.2, 2.7, 2.7],
    "rows": [
        ["Host Processor (CPU)", "Intel Core i7-13700H / AMD Ryzen 7 7840HS (8 Cores, 16 Threads, >= 3.8 GHz)", "Intel Xeon Silver 4410Y / AMD EPYC 9124 (16 Cores, 32 Threads, >= 3.2 GHz)"],
        ["System Memory (RAM)", "32 GB DDR5 RAM (4800 MHz)", "64 GB - 128 GB ECC Registered DDR5 RAM (5600 MHz)"],
        ["GPU Acceleration", "NVIDIA GeForce RTX 4070 (12 GB GDDR6 VRAM, CUDA Cores: 5888)", "NVIDIA RTX A6000 / A100 (48 GB - 80 GB VRAM, Tensor Cores: 336+)"],
        ["Primary Storage (OS & DB)", "1 TB PCIe 4.0 NVMe M.2 SSD (Read: 5000 MB/s, Write: 4500 MB/s)", "2 TB PCIe 5.0 Enterprise NVMe SSD (Read: 7500 MB/s, Write: 7000 MB/s) RAID-1"],
        ["Network Interface", "1 Gbps Ethernet NIC / Wi-Fi 6 (802.11ax)", "10 Gbps SFP+ Dedicated Low-Latency Enterprise Fiber NIC"],
        ["Virtualization / Hosting", "Local Bare-Metal Workstation / Docker Desktop 25.0+", "Kubernetes Cluster (Minikube / EKS / On-Premise MicroK8s)"]
    ]
}

CH3_TABLE2_DATA = {
    "caption": "Table 3.2: Software Environment and Middleware Specifications",
    "headers": ["Software Layer", "Technology / Framework Selected", "Version", "Operational Role & Justification"],
    "widths": [1.8, 2.0, 1.2, 2.6],
    "rows": [
        ["Operating System", "Ubuntu Linux LTS / Windows 11 Enterprise", "24.04 LTS / 23H2", "POSIX-compliant development environment with robust CUDA and container support."],
        ["Core Language Runtime", "Python", "3.11.8 / 3.12.2", "Native support for asynchronous event loops, typing, and modern AI ecosystem libraries."],
        ["Orchestration Engine", "LangGraph / LangChain Core", "0.2.x / 0.3.x", "State-machine-driven multi-agent execution, cyclic graphs, and state checkpointing."],
        ["Knowledge Graph DB", "Neo4j Community / Enterprise", "5.18.x LTS", "Labeled property graph engine supporting index-free adjacency and declarative Cypher."],
        ["Vector Database", "ChromaDB / Milvus", "0.4.24 / 2.3.x", "High-performance embedding storage, HNSW indexing, and cosine similarity searches."],
        ["Backend Web API", "FastAPI (Starlette + Pydantic v2)", "0.110.x", "High-throughput asynchronous REST endpoints and full-duplex WebSocket hub."],
        ["Evaluation Suites", "RAGAS & FActScore", "0.1.10 / 0.1.5", "Automated extrinsic evaluation of faithfulness, context relevance, and atomic facts."],
        ["Containerization", "Docker & Docker Compose", "25.0.3 / 2.24.x", "Multi-container microservice packaging ensuring environmental parity and portability."]
    ]
}

CH3_TABLE3_DATA = {
    "caption": "Table 3.3: Two-Semester Agile Implementation Plan (Stage 1 & Stage 2 Milestones)",
    "headers": ["Academic Phase", "Sprint / Milestone", "Target Timeline", "Key Technical Deliverables & Activities", "Status"],
    "widths": [1.2, 1.4, 1.3, 2.7, 1.0],
    "rows": [
        ["Semester VII (Stage 1)", "Sprint 1: Problem Formulation", "Weeks 1 – 4", "Conduct exhaustive literature survey; analyze limitations of vector RAG; formulate problem statement.", "Completed"],
        ["Semester VII (Stage 1)", "Sprint 2: Mathematical Modeling", "Weeks 5 – 8", "Derive Query Complexity Routing, Temporal Decay Graph Pruning, and Composite Extrinsic Verification models.", "Completed"],
        ["Semester VII (Stage 1)", "Sprint 3: SRS & System Architecture", "Weeks 9 – 12", "Draft complete SRS; model DFD Levels 0–2, ERD, and UML diagrams (Use Case, Class, Activity, Sequence).", "Completed"],
        ["Semester VII (Stage 1)", "Sprint 4: Prototype & Stage 1 Report", "Weeks 13 – 16", "Build baseline ingestion module; implement mock LangGraph state schema; submit Stage 1 Project Report.", "Completed"],
        ["Semester VIII (Stage 2)", "Sprint 5: Hybrid Backend Deployment", "Weeks 17 – 20", "Deploy production Neo4j property graph and ChromaDB; establish Cypher query generation pipeline.", "Planned"],
        ["Semester VIII (Stage 2)", "Sprint 6: Multi-Agent Orchestration", "Weeks 21 – 24", "Implement Planner, Router, Generator, Verifier, and Reflection agents via LangGraph state machines.", "Planned"],
        ["Semester VIII (Stage 2)", "Sprint 7: Verification & Benchmarking", "Weeks 25 – 28", "Integrate RAGAS and FActScore evaluators; benchmark on HotpotQA, TruthfulQA, and FinanceBench datasets.", "Planned"],
        ["Semester VIII (Stage 2)", "Sprint 8: UI Dashboard & Final Thesis", "Weeks 29 – 32", "Develop React web dashboard; execute ablation studies; publish research paper; submit final project thesis.", "Planned"]
    ]
}

CH3_SECTIONS = [
    {
        "type": "heading1",
        "text": "3.1 INTRODUCTION & SYSTEM OVERVIEW"
    },
    {
        "type": "paragraph",
        "text": "This Software Requirements Specification (SRS) establishes the foundational functional, operational, and non-functional requirements for the Adaptive Multi-Agent GraphRAG Framework. It serves as the formal engineering contract guiding the system design, algorithmic modeling, component implementation, and verification methodologies across both Stage 1 and Stage 2 of the Bachelor of Engineering project."
    },
    {
        "type": "heading2",
        "text": "3.1.1 Purpose and Intended Audience"
    },
    {
        "type": "paragraph",
        "text": "The primary purpose of the system is to provide enterprise organizations—particularly those operating in highly regulated, high-liability domains such as healthcare, pharmaceutical research, legal compliance, and financial auditing—with an autonomous, hallucination-resistant knowledge intelligence platform. The intended audience includes software engineers, AI system architects, database administrators, compliance auditors, and academic researchers tasked with evaluating the robustness and deterministic behavior of multi-agent LLM systems."
    },
    {
        "type": "heading2",
        "text": "3.1.2 User Classes and Operational Characteristics"
    },
    {
        "type": "paragraph",
        "text": "The framework identifies four distinct user classes with varying operational privileges, workflows, and technical expertise:"
    },
    {
        "type": "paragraph",
        "text": "1. Enterprise Knowledge Worker / End User: Interacts with the system via a web-based conversational interface to submit natural language inquiries regarding complex domain corpora. Requires rapid, accurate, fully grounded answers accompanied by inspectable citation links and confidence metrics."
    },
    {
        "type": "paragraph",
        "text": "2. Compliance & Audit Officer: Inspects the decision-making traces of the multi-agent system. Requires access to the Explainability Audit Trail to review the Planner's sub-task decomposition, generated Cypher traversal queries, verification faithfulness scores, and negative reflection constraints to ensure compliance with standards like NIST AI RMF [37] and the EU AI Act [38]."
    },
    {
        "type": "paragraph",
        "text": "3. System Administrator & Knowledge Engineer: Manages the knowledge ingestion lifecycle, monitors Neo4j graph integrity, inspects ChromaDB embedding health, configures policy routing thresholds (tau_1, tau_2), and tunes temporal edge decay pruning rates (lambda)."
    },
    {
        "type": "paragraph",
        "text": "4. Research Data Scientist: Evaluates quantitative hallucination benchmarks, conducts ablation experiments across retrieval modalities, evaluates token consumption profiles, and tunes agent prompt contracts and scoring hyperparameters (alpha, beta, gamma)."
    },
    {
        "type": "heading2",
        "text": "3.1.3 Assumptions and Technical Dependencies"
    },
    {
        "type": "paragraph",
        "text": "The development and operation of the framework operate under the following engineering assumptions and external dependencies:\n• Host hardware provides access to NVIDIA CUDA-compatible GPU acceleration for low-latency dense vector embedding generation.\n• Network connectivity is maintained between the multi-agent state engine, the Neo4j graph database, the vector database, and the external/local LLM inference gateway.\n• Enterprise documents ingested into the platform conform to supported unstructured text formats (PDF, DOCX, TXT, Markdown, JSON).\n• The underlying LLMs provide structured output generation (JSON schema enforcement) via tool calling or constrained decoding."
    },
    {
        "type": "heading1",
        "text": "3.2 FUNCTIONAL REQUIREMENTS"
    },
    {
        "type": "paragraph",
        "text": "The functional requirements define the explicit computational capabilities and operational behavior that the framework must deliver across its execution lifecycle:"
    },
    {
        "type": "paragraph",
        "text": "• FR-1: Document Ingestion and Hybrid Indexing Pipeline\n  - Ingestion: Ingest heterogeneous documents (PDF, DOCX, TXT, JSON), extract text, and remove formatting artifacts.\n  - Semantic Chunking: Partition text into overlapping token chunks (chunk_size=512, chunk_overlap=64 tokens).\n  - Dense Indexing: Transform chunks into dense continuous vectors (d=1536) and store them in ChromaDB with HNSW indexing.\n  - Graph Compilation: Extract entity-relation triplets (u, r, v) with confidence scores and timestamps, compiling a labeled property graph in Neo4j.\n  - Acceptance Criteria: Ingest 1,000 pages of enterprise text within 10 minutes, generating aligned vector and graph indices."
    },
    {
        "type": "paragraph",
        "text": "• FR-2: Query Pre-Processing and Planning Agent\n  - Pre-Processing: Normalize input queries, expand domain acronyms, and resolve coreferences.\n  - Task Decomposition: Execute Chain-of-Thought planning to decompose complex multi-hop queries into an ordered sequence of atomic sub-tasks T = {t1, t2, ..., tn}.\n  - Acceptance Criteria: Multi-hop queries from HotpotQA decomposed into valid logical sub-tasks with >= 95% semantic consistency."
    },
    {
        "type": "paragraph",
        "text": "• FR-3: Adaptive Policy Switching Router\n  - Complexity Scoring: Compute query complexity score C(Q) in [0, 1] using logistic sigmoid transform over dense query embedding, entity count, traversal depth, and subgraph density.\n  - Modality Gating: Route sub-tasks based on calibrated thresholds: C(Q) < tau_1 triggers Vector Retrieval; tau_1 <= C(Q) <= tau_2 triggers Hybrid Retrieval; C(Q) > tau_2 triggers Knowledge Graph Traversal.\n  - Acceptance Criteria: Route single-hop factual queries to vector store within < 50ms, achieving >= 90% routing accuracy against human expert annotations."
    },
    {
        "type": "paragraph",
        "text": "• FR-4: Dual Modality Retrieval Engine\n  - Vector Retrieval: Perform top-k cosine similarity search across ChromaDB embeddings.\n  - Graph Retrieval: Generate parameterized Cypher queries, execute traversals in Neo4j, and extract relevant subgraphs.\n  - Hybrid Fusion: Combine vector and graph candidate contexts using Reciprocal Rank Fusion (RRF) with smoothing constant k=60.\n  - Acceptance Criteria: Retrieve fused context within < 1.2s for hybrid queries, achieving context recall >= 88%."
    },
    {
        "type": "paragraph",
        "text": "• FR-5: Temporal Knowledge Pruning Subsystem\n  - Temporal Weighting: Calculate time-decayed weight w(e,t0) for each graph edge using exponential decay based on factual age (t0 - te) and decay constant lambda.\n  - Edge Filtering: Prune edges with w(e,t0) < tau_decay dynamically during retrieval traversal.\n  - Acceptance Criteria: Suppress obsolete or invalid edges from retrieved subgraphs with 100% adherence to defined time cutoffs."
    },
    {
        "type": "paragraph",
        "text": "• FR-6: Response Synthesis and Generator Agent\n  - Constrained Synthesis: Condition the generator LLM strictly upon the retrieved fused context Kfused.\n  - Citation Anchoring: Require the generator to attach explicit node/chunk source citations for every factual statement.\n  - Acceptance Criteria: Zero uncited factual assertions in generated output responses."
    },
    {
        "type": "paragraph",
        "text": "• FR-7: Extrinsic Verification and Gating Agent\n  - Algorithmic Gating: Evaluate candidate response Y against context K using extrinsic composite score Stotal combining RAGAS Faithfulness, FActScore atomic claim precision, answer relevance, and context temporal score.\n  - Gating Threshold: If Stotal >= tau_verify (default 0.85), emit the verified response to the user.\n  - Acceptance Criteria: Gating decision executed within < 1.5s; block responses containing ungrounded claims with >= 94% precision."
    },
    {
        "type": "paragraph",
        "text": "• FR-8: Self-Correction and Reflection Loop\n  - Feedback Injection: If Stotal < tau_verify, Reflection Agent generates precise negative constraints identifying ungrounded claims and updates retry counter N_retry = N_retry + 1.\n  - Bounded Execution: Loop back to Planner Agent with negative constraints if N_retry < N_max (N_max=3); otherwise, emit deterministic fallback response indicating verification failure.\n  - Acceptance Criteria: Zero runaway execution loops; strict termination at N_max <= 3 retries in 100% of test cases."
    },
    {
        "type": "paragraph",
        "text": "• FR-9: Audit Trail and Explainability Logger\n  - Audit Trail: Persist the full execution trace in the Memory Module: raw query, rewritten query, sub-tasks, routing decisions, Cypher queries, retrieved subgraphs, candidate response, verification metrics, and reflection history.\n  - Compliance Export: Expose structured JSON audit logs via REST API for regulatory compliance audits.\n  - Acceptance Criteria: Complete execution trace logged for every query with zero data loss."
    },
    {
        "type": "heading1",
        "text": "3.3 EXTERNAL INTERFACE REQUIREMENTS"
    },
    {
        "type": "paragraph",
        "text": "The framework interacts with external users, hardware, software systems, and communication networks through the following interfaces:"
    },
    {
        "type": "paragraph",
        "text": "• 3.3.1 User Interfaces: A modern React.js web dashboard providing three primary views: (1) Conversational Query Interface with streaming responses and interactive citations; (2) Interactive Graph Visualizer displaying Neo4j subgraphs traversed during reasoning; and (3) Compliance Audit Explorer visualizing LangGraph state execution traces, verification metric radars, and reflection history."
    },
    {
        "type": "paragraph",
        "text": "• 3.3.2 Hardware Interfaces: Interacts with NVIDIA GPU hardware via CUDA 12.x drivers and PyTorch C++ bindings for accelerated embedding generation. High-speed NVMe SSD storage interfaces provide low-latency I/O for database read/write operations."
    },
    {
        "type": "paragraph",
        "text": "• 3.3.3 Software Interfaces: Connects to Neo4j via the official Neo4j Python Bolt Driver over bolt://; interfaces with ChromaDB via Python client API; connects to OpenAI/Ollama LLM inference gateways via standard OpenAI-compatible REST APIs; orchestrates agent workflows via LangGraph state machine runtime."
    },
    {
        "type": "paragraph",
        "text": "• 3.3.4 Communication Interfaces: Exposes RESTful API endpoints and full-duplex WebSocket connections (RFC 6455) via FastAPI for real-time response token streaming. All network communications are secured using TLS 1.3 encryption with OAuth2 / JWT bearer token authentication."
    },
    {
        "type": "heading1",
        "text": "3.4 NON-FUNCTIONAL REQUIREMENTS"
    },
    {
        "type": "paragraph",
        "text": "The non-functional requirements define the quality attributes, performance constraints, and regulatory standards governing system operation:"
    },
    {
        "type": "paragraph",
        "text": "• 3.4.1 Performance Requirements: P95 query response latency shall not exceed 3.5 seconds for vector-routed single-hop queries, 7.0 seconds for multi-hop graph queries, and 12.0 seconds for hybrid queries requiring a single reflection cycle. The system shall support a minimum throughput of 25 concurrent multi-agent query sessions on standard hardware."
    },
    {
        "type": "paragraph",
        "text": "• 3.4.2 Safety and Compliance Requirements: The system shall enforce a maximum contextual hallucination rate of < 4.0% across benchmark evaluation sets. In the event of unrecoverable verification failure, the system shall emit a safe, deterministic refusal response rather than an unverified guess, adhering to NIST AI RMF [37] safety guidelines."
    },
    {
        "type": "paragraph",
        "text": "• 3.4.3 Security Requirements: All stored data at rest (vector embeddings, graph entities, audit logs) shall be encrypted using AES-256. Role-Based Access Control (RBAC) shall enforce distinct permission tiers for End Users, Auditors, and Administrators. API endpoints shall be protected against prompt injection attacks through input sanitization."
    },
    {
        "type": "paragraph",
        "text": "• 3.4.4 Software Quality Attributes: System availability shall maintain >= 99.9% uptime. System architecture shall be modular, allowing pluggable replacement of underlying LLMs or vector databases. All components shall be containerized via Docker to guarantee environment portability across on-premise and cloud infrastructure."
    },
    {
        "type": "heading1",
        "text": "3.5 SYSTEM REQUIREMENTS"
    },
    {
        "type": "paragraph",
        "text": "The minimum and enterprise production specifications for host hardware and software middleware are formally detailed in Table 3.1 and Table 3.2, respectively."
    },
    {
        "type": "table",
        "data": CH3_TABLE1_DATA
    },
    {
        "type": "table",
        "data": CH3_TABLE2_DATA
    },
    {
        "type": "heading1",
        "text": "3.6 ANALYSIS MODELS & SDLC IMPLEMENTATION PLAN"
    },
    {
        "type": "paragraph",
        "text": "The development lifecycle of the Adaptive Multi-Agent GraphRAG Framework follows an Agile Scrum Software Development Life Cycle (SDLC) tailored for applied artificial intelligence research. The methodology is structured across bi-weekly sprints encompassing iterative cycles of architectural design, mathematical modeling, prototype development, algorithmic benchmarking, and peer review."
    },
    {
        "type": "paragraph",
        "text": "The project is executed across two academic semesters (Semester VII and Semester VIII) as detailed in the comprehensive implementation roadmap presented in Table 3.3. Stage 1 (Semester VII) focuses on establishing rigorous theoretical foundations, mathematical formulations, SRS definitions, and baseline architectural modules. Stage 2 (Semester VIII) executes full system implementation, multi-agent LangGraph integration, benchmark evaluations across standardized datasets, and final dissertation defense."
    },
    {
        "type": "table",
        "data": CH3_TABLE3_DATA
    }
]

print("Chapter 3 content prepared successfully.")
