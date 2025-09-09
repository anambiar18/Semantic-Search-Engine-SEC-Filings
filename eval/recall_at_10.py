def calculate_recall_at_10(retrieved_results, relevant_results):
    """
    Calculate the Recall@10 metric.

    Parameters:
    - retrieved_results: List of retrieved document IDs (or relevant identifiers).
    - relevant_results: List of relevant document IDs (or relevant identifiers).

    Returns:
    - Recall@10 score as a float.
    """
    if not relevant_results:
        return 0.0

    # Consider only the top 10 retrieved results
    top_retrieved = retrieved_results[:10]
    
    # Count how many of the top retrieved results are relevant
    relevant_count = len(set(top_retrieved) & set(relevant_results))
    
    # Calculate Recall@10
    recall_at_10 = relevant_count / len(relevant_results)
    
    return recall_at_10

def evaluate_recall_at_10(retrieval_results, ground_truth):
    """
    Evaluate Recall@10 for a set of retrieval results against ground truth.

    Parameters:
    - retrieval_results: Dictionary where keys are query IDs and values are lists of retrieved document IDs.
    - ground_truth: Dictionary where keys are query IDs and values are lists of relevant document IDs.

    Returns:
    - Average Recall@10 score across all queries.
    """
    recall_scores = []
    
    for query_id, retrieved in retrieval_results.items():
        relevant = ground_truth.get(query_id, [])
        recall_score = calculate_recall_at_10(retrieved, relevant)
        recall_scores.append(recall_score)
    
    average_recall = sum(recall_scores) / len(recall_scores) if recall_scores else 0.0
    
    return average_recall