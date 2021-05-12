import numpy as np
import matplotlib.pyplot as plt

###############################################################################################################

def heun(func, to, tf, delta_t, xo):
    N = int((tf - to) / delta_t) + 1  # cantidad de iteraciones
    x_k = np.zeros(N)
    t_k = np.zeros(N)  # discretizacion
    x_k[0] = xo
    t_k[0] = to

    for i in range(N-1):
        B = delta_t/2
        Q = func(t_k[i], x_k[i])*delta_t
        x_k[i+1] = x_k[i] + (func(x_k[i], t_k[i]) + func(t_k[i]+delta_t, x_k[i]+Q)) * B
        t_k[i+1] = t_k[i] + delta_t

    return t_k, x_k

###############################################################################################################

def cauchy(func, to, tf, delta_t, xo):
    N = int((tf - to) / delta_t) + 1  # cantidad de iteraciones
    x_k = np.zeros(N)
    t_k = np.zeros(N)  # discretizacion
    x_k[0] = xo
    t_k[0] = to

    for i in range(N-1):
        P = delta_t/2
        Q = func(t_k[i], x_k[i])*delta_t/2
        x_k[i+1] = x_k[i] + func(t_k[i]+P, x_k[i]+Q)*delta_t
        t_k[i+1] = t_k[i] + delta_t

    return t_k, x_k

###############################################################################################################

def funcion(x, t):
    ec = 3*x + 3*t
    return ec


x0 = 1
t0 = 0
tfi = 0.6

t1, x1 = heun(funcion, t0, tfi, 0.01, x0)
t2, x2 = cauchy(funcion, t0, tfi, 0.01, x0)

# error = euler_error(x1, x2)

# print(error)

plt.plot(t1, x1, label='Heun')
plt.plot(t2, x2, label='Cauchy')
plt.plot(t1, 1.33 * np.exp(3*t1) - (3*t1+1)/3, label='Real')
plt.legend()
plt.show()
