import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    param= np.array(param)
    grad= np.array(grad)
    m= np.array(m)
    v= np.array(v)
    
    m2=beta1*m+ (1-beta1)*grad
    v2=beta2*v+ (1-beta2)*grad*grad
    m_err= m2/(1-beta1**t)
    v_err= v2/(1-beta2**t)
    param2= param- lr*(m_err)/(np.sqrt(v_err)+eps)
    return param2, m2, v2
    # Write code here
    pass