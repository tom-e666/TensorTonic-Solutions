def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    # Your code here
    from collections import defaultdict
    counts = defaultdict(int)
    for i in range(len(tokens)-1):
        w1,w2=tokens[i],tokens[i+1]
        counts[(w1,w2)]+=1
    vocab=set(tokens)
    V= len(vocab)
    first_counts= defaultdict(int)
    for (w1,w2), c in counts.items():
        first_counts[w1]+=c
    probs = {}
    for w1 in vocab:
        for w2 in vocab:
            num = counts[(w1,w2)]+1
            denom = first_counts[w1]+ V
            probs[(w1,w2)] = num/denom
    return dict(counts),probs
    
    
    
    