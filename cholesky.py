#librerias
# se usa numpy para los arreglos y math para las raices
import math
from math import sqrt
import numpy as np

#funcion para armar la matriz tridiagonal

#n --> tamaño de la matriz
#a_n --> valor en la diagonal principal
#b_n --> valor en la diagonal superior
#c_n --> valor en la diagonal inferior
def tridiagonal(n,a_n,b_n,c_n):

    # se construye la matriz A de nxn llena de ceros
    A = [[0 for j in range(n)] for k in range(n)]
    # Diagonal principal
    for i in range(n):
        A[i][i]=a_n
        
    #Diagonal superior e inferior respectivamente
    for i in range(n-1):
        A[i][i+1]=b_n
        A[i+1][i]=c_n

    return A

#funcion para hacer el vector d para la matriz tridiagonal

#n --> tamaño del vector
#a_n --> valores del primer y ultimo numero del vector
#b_n --> resto de numeros del vector
      
def vectorD(n,a_n,b_n):

    # se contrsuye el vector d de tamaño n
    b = [0 for j in range(n)]
    i=1
    for i in range(n-1):
        b[0]=b[n-1]=a_n #principio y finañ
        b[i]=b_n #resto de los valores 

    return b

#funcion de sustitucion hacia adelante
def sust_Adelante(L,b):
    #array de ceros con la misma forma del vector b
    x=np.zeros_like(b)
    for i in range(x.shape[0]):
        sum1=0.
        for j in range(i):
            sum1+=L[i,j]*x[j]
        x[i]=(b[i]-sum1)/L[i,i]
    return x.reshape(-1,1)

#funcion de sustitucion hacia atras
def sust_Atras(L,b):
    n = b.size
    #array de ceros con la misma forma del vector b
    x = np.zeros_like(b)
    x[n-1] = b[n-1]/L[n-1,n-1]
    MatrixAtras = np.zeros((n,n))
    for i in range(n-2,-1,-1):
        bb = 0
        for j in range (i+1,n):
            bb+=L[i,j]*x[j]
        MatrixAtras[i,i]=b[i]-bb
        x[i]=MatrixAtras[i,i]/L[i,i]

    return x

#Funcion de Cholesky para obtener la matriz L
#A --> matriz inicial
#L --> matriz de salida
def Cholesky(A):
    n = A.shape[0] #tamaño de la matriz

    # se crea la matriz de nxn vacia
    L = [[0.0]*n for i in range(n)]

    # se obtienen los valores de la matriz
    for i in range(n):
        for k in range(i+1): #se recorren las filas
            sum1=sum(L[i][j]*L[k][j] for j in range(k))
            
            if (i==k): # Elementos en la diagonal
                L[i][k]=sqrt(A[i][i]-sum1)
            else:
                L[i][k]=(1/L[k][k]*(A[i][k]-sum1))
    return L

#funcion para resolver sistemas de ecuaciones
# A --> matriz inicial
# b--> vector 
# x --> vector solucion de L^t x = y
def Fact_Cholesky(A,b):
    #verifica que la matriz sea simetrica
    if(A.shape[0] == b.shape[0]):
        #verifica que la matriz sea positiva definida por el determinante
        if(np.linalg.det(A)<0):
            #funcion para encontrar Ax=b
            L=Cholesky(A)
            # se resueleve Ly=b por sustitución hacia adelante
            y=sust_Adelante(L,b)
            # se resuevle L^t x=y por sustitucion hacia atras con el resultado anterior
            x=sust_Atras(np.transpose(L),y)

            print(x,"^t") #la t es por formato de traspuesta
            # Vector resultado
            return x

        #en caso de que la matriz no sea SDP 
        else:
            #se calcula A_ =A^t * A
            A_=np.transpose(A).dot(A)
            #se calcula b_= A^t * b
            b_=np.transpose(A).dot(b)
            # se llama la función con los nuevos valores
            L=Cholesky(A_)
            # se resueleve Ly=b por sustitución hacia adelante
            y=(np.linalg.inv(L)).dot(b_)
            # se resuevle L^t x=y por sustitucion hacia atras con el resultado anterior
            x=sust_Atras(np.transpose(L),y)

            print(x,"^t") #la t es por formato de traspuesta
            # Vector resultado "transpuesto"
            return x
            
    else:
        print("la matriz no es simetrica")

########################################################################
#Ejemplos de prueba de Cholesky

#A=np.array([[25,15,-5,-10],[15,10,1,-7],[-5,1,21,4],[-10,-7,4,18]])
#b=np.array([-25,-19,-21,-5])
#A=np.array([[5,-1,-6],[-1,5,-16],[-6,-16,69]])
#b=np.array([-4,-10,43])
#A=np.array([[1,-1,2],[-2,0,4],[0,-2,7]])
#b=np.array([0,2,5])
#########################################################################

#########################################################################
#Ejemplo de Matriz Tridiagonal 

A=np.array(tridiagonal(100,5,1,1)) 
b=np.array(vectorD(100,-12,-14))
x=Fact_Cholesky(A,b)






