function [x] = fact_qr(A, b)
  %% Ax = b. Metodo por factorizacion QR, donde A se puede descomponer en dos matrices;
  %% Q (matriz ortogonal) y R(matriz tringular superior). A=QR; donde (Q^T)Q=I
  %% Ax = b
  %% QRx = b
  %% (Q^-1)QRx = (Q^-1)b   
  %% Rx = (Q^-1)b 
  %% (R^-1)Rx = (R^-1)(Q^-1)b 
  %% x = (R^-1)(Q^T)b
  
  %% Las entradas de la funcion son la matriz de coeficientes A y la matriz de terminos
  %% independientes b
  
  %% La salidas es el vector solucion del sistema x
  
  [Q R] = houseHolderMethod(A);
  
  x = inv(R)*Q'*b';       %% x = (R^-1)(Q^T)b
  
end


function [Q, R] = houseHolderMethod(A)
  
  [m n] = size(A);
  Q = eye(m,m);
  R = A;
  

  nMin=min(m,n);
  
  %%Calculo de la reflexión de Householder para la matriz Q y R
  for i=1:nMin
    x = R(i:m, i);
    s=0;
   
    if x(1)==0
        s = 1;
    else
        s = sign(x(1));
    endif
   
   
    e = zeros(m - i + 1, 1);   
    e(1)=1;   
    v = s * norm(x) * e + x;
    v = v / norm(v);
    
    
    R(i:m, i:n) =  R(i:m, i:n) - 2*(v*v')*R(i:m, i:n);
    Q(:,i:m) = Q(:,i:m) - Q(:,i:m)*(2*v*v'); 
  end
  
  %%Correccion de signos
  for i=1:n
    R(end,i) = -R(end,i);
  endfor
  for i=1:m
    Q(i,end) = -Q(i,end);
  endfor

end

clc; clear;

%Ejemplos
  %[x] = fact_qr([5 1 1; 1 5 1; 1 1 5], [7, 7, 7])
  %[x] = fact_qr([1, 2; 3, 4], [1, 1])
  %[x] = fact_qr([10 3 1; 2 -10 3; 0 -1 2], [14,-5,2])