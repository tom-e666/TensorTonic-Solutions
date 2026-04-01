import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    x=np.array(X)
    mn=np.min(x,axis=axis,keepdims=True)
    mx=np.max(x,axis=axis,keepdims=True)
    x=(x-mn)/(mx-mn+eps)
    return x