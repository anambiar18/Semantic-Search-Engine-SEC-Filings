# Semantic-Search-Engine-SEC-Filings

## Overview
This project implements a semantic search engine for SEC filings (10-K/10-Q) using a FastAPI backend and a React frontend. The system allows users to search through SEC filings efficiently and effectively.

### Features:
- Ingestion of raw SEC filings, transforming them into clean text and performing section-aware chunking.
- Storage of text chunks and their embeddings in a Postgres database using pgvector.
- Hybrid retrieval mechanism that combines BM25 full-text search with vector approximate nearest neighbor (ANN) search, utilizing Reciprocal Rank Fusion for improved results.
- An API endpoint `/search?q=...` that returns the top snippets along with their citations.
- A minimalistic React user interface featuring a search bar and result cards for displaying search results.
- Evaluation scripts to measure performance using Recall@10 and nDCG metrics.

## Tech Stack
- **Backend**: FastAPI, psycopg2, sentence-transformers
- **Database**: Postgres with pgvector
- **Frontend**: React with Tailwind CSS
- **Infrastructure**: Docker Compose

## Setup Instructions
1. Clone the repository.
2. Navigate to the `backend` directory and install the required Python packages listed in `requirements.txt`.
3. Set up the Postgres database and configure the connection settings in the application.
4. Run the backend server using FastAPI.
5. Navigate to the `frontend` directory and install the necessary npm packages.
6. Start the React application.
7. Use the provided API endpoint to search through SEC filings.

## Usage
- Access the frontend application in your web browser.
- Enter your search query in the search bar to retrieve relevant SEC filing snippets.
- Review the results displayed in the result cards, which include citations for reference.

## Evaluation
To evaluate the search engine's performance, run the scripts located in the `eval` directory to compute Recall@10 and nDCG metrics. These evaluations will help assess the effectiveness and ranking quality of the search results.