def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    import numpy as np
    probs=[ p[a] for p, a in zip(prob_distributions,actual_tokens)]
    h = -np.mean(np.log(probs))
    return np.exp(h)