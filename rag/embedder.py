import ollama

def embed_text(text: str) -> list[float]:
    """Get embedding vector for a text using Ollama API"""
    response = ollama.embeddings(model='nomic-embed-text', prompt=text)
    return response['embedding'] # list of 768 floats

def embed_batch(texts: list[str]) -> list[list[float]]:
    """Get embedding vectors for a batch of texts using Ollama API"""
    return [embed_text(t) for t in texts] 

# from openai import OpenAI
# client = OpenAI()
# resp = client.embeddings.create(
#  model="text-embedding-3-small",
#  input=text,
#  dimensions=1536, 
# )
# vector = resp.data[0].embedding