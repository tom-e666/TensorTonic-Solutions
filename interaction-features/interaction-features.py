def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here 
    import numpy as np
    X = np.array(X,dtype=float)
    result=[]
    for sample in X:
        features=list(sample)
        width=len(sample)
        for i in range(width):
            for j in range(i+1,width):
                features.append(sample[i]*sample[j])
        result.append(features)
    return result
        
        
    
    