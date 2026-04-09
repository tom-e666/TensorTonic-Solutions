import numpy as np
def _median(values):
    median = 0
    mid=int((len(values)-1)/2)
    if len(values)%2==0:
        median=(values[mid]+values[mid+1])/2
    else:
        median=values[mid]
    return median
def robust_scaling(values):
    values = np.array(values, dtype=float)
    median=_median(values)
    # inclusive split
    lower_half = values[values < median]
    upper_half = values[values > median]
    if len(lower_half) ==0 or len(upper_half)==0:
        return values-median
    q1 = _median(lower_half)
    q3 = _median(upper_half)

    denom = (q3 - q1)
    if denom == 0:
        x_scaled = values - median
    else:
        x_scaled = (values - median) / denom

    return x_scaled.tolist()

values = [1,2,3,4,5]
print(robust_scaling(values))
