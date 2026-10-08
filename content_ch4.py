# content_ch4.py
# Chapter 4: System Design text, diagrams placeholders, and structure

CH4_TITLE = ("CHAPTER 4", "SYSTEM DESIGN")

CH4_SECTIONS = [
    {
        "type": "heading1",
        "text": "4.1 SYSTEM ARCHITECTURE"
    },
    {
        "type": "paragraph",
        "text": "The architectural foundation of the Adaptive Multi-Agent GraphRAG Framework is engineered upon a modular, decoupled, multi-tier topology designed to provide deterministic execution, high-throughput retrieval, and verifiable grounding. Unlike monolithic RAG pipelines that interleave ingestion, search, and generation into a single continuous call, our system establishes strict operational separation across four distinct tiers: (1) Knowledge Ingestion & Graph Compilation Tier, (2) Dual Storage & Indexing Tier, (3) Multi-Agent Orchestration Tier, and (4) Governance, Memory & Explainability Tier. Figure 4.1 provides a comprehensive visual representation of the end-to-end system architecture."
    },
    {
        "type": "nano_banana",
        "name": "Multi-Agent Adaptive GraphRAG System Architecture",
        "caption": "Figure 4.1: Comprehensive System Architecture Diagram of the Adaptive Multi-Agent GraphRAG Framework."
    },
    {
        "type": "heading2",
        "text": "4.1.1 Architectural Tiers and Module Breakdown"
    },
    {
        "type": "paragraph",
        "text": "1. Ingestion & Graph Compilation Tier: This tier is responsible for transforming raw, heterogeneous enterprise documents (PDF, DOCX, TXT, JSON) into structured dual knowledge representations. Ingestion proceeds through three asynchronous pipelines:\n• Document Preprocessing & Chunking: Ingests documents, eliminates formatting artifacts, and applies sliding-window tokenization to generate semantically cohesive chunks of 512 tokens with 64-token overlap.\n• Dense Embedding Generation: Passes each text chunk through a pre-trained dense bi-encoder model to generate high-dimensional continuous semantic vector representations (d=1536).\n• Triplet & Entity Extraction Pipeline: Prompts an LLM with specialized structured-output schemas to perform Named Entity Recognition (NER) and Relation Extraction (RE). For every extracted factual assertion, the module records head entity u, relation predicate r, tail entity v, extraction confidence weight w0 in (0, 1), and creation epoch timestamp te. Entities are resolved against an authority registry to prevent synonym fragmentation."
    },
    {
        "type": "paragraph",
        "text": "2. Dual Storage & Indexing Tier: Rather than forcing a single representation, the framework maintains two complementary persistence engines:\n• Vector Database (ChromaDB / Milvus): Stores dense chunk embeddings with Hierarchical Navigable Small World (HNSW) graph indexing, providing sub-millisecond approximate nearest neighbor (ANN) similarity search.\n• Property Knowledge Graph (Neo4j): Stores labeled property graphs where nodes represent domain entities and directed edges represent relationships. Neo4j's native index-free adjacency enables O(1) graph traversals, allowing arbitrary multi-hop path explorations without costly relational table joins."
    },
    {
        "type": "paragraph",
        "text": "3. Multi-Agent Orchestration Tier: The intellectual core of the framework is coordinated by a stateful LangGraph state machine runtime that manages communication and transitions between specialized autonomous agents:\n• User Query Interface: Accepts raw natural language input, resolves coreferences, and expands domain-specific acronyms to yield normalized query Q_rewritten.\n• Planner Agent: Employs Chain-of-Thought (CoT) reasoning to decompose Q_rewritten into an ordered Directed Acyclic Graph (DAG) of atomic sub-tasks T = {t1, t2, ..., tn}.\n• Policy Selection Router: Evaluates each sub-task against the mathematical Query Complexity Model C(Q) to select the optimal retrieval backend (Vector, Knowledge Graph, or Hybrid).\n• Hybrid Retriever Sub-Modules: Executes semantic vector lookups in ChromaDB and parameterized Cypher traversals in Neo4j, fusing candidate contexts via Reciprocal Rank Fusion (RRF).\n• Generator Agent: Conditions an autoregressive LLM to synthesize candidate response Y strictly grounded upon the fused retrieved context Kfused, inserting explicit chunk and node citation anchors.\n• Extrinsic Verifier Agent: Evaluates candidate generation Y against context K using non-LLM algorithmic evaluation suites (RAGAS and FActScore) to compute composite score Stotal. If Stotal >= tau_verify, the response is certified and emitted.\n• Reflection Agent: If verification fails, analyzes the failed propositions, generates precise negative feedback constraints F_neg, increments the retry counter N_retry, and loops control back to the Planner Agent."
    },
    {
        "type": "paragraph",
        "text": "4. Governance, Memory & Explainability Tier: Maintains a durable audit ledger of all system operations. The LangGraph State Checkpointer persists the global state schema S across every transition. The Memory Module stores dialogue history, while the Explainability Logger records the full causal chain—from original prompt to sub-task decomposition, routing rationale, Cypher queries, retrieved subgraphs, and verification metric scorecards—satisfying enterprise compliance mandates."
    },
    {
        "type": "heading1",
        "text": "4.2 DATA FLOW DIAGRAMS (DFD)"
    },
    {
        "type": "paragraph",
        "text": "Data Flow Diagrams model the movement of data through the system, illustrating how natural language inputs are transformed, routed, retrieved, verified, and stored across distinct process boundaries."
    },
    {
        "type": "heading2",
        "text": "4.2.1 DFD Level 0 — System Context Diagram"
    },
    {
        "type": "paragraph",
        "text": "The Level 0 Context Diagram establishes the macroscopic boundary of the system. As depicted in Figure 4.2, the system interacts with four primary external entities: (1) End User, (2) Enterprise Document Sources, (3) External LLM Inference Service, and (4) Compliance Auditor. The End User supplies natural language queries and receives verified, cited answers. Document Sources feed raw enterprise text into the ingestion system. The External LLM Service provides foundation model token inference for planning and generation. The Compliance Auditor extracts structured execution traces and verification scorecards."
    },
    {
        "type": "nano_banana",
        "name": "DFD Level 0 Context Diagram",
        "caption": "Figure 4.2: DFD Level 0 — System Context Diagram Illustrating Macroscopic System Boundaries."
    },
    {
        "type": "heading2",
        "text": "4.2.2 DFD Level 1 — Macro Data Flow Across Layers"
    },
    {
        "type": "paragraph",
        "text": "The Level 1 Data Flow Diagram decomposes the system into six core operational processes, as illustrated in Figure 4.3:\n• Process 1.0 (Document Ingestion & Indexing): Ingests raw documents, splits text into chunks, computes dense embeddings for Data Store D1 (Vector DB), and extracts entity-relationship triplets for Data Store D2 (Knowledge Graph DB).\n• Process 2.0 (Query Planning & Normalization): Ingests user query, performs rewriting, and decomposes the request into ordered sub-tasks.\n• Process 3.0 (Adaptive Policy Routing & Retrieval): Computes complexity score C(Q), dispatches sub-tasks to Vector or Graph retrieval engines, applies temporal decay pruning, and performs Reciprocal Rank Fusion.\n• Process 4.0 (Constrained Response Synthesis): Synthesizes candidate answer Y conditioned strictly upon retrieved context.\n• Process 5.0 (Extrinsic Verification & Reflection): Evaluates candidate answer against context, computes Stotal, and either emits verified answer to User or dispatches negative feedback constraints to Process 2.0.\n• Process 6.0 (Audit & Trace Persistence): Persists end-to-end execution states, Cypher statements, and metric scorecards to Data Store D3 (Audit Log DB)."
    },
    {
        "type": "nano_banana",
        "name": "DFD Level 1 Macro Data Flow",
        "caption": "Figure 4.3: DFD Level 1 — Data Flow Across Multi-Agent and Storage Layers."
    },
    {
        "type": "heading2",
        "text": "4.2.3 DFD Level 2 — Detailed Sub-Process Decomposition"
    },
    {
        "type": "paragraph",
        "text": "Figure 4.4 illustrates the granular Level 2 decomposition focusing on Process 3.0 (Policy Routing and Retrieval) and Process 5.0 (Extrinsic Verification and Reflection). Process 3.0 is decomposed into: Sub-Process 3.1 (Query Embedding & Entity Extraction), Sub-Process 3.2 (Complexity Scoring & Threshold Comparison), Sub-Process 3.3 (ChromaDB Vector Lookup), Sub-Process 3.4 (Cypher Traversal & Temporal Edge Decay Pruning), and Sub-Process 3.5 (Reciprocal Rank Fusion Context Aggregator). Process 5.0 is decomposed into: Sub-Process 5.1 (Atomic Claim Decomposition via FActScore), Sub-Process 5.2 (RAGAS Faithfulness & Relevance Scorer), Sub-Process 5.3 (Composite Gating Comparator), Sub-Process 5.4 (Negative Constraint Formulator), and Sub-Process 5.5 (Retry Threshold Controller)."
    },
    {
        "type": "nano_banana",
        "name": "DFD Level 2 Sub-Process Decomposition",
        "caption": "Figure 4.4: DFD Level 2 — Detailed Sub-Process Flow of Policy Routing and Extrinsic Verification."
    },
    {
        "type": "heading1",
        "text": "4.3 ENTITY RELATIONSHIP DIAGRAM (ERD)"
    },
    {
        "type": "paragraph",
        "text": "The data architecture of the platform unifies relational metadata, vector embeddings, graph topologies, and audit traces into an integrated logical entity-relationship model. Figure 4.5 illustrates the complete Entity Relationship Diagram (ERD), defining eight core entity classes, their attributes, and their cardinalities:"
    },
    {
        "type": "nano_banana",
        "name": "Entity Relationship Diagram",
        "caption": "Figure 4.5: Entity Relationship Diagram (ERD) of the Hybrid Knowledge and Verification Platform."
    },
    {
        "type": "paragraph",
        "text": "Entity Specifications and Cardinality Relationships:\n1. DOCUMENT (Doc_ID [PK], Title, File_Path, MIME_Type, File_Size, Ingest_Timestamp, Author): Represents source files ingested into the system. Holds a 1:N relationship with CHUNK.\n2. CHUNK (Chunk_ID [PK], Doc_ID [FK], Chunk_Index, Text_Content, Token_Count, Vector_Embedding_ID, Created_At): Represents discrete passages partitioned from documents. Linked 1:1 with vector index records.\n3. NAMED_ENTITY (Entity_ID [PK], Name, Entity_Type, Canonical_URI, First_Seen_Timestamp): Represents real-world concepts extracted from chunks. Holds an M:N relationship with CHUNK via MENTION table, and 1:N relationships with RELATION_EDGE (as Head_Entity and Tail_Entity).\n4. RELATION_EDGE (Edge_ID [PK], Head_Entity_ID [FK], Tail_Entity_ID [FK], Relation_Type, Extraction_Weight, Origin_Timestamp, Last_Verified_Timestamp): Represents directed knowledge graph edges connecting entities in Neo4j.\n5. QUERY_LOG (Query_ID [PK], Raw_Query, Normalized_Query, Session_ID, User_ID, Start_Timestamp, End_Timestamp, Final_Status): Tracks user query sessions. Holds a 1:N relationship with AGENT_TASK.\n6. AGENT_TASK (Task_ID [PK], Query_ID [FK], Task_Sequence, Task_Type, Routed_Modality, Complexity_Score, Execution_Latency): Records atomic sub-tasks generated by the Planner Agent.\n7. VERIFICATION_RESULT (Verification_ID [PK], Query_ID [FK], Candidate_Response, Faithfulness_Score, Relevance_Score, Temporal_Score, Composite_Score, Gating_Decision, Evaluated_At): Stores the algorithmic evaluation scorecard produced by the Verifier Agent.\n8. FEEDBACK_CONSTRAINT (Constraint_ID [PK], Verification_ID [FK], Retry_Attempt, Negative_Prompt, Violating_Propositions): Records negative feedback constraints injected into the reflection loop upon verification failure."
    },
    {
        "type": "heading1",
        "text": "4.4 UML DIAGRAMS"
    },
    {
        "type": "paragraph",
        "text": "To capture the structural, behavioral, and deployment characteristics of the software system from an object-oriented and distributed systems perspective, this section presents five comprehensive Unified Modeling Language (UML) specifications."
    },
    {
        "type": "heading2",
        "text": "4.4.1 UML Use Case Diagram"
    },
    {
        "type": "paragraph",
        "text": "The Use Case Diagram depicted in Figure 4.6 models the functional interactions between external actors and system capabilities. Four primary actors participate in the system:\n• End User: Executes 'Submit Complex Query', 'Stream Grounded Answer', and 'View Source Citations'.\n• Compliance Officer: Executes 'Audit Verification Scorecard', 'Inspect Reasoning Subgraph', and 'Export EU AI Act Trace Ledger'.\n• Knowledge Engineer: Executes 'Trigger Document Ingestion', 'Tune Policy Routing Thresholds', 'Inspect Graph Connectivity', and 'Trigger Temporal Pruning Job'.\n• System Administrator: Executes 'Manage User Privileges', 'Monitor Service Health', and 'Configure Database Connections'."
    },
    {
        "type": "nano_banana",
        "name": "UML Use Case Diagram",
        "caption": "Figure 4.6: UML Use Case Diagram for the Adaptive GraphRAG System."
    },
    {
        "type": "heading2",
        "text": "4.4.2 UML Class Diagram"
    },
    {
        "type": "paragraph",
        "text": "Figure 4.7 presents the static structural design of the software via the UML Class Diagram. Key classes and their associations include:\n• StateEngine: Central singleton orchestrating the LangGraph state machine, maintaining the global state dictionary, executing node functions, and evaluating conditional edge routing functions.\n• QueryPlanner: Analyzes rewritten queries and generates atomic sub-task execution graphs.\n• PolicyRouter: Evaluates query complexity and maps sub-tasks to retrieval backend policies.\n• VectorRetriever: Interfaces with ChromaDB client to execute dense embedding ANN queries.\n• GraphRetriever: Interfaces with Neo4j Bolt driver, generates parameterized Cypher queries, and executes temporal edge filtering.\n• HybridFuser: Combines disparate candidate lists using Reciprocal Rank Fusion (RRF).\n• GeneratorAgent: Formulates grounded synthesis prompts and generates candidate responses.\n• VerifierAgent: Interfaces with RAGAS and FActScore evaluator suites to compute Stotal.\n• ReflectionAgent: Formulates negative constraints and manages bounded retry counters."
    },
    {
        "type": "nano_banana",
        "name": "UML Class Diagram",
        "caption": "Figure 4.7: UML Class Diagram Representing the Object-Oriented Multi-Agent Architecture."
    },
    {
        "type": "heading2",
        "text": "4.4.3 UML Activity Diagram"
    },
    {
        "type": "paragraph",
        "text": "Figure 4.8 models the dynamic operational workflow of the complete query resolution lifecycle using an Activity Diagram. The activity begins with Query Ingestion, proceeds through Query Rewriting, and triggers Chain-of-Thought Sub-task Decomposition. For each sub-task, a decision diamond evaluates the Complexity Score C(Q). Depending on threshold conditions, the flow branches concurrently into Vector Lookup, Cypher Graph Traversal with Temporal Pruning, or Hybrid Fusion. Following context retrieval, the Generator Agent synthesizes a candidate answer. The flow enters the Verification Activity, calculating Stotal. A critical decision diamond evaluates whether Stotal >= tau_verify. If True, the activity transitions to Emission and Logging, terminating successfully. If False, the flow evaluates whether Retry Counter < N_max. If True, Negative Constraints are formulated, Retry Counter is incremented, and control loops back to Query Planning. If False, a Deterministic Fallback Error Response is emitted, terminating the cycle safely."
    },
    {
        "type": "nano_banana",
        "name": "UML Activity Diagram",
        "caption": "Figure 4.8: UML Activity Diagram of the Complete Adaptive Query Resolution Lifecycle."
    },
    {
        "type": "heading2",
        "text": "4.4.4 UML Sequence Diagram"
    },
    {
        "type": "paragraph",
        "text": "Figure 4.9 details the time-ordered message interactions between collaborating agents and storage subsystems during a query resolution sequence. The sequence tracks messages exchanged across: User -> API Gateway -> StateEngine -> PlannerAgent -> PolicyRouter -> VectorRetriever / GraphRetriever -> HybridFuser -> GeneratorAgent -> VerifierAgent -> ReflectionAgent -> AuditMemory. The diagram explicitly models both the happy-path execution and the cyclic reflection loop triggered upon initial verification failure."
    },
    {
        "type": "nano_banana",
        "name": "UML Sequence Diagram",
        "caption": "Figure 4.9: UML Sequence Diagram of End-to-End Query Orchestration and Gated Verification."
    },
    {
        "type": "heading2",
        "text": "4.4.5 UML Component Diagram"
    },
    {
        "type": "paragraph",
        "text": "Figure 4.10 illustrates the high-level physical software components and containerized deployment topology. The architecture comprises seven containerized microservices managed via Docker Compose / Kubernetes:\n• Client Web UI Component (React.js, Nginx on port 80/443)\n• API Gateway & Orchestrator Component (FastAPI, Python 3.11 on port 8000)\n• LangGraph Multi-Agent Execution Worker Component (Celery / Asyncio Worker Pool)\n• Knowledge Graph Database Component (Neo4j Enterprise on ports 7474/7687)\n• Vector Search Service Component (ChromaDB on port 8001)\n• Algorithmic Verification Engine Component (RAGAS / FActScore evaluation daemon)\n• Audit & Checkpoint Persistence Component (PostgreSQL 16 on port 5432)"
    },
    {
        "type": "nano_banana",
        "name": "UML Component Diagram",
        "caption": "Figure 4.10: UML Component Diagram of the Containerized Microservice Infrastructure."
    }
]

print("Chapter 4 content prepared successfully.")
