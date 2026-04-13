import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    # episodes=np.array(episodes)
    state_record=[[] for _ in range(n_states)]
    for episode in episodes:
        records=dict()
        prev=0
        for state,reward in reversed(episode):
            records[state]=reward + prev*gamma
            prev=records[state]
        for state,v in records.items():
            state_record[state].append(v)
    V=np.zeros(n_states)
    for i in range(len(state_record)):
        if len(state_record[i])!=0:
            V[i]=np.mean(state_record[i])
        else:
            V[i]=0.0
    return V
episodes=[[[0,1],[1,2],[2,3]]]
gamma=0.9
n_states=3
print(mc_policy_evaluation(episodes, gamma, n_states))
            
            
        
        
    
    
    