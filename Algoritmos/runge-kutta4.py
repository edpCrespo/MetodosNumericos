import numpy as np
import matplotlib.pyplot as plt

###############################################################################################################

def rk4(func, to, tf, delta_t, xo):
    N = int((tf - to) / delta_t) + 1  # cantidad de iteraciones
    x_k = np.zeros(N)
    t_k = np.zeros(N)  # discretizacion
    x_k[0] = xo
    t_k[0] = to

    for i in range(N-1):
        f1 = func(t_k[i], x_k[i])
        f2 = func(t_k[i] + delta_t/2, x_k[i] + (delta_t/2)*f1)
        f3 = func(t_k[i] + delta_t/2, x_k[i] + (delta_t/2)*f2)
        f4 = func(t_k[i] + delta_t, x_k[i] + delta_t*f3)
        x_k[i+1] = x_k[i] + (f1 + 2*f2 + 2*f3 + f4)*(delta_t/6)
        t_k[i+1] = t_k[i] + delta_t

    return t_k, x_k

###############################################################################################################

def funcion(x, t):
    ec = 3*x + 3*t
    return ec


x0 = 1
t0 = 0
tfi = 0.6

t1, x1 = rk4(funcion, t0, tfi, 0.01, x0)

# error = euler_error(x1, x2)

# print(error)

plt.plot(t1, x1, label='RK4')
# plt.plot(t2, x2, label='Cauchy')
plt.plot(t1, 1.33 * np.exp(3*t1) - (3*t1+1)/3, label='Real')
plt.legend()
plt.show()
