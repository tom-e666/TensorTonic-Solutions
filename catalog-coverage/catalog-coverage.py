import numpy as np

def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # flatten list of lists
    recs = [item for sublist in recommendations for item in sublist]
    unique_items = set(recs)
    
    if n_items == 0:
        return 0.0
    
    coverage = len(unique_items) / n_items
    return float(coverage)
