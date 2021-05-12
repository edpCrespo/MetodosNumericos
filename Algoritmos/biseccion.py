
"""
    biseccion: Metodo de la biseccion en [a, b] con tolerancia 'tol', recibe callback a la funcion para evaluarla
"""

def biseccion(a, b, tol, f):    # no seria mala idea agregar max de iter por si la tol es muy chica y tarda demasiado
    c = (a + b) / 2

    if f(a) * f(b) > 0:  # no tiene cambio de signo en el intervalo
        print("Error")
        return -1

    a_new = a
    b_new = b

    num_iter = 0

    while ((b_new - a_new) > tol) and f(c) != 0:
        c = (a_new + b_new) / 2
        if (f(c) * f(a_new)) > 0:
            a_new = c
        else:
            b_new = c
        num_iter += 1

    error = (b - a)/(2**num_iter)   # con esta formula puedo calcular el num de iter necesaria para cierto error

    return c, num_iter, error


A = -2
B = 10
tol = 0.000001  # debe ser pequeña, el error va a ser menor a la toleranciaa
X = biseccion(A, B, tol, lambda x: x ** 3)  # el lambda x: permite incluir a x como parametro

print(X)