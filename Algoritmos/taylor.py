import numpy as np
import matplotlib.pyplot as plt


# func: arreglo de las funciones derivadas, to y tf: intervalo de t, delta_t: paso de integ, xo = x(to)
def taylor(func, to, tf, delta_t, xo):
    N = int((tf - to) / delta_t) + 1  # cantidad de iteraciones
    x_k = np.zeros(N)
    t_k = np.zeros(N)  # discretizacion
    x_k[0] = xo
    t_k[0] = to
    for i in range(N - 1):
        m = 1
        suma = 0
        deriv = np.array([f(x_k[i], t_k[i]) for f in func])
        orden = len(deriv)
        for n in range(orden):
            m *= (n + 1)
            suma += deriv[n] * (delta_t ** (n + 1)) / m
        x_k[i + 1] = x_k[i] + suma
        t_k[i + 1] = t_k[i] + delta_t
    return t_k, x_k


#################################################################################################

def f1(x, t):
    return 3 * x + 3 * t


def f2(x, t):
    return 3 * (3 * x + 3 * t) + 3


func = [f1, f2]

x0 = 1
t0 = 0
tfi = 0.8

t1, x1 = taylor(func, t0, tfi, 0.001, x0)
# t2, x2 = taylor(func, t0, tfi, 0.01/2, x0)

# error = euler_error(x1, x2)

# print(error)

plt.plot(t1, x1, label='Taylor delta_t')
# plt.plot(t2, x2, label='Euler delta_t/2')
plt.plot(t1, 1.33 * np.exp(3 * t1) - (3 * t1 + 1) / 3, label='Real')
plt.legend()
plt.show()
