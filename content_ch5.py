# content_ch5.py
# Chapter 5: Mathematical Model & Algorithmic Mechanics text, equations, tables, algorithms, and structure

CH5_TITLE = ("CHAPTER 5", "MATHEMATICAL MODEL & ALGORITHMIC MECHANICS")

CH5_TABLE1_DATA = {
    "caption": "Table 5.1: Mathematical Notation, Symbol Definitions, and Tensor Dimensions",
    "headers": ["Symbol / Variable", "Mathematical Domain / Dimension", "Formal Definition & Operational Role"],
    "widths": [1.8, 1.8, 3.8],
    "rows": [
        ["Q, Q_rewritten", "Text String / Token Sequence", "Original natural language user query and normalized, expanded query string."],
        ["E(Q)", "R^d (d = 1536)", "Dense semantic embedding vector generated via bi-encoder neural model."],
        ["w_c", "R^d (d = 1536)", "Learnable projection weight vector for linear combination with query embedding."],
        ["b_c", "R (Scalar)", "Scalar bias term calibrated for sigmoid centering."],
        ["|E_Q|", "Z^+ (Non-negative Integer)", "Total count of explicit named entities identified in query Q."],
        ["depth_Q", "Z^+ (Integer >= 1)", "Estimated multi-hop relational traversal depth required to resolve dependencies."],
        ["D_Q", "R^+ (Continuous Scalar)", "Local subgraph density surrounding the recognized named entities in the graph."],
        ["omega_1, omega_2, omega_3", "R^+ (Weights)", "Hyperparameter scaling weights for topological graph complexity indicators."],
        ["C(Q)", "[0, 1] (Continuous Scalar)", "Composite multi-hop query complexity score governing policy dispatch."],
        ["tau_1, tau_2", "[0, 1] (Threshold Scalars)", "Calibrated routing thresholds: tau_1 separates Vector; tau_2 separates Graph."],
        ["P(Q)", "{Vector, Hybrid, Graph}", "Discrete routing decision emitted by the Policy Selection Module."],
        ["e = (u, v)", "E_G (Directed Edge)", "Directed factual edge in knowledge graph connecting head node u to tail node v."],
        ["w_0", "(0, 1] (Scalar)", "Initial confidence weight assigned during entity-relation extraction."],
        ["lambda", "R^+ (Decay Rate)", "Continuous exponential temporal decay rate constant (lambda > 0)."],
        ["t_0, t_e", "R^+ (Epoch Timestamps)", "Current system execution timestamp and factual edge creation origin timestamp."],
        ["w(e, t_0)", "[0, 1] (Time-decayed Weight)", "Chronologically adjusted edge confidence weight at execution time t_0."],
        ["tau_decay", "(0, 1) (Pruning Threshold)", "Scalar confidence threshold below which edges are dynamically pruned."],
        ["Y, K", "Text Sequence / Subgraph", "Candidate LLM-generated response and retrieved fused context repository."],
        ["A(Y)", "Set of Atomic Claims", "Discrete set of atomic factual propositions decomposed from candidate response Y."],
        ["S_faith(Y, K)", "[0, 1] (Faithfulness Metric)", "Programmatic context faithfulness score computed via FActScore / RAGAS."],
        ["S_ans_rel(Y, Q)", "[0, 1] (Relevance Metric)", "Semantic cosine alignment between candidate response Y and prompt Q."],
        ["S_temp(K)", "[0, 1] (Temporal Metric)", "Mean chronological validity score of all retrieved context edges."],
        ["alpha, beta, gamma", "[0, 1] (Coefficients)", "Verification weight normalization coefficients satisfying alpha + beta + gamma = 1."],
        ["S_total", "[0, 1] (Composite Score)", "Final extrinsic factual verification score evaluated by the Verifier Agent."],
        ["tau_verify", "[0, 1] (Gating Threshold)", "Strict minimum composite score threshold required for response emission."],
        ["N_retry, N_max", "Z^+ (Integer Counters)", "Current reflection loop counter and maximum bounded retry threshold (N_max = 3)."]
    ]
}

