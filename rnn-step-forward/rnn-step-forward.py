import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    x_t,h_prev,Wx, Wh,b=map(np.array,(x_t,h_prev,Wx, Wh,b))
    pre_act=x_t@Wx + h_prev@Wh +b
    ht=np.tanh(pre_act)
    return ht
