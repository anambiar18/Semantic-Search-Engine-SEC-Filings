from sqlalchemy import Column, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FilingChunk(Base):
    __tablename__ = 'filing_chunks'

    id = Column(String, primary_key=True)
    text = Column(Text, nullable=False)
    section = Column(String, nullable=True)
    embedding = Column(Float, nullable=False)  # Assuming embedding is stored as a float array

    def __repr__(self):
        return f"<FilingChunk(id={self.id}, section={self.section})>"