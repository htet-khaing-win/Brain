from dataclasses import dataclass

@dataclass
class Config:
# models
    chat_model: str = "llama3.2"
    embed_model: str = "nomic-embed-text"

    # chunking
    chunk_size: int = 400
    chunk_overlap: int = 60

    # retrieval
    top_k: int = 3
    rerank_top_n: int = 20 # Retrieve total 20 and then rerank to top_k
    similarity_threshold: float = 0.55 # Calibrated later
    use_hybrid: bool = False # For BM25 + Dense


    # Generation
    temperature: float = 0.2 # randomness
    num_ctx: int = 4096 # context window size

CONFIG = Config()
