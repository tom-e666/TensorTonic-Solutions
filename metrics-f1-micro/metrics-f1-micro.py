def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    import numpy as np
    y_true=np.array(y_true)
    y_pred= np.array(y_pred)
    t= y_pred[y_true == y_pred]
    f= y_pred[y_true != y_pred]

    
    return len(t)/len(y_true)
        
    