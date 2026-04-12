def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    import numpy as np
    y_true=np.array(y_true)
    y_pred=np.array(y_pred)
    bins=np.linspace(0,1,n_bins+1)
    print(bins)
    n=len(y_true)
    ece=0
    for i in range(n_bins):
        in_bin= (y_pred>=bins[i]) & (y_pred< bins[i+1])
        print(in_bin)
        bin_size=np.sum(in_bin)
        if bin_size>0:
            acc= np.mean(y_true[in_bin])
            conf= np.mean(y_pred[in_bin])
            ece += (bin_size/n)* abs(acc-conf)
    return ece
y_pred=[0.9,0.9,0.9,0.9]
y_true=[1,1,1,0]
n_bins=5
print(expected_calibration_error(y_true, y_pred, n_bins))
    
        
        
    #make calculations

    