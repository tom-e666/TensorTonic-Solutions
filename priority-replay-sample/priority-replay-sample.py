import numpy as np
def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    # Write code 
    p,a,b= map(np.array, (priorities, alpha,beta))
    pp=p**a
    probs= pp/np.sum(pp)
    n=pp.size
    w=(n*probs)**-b
    nw=w/np.max(w)
    return [probs.tolist(),nw.tolist()]