import math
from numpy import *
from decimal import *
#cantidad de decimales
getcontext().prec = 30 # decimales
###########################################
#           Falsa Posicion Modificado
###########################################

#Entradas
# funcion --> string
# a --> primer rango entero del rango
# b --> segundo rango entero del rango
# tol --> tolerancia
#n --> subdiviones maximas de los intervalos

#Salidas
#valor aproximado

def falsa_posicion_modificado(f, a, b, tol,n):

    #extremos de los intervalos [C_k, Ck_+1]
    C_k_1=b
    C_k=a
    itera=1
    f1_x=1

    if(tol<=0):
        print("la tolerancia debe ser positiva")
        return None
    elif(b<=a):
        print("los valores del intervalo son incorrecto")
        return None
    elif(isinstance(n,int)and n>0):

        while(f1_x> tol and n!=itera):
            #se evalua la funcion en la segunda mitad del intervalo 
            x=C_k_1
            fCk_1=eval(f)
            #se evalua la funcion en la primera mitad del intervalo 
            x =C_k
            fCk=eval(f)
            #formula de Regula Falsi Modificado
            xAprox=C_k_1-((C_k_1-C_k)/(fCk_1-fCk))*fCk_1
            f1_x=(abs(n-C_k_1)/n)
            itera=itera + 1    

        print("Aproximacion:",xAprox, "Iteraciones:", itera)
        return xAprox, itera
    else:
        print("el valor de la division de los intervalos debe ser entero positivo")
        return None

falsa_posicion_modificado("sin(x)**2+x**2-1", 0, 2, 10**-10,10)
