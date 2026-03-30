def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here
    import numpy as np
    matrix = np.array(matrix,dtype= float)
    for i in range (matrix.shape[0]):
        mean= np.mean(matrix[i][matrix[i]!=0])
        matrix[i]=np.where(matrix[i]!=0, matrix[i] - mean,0.0)
    return matrix.tolist()