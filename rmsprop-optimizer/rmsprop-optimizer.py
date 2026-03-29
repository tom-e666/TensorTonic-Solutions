import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Convert inputs to numpy arrays
    w, g, s = map(np.array, (w, g, s))
    
    # Update running average of squared gradients
    s = beta * s + (1 - beta) * (g * g)
    
    # Update parameter
    w = w - lr * g / (np.sqrt(s) + eps)
    
    return w, s
