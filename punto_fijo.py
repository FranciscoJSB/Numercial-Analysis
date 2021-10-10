#Librerias
import numpy as np
from sympy import *
from numpy import *
from matplotlib import pyplot as plt

# Metodo de Punto Fijo
#func = funcion ("string")
#x0 = valor inicial (entero)
#tol = tolerancia (float)
#iterMax = iteraciones maximas (entero)
def punto_fijo(func,x0,tol,iteraMax):

    #Almacenamiento de los valores para la gráfica
    iteraStore=[] #numero de iteraciones
    errorStore=[] #errores
    #labels de la grafica
    plt.ylabel("Error") #eje y
    plt.xlabel("Iteraciones") # eje x
    plt.suptitle(func) #el título de la gráfica es la función

    #valores iniciales
    aprox = x0
    itera = 0 
    error = 1

    #condicion de parada
    for itera in range(0,iteraMax):

        x = aprox
        aprox = eval(func)
        error = (abs(aprox - x) / aprox)
        itera= itera + 1

        #se agregan los valores a los arreglos 
        iteraStore.append(itera+1)
        errorStore.append(error)

    print("aproximacion:",aprox)
    print("error:",error)

    #impresion de la grafica
    plt.plot(iteraStore,errorStore,"r")
    plt.show()
    return aprox, error


#Ejemplo
#tomado de las presentaciones

punto_fijo("sin(x)",2,10**-4,5)

