import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    position=np.arange(seq_len)[:,np.newaxis]
    dim=np.arange(d_model)[np.newaxis,:]
    freq= 1/np.power(base,(dim//2)*2/d_model)
    rads=position*freq #(N*M)
    pe=np.zeros((seq_len,d_model))
    pe[:,0::2]= np.sin(rads[:,0::2])
    pe[:,1::2]= np.cos(rads[:,1::2])
    return pe
    