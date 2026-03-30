import numpy as np
def entropy_node(y):
    y= np.array(y)
    if len(y) == 0:
        return 0.0
    _,counts= np.unique(y,return_counts=True)
    probs= counts/len(y)
    entropy = -np.sum(probs * np.log2(probs))
    return entropy
y= [0, 0, 1, 1, 1]
print(entropy_node(y))