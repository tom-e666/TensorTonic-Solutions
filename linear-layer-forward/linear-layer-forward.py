def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    import numpy as np
    X= np.array(X)
    W= np.array(W)
    b= np.array(b)
    return (X.dot(W)+b).tolist()
    # Write code here