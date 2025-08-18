import pandas as pd
import numpy as np
import faiss

def build_faiss_index():
    chunks = pd.read_json("./data/data.json")
    metadata = pd.json_normalize(chunks["metadata"])
    chunks = chunks.drop("metadata", axis=1).join(metadata)

    embeddings = chunks["embedding"].to_numpy()
    embeddings = np.vstack(embeddings)

    embeddings = embeddings.astype("float32")
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, "faiss/faiss_index_mmap.index")