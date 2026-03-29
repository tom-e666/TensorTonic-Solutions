def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    def derivativeQ(a,b,c,x):
        return x*2*a+b
    x= x0
    for i in range(steps):
         x = x - lr*derivativeQ(a,b,c,x)
    return x




