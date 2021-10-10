function descensoCoordinado
  %Ejemplo Numérico tomado de las presentaciones
  %funcion por aproximar(sring)
  %tomada de las presentaciones
  func='(x(1)-2)**2 + (x(2)+3)**2+ x(1)*x(2)';
  %valores iniciales (numeros)
  x=[1,1];
  tol=10^-8;
  %iteraciones maximas (int)
  iterMax=100;
  %Se llama a la funcion coordinado
  [aprox,eAux]=coordinado(func,x,tol,iterMax)
end

%Metodo del descenso coordinado

%Entradas
% func --> funcion por evaluar --> string("funcion")
% x --> intervalo de valores iniciales --> [x,y]
%tol --> tolerancia --> float
%iterMax --> iteraciones maximas --> int 

%Salidas
% aprox --> valor de la aproximacion 
% error del calculo 
% grafica de error vs iteraciones

function [aprox,eAux] = coordinado(func, x, tol,iterMax)
  format long;%formato de los numeros para que tengan 15 decimales
  eAux=1;
  error = Inf;
  xAux = x;
  %arreglos para almacenar los valores de la grafica
  e=[]; i=[];
  
  for k =1:iterMax
      
      while(error >= tol)
      [aprox,error] = minGS(func, xAux);
      
      xAux = aprox;
      %iteraciones
      k++;
      eAux=-norm(gradient(aprox));
      e=[e eAux];
      i=[i k];
      endwhile
  endfor
  
  %seccion de la grafica
  plot(i,e)
  %impresión de la graficaa
  title ("Grafica de Error vs Iteraciones");
  legend(func);
  xlabel("iteraciones");
  ylabel("Error");  
  
endfunction

%Se aplica una funcion auxiliar para obtener los minimos de la funcion de coordinado
% se aplica la regla de Sneidell para obtener los minimos
function [minimo,tol] = minGS(func, x)
  %valores iniciales
  tamano = size(x)(2);
  minimo = [];
  func = @(x) eval(func);
    %iteraciones para el primer valor del intervalo
    for i = 0:tamano-1
      func = @(z) func([x(1 : i), z, x(i + 2 : tamano)]);
      minimo(i+1) = fminsearch(func,x(i+1)); 
    endfor 
  tamano = size(minimo)(2);
  tol = 0;
    %iteraciones para el segundo valor del intervalo 
    for i=1:tamano
      tol +=(x(i)- minimo(i))**2;
    endfor 
  tol = sqrt(tol);
endfunction