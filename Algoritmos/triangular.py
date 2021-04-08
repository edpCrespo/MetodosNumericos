import numpy as np

# hace la triangular superior de una matriz de coeficientes y terminos independientes
def gauss(matrix):
    row, col = matrix.shape
    if row >= 2:
        for j in range(row):
            # si el primer elemento de fila es 0, intercambio filas
            if matrix[j, 0] != 0:
                matrix[[j, 0]] = matrix[[0, j]]
                break
        for i in range(row-1):
            # calculo el divisor con el cual voy a hacer las operaciones entre filas
            div = matrix[i+1, 0]/matrix[0, 0]
            matrix[i+1] = matrix[i+1] - div * matrix[0]

        # guardo una sub matriz de la original que no tiene la fila y col 0, y vuelvo a empezar
        sub_matrix = matrix[1:, 1:]  # va de col y row desde 1 en adelante -> :
        sub_matrix = gauss(sub_matrix)
        row_0 = matrix[0, 1:]
        col_0 = matrix[:, 0]
        # le agrego la fila y columna que le saque a sub_matrix
        matrix = np.append([row_0], sub_matrix, axis=0)
        matrix = np.append(col_0.reshape(-1, 1), matrix, axis=1)

    return matrix


A = np.array([[0, 2, 5, 4, 7],
              [1, 3, 2, 7, 8],
              [1, 2, 3, 4, 5],
              [4, 7, 32, 4, 65]])

print(gauss(A))
