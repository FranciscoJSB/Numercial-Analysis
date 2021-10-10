import numpy as np
from matplotlib import pyplot as plt


#Esta función aproxima la solucion de un sistema de ecuaciones lineales mediante el método de relajacion
#Parametros de entrada: coeficientes : matriz de coeficientes
#                       independientes: vector de valores independientes
#                       valor_inicial: vector con el valor inicial
#                       w: factor omega
#                       tol: tolerancia permitida
#                       iterMax: iteraciones máximas permitidas
#Parametros de salida:  x_k : aproximacion de la solución
#                       error: error absoluto
def relajacion(coeficientes, independientes, valor_inicial, w, tol, iterMax):
    

    A = np.array(coeficientes)
    b = np.array(independientes)

    if(verificar_SDP(A,len(A)) == False):
        A = np.transpose(A) * A
        b = np.transpose(A) * b
    
    U = obtener_u(A)
    D = obtener_d(A)
    L = np.array(A - U - D)    

    c = sustitucion_atras((D + (w * L)), (w * b))


    x_k = valor_inicial

    error = 0

    iteraciones =[]
    errores = []
   

    for k in range (0, iterMax):

        iteraciones.append(k+1)

        d_k = (((1-w)*D - w*U).dot(x_k)).tolist()
        
        z_k = sustitucion_atras(D + (w*L),d_k)

        x_k_mas_1 = (np.array(z_k) + np.array(c)).tolist()


        error = np.linalg.norm((A.dot(x_k_mas_1) - b),2) #Calcula el error con norma 2

        errores.append(error)


        if (error < tol):
            
            break

        x_k = x_k_mas_1
    
    plt.plot(iteraciones, errores)
    plt.xlabel("Iteraciones")
    plt.ylabel("Error")
    plt.title("Iteraciones vs error")
    plt.show()

    return x_k, error


def obtener_u(A):
    n = len(A)
    U = np.zeros((n,n))

    for i in range(0,n):
        for j in range(0,n):
            if j>i:
                U[i][j] = A[i][j]

    return U

def obtener_d(A):
    n = len(A)
    D = np.zeros((n,n))

    for i in range(0,n):
        for j in range(0,n):
            if j==i:
                D[i][j] = A[i][j]

    return D


def sustitucion_atras(A,b):
    n = len(A)
    x = [0 for a in range(n)]    
   
    for i in range (n-1, -1 , -1):
        suma1 = 0
        for j in range(i, n):
            suma1 += (A[i][j]*x[j])
        x[i] = (b[i]-suma1)/A[i][i]

    return x

#Metodo para verificar si una matriz es Simetrica Definida Positiva
#A: matriz a evaluar
#n: tamaño de la matriz
#Salida: booleano
def verificar_SDP(A,n): 
    A_T = np.transpose(A)
    SDP = True
    if (A_T == A).all():
        SPD =  verificar_PD(A,n)
    else:
        SPD = False
    return SPD


#Metodo auxiliar para verificar si una matriz es Positiva definida
#A: matriz a evaluar
#n: tamaño de la matriz
#Salida: booleano
def verificar_PD(A,n):
    PD = True
    for i in range(n):
        sub_matriz = A[0:i+1,:i+1]
        if(np.linalg.det(sub_matriz) < 0):
            PD = False
            break
        
    return PD


#Ejemplo numerico - Debe cerrar el grafico, para poder continuar y visualizar el retorno de la función

y = relajacion([[25, 15,-5,-10],[15,10,1,-7],[-5,1,21,4],[-10,-7,4,18]],[-25,-19,-21,-5],[0,0,0,0],1.24,0.00001,100)
print(y)
