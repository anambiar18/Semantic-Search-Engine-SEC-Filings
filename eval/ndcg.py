def calculate_dcg(relevance_scores):
    dcg = 0.0
    for i, score in enumerate(relevance_scores):
        if i == 0:
            dcg += score
        else:
            dcg += score / (math.log2(i + 1))
    return dcg

def calculate_ndcg(relevance_scores):
    ideal_relevance_scores = sorted(relevance_scores, reverse=True)
    dcg = calculate_dcg(relevance_scores)
    ideal_dcg = calculate_dcg(ideal_relevance_scores)
    
    if ideal_dcg == 0:
        return 0.0
    return dcg / ideal_dcg

def evaluate_ndcg(predicted_relevance, true_relevance):
    ndcg_scores = []
    for predicted, true in zip(predicted_relevance, true_relevance):
        ndcg_score = calculate_ndcg(predicted)
        ndcg_scores.append(ndcg_score)
    return ndcg_scores