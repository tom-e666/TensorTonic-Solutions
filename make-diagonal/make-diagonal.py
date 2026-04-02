import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v=np.array(v,dtype=float)
    
    return np.diag(v)
    
