def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    #sort : index:value
    #set(value)
    #value-> mean(index)
    import numpy as np
    values=np.array(values, dtype=float)    
    order= values.argsort()
    ranks=np.empty_like(order,dtype=float)
    ranks[order]=np.arange(1, len(values)+1)

    result= np.zeros_like(values, dtype=float)
    unique_vals= np.unique(values)
    for val in unique_vals:
        idx= np.where(values == val)[0]
        avg_rank=ranks[idx].mean()
        result[idx]=avg_rank
    return result.tolist()
    
        
    