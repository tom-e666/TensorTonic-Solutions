import numpy as np
def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    values, weights= map(np.array,(values, weights))
    N=weights.size
    wma=np.zeros(values.size-N+1)
    for i in range(values.size-N+1):      
        wma[i]= (np.dot(weights, values[i:i+N]))/np.sum(weights)
    return wma.tolist()
    