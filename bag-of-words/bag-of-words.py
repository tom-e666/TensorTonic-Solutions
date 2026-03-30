import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    bow= np.zeros(len(vocab), dtype = int)
    bow_i={word: i for i, word in enumerate(vocab)}
    
    for token in tokens:
        if token in bow_i:
            bow[bow_i[token]]+=1
    # Your code here
    return bow