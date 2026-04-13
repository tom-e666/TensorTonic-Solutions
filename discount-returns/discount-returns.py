def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    # Write code here
    returns=[]
    prev=0
    for r in reversed(rewards):
        g=r + prev*gamma
        prev=g
        returns.append(g)
    
    return returns[::-1]