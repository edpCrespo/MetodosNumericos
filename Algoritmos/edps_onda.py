import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import cm

# f: funcion, g: f' (derivada segunda), n: cantidad de x, m: cantidad de t, cte: c
def ec_onda(f, g, t_0, t_f, x_0, x_f, n, m, cte):

    # Discretización
    delta_t = (t_f - t_0)/(m-1)
    delta_x = (x_f - x_0)/(n-1)

    # Constantes
    r = (cte * delta_t) / delta_x
    if r > 1:
        print('r es mayor a 1, no va a converger :(')
        return -1

    # Todos los x y t
    t = np.linspace(t_0, t_f, m)
    x = np.linspace(x_0, x_f, n)
    # Matriz con las aproximaciones
    u = np.zeros((n, m))    # u(x,t)

    # Determino condiciones inciales -> los bordes quedan definidos implicitamente porque son 0
    u[1:-1, 0] = f(x[1:-1])    # u(x,0)
    aprox_f2 = (f(x[2:])-2*f(x[1:-1])+f(x[0:-2]))/delta_x**2
    u[1:-1, 1] = f(x[1:-1]) + g(x[1:-1]) * delta_t + aprox_f2 * cte**2 * delta_t**2/2  # u(x,1)

    for j in range(2, m):   # recorro hasta mi ultimo valor de t
        u[1:-1, j] = 2 * (1 - r ** 2) * u[1:-1, j-1] + r ** 2 * (u[2:, j-1] + u[:-2, j-1]) - u[1:-1, j-2]

    return x, t, u

def test():
    f = lambda x: np.sin(np.pi*x) + np.sin(2*np.pi*x)
    g = lambda x: np.zeros(x.size)

    x_0 = 0
    x_f = 1
    t_0 = 0
    t_f = 1
    c = 2
    n = 109
    m = 221
    x, t, u = ec_onda(f, g, t_0, t_f, x_0, x_f, n, m, c)

    #Analitica
    ua = np.zeros(u.shape)
    for k in range(x.shape[0]):
        ua[k, :] = np.sin(np.pi*x[k]) * np.cos(2*np.pi*t) + np.sin(2*np.pi*x[k]) * np.cos(4*np.pi*t)
    print(np.max(np.abs(u-ua)))

    j1 = int(m / 4)
    j2 = int(m / 2)
    j3 = int(3 * m / 4)
    j4 = int(m - 1)
    fig, ax = plt.subplots()
    ax.plot(x, ua[:, j1], label='Cuarto de tiempo')
    ax.plot(x, ua[:, j2], label='Mitad de tiempo')
    ax.plot(x, ua[:, j3], label='Tres cuartos')
    ax.plot(x, ua[:, j4], label='Final')
    ax.legend()
    ax.set_title('Solución')
    fig, ax = plt.subplots()
    ax.plot(x, u[:, j1], label='Cuarto de tiempo')
    ax.plot(x, u[:, j2], label='Mitad de tiempo')
    ax.plot(x, u[:, j3], label='Tres cuartos')
    ax.plot(x, u[:, j4], label='Final')
    ax.legend()
    ax.set_title('Aproximación numérica')

    fig, ax = plt.subplots()
    ax.plot(x, ua[:, j1] - u[:, j1], label='Cuarto de tiempo')
    ax.plot(x, ua[:, j2] - u[:, j2], label='Mitad de tiempo')
    ax.plot(x, ua[:, j3] - u[:, j3], label='Tres cuartos')
    ax.plot(x, ua[:, j4] - u[:, j4], label='Final')
    ax.legend()
    ax.set_title('Errores')

    plt.show()



test()
