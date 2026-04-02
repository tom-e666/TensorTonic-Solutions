import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x=np.array(x)
    m=np.mean(x)
    ss=np.sum((x-m)**2)/(len(x)-1)
    s=ss**0.5
    return ss,s