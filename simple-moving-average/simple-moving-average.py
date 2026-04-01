def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    import numpy as np
    values= np.array(values, dtype= float)
    if window_size <= 0:
        raise ValuesError("window_size must be postitive")
    sma = []
    for i in range(len(values)-window_size+1):
        window= values[i:i+window_size]
        sma.append(np.mean(window))
    return sma
        
