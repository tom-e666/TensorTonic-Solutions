import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x=np.array(x)
    root2=2**0.5
    return 0.5 * x * (1.0 + np.vectorize(math.erf)(x / math.sqrt(2)))
        
