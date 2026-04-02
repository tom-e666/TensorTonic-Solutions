import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v= np.array(v,dtype=float)
    if v.ndim == 1:
        norm = np.linalg.norm(v,keepdims=True)
        norm=np.where(norm!=0, norm, 1)
        
        v/=norm
    if v.ndim == 2:
        norms = np.linalg.norm(v, axis=1, keepdims=True)
        norms=np.where(norms!=0, norms, 1)
        v /= norms
    return v
    