ALGORITHM_5_1_TEXT = """Algorithm 5.1: Adaptive Multi-Agent GraphRAG State Orchestration Algorithm
Input: Raw User Query Q_raw, Hybrid Repositories (Vector DB D_vec, Graph DB D_graph), Thresholds (tau_1, tau_2, tau_verify, tau_decay), Max Retries N_max
Output: Verified Response Y_final with Citation Graph or Deterministic Fallback Error Response

1:  Initialize Global State Schema S = {
        Q_raw: Q_raw, Q_rewritten: "", Tasks: [], K_fused: [], 
        Y_gen: "", S_total: 0.0, N_retry: 0, F_neg: [], Status: "PROCESSING"
    }
2:  S.Q_rewritten <- PreRetrievalRewrite(S.Q_raw)   // Normalize acronyms, coreference
3:  S.Tasks <- PlannerAgent.Decompose(S.Q_rewritten, S.F_neg)   // CoT planning
4:  
5:  while S.N_retry <= N_max do
6:      S.K_fused <- []
7:      for each subtask t in S.Tasks do
8:          C_t <- ComputeQueryComplexity(t, D_graph)   // Equation (5.1)
9:          P_t <- EvaluateRoutingPolicy(C_t, tau_1, tau_2)   // Equation (5.2)
10:         
11:         if P_t == "Vector" then
12:             K_t <- VectorRetriever.ANN_Search(t, D_vec, top_k=5)
13:         else if P_t == "Graph" then
14:             K_t <- GraphRetriever.TraverseAndPrune(t, D_graph, tau_decay)
15:         else    // Hybrid Modality
16:             K_vec <- VectorRetriever.ANN_Search(t, D_vec, top_k=5)
17:             K_graph <- GraphRetriever.TraverseAndPrune(t, D_graph, tau_decay)
18:             K_t <- ReciprocalRankFusion(K_vec, K_graph, k=60)
19:         end if
20:         S.K_fused.Append(K_t)
21:     end for
22:     
23:     S.Y_gen <- GeneratorAgent.Synthesize(S.Q_rewritten, S.K_fused, S.F_neg)
24:     S.S_total <- VerifierAgent.ComputeCompositeScore(S.Y_gen, S.K_fused, S.Q_rewritten)
25:     
26:     if S.S_total >= tau_verify then
27:         S.Status <- "CERTIFIED"
28:         AuditLogger.Persist(S)
29:         return EmitResponse(S.Y_gen, S.K_fused, S.S_total)
30:     else
31:         S.N_retry <- S.N_retry + 1
32:         if S.N_retry > N_max then
33:             S.Status <- "FALLBACK_TERMINATED"
34:             AuditLogger.Persist(S)
35:             return EmitSafeFallback("Verification threshold failed after maximum retries.")
36:         end if
37:         S.F_neg <- ReflectionAgent.GenerateNegativeFeedback(S.Y_gen, S.K_fused, S.S_total)
38:         S.Tasks <- PlannerAgent.Replan(S.Q_rewritten, S.F_neg)
39:     end if
40: end while"""

ALGORITHM_5_2_TEXT = """Algorithm 5.2: Query Complexity Estimation and Policy Switching Algorithm
Input: Query Token Sequence Q, Entity Dictionary, Graph Database D_graph, Weights (w_c, b_c, omega_1, omega_2, omega_3), Thresholds (tau_1, tau_2)
Output: Complexity Score C(Q) in [0, 1] and Routing Decision P(Q) in {Vector, Hybrid, Graph}

1:  E(Q) <- BiEncoderEmbed(Q)   // Generate d-dimensional dense vector in R^d
2:  Entities_Q <- NamedEntityRecognizer(Q)
3:  N_entities <- |Entities_Q|
4:  
5:  if N_entities == 0 then
6:      depth_Q <- 1
7:      D_Q <- 0.0
8:  else
9:      Subgraphs <- D_graph.Extract1HopNeighborhood(Entities_Q)
10:     depth_Q <- EstimateRelationalDepth(Q, Entities_Q)
11:     D_Q <- CalculateGraphDensity(Subgraphs)
12: end if
13: 
14: LinearLogit <- DotProduct(w_c, E(Q)) + b_c + (omega_1 * N_entities) + (omega_2 * depth_Q) + (omega_3 * D_Q)
15: C(Q) <- 1.0 / (1.0 + exp(-LinearLogit))   // Equation (5.1) Logistic Sigmoid
16: 
17: if C(Q) < tau_1 then
18:     P(Q) <- "Vector"
19: else if C(Q) <= tau_2 then
20:     P(Q) <- "Hybrid"
21: else
22:     P(Q) <- "Graph"
23: end if
24: 
25: return (C(Q), P(Q))"""

