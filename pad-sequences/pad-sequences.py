import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    L = max_len if max_len is not None else max(len(seq) for seq in seqs)
    padded=[]
    for seq in seqs:
        seq = list(seq)[:L]
        seq=seq+[pad_value]*(L-len(seq))
        padded.append(seq)
    return np.array(padded)
    