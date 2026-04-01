def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    import numpy as np
    res=[]
    for i in range(0,len(values)-window_size+1):
        median=np.median(values[i:i+window_size])
        res.append(median)
    return res
        