import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p,y=map(np.array,(p,y))
    dice= (np.sum(p*y)*2 +eps)/(np.sum(p)+np.sum(y) +eps)
    dl=1-dice
    return dl