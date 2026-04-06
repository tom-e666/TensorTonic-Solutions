import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    t,p=map(np.array,(y_true,y_pred))
    py=p[np.arange(len(y_pred)),y_true]
    CE=-np.mean(np.log(py))
    return CE
    

    