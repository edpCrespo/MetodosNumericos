from sympy import diff
import numpy as np
from sympy.abc import x


def newton_raphson(x_0, tol, f):
    # calculo la derivada de f respecto de x
    f_prime = diff(f, x)

    # hago la primer iter
    x_k = x_0
    x_k1 = x_k - (f(x_k) / f_prime(x_k))
    num_iter = 1

    while np.abs(x_k1 - x_k) > tol:  # si la diferencia entre iter sigue siendo mas de lo que quiero (tol), sigo
        x_k = x_k1
        x_k1 = x_k - (f(x_k) / f_prime(x_k))
        num_iter += 1

    return x_k1, num_iter


rta = newton_raphson(2, 0.00001, lambda x: x ** 2 - 2)
print(rta)
