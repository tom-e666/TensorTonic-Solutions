import numpy as np

def geometric_pmf_mean(k, p):
    k=np.array(k)
    return [p*(1-p)**(k-1), 1/p]