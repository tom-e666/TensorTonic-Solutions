def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    scores= list(enumerate(scores))
    scores= sorted(scores, key = lambda x: x[1], reverse= True)
    res=[]
    for idx, score in scores:
        if idx not in rated_indices:
            res.append(idx)
            if len(res) ==k:
                break
    return res
        
        
    
        