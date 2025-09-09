from typing import List, Dict, Any
from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import FilingChunk
from .vector_search import vector_search  # Assuming you have a vector search implementation

def hybrid_search(query: str, db: Session, top_k: int = 10) -> List[Dict[str, Any]]:
    # Perform BM25 search
    bm25_results = db.query(FilingChunk).filter(FilingChunk.text.ilike(f"%{query}%")).limit(top_k).all()
    
    if not bm25_results:
        raise HTTPException(status_code=404, detail="No results found")

    # Extract IDs for vector search
    bm25_ids = [result.id for result in bm25_results]

    # Perform vector search
    vector_results = vector_search(query, top_k)

    # Combine results
    combined_results = {result.id: result for result in bm25_results}

    for result in vector_results:
        if result.id not in combined_results:
            combined_results[result.id] = result

    # Sort combined results based on some ranking criteria
    sorted_results = sorted(combined_results.values(), key=lambda x: x.rank_score, reverse=True)

    return sorted_results[:top_k]  # Return top K results