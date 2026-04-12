import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    """
    Compute confusion matrix with optional normalization.
    """
    # Write code here
    y_pred=np.array(y_pred)
    y_true=np.array(y_true)
    if num_classes==None:
        num_classes=max(y_pred)+1
    C=np.zeros((num_classes,num_classes))
    for i in range(num_classes):
        for j in range(num_classes):
            mask= (y_true==i) & (y_pred==j)
            C[i][j]= np.sum(mask)
    if normalize=='none':
        return C
    elif normalize=='true':
        row_s= C.sum(axis=1, keepdims=True)
        C=C/np.maximum(row_s,1)
    elif normalize=='pred':
        col_s=C.sum(axis=0,keepdims=True)
        C=C/np.maximum(col_s,1)
    elif normalize=='all':
        C = C/np.maximum(C.sum(),1)
    return C
        
    