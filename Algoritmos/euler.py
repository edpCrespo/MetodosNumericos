import numpy as np
import matplotlib.pyplot as plt

# func: la funcion derivada (EDO), to y tf: intervalo de t, delta_t: paso de integ, xo = x(to)
def euler(func, to, tf, delta_t, xo):
    N = int((tf - to) / delta_t) + 1    # cantidad de iteraciones
    x_k = np.zeros(N)
    t_k = np.zeros(N)  # discretizacion
    x_k[0] = xo
    t_k[0] = to

    for i in range(N-1):
        x_k[i+1] = x_k[i] + func(x_k[i], t_k[i]) * delta_t
        t_k[i+1] = t_k[i] + delta_t

    return t_k, x_k

def euler_error(x1, x2):    # x1 es con delta_t y x2 es con delta_t/2
    error = np.zeros(len(x1))
    for i in range(len(x1)):
        error[i] = (x2[2*i] - x1[i])*2  # saco el error para el paso delta_t
    return error

#################################################################################################

def funcion(x, t):
    ec = 3*x + 3*t
    return ec


x0 = 1
t0 = 0
tfi = 0.6

t1, x1 = euler(funcion, t0, tfi, 0.01, x0)
t2, x2 = euler(funcion, t0, tfi, 0.01/2, x0)

error = euler_error(x1, x2)

print(error)

plt.plot(t1, x1, label='Euler delta_t')
plt.plot(t2, x2, label='Euler delta_t/2')
plt.plot(t1, 1.33 * np.exp(3*t1) - (3*t1+1)/3, label='Real')
plt.legend()
plt.show()

# print(t2)
# print(x2)



