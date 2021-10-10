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
double d[4][4];
double nM[4][4];
double C[4];
double T[4][4];
double x[4];
//Iteraciones maximas
int Max = 50;
// Errores calculados en cada iteracion
list <double> errores;

//Verifica si una matriz es diagonalmente dominante
bool dominante(double A[4][4]){
	bool dominante = true;
	int d;
	double suma = 0;
	for(int i = 0; i < n; i = i + 1)
	{
	   for(int j = 0; j < n; j = j + 1)
		{
			if(i == j){
				d = A[i][i];
			}else{
				suma += A[i][j];
			}
		     
		}
		
		if(d<suma){
			dominante = false;
			i = n;
		}
		suma = 0;
	}
	return dominante;
	
}
//Calcula la diagonal de una matriz
int diagonal(double A[4][4]){
	for(int i = 0; i < n; i = i + 1)
	{
	   for(int j = 0; j < n; j = j + 1)
		{
			if(i == j){
				int num =  (A[i][i]);
				d[i][i] = pow(num, -1);
			}else{
				d[i][j] = 0;
			}
		     
		}
		
	}
	

	return 1;
	
}

//Calcula el producto de la matriz A con el vector b
int CalcC(double A[4][4],double b[4]){
	double suma = 0;
   for(int i=0; i<n; ++i){
   	for(int j=0; j<n; ++j){
   			suma += A[i][j] * b[j];
               
	   }
	   C[i] = suma;
	   suma = 0;
            
   }
        
}

// Calcula el x de la iteracion actual
int CalcX(double T[4][4]){
	double suma = 0;

   for(int i=0; i<n; ++i){
   	for(int j=0; j<n; ++j){
   			suma += T[i][j] * x[j];
               
	   }
	   x[i] = suma + C[i];
	   suma = 0;
            
   }
        
}
// Calcula el error de la iteracion actual
double CalError(double A[4][4], double X[4],double b[4]){
	double suma = 0;
	double error =0;
   for(int i=0; i<n; ++i){
   	for(int j=0; j<n; ++j){
   			suma += A[i][j] * x[j];
   			
               
	   }
	   suma -= b[i];

	   error += pow(suma, 2);
	   
	   suma = 0;
            
   }
   error = sqrt(error);
     return error;   
}
// Multiplica la matriz d por la matriz N
int CalcT(double D[4][4],double B[4][4]){
	double suma = 0;
     for(int i=0; i<n; ++i){
     	for(int j=0; j<n; ++j){
     		for(int z=0; z<n; ++z){
     			suma += D[i][z] * B[z][j];
     			 
			 }
			 T[i][j] = suma;
			 suma = 0;
			 
                
		 }
		 
            
	 }
        
        
}
        
//Calcula la matriz N             
int N(double A[4][4]){

	for(int i = 0; i < n; i = i + 1)
	{
	   for(int j = 0; j < n; j = j + 1)
		{
			if(i == j){
				nM[i][i] = 0;
			}else{
				nM[i][j] = A[i][j]*-1;
			}
		     
		}
		
	}


	return 1;
	
}
double jacobi (double A[4][4],double b[4],double tol,double x0[4]){
  // Esta funcion aproxima la solución de un sistema de ecuaciones 
  //lineales utilizando el método iterativo de Jacobi
  // Parametros de entrada: A=matriz de coeficientes
  //						b = vector de términos independientes
  //						X0 =  valor inicial
  //						MAX = iteraciones máximas
  //                        tol= tolerancia
  // Parametros de salida:  x=aproximacion numerica de la solucion
  //                        e = error
  
  //Verifica si la matriz es diagonalmente dominante
    if (dominante(A)){
        diagonal(A);
        N(A);
        CalcC(d, b);
        CalcT(d,nM);
         for(int i = 0; i < n; i = i + 1){
        	x[i] = x0[i];
		}
		int it =0;
		double error = tol +1;
        while(it<Max && error>tol) 
		{
        	CalcX(T);
        	error = CalError(A,x,b);
        	errores.push_back(error);
        	it++;
        
		}
		for(int z=0; z<n; ++z){
     		cout << "X" <<z+1<<"="<<x[z]<<"\n";
     			 
			 }
			 cout << "Error= " << error<<"\n";
			  cout << "Iteracion= " << it<<"\n";
			  	initwindow(500, 500);	
				line(40,10, 40,420);
				line(10,400, 450,400);
				settextstyle(4,0,1);
				outtextxy(100, 420, "Cantidad de iteraciones");
				settextstyle(4,1,1);
				outtextxy(30, 50, "Error");
				// init window graphics
				
    
    int i = 1;
     while( !errores.empty() )
    {
      double num1 = errores.front()*1000;
      errores.pop_front();
      double num2 = errores.front()*1000;
      setcolor(4);
      line(40+(i*20),400- num1, (40+(i+1)*20),400-num2);
      putpixel(i*20,400,2);
      i++;
      
    }

	while(!kbhit()) delay(1);	
			   
        
      

        return 0;
    }
    else{
        cout << "La matriz debe ser diagonalmente dominante \n";
        return 0;
    }
}

main(int argc, char *argv[])
{
	 double A[4][4] = {{8,2,5,0},{9,70,8,1},{14,1,21,2},{7,1,2,21}};
     double x0[4] = {0,0,0,0};
    double b[4] = {1,1,1,1};
   

  cout << jacobi(A,b,0.0000003,x0);
}

