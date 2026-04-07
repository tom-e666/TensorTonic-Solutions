import numpy as np

def calculate_eigenvalues(matrix):
    try:
        matrix=np.array(matrix)
    except Exception as e:
        return None
    if matrix.ndim!=2 or matrix.shape[0]!=matrix.shape[1]:
        return None
    eigenvalues,eigenvectors= np.linalg.eig(matrix)
    
    return eigenvalues