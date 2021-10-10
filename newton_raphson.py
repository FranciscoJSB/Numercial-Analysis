#Librerias
import numpy as np
from sympy import *
from numpy import *
from matplotlib import pyplot as plt 

#metodo de derivación
def derivative(func, z):
#permite realizar la derivada de la funcion de entrada    
    x = Symbol('x') 
    y = eval(func)
#Cálculo de la n-ésima diferencia discreta a lo largo del eje y.
    yDx = y.diff(x)
#hace uso de la biblioteca de numpy
    f = lambdify(x, yDx, 'numpy')
#valor de la derivada
    return f(z)
#                             Método de Newton-Raphson

#formato de entradas (String,int,float,int) => f(x), valor inicial, tolerancia, iteraciones maximas

def newton_raphson(f, xo, tol, iterMax):

#Almacenamiento de los valores para la gráfica
    iteraStore=[] #numero de iteraciones
    errorStore=[] #errores

#asignacion del valor inicial para su uso
    x=xo
    tolFijo=10**-10
#labels de la grafica
    plt.ylabel("Error") #eje y
    plt.xlabel("Iteraciones") # eje x
    plt.suptitle(f) #el título de la gráfica es la función
    
# ciclo mientras n sea menor o igual a la cantidad de iteraciones
    for k in range(0,iterMax):

        aprox = eval(f)
        error= abs(eval(f))
# Se asigna el valor de la derivada, calculada a partir del método derivate
        Dfx = derivative(f,x)

#  cuando el valor absoluto de la aproximacion es menor a la 
#  tolerancia se devuelve el valor de la raiz

        if abs(aprox)<tolFijo:

# impresion en consola de los valores requeridos
            print("iteraciones:",k)
            print("solución:",x)
            print("error:",error)

# impresion de la gráfica
            plt.plot(iteraStore,errorStore,"r")
            plt.show()
            return x
            
#Si la derivada obtenida es 0
        if Dfx==0:

            print('La derivada de la función es cero')
            return None

        if tol<=0:
            print('La tolerancia no puede ser negativa o cero')
            return None

#la formula permite aproximar el valor de X
        else:
            x = x - eval(f)/Dfx

# se almacenanan los valores para graficar
            iteraStore.append(k+1)
            errorStore.append(error)

    #caso de que las iteraciones sean más de las requeridas       
    print('Las iteraciones necesarias exceden el valor especificado. No tiene solución')
    return None

####### Ejemplos  (quitar el # del que se quiere probar)
#Ejemplo 1
#newton_raphson("e**x-(1/x)", 1, 10**-8,10)
#Ejemplo 2
newton_raphson("e**x-2*x-1", 4,10**-8, 10)
#newton_raphson("cos(x)-x", 4,10**-8, 10)
