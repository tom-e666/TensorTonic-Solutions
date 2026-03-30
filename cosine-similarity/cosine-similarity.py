import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a=np.array(a)
    b= np.array(b)
    # Write code here
    return np.nan_to_num( np.dot(a,b) / np.linalg.norm(a)/np.linalg.norm(b))
    pass