import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x, p = map(np.array,(x, p))
    if not np.isclose(np.sum(p),1.0):
        raise ValueError
    return float(np.dot(x,p))
    pass
