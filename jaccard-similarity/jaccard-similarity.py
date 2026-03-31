def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    # import numpy as np
    # a = np.array(set_a)
    # b= np.array(set_b)
    c = set_a+set_b
    import numpy as np
    c= np.unique(c)
    count_and=0
    count_or=0
    for i in c:
        if i in set_a and i in set_b:
            count_and+=1
    if len(set_a)==0 and len(set_b)==0:
        return 0.0
    j= count_and/len(c)
    return j
            
    