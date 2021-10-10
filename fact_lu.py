import numpy as np


def matrices_LU(A):
    [n, m] = A.shape
    if n == m:  # Verifica que A sea cuadrada
        # Determina si A y sus submatrices principales son invertibles
        invertibles = True

        if A[0, 0] == 0:
            invertibles = False
        else:
            for i in range(1, n):
                # Los rangos van de 0:i+1 pues el i+1 es excluido
                subMatrizActual = (A[0:i+1, 0:i+1])
                determinante = np.linalg.det(subMatrizActual)
                if determinante == 0:
                    invertibles = False
                    break

        if invertibles:
            L = np.identity(n)
            for k in range(0, n):
                for i in range(k+1, n):
                    L[i, k] = A[i, k]/A[k, k]
                    A[i, k] = 0
                    for j in range(k+1, n):
                        A[i, j] = A[i, j] - L[i, k]*A[k, j]
            U = A.copy()

            return [L, U]
        else:
            return "A o sus submatrices principales no son invertibles"

    else:
        return "N/A A no es cuadrada"

# ------------ Util para probar la generacion de matrices L y U; utiles en la fact LU ------------
#A = np.array([[2, 3, 0, 1], [4, 5, 3, 3], [-2, -6, 7, 7], [8, 9, 5, 21]])
#[L, U] = matrices_LU(A)
# print(L)
# print(U)
# print(np.matmul(L, U))
# ------------ Util para probar la generacion de matrices L y U; utiles en la fact LU -------------


def sust_adelante(A, b):

    [n, m] = A.shape
    [nb, mb] = b.shape
    if mb == 1:  # Está en forma de columna
        b = b.transpose()
        [nb, mb] = b.shape

    if n == m & n == mb:
        x = np.zeros((1, n))  # Matrix de una fila y n columnas
        # Init en cero, termina en n menos uno
        for i in range(n):
            # Calculo de la sumatoria
            j = 0
            sumatoria = 0

            while j <= i:
                sumatoria = sumatoria + A[i, j]*x[0, j]
                j = j + 1
            # Calculo de la sumatoria

            x[0, i] = (1/A[i, i])*(b[0, i] - sumatoria)
    else:
        print("Error")

    return x.transpose()  # Se retorna en su forma de n filas y una columna


def sust_atras(A, b):

    [n, m] = A.shape
    [nb, mb] = b.shape
    if mb == 1:  # Está en forma de columna
        b = b.transpose()
        [nb, mb] = b.shape

    if n == m & n == mb:
        x = np.zeros((1, n))  # Matrix de una fila y n columnas
        # Init en cero, termina en n menos uno
        for i in range(n-1, -1, -1):
            # Calculo de la sumatoria
            j = i+1
            sumatoria = 0

            while j <= n-1:
                sumatoria = sumatoria + A[i, j]*x[0, j]
                j = j + 1

            # Calculo de la sumatoria
            x[0, i] = (1/A[i, i])*(b[0, i] - sumatoria)
    else:
        print("Error")

    return x.transpose()  # Se retorna en su forma de n filas y una columna


def fact_lu(A, b):
    # Funcion que calcula la solucion de un sistema de ecuaciones cuyo matriz de coeficientes tiene inversa
    # Parametros de entrada: Matriz A y su vector de constantes
    # Parametros de salida: Solucion x del sistema
    # Restricciones: A debe de ser Invertible. Ademas, por el metodo usado para averiguar la solucion, sus sub-matrices principales tambien deben sern invertibles.

    # Todas las verificaciones correspondientes se hacen a lo interno de cada modulo.
    [L, U] = matrices_LU(A)
    y = sust_adelante(L, b)
    x = sust_atras(U, y)
    return x


A = np.array([[4, -2, 1], [20, -7, 12], [-8, 13, 17]])
b = np.array([[11], [70], [17]])
x = fact_lu(A, b)

print(x)
