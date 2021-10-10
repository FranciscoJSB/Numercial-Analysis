function archivo_gaussiana
  %Ejemplo Numérico
  %P1: Definir parámetros de entrada
  
  %ejemplo tomado de la presentacion 4 diapositiva 16
  A=[1,1,-1,3;0,-1,-1,-5;0,0,3,13;0,0,0,-13]
  b=[4;-7;13;-13];
  
  %P2: Llamar a la función
  [x]=gaussiana(A,b)
end

%Entradas
% Matriz A --> arreglo de numeros, la ";" representa la siguiente fila
% Vector b --> vector de términos independientes

%Salida
% x --> solución del sistema como vector 
function[x]=gaussiana(A,b)
  %tamaño del vector 
  n=length(b);
  i=n;
  %se recorre la matriz
  for k=1:(n-1)
      for j=(k + 1):n
        f=A(j,k)/A(k,k);
        A(j,:)=A(j,:)-(f * A(k,:));
        b(j)=b(j)-(f*b(k));
      endfor
  endfor
  x=[];
  while i>=1
    x_i=0;
    for j=i+1:n
      x_i+=A(i,j)*x(j);
    endfor
    %se resuelve Ax=b 
    x(i)=(1/A(i,i))*(b(i)-x_i);
    i--;
  endwhile
  
endfunction
