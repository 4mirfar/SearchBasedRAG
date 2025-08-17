from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def prr_doc()

    instr = "Represent this sentence for searching relevant passages: Provide a detailed and accurate representation of the query to retrieve relevant technical documentation, explanations, or examples related to KServe."

    model = FlagModel('BAAI/bge-large-en-v1.5', 
                    query_instruction_for_retrieval=instr,
                    use_fp16=True)
    docs_dir = "./clones/KServe/website/docs"
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    all_chunks = []

    total_files = sum(len(files) for _, _, files in os.walk(docs_dir))

    for root, dirs, files in tqdm(os.walk(docs_dir), total=total_files):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                
                loader = UnstructuredMarkdownLoader(path)
                docs = loader.load()
                
                chunks = text_splitter.split_documents(docs)
                
                for idx, chunk in enumerate(chunks):
                    embedding_vector = model.encode(chunk.page_content).tolist()
                    all_chunks.append({
                        'id': f"{os.path.relpath(path)}-{idx}",
                        'content': chunk.page_content,
                        'metadata': {
                            'source': os.path.relpath(path),
                            'category': root.split('/')[-1],
                            'filename': file,
                            'embedding': embedding_vector
                        }
                    })


    with open("./data/kserve/kserve_rag_data.json", "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)