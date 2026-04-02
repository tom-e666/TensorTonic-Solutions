import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    import numpy as np
    y_true,y_pred=np.array(y_true),np.array(y_pred)
    y=np.clip(y_pred,eps,1-eps)
    loss= -(y_true*np.log(y)+(1-y_true)*np.log(1-y))
    return loss.tolist()