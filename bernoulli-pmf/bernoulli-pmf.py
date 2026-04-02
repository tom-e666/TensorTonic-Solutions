import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code
    pmf=[p if y==1 else 1-p for y in x]
    mean=p
    variance= (p*(1-p))
    return np.array(pmf),mean,variance