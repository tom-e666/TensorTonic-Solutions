def compute_monitoring_metrics(system_type, y_true, y_pred):
    """
    Compute the appropriate monitoring metrics for the given system type.
    """
    import numpy as np
    # Write code here
    y_pred=np.array(y_pred)
    y_true=np.array(y_true)
    if system_type=="classification":
        tp= np.sum(np.where((y_pred==y_true)&( y_pred==1),1,0))
        tn= np.sum(np.where((y_pred==y_true)&(y_pred==0),1,0))
        fp= np.sum(np.where((y_true==0)&(y_pred==1),1,0))
        fn= np.sum(np.where((y_true==1)&(y_pred==0),1,0))
        accuracy= (tp+tn)/(len(y_pred))
        precision= tp/(tp+fp)
        recall= tp/(tp+fn)
        f1= 2*precision*recall/(precision+recall)


        return [("precision", precision), ("recall", recall), ("f1", f1), ("accuracy", accuracy)]
    if system_type=="regression":
        mae= np.mean(np.abs(y_pred-y_true))
        rmse= np.mean((y_pred-y_true)**2)**0.5
        return [("mae", mae), ("rmse", rmse)]
    if system_type=="ranking":
        
        top3= np.argsort(y_pred)[-3:]
        precision_3=np.mean(y_true[top3])
        recall_3= sum(y_true[top3])/np.sum(y_true)
        return [("precision_at_3", precision_3), ("recall_at_3", recall_3)]




        
        
        