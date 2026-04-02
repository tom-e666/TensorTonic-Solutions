def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    """
    Perform one SARSA update and return the updated Q-table.
    """
    # Write code here
    import numpy as np 
    q=np.array(q_table,dtype=float)
    error = reward + gamma*q[next_state,next_action]-q[state,action]
    s,a=state,action
    q[s][a]=q[s][a]+ alpha*error
    return q
    
    
    