import os
import openai
import yaml
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec, Index
from src.log_manager import logger

# Load environment variables
load_dotenv(dotenv_path=".env")

pinecone_api_key = os.environ.get("PINECONE_API_KEY")
pinecone_env = os.environ.get("PINECONE_ENV")
index_name = os.environ.get("PINECONE_INDEX_NAME")

if not pinecone_api_key:
    logger.error("PINECONE_API_KEY not found in .env.")
if not pinecone_env:
    logger.error("PINECONE_ENV not found in .env.")
if not index_name:
    logger.error("PINECONE_INDEX_NAME not found in .env.")

# Create Pinecone client instance
pc = Pinecone(
    api_key=pinecone_api_key,
    environment=pinecone_env
)

# Check if the index exists; if not, create it
existing_indexes = pc.list_indexes().names()
if index_name not in existing_indexes:
    logger.info(f"Index {index_name} does not exist. Creating new index.")
    pc.create_index(
        name=index_name,
        dimension=1536,  # For text-embedding-ada-002
        metric='cosine', # Adjust metric if needed
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1' # Match your region if required
        )
    )
else:
    logger.info(f"Index {index_name} found.")

# Now instantiate the index using Index class directly
index = Index(
    name=index_name,
    api_key=pinecone_api_key,
    environment=pinecone_env
)

# Set OpenAI API key
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    logger.error("OPENAI_API_KEY not found in .env.")
else:
    openai.api_key = openai_api_key

def embed_text(text: str):
    try:
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=[text]
        )
        return response['data'][0]['embedding']
    except Exception as e:
        logger.error(f"Error embedding text: {e}")
        return None

def add_text_to_pinecone(unique_id: str, text: str):
    embedding = embed_text(text)
    if embedding is not None:
        index.upsert([(unique_id, embedding, {"text": text})])
        logger.info(f"Added text with ID {unique_id} to Pinecone.")
    else:
        logger.warning(f"Skipping upsert because embedding failed for ID {unique_id}.")

def query_similar_texts(query: str, top_k: int = 3):
    q_embedding = embed_text(query)
    if q_embedding is not None:
        results = index.query(q_embedding, top_k=top_k, include_metadata=True)
        matches = [match['metadata']['text'] for match in results.get('matches', [])]
        logger.info(f"Querying Pinecone for context. Found {len(matches)} matches.")
        return matches
    else:
        logger.warning("Query embedding failed, returning empty results.")
        return []
