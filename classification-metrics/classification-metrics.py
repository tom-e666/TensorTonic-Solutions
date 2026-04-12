import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    y_true=np.array(y_true)
    y_pred=np.array(y_pred)
    eps=1e-12
    num_labels=max(max(y_pred),max(y_true)) +1
    if average=='micro':
        tp=np.sum(y_true==y_pred)
        acc=(tp)/len(y_pred)
        pre=tp/(len(y_true)+eps)
        recall=tp/(len(y_true)+eps)
        f1= tp/(len(y_true)+eps)
        return {"accuracy": acc, "precision": pre, "recall": recall, "f1": f1}
    elif average=='macro':
        acct,pret,recallt,f1t=[],[],[],[]
        for label in range(num_labels):
            tp=np.sum((y_true==label) &( y_pred==label))
            tn=np.sum((y_true!=label) &( y_pred!=label))
            fp=np.sum((y_true!=label) &( y_pred==label))
            fn=np.sum((y_true==label) &( y_pred!=label))
            acc=(tp+tn)/len(y_pred)
            pre=tp/(tp+fp+eps)
            recall=tp/(tp+fn+eps)
            f1= 2*recall*pre/(recall+pre)
            acct.append(acc)
            pret.append(pre)
            recallt.append(recall)
            f1t.append(f1)
        return {"accuracy": np.sum(y_true==y_pred)/len(y_true), "precision": np.mean(pret), "recall": np.mean(recallt), "f1": np.mean(f1t)}
    elif average=='weighted':
        acct,pret,recallt,f1t=[],[],[],[]
        for label in range(num_labels):
            tp=np.sum((y_true==label) &( y_pred==label))
            tn=np.sum((y_true!=label) &( y_pred!=label))
            fp=np.sum((y_true!=label) &( y_pred==label))
            fn=np.sum((y_true==label) &( y_pred!=label))
            acc=(tp+tn)/len(y_pred)
            pre=tp/(tp+fp+eps)
            recall=tp/(tp+fn+eps)
            f1= 2*recall*pre/(recall+pre)
            count_label=np.sum(y_true==label)
            acct.append(acc*count_label/len(y_true))
            pret.append(pre*count_label/len(y_true))
            recallt.append(recall*count_label/len(y_true))
            f1t.append(f1*count_label/len(y_true))
        return {"accuracy": np.sum(y_true==y_pred)/len(y_true), "precision": np.sum(pret), "recall": np.sum(recallt), "f1": np.sum(f1t)}
    elif average=='binary':
        acct,pret,recallt,f1t=[],[],[],[]
        label=pos_label
        tp=np.sum((y_true==label) &( y_pred==label))
        tn=np.sum((y_true!=label) &( y_pred!=label))
        fp=np.sum((y_true!=label) &( y_pred==label))
        fn=np.sum((y_true==label) &( y_pred!=label))
        acc=(tp+tn)/len(y_pred)
        pre=tp/(tp+fp+eps)
        recall=tp/(tp+fn+eps)
        f1= 2*recall*pre/(recall+pre)
        acct.append(acc)
        pret.append(pre)
        recallt.append(recall)
        f1t.append(f1)
        return {"accuracy": np.sum(y_true==y_pred)/len(y_true), "precision": np.mean(pret), "recall": np.mean(recallt), "f1": np.mean(f1t)
}
y_true=[0,1,2,2]
y_pred=[0,1,0,2]
print(classification_metrics(y_true, y_pred, average="micro"))