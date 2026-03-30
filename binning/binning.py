def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    import numpy as np
    min= np.min(values)
    max = np.max(values)
    if min==max:
        return np.zeros(len(values)).tolist()
    w= (max-min)/num_bins
    bins=np.floor((values-min)/w).astype(int)
    bins=np.clip(bins, 0, num_bins-1)
    
    return bins.tolist()