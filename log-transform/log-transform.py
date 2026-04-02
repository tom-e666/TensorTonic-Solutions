def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    import numpy as np
    return [np.log(value+1) for value in values] 