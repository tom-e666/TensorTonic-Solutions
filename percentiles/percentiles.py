import numpy as np

def percentiles(x, q):

    x = np.array(x, dtype = float)
    q= np.array(q, dtype = float)
    x.sort()
    n= x.size
    res = []
    for p in q:
        pos= (n-1)*p/100
        lower= int (np.floor(pos))
        upper = int (np.ceil(pos))
        if lower == upper:
            res.append(x[lower])
        else:
            weight= pos- lower
            interp= x[lower]+ weight* (x[upper]- x[lower])
            res.append(interp)
    return np.array(res)