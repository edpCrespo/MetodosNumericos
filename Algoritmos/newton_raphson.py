import numpy as np

def newton_raphson(x_0, tol, f, f_prime):
    # hago la primer iter
    x_k = x_0
    x_k1 = x_k - (f(x_k) / f_prime(x_k))
    num_iter = 1

    while np.abs(x_k1 - x_k) > tol:  # si la diferencia entre iter sigue siendo mas de lo que quiero (tol), sigo
        x_k = x_k1
        x_k1 = x_k - (f(x_k) / f_prime(x_k))
        num_iter += 1

    return x_k1, num_iter

def newton_raphson_v2(x_0, tol, f, f_prime, max_iter):
    # hago la primer iter
    x_k = np.zeros(max_iter)
    x_k[0] = x_0
    x_k[1] = x_k[0] - (f(x_k[0]) / f_prime(x_k[0]))
    num_iter = 1

    while np.abs(x_k[num_iter] - x_k[num_iter-1]) > tol and num_iter <= max_iter:  # si la diferencia entre iter sigue siendo mas de lo que quiero (tol), sigo
        x_k[num_iter+1] = x_k[num_iter] - (f(x_k[num_iter]) / f_prime(x_k[num_iter]))
        num_iter += 1

    return x_k[:num_iter], num_iter

#rta = newton_raphson(2, 0.00001, lambda x: x ** 2 - 2, lambda x: 2*x)
#print(rta)


#rta = newton_raphson(2, 0.00001, lambda x: x ** 2 - 2, lambda x: 2*x)
#print(rta)
