import numpy as np

import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    anchor = np.array(anchor, dtype=float)
    positive = np.array(positive, dtype=float)
    negative = np.array(negative, dtype=float)
    # print(anchor)
    # print(positive)
    # print(anchor - positive)

    dap = np.sum((anchor - positive) ** 2,axis=-1)
    dan = np.sum((anchor - negative) ** 2,axis=-1)
    loss=np.maximum(0.0, dap-dan+margin)
    return np.mean(loss)

anchor=[[0.5,-0.3,1.2,0.1,-0.7],[-0.4,0.8,-0.5,1.1,0.3],[1,0.2,-0.8,0.4,0.6],[-0.1,-0.9,0.7,-0.3,1.4],[0.3,1.1,0.5,-0.6,-0.2],[-0.7,0.4,1.3,0.8,-0.1],[0.9,-0.5,-0.3,1,0.2],[-0.2,0.7,0.4,-0.8,0.9],[1.1,-0.4,0.6,0.3,-0.5],[0.4,0.2,-0.9,1.2,0.7]]

negative=[[2.5,1.7,3.2,2.1,1.3],[0.1,1.3,-0.2,1.6,0.8],[3,2.2,1.2,2.4,2.6],[0.3,-0.4,1.1,0.1,1.8],[2.3,3.1,2.5,1.4,1.8],[-0.2,0.9,1.6,1.1,0.2],[2.9,1.5,1.7,3,2.2],[0.2,1.1,0.7,-0.3,1.4],[3.1,1.6,2.6,2.3,1.5],[0.8,0.5,-0.4,1.7,1.1]]
positive=[[0.6,-0.2,1.3,0.2,-0.6],[-0.3,0.9,-0.4,1.2,0.4],[1.1,0.3,-0.7,0.5,0.7],[0,-0.8,0.8,-0.2,1.5],[0.4,1.2,0.6,-0.5,-0.1],[-0.6,0.5,1.4,0.9,0],[1,-0.4,-0.2,1.1,0.3],[-0.1,0.8,0.5,-0.7,1],[1.2,-0.3,0.7,0.4,-0.4],[0.5,0.3,-0.8,1.3,0.8]]
print(triplet_loss(anchor, positive, negative))

