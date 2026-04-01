import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    y=np.array(y_train)
    values, counts= np.unique(y, return_counts=True)
    res=values[np.argmax(counts)]
    return [res for _ in range (len(X_test))]