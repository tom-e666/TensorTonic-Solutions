import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
    a,b,y=map(np.array,(a,b,y))
    if a.ndim==1:
        a=a[None,:]
        b=b[None,:]
    # a,b=np.broadcast_arrays(a,b)
    
    d= np.linalg.norm(a-b,axis=1)
    print(d)
    l=y*d**2 + (1-y)* np.maximum(0,margin-d)**2
    if reduction=="sum":
        return np.sum(l)
    if reduction=="mean":
        return np.mean(l)
a = [[1, 2], [3, 4]]
b = [[1, 2], [5, 6]]
y = [1, 0]
print(contrastive_loss(a, b, y))