import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    z1,z2=map(np.array,(Z1,Z2))
    S= z1@z2.T/temperature
    S-=np.max(S,axis=1,keepdims=True)
    L= -np.mean(np.log(np.exp(np.diag(S))/np.sum(np.exp(S), axis=1)))
    return L
z1=[[1,0],[0,1]]
z2=[[1,0],[0,1]]
print(info_nce_loss(z1, z2))

