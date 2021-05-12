import numpy as np

def sec(x_0, x_1, tol, f):

    # hago la primer iter
    x_k0 = x_0
    x_k1 = x_1
    x_k2 = x_k1 - (f(x_k1)*(x_k1 - x_k0))/(f(x_k1) - f(x_k0))
    num_iter = 1

    while np.abs(f(x_k2)) > tol:  # si la diferencia entre iter sigue siendo mas de lo que quiero (tol), sigo
        x_k0 = x_k1
        x_k1 = x_k2
        x_k2 = x_k1 - (f(x_k1)*(x_k1 - x_k0))/(f(x_k1) - f(x_k0))
        num_iter += 1

    return x_k1, num_iter


rta = sec(2, 1.7, 0.0000000001, lambda x: x ** 2 - 2)
print(rta)