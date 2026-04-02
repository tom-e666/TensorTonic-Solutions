def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    import numpy as np
    values=np.array(values,dtype=float)
    theta=values/period*2*np.pi
    encode_sine=np.sin(theta)
    encode_cossine=np.cos(theta)
    return [[float(s),float(c)] for s, c in zip(encode_sine,encode_cossine) ]