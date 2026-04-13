import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    # Write code here
    n=len(states)
    returns=np.zeros(n)
    last_return=0
    for i,(s,r) in reversed(list(enumerate(zip(states,rewards)))):
        returns[i]=r + gamma*last_return
        last_return=returns[i]
    returns-=V
    return returns
    
