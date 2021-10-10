function [error,x_k] = gauss_seidel(A,b, x_0, tol, iterMax)

  [n,m] = size(A);
  x_k = x_0;

  if n==m % Verifica que A sea cuadrada
    if det(A) != 0 % verifica que A sea invertible.
      %---------------- Verificar que sea convergente. ------------------
      D = diag(diag(A));
      convergencia = 1;
      for i = 1:n
        suma = 0;
        for j = 1:n
          if i != j
            suma = suma + abs(A(i,j));
          endif
        endfor
        if suma > abs(D(i,i))
          convergencia = -1;
          break
        endif
      endfor
      %---------------- Verificar que sea convergente. ------------------
      
      if convergencia == 1 %Si A converge    
        U = zeros(n);
        for i = 1:n
          for j = 2:n
            if j>i
              U(i,j) = A(i,j);
            endif
          endfor  
        endfor

        L_mas_D = A - U;
        c = sust_adelante(L_mas_D,b);
        
        % --------------- Metodo Iterativo --------------------
        
        for k = 1:iterMax
          menos_U_por_x = -U*x_k;
          z = sust_adelante(L_mas_D,menos_U_por_x);
          x_k = z + c;
          error = norm(A*x_k-b,2);
          e = [e error];
          if error<tol 
            break
          endif
        endfor
        
        % --------------- Metodo Iterativo --------------------

        plot(0:k,e)
        
      else 
        display("A no converge");
      end       
    else
      display("A no es invertible")
    end
  else
    display("A no es cuadrada")
  end
end
% --------------- Valores para probar a el metodo Gauss Seidel ----------------
%A = [5 1 1; 1 5 1;1 1 5];
%b = [7 7 7];
%iterMax=50; 
%tol = 1e-10;
%[n,m] = size(A)
%x_0 = zeros(m,1)




% A = [10 3 1; 2 -10 3; 0 -1 2]
% b = [14;-5;14]
% --------------- Valores para probar a el metodo Gauss Seidel ----------------



% ----------------------------------- sust_adelante ----------------------------------------
% Requisitos: Matriz A: invertible y Triangular Inferior(Los numeros abajo)
% Ax = b

function x = sust_adelante(A, b)
  
  [n,m] = size(A);
  x = zeros(n,1);  
  
  for i = 1:n

    % Calculo de la sumatoria
    j = 1;
    sumatoria = 0;
 
    while j <= i-1
      sumatoria = sumatoria + A(i,j)*x(j);
      j = j + 1;
    endwhile
  
    x(i) = (1/A(i,i))*(b(i) - sumatoria);
 
  endfor
end
% ------------------------- sust_adelante --------------------------------------

clc; clear;


