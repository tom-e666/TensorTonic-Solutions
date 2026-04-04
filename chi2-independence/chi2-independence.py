import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    c=np.array(C)
    row=np.sum(c,axis=1)
    col=np.sum(c,axis=0)
    total=np.sum(row)
    e=row[:,None]*col[None,:]/total
    chi2= np.sum((c-e)**2/e)
    return chi2,e