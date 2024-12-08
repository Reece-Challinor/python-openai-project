from src.vector_store import query_similar_texts
from src.db_manager import load_recent_interactions

def build_contextual_prompt(user_prompt):
    # Get Pinecone context
    pinecone_context = query_similar_texts(user_prompt, top_k=3)
    # Get recent conversation from DB
    recent_interactions = load_recent_interactions(limit=3)
    conversation_context = "\n".join([f"User: {r.user_input}\nAssistant: {r.model_response}" for r in reversed(recent_interactions)])
    final_prompt = "\n\n".join(pinecone_context + [conversation_context, user_prompt])
    return final_prompt
