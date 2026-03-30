import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    if rng is None:
        rng = np.random.default_rng()
    x = np.array(x, dtype = float)
    mask = (rng.random(x.shape) > p)/(1-p)
    out = (x*mask)
    return out, mask
    
x=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

print(dropout(x,0.25))