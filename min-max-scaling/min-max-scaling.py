def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    import numpy as np
    data=np.array(data)
    mins=data.min(axis=0)
    maxs=data.max(axis=0)
    scaled=np.where(maxs!=mins,(data-mins)/(maxs-mins),0.0)
    return scaled.tolist()