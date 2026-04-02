def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    result=[]
    for value in values:
        result.append([value**i for i in range(degree+1)])
    return result