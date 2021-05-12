import numpy as np

""" 
    fixed_point: Metodo de punto fijo arranca en xo con tolerancia 'tol', recibe callback a la funcion para evaluarla
"""

def fixed_point(xo, tol, f):
    x0 = 0
    x1 = xo
    i = 0
    while np.abs(x1 - x0) > tol or not i:
        x0 = x1
        x1 = f(x0)
        i += 1
        print(f'Raiz en iteracion {i}: x{i} = {x1}')
    return x1


a = 0
b = 5
tol = 1
root_fp = fixed_point((a + b) / 2, tol, lambda x: x**2 - 5*x + 3)
print(f'Raiz por punto fijo: {root_fp}')
