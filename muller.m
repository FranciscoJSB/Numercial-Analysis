% Método de Muller

function muller
  %Ejemplo Numérico tomado de las presentaciones
  %funcion por aproximar(sring)
  func='sin(x)-(x/2)';
  %valores iniciales (numeros)
  x0=2; 
  x1=2.2;
  x2=1.8;
  tolerancia=10^-8;
  %iteraciones maximas (int)
  iterMax=5;
  %Se llama a la funcion metodoMuller
  [aprox,error]=metodoMuller(func,x0,x1,x2,tolerancia,iterMax)
end

function [aprox,error] = metodoMuller(func, x0, x1, x2, tolerancia,iterMax)
  format long;%formato de los numeros para que tengan 15 decimales
  %cargar los paquetes para la grafica
  pkg load symbolic
  syms x
  f1=sym(func); %Convierte el texto a simbolico
  fr = Inf;
  f=matlabFunction(f1); %Función f en formato del lenguaje M
  %arreglo de errores para la gráfica
  e=[]; kg=[]; k=0;
  %aproximacion inicial
  aprox = 0;
    
    %condicion de parada cuando la aproximacion sea igual o menor a la tolerancia
    while(fr >= tolerancia )
      %se incrementa la iteración
      k++; 
      %se llama a la funcion para resolver el sistema de ecuaciones
      values = SistEcuaciones(func, x0, x1, x2);
      %se llama a la funcion para resolver la ecuacion cuadratica
      [s1, s2] = SolucCuadratica(values(1), values(2), values(3));     
      %se llama a la funcion para obtener el valor de las constantes del sistema
      [x0, x1, x2] = Constat_Sistema(s1, s2, x0, x1, x2);
      %valor de la aproximacion
      aprox = x0;
      %condicion de parada
      fr = abs(evaluar(func, aprox));
      
      %Error relativo de la aproximación
      error=abs(x0-(x1))/abs(x0);
      
      %se llenan los arreglos de la grafica
      e=[e error];
      kg=[kg k];
      
    endwhile
    %impresión de la graficaa
    plot(kg,e); %impresion 
    title ("Grafica de Error vs iteraciones");%titulo de la grafica
    legend(func); %titulo de la linea
    xlabel("iteraciones"); %eje x
    ylabel("Error");  %eje y

endfunction 

% funciones auxiliares

%funcion para encontrar el valor de las constantes del sistema de ecuaciones
function [a, b, c] = Constat_Sistema(s1, s2, x1, x2, x3)

  [f1, f2] = aproxNumeros(s1, x1, x2, x3);
  [p1, p2] = aproxNumeros(s2, x1, x2, x3);
  %se orden de mayor a menor
  if(abs(f1 - f2) < abs(p1 - p2))
    a = s1; %solucion 1
    b = f1; %funcion 1
    c = f2; %funcion 2
  else
    a = s2; %solucion 2
    b = p1; %funcion 1
    c = p2; %funcion 2
  endif
endfunction

%funcion para resolver los sistemas de ecuaciones
function [solution] = SistEcuaciones(func, x0, x1, x2)
  %se crea el sistema de ecuaciones como matrices
  matrixA = [x0^2, x0, 1; x1^2, x1, 1; x2^2, x2, 1];
  matrixB = [evaluar(func, x0); evaluar(func, x1); evaluar(func, x2)];
  solution = matrixA\matrixB;
endfunction

%funcion para obtener valores de funciones cuadraticas por medio del discriminante
function [s1, s2] = SolucCuadratica(a, b, c)
    %se obtiene el discriminante por formula general
  discriminante = b ^ 2 - 4 * a * c;
  %se tienen ambas soluciones
  s1 = (-b + sqrt(discriminante)) / (2 * a);
  s2 = (-b - sqrt(discriminante)) / (2 * a);
endfunction

% se crea la funcion para poder evaluar la funcion en diferentes variables (x0,x1,x2)
function [r] = evaluar(func, x) %r corresponde a un arreglo de las variables
  r = eval(func);% se evalua la función
endfunction

function [a, b] = aproxNumeros(s, x1, x2, x3)
  dS = [abs(s - x1), abs(s - x2), abs(s - x3)];  
  a = x1;
  b = x2;
  if(dS(3) < dS(1))
    a = x3;
  elseif(dS(3) < dS(2))
    b = x3;
  endif
endfunction
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%