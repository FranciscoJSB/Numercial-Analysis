#Librerias

from sympy import *
import numpy as np
import random
import math
from operator import add
from sympy.printing import gtk
from matplotlib import pyplot as plt 

#symbolic
x = Symbol("x")
y = Symbol("y")

#variables
vars = (x, y)

# metodo para la obtencion del gradiente
def gradient(f, vars):
    grad = []
    #por cada variable presente se ejecuta
    for var in vars:
        grad.append(f.diff(var)) #se crea un solo valor
    return np.array(grad) # array de gradientes

#Entradas
#
#f --> funcion 
#vars --> variables
#xk --> valores iniciales
#tol --> tolerancia
#iterMax --> iteraciones maximas

# xk es, vars son np array

def gradiente(f, vars, xk, tol, iterMax):

#Almacenamiento de los valores para la gráfica
    iteraStore=[] #numero de iteraciones
    errorStore=[] #errores

#labels de la grafica
    plt.ylabel("Error") #eje y
    plt.xlabel("Iteraciones") # eje x
    plt.suptitle(f) #el título de la gráfica es la función

    alpha = 1
    #gradiente
    grad = gradient(f, vars)
    #gradiente vector
    gk = Subs(grad, vars, xk).doit()
    #direccion
    d = -gk
    delta = 0.5  # random.random()
    #norma de la funcion
    def norm(x): return sqrt(sum(pow(np.array(x), 2))).evalf()

    for i in range(iterMax):
        l = xk+(alpha*d)
        alpha = 1
        while True:
            #reducir el valor de alpha
            alpha = alpha/2
            #creacion de los intervalos
            izq = Subs(f, vars, xk+(alpha*d)).doit() - Subs(f, vars, xk).doit()
            der = delta*alpha * np.dot(np.array(gk), np.array(d))
            #condicion para reducir el alpha
            if (izq <= der):
                break
        #formulas del GCNL
        xk1 = xk+alpha*Subs(d, vars, xk).doit()
        gk = Subs(grad, vars, xk).doit()
        gk1 = Subs(grad, vars, xk1).doit()
        norm1 = norm(gk1)
        norm0 = norm(gk)
        beta = (norm1**2)/(norm0**2)

        if norm(gk).evalf() <= tol:
            return xk

        xk = xk1
        d = -gk1+beta*d
        #norma del gradiente de la funcion
        gk = gk1

        # se almacenanan los valores para graficar
        iteraStore.append(i)
        errorStore.append(norm0)

    #impresion de los valores
    print ("aproximacion",xk1)
    print ("error",norm0)
    
    # impresion de la gráfica
    plt.plot(iteraStore,errorStore,"r")
    plt.show()
    return xk

#Salidas
# xk --> valor de la aproximacion
# gk --> valor del error
# grafica error vs iteracion


#Ejemplo tomado de las presentaciones
gradiente((x-2)**4+(x-2*y)**2, np.array([x, y]), np.array([0, 3]), 10**-8, 13)
