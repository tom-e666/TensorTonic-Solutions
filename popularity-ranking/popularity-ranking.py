import numpy as np
def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    
    #bayesian weighted rating
    res =[]
    for item in items:
        r,v= item
        rank = v/(v+ min_votes)*r + min_votes/(v+ min_votes)*global_mean
        res.append(rank)
    return res