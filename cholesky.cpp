//Se importan las librerías

#include <iostream>
#include <armadillo>
#include <vector>

using namespace std;
using namespace arma;

//Fin de las importaciones

//Se declaran las funciones que se van a utilizar

Mat<double> fact_cholesky(string, string);
Mat<double> fact_cholesky_aux(Mat<double>);
Mat<double> sustitucion_adelante(Mat<double>, Mat<double>);
Mat<double> sustitucion_atras(Mat<double>, Mat<double>);

//Fin de las declaraciones


//Ejemplo numerico

int main() {
   
    Mat<double> vector_solucion = fact_cholesky("25 15 -5 -10; 15 10 1 -7; -5 1 21 4; -10 -7 4 18", "-25 -19 -21 -5"); 
    cout<<vector_solucion<<endl;
    return 0;
}

// Esta funcion calcularnumericamente el conjunto solucion de un sistema de ecuaciones dado
// Parametros de entrada : matriz_coeficientes = matriz con los coeficientes
//                         vector_terminos = vector con los terminos independientes                   

// Parametros de salida : matriz_y = solucion del sistema
Mat<double> fact_cholesky(string matriz_coeficientes, string vector_terminos){
    Mat<double> matriz_A = mat(matriz_coeficientes);
    Mat<double> matriz_B = mat(vector_terminos);

    Mat<double> matriz_L;
    Mat<double> matriz_Y;
    Mat<double> matriz_X;

    if(!matriz_A.is_sympd()){

        matriz_A = trans(matriz_A) * matriz_A;
        matriz_B = trans(matriz_B) * matriz_B;
    }

    matriz_L = fact_cholesky_aux(matriz_A);
    matriz_Y = sustitucion_adelante(matriz_L,matriz_B);
    matriz_X = sustitucion_atras(trans(matriz_L),matriz_Y);

    return matriz_X;    
    
}

Mat<double> fact_cholesky_aux(Mat<double> matriz_A){
    
    int n = size(matriz_A).n_rows;

    Mat<double> matriz_L = mat(n,n, fill::zeros);

    for(int i  = 0; i < n; i++){
        for(int j = 0; j < i+1 ; j ++ ){

            double suma = 0;
            
            if(j==i){

                for(int k = 0; k < j; k++){
                    suma += pow(matriz_L(j,k),2);                    
                }

                matriz_L(j,j) = sqrt(matriz_A(j,j)-suma);
            }
            else{

                for(int k = 0; k < j; k++){
                    suma += matriz_L(i,k) * matriz_L(j,k);
                }

                matriz_L(i,j) = (matriz_A(i,j) - suma)/matriz_L(j,j);
            }
        }
    }

    return matriz_L;
}

Mat<double> sustitucion_adelante(Mat<double> matriz_A, Mat<double> matriz_b){
    int n = size(matriz_A).n_rows;
    Mat<double> x = mat(1,n, fill::zeros);

    for (int i = 0; i < n; i++)
    {
        double suma = 0;
        for(int j = 0; j < i; j++){
            suma += (matriz_A(i,j)*x(j));
        }

        x(i) = (matriz_b(i)-suma)/matriz_A(i,i);
    }    

    return x;
}

Mat<double> sustitucion_atras(Mat<double> matriz_A, Mat<double> matriz_b){
    int n = size(matriz_A).n_rows;
    Mat<double> x = mat(1,n, fill::zeros);

    for (int i = n-1; i > -1; i--)
    {
        int suma = 0;
        for(int j = i; j < n; j++){
            suma += (matriz_A(i,j)*x(j));
        }
        x(i) = (matriz_b(i)-suma)/matriz_A(i,i);
    }    

    return x;
}
