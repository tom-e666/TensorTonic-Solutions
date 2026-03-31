import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x= np.array(x)
    mean= np.mean(x)
    
    median = np.median(x)
    from collections import Counter
    counts= Counter(x)
    max_count= max(counts.values())
    mode = [val for val, freq in counts.items() if freq==max_count]
    mode= min(mode)
    return mean,median, mode