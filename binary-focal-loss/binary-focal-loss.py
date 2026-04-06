def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    import numpy as np
    p,t=map(np.array,(predictions,targets))
    fl=np.where(
        t==1,
        -alpha * (1-p )**gamma *np.log(p),
        -alpha * (p) **gamma *np.log(1-p)
    )
    return np.mean(fl)