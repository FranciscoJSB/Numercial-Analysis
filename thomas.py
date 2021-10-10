#librerias
# se usa numpy para los arreglos 
import math
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
    d = [0 for j in range(n)]
    i=1
    for i in range(n-1):
        d[0]=d[n-1]=a_n #principio y finañ
        d[i]=b_n #resto de los valores 

    return d

#############################################################
#    Metodo de Thomas para resolver matrices tridiagonales  #
#############################################################

#entradas
# A--> matriz tridiagonal nxn 
# d--> vector tamaño n

#Salidas
#vector solucion

def thomas(A,d):
    #tamaño de la matriz y el vector
    n= A.shape[0]
    m= d.shape[0]
    if(n==m):
        #array de ceros con la misma forma del vector b
        x = np.zeros_like(d)
        x[n-1] = d[n-1]/A[n-1,n-1]
        q_i = np.zeros((n,n))
        for i in range(n-2,-1,-1):
            p_i = 0
            for j in range (i+1,n):
                p_i+=A[i,j]*x[j]
            q_i[i,i]=d[i]-p_i
            x[i]=q_i[i,i]/A[i,i]
            
        print("solución del sistema Ax=d")
        print("x=",x,"^t")
        return x

    else:
        print("la matriz y el vector deben tener las mismas dimensiones")


# Ejemplo de prueba tomado de las presentaciones

#A=np.array(tridiagonal(tamaño matriz,valor 1,valor 2,valor 3))
A=np.array(tridiagonal(100,5,1,1))
d=np.array(vectorD(100,-12,-14))
thomas(A,d)


