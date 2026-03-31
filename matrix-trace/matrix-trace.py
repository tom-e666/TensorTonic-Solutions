import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A=np.array(A)
    N=A.shape[0]
    return np.sum([A[i][i] for i in range(N)])
