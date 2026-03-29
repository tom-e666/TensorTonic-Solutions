def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    arr = {}
    for sentence in sentences:
        for word in sentence:
            word= word.lower().strip(".,!?")
            arr[word]=arr.get(word,0)+ 1
    return arr
sentences= [["i","love","ml"],["i","love","coding"]]
count = word_count_dict(sentences)
print(count)