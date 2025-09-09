from typing import List
import os
import re

def clean_text(raw_text: str) -> str:
    # Remove unnecessary whitespace and special characters
    cleaned_text = re.sub(r'\s+', ' ', raw_text).strip()
    return cleaned_text

def chunk_text(cleaned_text: str, section_delimiter: str = r'\n\n') -> List[str]:
    # Split the cleaned text into chunks based on the section delimiter
    chunks = re.split(section_delimiter, cleaned_text)
    return [chunk for chunk in chunks if chunk]

def process_filings(raw_filings: List[str]) -> List[dict]:
    processed_filings = []
    
    for filing in raw_filings:
        cleaned = clean_text(filing)
        chunks = chunk_text(cleaned)
        
        for chunk in chunks:
            processed_filings.append({
                'chunk': chunk,
                'length': len(chunk)
            })
    
    return processed_filings

def save_chunks_to_db(chunks: List[dict], db_session) -> None:
    for chunk in chunks:
        # Assuming a SQLAlchemy model named FilingChunk exists
        filing_chunk = FilingChunk(content=chunk['chunk'], length=chunk['length'])
        db_session.add(filing_chunk)
    db_session.commit()