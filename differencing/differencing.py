import numpy as np
def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    series= np.array(series)
    for _ in range(order):
        series = np.diff(series)
    return series.tolist()
        