import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    e=np.exp(x)
    return (e - 1/e)/(e+ 1/e)
    pass