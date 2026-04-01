def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    hits=[]
    import numpy as np 
    for rec, truth in zip(recommendations,ground_truth):
        topk= rec[:k]
        hit= int(len(set(topk) & set(truth))>0)
        hits.append(hit)
    return np.mean(hits)
    