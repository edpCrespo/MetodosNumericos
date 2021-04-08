import numpy as np

# recibe array con las ecuaciones ordenadas como requiere el metodo
def jacobi(coef: np.array, y: np.array, x: np.array = None, ep=0.0, num_iter=0):

    row, col = coef.shape  #shape me devuelve (f,c)

    if x is None:
        x = np.zeros(row)
    x_iter = np.zeros(row)

    # lista de indices de 0 a row, con ellos armo los coef de la diagonal en diag
    idx = np.arange(row)
    diag = coef[idx, idx]

    # para hacer el metodo por numero de iteraciones
    if num_iter:
        for k in range(num_iter):
            sums_ = np.dot(coef, x.reshape(-1, 1)).reshape(-1) - diag * x  #cada fila por todos los x en forma de columna
            x = (y - sums_) / diag
    # para hacer el metodo por epsilon
    elif ep:
        num_iter, done = 0, False
        while not done or np.any(error > ep):
            sums_ = np.dot(coef, x.reshape(-1, 1)).reshape(-1) - diag * x  # cada fila por todos los x en forma de columna
            x = (y - sums_) / diag
            num_iter += 1
            error = np.abs(x - x_iter)
            x_iter = x.copy()
            done = True

    return x, num_iter


coef = np.array([[6, 2, 1],
                 [-1, 8, 2],
                 [1, -1, 6]])

y = np.array([22, 30, 23])
print(np.linalg.solve(coef, y))
ep = 0.001

x, n = jacobi(coef, y, num_iter=20)
print(x)
print(n)
