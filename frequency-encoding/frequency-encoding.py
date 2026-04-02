def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    import numpy as np
    v=np.array(values)
    val,counts=np.unique(v,return_counts=True)
    freq= counts/len(v)
    mapping=dict(zip(val,freq))
    return [mapping[x] for x in values]