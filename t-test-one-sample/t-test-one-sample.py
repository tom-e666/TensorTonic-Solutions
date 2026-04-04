import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x_mean=np.mean(x)
    s= (np.sum((x-x_mean)**2)/(len(x)-1))**0.5
    return (x_mean-mu0)/s*(len(x)**0.5)