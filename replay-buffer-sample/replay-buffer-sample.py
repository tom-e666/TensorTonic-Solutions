def replay_buffer_sample(buffer, batch_size, seed):
    """
    Sample a batch of transitions from the replay buffer.
    """
    # Write code here
    import numpy as np
    rand= np.random.RandomState(seed=seed)
    idx=rand.choice(len(buffer),size=batch_size, replace=False)
    res=[buffer[i] for i in idx]
    return res
