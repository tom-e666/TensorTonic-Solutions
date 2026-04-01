def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    import numpy as np
    x1= np.array(x1)
    x2= np.array(x2)
    cos= x1.dot(x2)/np.linalg.norm(x1)/np.linalg.norm(x2)
    if label==1:
        return 1-cos
    if label ==-1:
        return max(0, cos-margin)
    