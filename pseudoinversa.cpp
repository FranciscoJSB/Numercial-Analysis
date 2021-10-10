//Se importan las librerias a utilizar.
#include <winbgim.h>
#include <math.h>
#include <iostream>
#include <list>
//Fin de la importacion de librerias.
using namespace std;
//Cantidad de filas
int n = 4; 
// Matrices y vectores a utilizar
double x[3][2];
double transposed[3][2] = {};
double id[2][2] = {{2,0},{0,2}};
//Iteraciones maximas
int Max = 50;
// Errores calculados en cada iteracion
list <double> errores;
// Se calcula la transpuesta de A
int transpuesta(double A[2][3]){
	for(int i = 0; i < 2; i++) { 
		for(int j = 0; j < 3; j++) {
			transposed[j][i] = A[i][j];
		}
}
return 0;
}

// Se calcula el error de la iteracion actual
double CalError(double A[2][3],double x[3][2]){
	double suma = 0;
	double suma2= 0;
	double error= 0;
	double Ax[2][2] = {};
    for(int i=0; i<2; ++i){
     	for(int j=0; j<2; ++j){
     		for(int z=0; z<3; ++z){
     			suma += A[i][z] * x[z][j];	 
			 }
			 Ax[i][j] = suma;
			 suma = 0;    
		 }	     
	 }
	   for(int i=0; i<2; ++i){
     	for(int j=0; j<3; ++j){
     		for(int z=0; z<2; ++z){
     			suma2 += Ax[i][z]* A[z][j];	 
			 }
			 error += pow((suma2 - A[i][j]), 2);
			 suma2 = 0;     
		 }     
	 }
	 error = sqrt(error);
	 return error;
	 
        
}
// Calcula el x de la iteracion actual
int CalcX(double A[2][3],double x[3][2]){
	double suma = 0;
	double suma2= 0;
	double IAx[2][2] = {};
    for(int i=0; i<2; ++i){
     	for(int j=0; j<2; ++j){
     		for(int z=0; z<3; ++z){
     			suma += A[i][z] * x[z][j];	 
			 }
			 IAx[i][j] =id[i][j] - suma;
			 suma = 0;
			 
                
		 }
		 
            
	 }
	   for(int i=0; i<3; ++i){
     		for(int j=0; j<2; ++j){
     			for(int z=0; z<2; ++z){
     				suma2 += x[i][z]* IAx[z][j];	 
			 	}
			 	x[i][j] = suma2;
			 	suma2 = 0;      
		 	}      
	 	}
	 
        
}
// Calcula Alfa
double CalcAlfa(double A[2][3]){
	double norma =0;
	double alfa  =0;
   	for(int i=0; i<2; ++i){
   		for(int j=0; j<3; ++j){
   			norma += pow(abs(A[i][j]), 2) ;
   		}   
    }
    alfa = pow(norma,-1);

    return alfa;   
}
// Calcula el x inicial
int Calcx0(double transposed[3][2],double alfa){
	double suma = 0;
    for(int i=0; i<3; ++i){
    	for(int j=0; j<2; ++j){
			x[i][j] =  transposed[i][j]*alfa;     
		}      
	}    
}
        

double pseudoinversa (double A[2][3],double b[4],double tol,double Max){
  // Esta funcion aproxima la solución de un sistema de ecuaciones 
  //lineales utilizando el método iterativo de Jacobi
  // Parametros de entrada: A=matriz de coeficientes
  //						b = vector de términos independientes
  //						MAX = iteraciones máximas
  //                        tol= tolerancia
  // Parametros de salida:  x=aproximacion numerica de la solucion
  //                        e = error
    double sol[3];
	int it =0;
	double error = tol +1;
	transpuesta(A);
    Calcx0(transposed,CalcAlfa(A));
    while(it<Max && error>tol) 
		{
     		CalcX(A,x);
        	error = CalError(A,x);
        	errores.push_back(error);
        	it++;
        
		}
		double solsum = 0;
		for(int i=0; i<3; ++i){
   			for(int j=0; j<2; ++j){
   				solsum += x[i][j] * b[j];
  			}
	   		sol[i] = solsum;
	   		cout << solsum<< " ";
	   		solsum = 0;
	    	cout << "\n";
		}
		cout << "Error= " << error<<"\n";
		cout << "Iteracion= " << it<<"\n";
		//Muestra la grafica Iteraciones vs Error
		initwindow(500, 500);	
		line(80,100, 80,300);
		line(10,200, 450,200);
		settextstyle(4,0,1);
		outtextxy(90, 230, "Cantidad de iteraciones");
		settextstyle(4,1,1);
		outtextxy(70, 50, "Error");
		int i = 1;
    	while( !errores.empty() )
    	{
	      double num1 = errores.front()*40;
	      errores.pop_front();
	      double num2 = errores.front()*40;
	      setcolor(4);
	      line(80+(i*40),200- num1, (80+(i+1)*40),200-num2);
	      putpixel(i*40,200,2);
	      i++;
		}
		while(!kbhit()) delay(1);	
        	return 0;

}

main(int argc, char *argv[])
{
	double A[2][3] = {{1,2,-1},{-3,1,5}};
    double b[2] = {1,4};
    pseudoinversa (A,b,0.0003,Max);
}

