import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    y_score,y_true=np.array(y_score),np.array(y_true)
    if reduction=="mean":
        return np.mean(np.where(margin>y_true*y_score,margin-y_true*y_score,0))
    if reduction=="sum":
        return np.sum(np.where(margin>y_true*y_score,margin-y_true*y_score,0))
    