ALGORITHM_5_3_TEXT = """Algorithm 5.3: Temporal Graph Traversal and Pruning Algorithm
Input: Subtask Query t, Graph Database D_graph, Decay Rate lambda, Current Epoch Time t_0, Pruning Threshold tau_decay, Max Hops H_max
Output: Pruned Subgraph Context K_graph

1:  SeedEntities <- ExtractEntities(t)
2:  ActiveNodes <- SeedEntities
3:  PrunedEdges <- []
4:  RetrievedTriplets <- []
5:  
6:  for hop = 1 to H_max do
7:      CandidateEdges <- D_graph.FetchIncidentEdges(ActiveNodes)
8:      NextHopNodes <- []
9:      
10:     for each edge e = (u, r, v) in CandidateEdges do
11:         t_e <- e.OriginTimestamp
12:         w_0 <- e.ExtractionWeight
13:         delta_t <- max(0.0, t_0 - t_e)
14:         
15:         // Calculate Exponential Temporal Weight via Equation (5.3)
16:         w_decay <- w_0 * exp(-lambda * delta_t)
17:         
18:         if w_decay >= tau_decay then
19:             e.ActiveWeight <- w_decay
20:             PrunedEdges.Append(e)
21:             RetrievedTriplets.Append((u, r, v, w_decay))
22:             NextHopNodes.Append(v)
23:         end if
24:     end for
25:     ActiveNodes <- Unique(NextHopNodes)
26:     if IsEmpty(ActiveNodes) then break
27: end for
28: 
29: K_graph <- SerializeTripletsToStructuredContext(PrunedEdges)
30: return K_graph"""

ALGORITHM_5_4_TEXT = """Algorithm 5.4: Extrinsic Verification Gating and Negative Reflection Algorithm
Input: Candidate Answer Y, Retrieved Fused Context K, Rewritten Query Q, Normalization Coefficients (alpha, beta, gamma), Threshold tau_verify
Output: Composite Score S_total, Gating Decision in {ACCEPT, REJECT}, Negative Constraints F_neg

1:  // Step 1: Decompose Answer into Atomic Propositions via FActScore
2:  AtomicClaims A(Y) <- DecomposeIntoAtomicPropositions(Y)
3:  SupportedCount <- 0
4:  ViolatingPropositions <- []
5:  
6:  for each claim a in A(Y) do
7:      is_supported <- EvaluatorModel.CheckContextEntailment(claim=a, context=K)
8:      if is_supported == True then
9:          SupportedCount <- SupportedCount + 1
10:     else
11:         ViolatingPropositions.Append(a)
12:     end if
13: end for
14: S_faith <- SupportedCount / max(1, |A(Y)|)   // Equation (5.6)
15: 
16: // Step 2: Calculate Semantic Answer Relevance via Cosine Similarity
17: Emb_Y <- BiEncoderEmbed(Y)
18: Emb_Q <- BiEncoderEmbed(Q)
19: S_ans_rel <- DotProduct(Emb_Y, Emb_Q) / (Norm(Emb_Y) * Norm(Emb_Q))   // Equation (5.7)
20: 
21: // Step 3: Calculate Mean Temporal Context Validity
22: S_temp <- Mean([edge.ActiveWeight for edge in K.Edges])   // Equation (5.8)
23: 
24: // Step 4: Calculate Composite Score via Equation (5.5)
25: S_total <- (alpha * S_faith) + (beta * S_ans_rel) + (gamma * S_temp)
26: 
27: if S_total >= tau_verify then
28:     return (S_total, "ACCEPT", [])
29: else
30:     // Synthesize Explicit Negative Reflection Constraints
31:     F_neg <- FormulateNegativeFeedback(ViolatingPropositions, S_total)
32:     return (S_total, "REJECT", F_neg)
33: end if"""

