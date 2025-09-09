from fastapi import APIRouter, Query
from typing import List, Dict
from ..db.models import FilingChunk
from ..retrieval.hybrid import search_filings

router = APIRouter()

@router.get("/search", response_model=List[Dict[str, str]])
async def search(
    q: str = Query(..., description="Search query for SEC filings"),
    top_k: int = Query(10, description="Number of top results to return")
):
    """
    Search for SEC filings based on the query and return top snippets with citations.
    """
    results = search_filings(q, top_k)
    return results