import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here
    tokenized_docs = [doc.split() for doc in documents]
    vocab = list(set(word for doc in tokenized_docs for word in doc))
    vocab.sort()
    vocab_index= {word: i for i, word in enumerate(vocab)}

    N=len(documents)
    tfidf_mt= np.zeros((N,len(vocab)))
    df = { word : sum(1 for doc in tokenized_docs if word in doc) for word in vocab}
    for doc_idx, doc in enumerate(tokenized_docs):
        counter = Counter(doc)
        doc_len=len(doc)
        for word, count in counter.items():
            tf = count / doc_len
            # if tf>0:
            #     tf+=1
            if df[word]==0:
                idf=0
            else:
                idf= np.log((N)/ (df[word]))
            tfidf_mt[doc_idx, vocab_index[word]]=tf*idf


    return tfidf_mt,vocab
document= ["the cat sat","the cat ran","the dog sat"]
print(tfidf_vectorizer(document))

    
        
        
        
    
    
                              
    
    
    
    
    