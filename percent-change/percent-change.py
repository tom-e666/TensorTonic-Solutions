def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    import numpy as np
    series = np.array(series,dtype=float)
    diffs= series[1:]- series[:-1]
    pct= np.where(series[:-1]==0,0.0, diffs/series[:-1])
    return pct.tolist()
    
     