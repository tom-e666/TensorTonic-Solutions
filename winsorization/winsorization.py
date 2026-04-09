def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    # Write code here
    import numpy as np
    values=sorted(values)
    kl=(len(values)-1)*lower_pct/100
    kl_l=int(np.floor(kl))
    kl_u=int(np.ceil(kl))
    ku=(len(values)-1)*upper_pct/100
    ku_l=int(np.floor(ku))
    ku_u=int(np.ceil(ku))
    lower_bound=values[kl_l] + (kl-kl_l)*(values[kl_u] - values[kl_l])
    upper_bound=values[ku_l] + (ku-ku_l)*(values[ku_u] - values[ku_l])
    values=np.clip(values, lower_bound, upper_bound)
    return values.tolist()
    