def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    import numpy as np
    values=np.array(values)
    ema=np.zeros(len(values))
    ema[0]=values[0]
    for i in range (1,len(values)):
        ema[i]= alpha*values[i]+ (1-alpha)*ema[i-1]
    return ema.tolist()
    