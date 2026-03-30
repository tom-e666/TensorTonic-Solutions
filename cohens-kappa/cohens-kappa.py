import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    rater1 = np.array(rater1)
    rater2 = np.array(rater2)
    N=len(rater1)
    po=np.sum(rater1==rater2)/N
    labels = np.unique(np.concatenate([rater1, rater2]))
    pe=0
    for label in labels:
        p1=np.sum(rater1==label)/N
        p2=np.sum(rater2==label)/N
        pe +=p1*p2
    if (pe==1):
        return 1
    kappa= (po-pe)/(1-pe)
    return kappa
    
    
    
    