CH5_SECTIONS = [
    {
        "type": "heading1",
        "text": "5.1 MATHEMATICAL FORMULATIONS"
    },
    {
        "type": "paragraph",
        "text": "The operational integrity, policy switching dynamics, temporal graph hygiene, and extrinsic verification gating of the Adaptive Multi-Agent GraphRAG Framework are grounded in four formal mathematical formulations. These models replace stochastic heuristics with deterministic, mathematically provable execution bounds."
    },
    {
        "type": "heading2",
        "text": "5.1.1 Query Complexity & Topology Routing Model"
    },
    {
        "type": "paragraph",
        "text": "To solve Research Gap 1 (Disjointed Modality Routing), the framework formulates an autonomous Query Complexity Routing Model that evaluates whether a given natural language query requires simple vector lookups or multi-hop relational graph traversals. Given an input query Q, the model maps its dense embedding vector, recognized entity count, required traversal depth, and topological subgraph density into a continuous complexity metric C(Q) in [0, 1] via Equation (5.1):"
    },
    {
        "type": "equation_box",
        "label": "Equation (5.1)",
        "formula": "C(Q) = sigma( w_c^T E(Q) + b_c + omega_1 |E_Q| + omega_2 depth_Q + omega_3 D_Q )",
        "explanation": "where sigma(z) = 1 / (1 + exp(-z)) denotes the standard logistic sigmoid activation function; E(Q) in R^d is the d-dimensional dense semantic query embedding (d=1536); w_c in R^d is a learnable projection vector; (.)^T denotes the vector transpose operation; b_c in R is a calibrated scalar bias; |E_Q| in Z^+ is the count of explicit named entities extracted from Q; depth_Q in Z^+ represents the estimated relation traversal depth; D_Q in R^+ is the local subgraph density around the recognized entities in Neo4j; and omega_1, omega_2, omega_3 in R^+ are non-negative hyperparameter scaling coefficients."
    },
    {
        "type": "paragraph",
        "text": "The dynamic routing policy decision P(Q) dispatches the sub-task across discrete retrieval backends based on calibrated decision thresholds tau_1 and tau_2, as defined in Equation (5.2):"
    },
    {
        "type": "equation_box",
        "label": "Equation (5.2)",
        "formula": "P(Q) = { Vector Retrieval, if C(Q) < tau_1; Hybrid Retrieval, if tau_1 <= C(Q) <= tau_2; Graph Traversal, if C(Q) > tau_2 }",
        "explanation": "where tau_1 is the lower scalar threshold isolating single-hop factual queries (default calibrated to 0.35), and tau_2 is the upper scalar threshold triggering structural knowledge graph exploration (default calibrated to 0.70). Queries falling in the intermediate interval [tau_1, tau_2] execute hybrid retrieval combining vector search and subgraph exploration."
    },
    {
        "type": "heading2",
        "text": "5.1.2 Temporal Decay Graph Pruning Model"
    },
    {
        "type": "paragraph",
        "text": "To address Research Gap 4 (Graph Construction Noise and Temporal Invalidation), the framework models knowledge decay mathematically. In dynamic enterprise corpora, the factual veracity of extracted edges diminishes over time, and automated extraction errors introduce weak spurious triplets. Each directed factual edge e = (u, v) in edge set E_G is weighted by a continuous exponential temporal decay function according to Equation (5.3):"
    },
    {
        "type": "equation_box",
        "label": "Equation (5.3)",
        "formula": "w(e, t_0) = w_0 * exp( -lambda * (t_0 - t_e) )",
        "explanation": "where e = (u, v) in E_G is a directed knowledge graph edge; w(e, t_0) in [0, 1] is the chronologically adjusted edge weight evaluated at system execution time t_0; w_0 in (0, 1] is the initial extraction confidence weight assigned during LLM extraction; lambda > 0 is the continuous temporal decay rate constant; t_0 in R^+ is the current execution epoch timestamp; t_e in R^+ is the origin timestamp recording factual edge creation; and (t_0 - t_e) in R_0^+ represents the elapsed chronological age of the fact."
    },
    {
        "type": "paragraph",
        "text": "During query execution, the Graph Retriever applies a dynamic pruning filter, defining the active subgraph edge set E_G^*(t_0) via Equation (5.4):"
    },
    {
        "type": "equation_box",
        "label": "Equation (5.4)",
        "formula": "E_G^*(t_0) = { e in E_G | w(e, t_0) >= tau_decay }",
        "explanation": "where tau_decay in (0, 1) is the pruning confidence threshold (default 0.40). Any edge whose decayed weight falls below tau_decay is dynamically excluded from traversal paths, eliminating extraction noise and obsolete facts. The factual half-life is analytically derived as t_half = ln(2) / lambda."
    },
    {
        "type": "heading2",
        "text": "5.1.3 Composite Extrinsic Verification Score Model"
    },
    {
        "type": "paragraph",
        "text": "To fundamentally resolve Research Gap 2 (The Self-Correction Paradox), candidate response Y synthesized against retrieved context K is evaluated by an extrinsic, non-LLM algorithmic gating model. The Composite Extrinsic Verification Score S_total in [0, 1] is computed as a convex combination of three orthogonal verification metrics via Equation (5.5):"
    },
    {
        "type": "equation_box",
        "label": "Equation (5.5)",
        "formula": "S_total(Y, K, Q) = alpha * S_faith(Y, K) + beta * S_ans_rel(Y, Q) + gamma * S_temp(K)",
        "explanation": "where S_total in [0, 1] is the composite factual verification score; S_faith(Y, K) in [0, 1] measures programmatic context faithfulness; S_ans_rel(Y, Q) in [0, 1] measures semantic answer relevance relative to prompt Q; S_temp(K) in [0, 1] measures the average temporal validity of retrieved context K; and alpha, beta, gamma in [0, 1] are normalization coefficients satisfying alpha + beta + gamma = 1, alpha, beta, gamma >= 0 (default: alpha = 0.55, beta = 0.30, gamma = 0.15)."
    },
    {
        "type": "paragraph",
        "text": "The programmatic Faithfulness metric S_faith(Y, K) is formally computed via FActScore atomic claim decomposition in Equation (5.6):"
    },
    {
        "type": "equation_box",
        "label": "Equation (5.6)",
        "formula": "S_faith(Y, K) = (1 / |A(Y)|) * sum_{a in A(Y)} I(K |= a)",
        "explanation": "where A(Y) is the finite set of decomposed atomic factual claims in candidate response Y; |A(Y)| is the total count of atomic claims; I(.) is the indicator function returning 1 if atomic claim a is strictly entailed by context K (K |= a), and 0 otherwise."
    },
    {
        "type": "paragraph",
        "text": "The Answer Relevance metric S_ans_rel(Y, Q) is computed as the normalized cosine similarity between dense embeddings of candidate answer Y and query Q via Equation (5.7):"
    },
    {
        "type": "equation_box",
        "label": "Equation (5.7)",
        "formula": "S_ans_rel(Y, Q) = ( E(Y) . E(Q) ) / ( ||E(Y)|| * ||E(Q)|| )",
        "explanation": "where E(Y) and E(Q) denote dense embedding vectors in R^d, (.) represents the Euclidean dot product, and ||.|| represents the L2 vector norm."
    },
    {
        "type": "paragraph",
        "text": "The Context Temporal Validity S_temp(K) evaluates the mean time-decayed weight of all factual edges contributing to context K via Equation (5.8):"
    },
    {
        "type": "equation_box",
        "label": "Equation (5.8)",
        "formula": "S_temp(K) = (1 / |E_K|) * sum_{e in E_K} w(e, t_0)",
        "explanation": "where E_K is the set of all active knowledge graph edges included in context K, and w(e, t_0) is the time-decayed weight calculated via Equation (5.3)."
    },
    {
        "type": "heading2",
        "text": "5.1.4 Reciprocal Rank Fusion (RRF) for Hybrid Modalities"
    },
    {
        "type": "paragraph",
        "text": "When the policy router selects the Hybrid modality, candidate passages retrieved from the vector index and candidate subgraphs retrieved from Neo4j are harmonized into a unified ranking using Reciprocal Rank Fusion (RRF) as defined in Equation (5.9):"
    },
    {
        "type": "equation_box",
        "label": "Equation (5.9)",
        "formula": "RRF_Score(d) = sum_{m in {Vector, Graph}} 1 / ( k + r_m(d) )",
        "explanation": "where d is an individual retrieved knowledge document or subgraph element; m in {Vector, Graph} denotes the retrieval modality; r_m(d) in Z^+ represents the integer rank position of item d within the result list emitted by modality m; and k is a smoothing hyperparameter constant (empirically set to k = 60) that prevents top-ranked outliers from disproportionately dominating the fused candidate pool."
    },
    {
        "type": "table",
        "data": CH5_TABLE1_DATA
    },
    {
        "type": "heading1",
        "text": "5.2 ALGORITHMIC PSEUDOCODE & EXECUTION STRATEGY"
    },
    {
        "type": "paragraph",
        "text": "The operational mechanics of the framework are governed by four formal algorithmic procedures executed within the LangGraph state machine runtime. Figure 5.1 depicts the stateful graph execution topology, highlighting node transitions, conditional routing edges, and cyclic reflection boundaries."
    },
    {
        "type": "nano_banana",
        "name": "LangGraph Stateful Execution Graph",
        "caption": "Figure 5.1: LangGraph Stateful Execution Graph with Cyclic Self-Correction Boundaries."
    },
    {
        "type": "algorithm_box",
        "number": "5.1",
        "title": "Adaptive Multi-Agent GraphRAG State Orchestration Algorithm",
        "code": ALGORITHM_5_1_TEXT
    },
    {
        "type": "algorithm_box",
        "number": "5.2",
        "title": "Query Complexity Estimation and Policy Switching Algorithm",
        "code": ALGORITHM_5_2_TEXT
    },
    {
        "type": "algorithm_box",
        "number": "5.3",
        "title": "Temporal Graph Traversal and Pruning Algorithm",
        "code": ALGORITHM_5_3_TEXT
    },
    {
        "type": "algorithm_box",
        "number": "5.4",
        "title": "Extrinsic Verification Gating and Negative Reflection Algorithm",
        "code": ALGORITHM_5_4_TEXT
    }
]

print("Chapter 5 content prepared successfully.")
