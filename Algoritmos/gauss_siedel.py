import numpy as np

# recibe array con las ecuaciones ordenadas como requiere el metodo
def gauss_seidel(coef: np.array, y: np.array, x: np.array = None, ep=0.0, num_iter=0):

    row, col = coef.shape  # shape me devuelve (f,c)

    if x is None:
        x = np.zeros(row)
    x_iter = np.zeros(row)

    # para hacer el metodo por numero de iteraciones
    if num_iter:
        for k in range(num_iter):
            for i in range(row):  # Me muevo fila por fila
                sum_ = np.dot(coef[i], x) - coef[i, i] * x[i]
                x[i] = (y[i] - sum_) / coef[i, i]  # Calculo el valor y lo guardo en x

    # para hacer el metodo por epsilon
    elif ep:
        num_iter, done = 0, False
        while not done or np.any(step > ep):
            for i in range(row):  # Me muevo fila por fila
                sum_ = np.dot(coef[i], x) - coef[i, i] * x[i]
                x[i] = (y[i] - sum_) / coef[i, i]  # Calculo el valor y lo guardo en x
            num_iter += 1
            step = np.abs(x - x_iter)
            x_iter = x.copy()
            done = True

    return x, num_iter


coef = np.array([[6, 2, 1],
                 [-1, 8, 2],
                 [1, -1, 6]])

y = np.array([22, 30, 23])
ep = 0.001
print(np.linalg.solve(coef, y))

x, n = gauss_seidel(coef, y, num_iter=10)
print(x)
print(n)


