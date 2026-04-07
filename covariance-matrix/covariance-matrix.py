import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    x= np.array(X)
    if len(x)<2 or x.ndim!=2:
        return None
    muy= np.mean(x, axis=0)
    x= x-muy
    cm = x.T / (x.shape[0]-1) @ x
    return cm