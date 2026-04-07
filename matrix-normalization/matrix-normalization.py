import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    mt=np.array(matrix)
    if axis is not None and mt.ndim<=axis:
        return None
    if mt.ndim>2:
        return None
    if norm_type=='l1':
        norm = np.sum(np.abs(mt), axis=axis,keepdims=True)
    elif norm_type=='l2':
        norm = np.sqrt(np.sum(mt**2,axis=axis,keepdims=True))
    elif norm_type=='max':
        norm = np.max(np.abs(mt),axis= axis, keepdims=True)
    else:
        return None
    norm[norm==0] = 1.0
    return mt/norm
        