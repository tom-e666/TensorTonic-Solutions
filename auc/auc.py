import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    thresholds=len(fpr)
    auc=0
    for i in range(thresholds-1):
        auc+=(tpr[i]+tpr[i+1]) * (fpr[i+1]-fpr[i])/2
    return auc







