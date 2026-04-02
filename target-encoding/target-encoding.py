def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    import numpy as np
    categories=np.array(categories)
    targets=np.array(targets)
    uniques=np.unique(categories)
    encoding=np.zeros(len(uniques))
    for i in range(len(uniques)):
        mean=np.mean(targets[categories==uniques[i]])
        encoding[i]=mean
    mp=dict(zip(uniques,encoding))
    result=[mp[c] for c in categories]
    return result