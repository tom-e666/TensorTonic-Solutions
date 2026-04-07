import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    x= np.array(X,dtype=float)
    n_feats= x.shape[1]
    pcm=np.zeros((n_feats,n_feats))
    x_mean= np.mean(x, axis=0)
    x_std= np.std(x,axis=0, ddof=0)
    for i in range(n_feats):
        for j in range(n_feats):
            num=np.sum( (x[:, i] - x_mean[i])*(x[:,j] - x_mean[j]) )
            denom= x_std[i]*x_std[j]*x.shape[0]
            pcm[i,j]=num/denom
    return pcm
    