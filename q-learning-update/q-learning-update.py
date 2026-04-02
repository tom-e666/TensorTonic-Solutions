import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    Q = np.array(Q, dtype=float)
    best_next= np.max(Q[s_next])
    td_target= r+ gamma*best_next - Q[s][a]
    Q[s][a]= Q[s][a] + alpha*td_target
    return Q