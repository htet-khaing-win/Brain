import numpy as np

class InMemoryVectorStore:
    def __init__(self):
        self.vectors = []
        self.chunks = []

    def add_vector(self, vector, meta):
        self.vectors.append(vector)
        self.chunks.append(meta)

    def search(self, query_vector, top_k=4):
        """ Compare against all vectors and return the top_k closest ones """
        sims = [self.cosine_similarity(query_vector, v) for v in self.vectors]
        top_indices = np.argsort(sims)[-top_k:][::-1]  # Get indices of top_k highest similarities
        return [(self.chunks[i], sims[i]) for i in top_indices]
    
    def _cosine(self, a, b):
        """ Compute cosine similarity between two vectors """
        a, b = np.array(a), np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))