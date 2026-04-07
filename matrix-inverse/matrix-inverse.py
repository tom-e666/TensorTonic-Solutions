import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    a= np.array(A)
    if a.ndim!= 2 or a.shape[0]!=a.shape[1]:
        return None
    det=np.linalg.det(a)
    if det==0:
        return None
    inv_a=np.linalg.inv(a)
    return inv_a
    
