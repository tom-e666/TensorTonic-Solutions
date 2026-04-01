def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    W= np.array(W)
    L= (6/fan_in)**0.5
    HeW= W*2*L - L
    return HeW