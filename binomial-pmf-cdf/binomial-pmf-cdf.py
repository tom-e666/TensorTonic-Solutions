import numpy as np
from scipy.special import comb

def PMF(n,p,k):
    return comb(n,k)*(p**k)*((1-p)**(n-k))
def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pmf=PMF(n,p,k)
    cdf=np.sum([PMF(n,p,j) for j in range(k+1)])
    return pmf, cdf
