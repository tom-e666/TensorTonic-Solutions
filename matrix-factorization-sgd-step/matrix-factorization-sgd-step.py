def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Write code here
    import numpy as np
    U= np.array(U)
    V= np.array(V)
    e= r- U.T.dot(V)
    U_2= U+ lr*(e*V-reg*U)
    V_2= V + lr*(e*U-reg*V)
    return U_2,V_2 