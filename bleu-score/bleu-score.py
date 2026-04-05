def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """
    # Write code here
    import math
    from collections import Counter
    precisions=[]
    for n in range(1, max_n+1):
        can_ngrams =[tuple(candidate[i:i+n]) for i in range(len(candidate)-n+1)]
        ref_ngrams =[tuple(reference[i:i+n]) for i in range(len(reference)-n+1)]
        cand_counts= Counter(can_ngrams)
        ref_counts= Counter(ref_ngrams)
        clips = {ng: min(count,ref_counts.get(ng,0)) for ng,count in cand_counts.items()}
        numerator= sum(clips.values())
        denominator= sum(cand_counts.values())
        precisions.append(numerator/denominator if denominator>0 else 0.0)
    c=len(candidate)
    r=len(reference)
    if c<r:
        bp=math.exp(1-r/c) if c>0 else 0.0
    else:
        bp=1.0
    bleu = bp* math.exp(sum(math.log(p) if p>0 else 0 for p in precisions)/max_n)
    return bleu
candidate=["the","cat","sat","on","the","mat"]
reference=["the","cat","sat","on","the","mat"]
max_n=4
print(bleu_score(candidate, reference, max_n))