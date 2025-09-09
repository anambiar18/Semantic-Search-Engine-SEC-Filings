# Evaluation Scripts for Semantic Search Engine

## Overview
This directory contains scripts for evaluating the performance of the semantic search engine specifically focusing on two key metrics: Recall@10 and normalized Discounted Cumulative Gain (nDCG). These metrics help assess the effectiveness and ranking quality of the search results returned by the engine.

## Files
- **recall_at_10.py**: This script implements the logic for calculating the Recall@10 metric. It evaluates how many of the top 10 retrieved results are relevant to the search query.
  
- **ndcg.py**: This script calculates the nDCG metric, which measures the ranking quality of the search results by considering the position of relevant documents in the result set.

## Usage
To run the evaluation scripts, ensure that the backend is operational and that you have access to the necessary data. Execute the scripts in your Python environment to obtain the evaluation metrics.

## Interpretation of Results
- **Recall@10**: A higher Recall@10 value indicates that a larger proportion of relevant documents are found within the top 10 results, suggesting better retrieval performance.
  
- **nDCG**: The nDCG score ranges from 0 to 1, with higher values indicating better ranking quality. It accounts for the position of relevant documents, rewarding higher-ranked relevant results more than those ranked lower.

## Conclusion
These evaluation scripts are essential for understanding the performance of the semantic search engine and guiding improvements in the retrieval algorithms.