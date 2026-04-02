def lag_features(series, lags):
    import numpy as np
    series=np.array(series)
    feats=max(lags)
    if(len(series)<=feats):
        return [[]]
    res=[]
    for i in range(feats, len(series)):
        res.append([series[i-f] for f in lags])
    return res
    