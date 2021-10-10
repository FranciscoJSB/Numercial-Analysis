#Importar sympy, numpy y scipy
from sympy import *
from numpy import *
from scipy.optimize import *
from numpy.linalg   import *
from matplotlib import pyplot as plt 

## Comprobacion del teorema de Bolzano
def bolzano(a, b, f): 
    x = a
    fa = eval(f)
    x = b
    fb = eval(f)
    return (fa * fb <= 0)

def biseccion(f, a, b, tol,iterMax):

    x = 0
    itera = 0
    iteraStore=[] #numero de iteraciones
    errorStore=[] #errores

    tolFijo=10**-10
    
    plt.ylabel("Error") #eje y
    plt.xlabel("Iteraciones") # eje x
    plt.suptitle(f) #el título de la gráfica es la función

    if((b-a)>0):

        if(tol<=0):
            print("el valor de la tolerancia no puede ser 0 o negativo")
            return None

        if (bolzano(a, b, f)):
            tempA = a
            tempB = b
            error = (b - a) / 2

            while (error > tolFijo and itera<=iterMax):
                x = (tempA + tempB) / 2
                if(bolzano(x, tempB, f)):
                      empA = x
                elif(bolzano(tempA, x, f)):
                    tempB = x
                itera=itera+1
                error = (b - a) / (2**itera)

            print("aproximacion:",x)
            print("iteraciones:",itera)
            print("error:",error)
            return itera, x

    else:
        print("No se cumple el teorema de Bolzano")
        return None
        

#Ejemplo de pruebra
biseccion("e**x-x-2",1, 2, 10**-8,50)


