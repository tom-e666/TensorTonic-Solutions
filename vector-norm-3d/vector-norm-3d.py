import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    v= np.array(v)
    x=v[...,0]
    y=v[...,1]
    z=v[...,2]
    res = np.sqrt(x*x + y*y +z*z)
    return res
    