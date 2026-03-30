import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    y_true=np.array(y_true)
    y_pred=np.array(y_pred)
    mean= np.mean(y_true)
    diff=y_pred[y_pred!=y_true]
    if np.all(y_true==y_true[0]):
        if np.allclose(y_true,y_pred):
            return 1.0
        else:
            return 0.0
    rss=np.sum((y_true-y_pred)**2)
    tss=np.sum((y_true-mean)**2)
    return float(1-rss/tss)
        
    # Write code here
    pass