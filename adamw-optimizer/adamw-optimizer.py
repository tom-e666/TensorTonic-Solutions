import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """
    w= np.array(w)
    m= np.array(m)
    v= np.array(v)
    grad = np.array(grad)
    # Write code here
    m2=beta1*m + (1-beta1)*grad
    v2=beta2*v + (1-beta2)*grad*grad
    w2= w -lr*weight_decay*w - lr*m2/(v2**0.5+eps)
    return w2,m2,v2
    