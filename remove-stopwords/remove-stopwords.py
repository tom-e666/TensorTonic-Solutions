def remove_stopwords(tokens, stopwords):
    result=[]
    for token in tokens:
        if token not in stopwords:
            result.append(token)
    return result