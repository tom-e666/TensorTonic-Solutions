import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Write code here
    import numpy as np
    rel=np.array(relevance_scores)[:k]
    idx= np.array([ i for i in range(1,len(rel)+1)])
    dcgk=np.sum((2**rel-1)/np.log2(idx+1))
    rel=np.array(sorted(relevance_scores, reverse=True))[:k]
    idcgk=np.sum((2**rel-1)/np.log2(idx+1))
    return dcgk/idcgk if idcgk!=0 else 0.0
relevance_scores=[0,1,2,3]
print(ndcg(relevance_scores, k=3))
