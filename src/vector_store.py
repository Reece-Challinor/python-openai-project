import os
import pinecone
import openai
import yaml
from dotenv import load_dotenv
from src.log_manager import logger

load_dotenv()

pinecone_api_key = os.environ.get("PINECONE_API_KEY")
pinecone_env = os.environ.get("PINECONE_ENV")
index_name = os.environ.get("PINECONE_INDEX_NAME", "my_vector_index")

pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)

if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536)
index = pinecone.Index(index_name)

def embed_text(text):
    response = openai.Embedding.create(model="text-embedding-ada-002", input=[text])
    return response['data'][0]['embedding']

def add_text_to_pinecone(unique_id, text):
    embedding = embed_text(text)
    index.upsert([(unique_id, embedding, {"text": text})])
    logger.info(f"Added text with ID {unique_id} to Pinecone.")

def query_similar_texts(query, top_k=3):
    q_embedding = embed_text(query)
    results = index.query(q_embedding, top_k=top_k, include_metadata=True)
    matches = [match['metadata']['text'] for match in results['matches']]
    logger.info(f"Querying Pinecone for context. Found {len(matches)} matches.")
    return matches
