def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    import numpy as np
    x=np.array(x)
    x= [y if y>0 else alpha*(np.exp(y)-1) for y in x]
    return x
    # Write code here