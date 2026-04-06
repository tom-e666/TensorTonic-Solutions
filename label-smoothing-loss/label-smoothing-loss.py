def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    import numpy as np
    p,t=map(np.array,(predictions,target))
    K=len(p)
    dist = np.where(np.arange(len(p)) == t,
                   (1-epsilon)+ epsilon/K,
                   epsilon/K)
    CE=-np.sum(dist*np.log(p))
    return CE