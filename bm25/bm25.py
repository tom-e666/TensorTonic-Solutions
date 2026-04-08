import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    #tf(t,D): term freq per doc
    #df(term): doc contain term frq count then make dict
    #idf() rever per term
    # query_tokens=np.array(query_tokens)
    # docs=np.array(docs)
    tf = []
    for doc in docs:
        counter=Counter(doc)
        dic={t: f for t,f in counter.items()}
        tf.append(dic)
    term_set=sorted({t for dic in tf for t in dic  })
    
    df=np.zeros(len(term_set))
    for i,term in enumerate(term_set):
        for dic in tf:
            if term in dic:
                df[i]+=1
    N=len(docs)
    idf=np.log((N-df+0.5)/(df+0.5) +1)
    idf=dict(zip(term_set, idf))
    bm25=np.zeros(N)
    avgdl=np.mean([len(doc) for doc in docs])
    doc_len=np.array([len(doc) for doc in docs])
    for i,doc in enumerate(docs):
        bm25[i]=sum(idf[term] * tf[i].get(term,0) * (k1+1)/(tf[i].get(term,0)+ k1*(1-b+b*doc_len[i]/avgdl)) for term in query_tokens if term in term_set)
    return bm25
query_tokens = ["machine","learning"]
docs = [["machine","learning","is","fun"], ["I","love","learning"], ["machine","learning","is","hard"]]
print(bm25_score(query_tokens, docs))
        
        
    
        
    
    
    
    
    