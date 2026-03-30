import numpy as np

def dropout(x, p=0.5, rng=None):
    x=np.array(x)
    if rng is None:
        rng= np.random.default_rng()
    mask=(rng.random(x.shape)>p)/(1-p)
    x=x*mask
    return x,mask
    