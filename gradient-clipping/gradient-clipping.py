import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g=np.array(g)
    g2=np.linalg.norm(g)
    if max_norm<=0:
        return g
    g=np.where(g2<=max_norm,g,g/g2*max_norm)
    return g