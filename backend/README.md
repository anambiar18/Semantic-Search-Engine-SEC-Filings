# backend README

## Overview
This backend is built using FastAPI and is designed to serve as the API for a semantic search engine focused on SEC filings (10-K/10-Q). It handles the ingestion of raw SEC filings, stores processed data in a PostgreSQL database, and provides an API for searching through the filings.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd semantic-search-engine-sec-filings/backend
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database**:
   - Ensure PostgreSQL is installed and running.
   - Create a database for the application.
   - Update the database connection settings in the application as needed.

5. **Run the application**:
   ```
   uvicorn app.main:app --reload
   ```

## API Endpoints
- **Search Endpoint**: 
  - **URL**: `/search?q=<query>`
  - **Method**: GET
  - **Description**: Returns the top snippets from SEC filings based on the search query.

## Directory Structure
- `app/`: Contains the main application code.
  - `api/`: Contains API endpoint logic.
  - `db/`: Contains database models and configurations.
  - `ingestion/`: Contains logic for processing and ingesting SEC filings.
  - `retrieval/`: Contains logic for hybrid retrieval of search results.
  - `main.py`: Entry point for the FastAPI application.

## Evaluation
Scripts for evaluating the search engine's performance are located in the `eval/` directory. These include metrics such as Recall@10 and nDCG.

## License
This project is licensed under the MIT License. See the LICENSE file for details.