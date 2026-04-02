def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    import numpy as np
    
    cur=1
    res=[]
    for i in returns:
        cur*=(1+i)
        res.append(cur-1)
    return res