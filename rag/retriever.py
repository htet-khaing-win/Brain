from rank_bm25 import BM25Okapi

def hybrid_search(query, store, bm25, embed, k = 4, rrf_k = 60):
    """
    Perform a hybrid search using both BM25 and embedding-based retrieval.

    Returns:
        list: A list of tuples containing document IDs and their combined scores.
    """
    # Dense: Close match using embeddings
    dense = store.search(embed(query), top_k=10)

    # Sparse: best by keywords overlap
    sparse = bm25.get_top_n(query.split(), store.chunks, n=10)

    # Combine results using Reciprocal Rank Fusion (RRF)
    scores = {}
    for rank, (chunk, _) in enumerate(dense):
        scores[chunk.id] = scores.get(chunk.id, 0) + 1/(rrf_k + rank)
    for rank, chunk in enumerate(sparse):
        scores[chunk.id] = scores.get(chunk.id, 0) + 1/(rrf_k + rank)
    return sorted(scores, key=scores.get, reverse=True)[:k]
