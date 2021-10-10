% Metodo de la Biseccion

function biseccion
  %Ejemplo Num�rico tomado de las presentaciones
  func='e**x-x-2'; %funci�n (str)
  v_inicial=0; % valor del intervalo inicial (int)
  v_final=2; %valor del intevalo final (int)
  tolerancia=10**-8; %tolerancia (float)
  itera_max=10;  %iteraciones m�ximas (int)
  %llamar a la funci�n de Bisecci�n principal
  [x,error]=biseccion_metodo(func,v_inicial, v_final, tolerancia, itera_max)
end

function [x,error] = biseccion_metodo(func,v_inicial, v_final, tolerancia, itera_max)
  format long;
  %cargar los paquetes para la grafica
  pkg load symbolic
  syms x
  f1=sym(func); %Convierte el texto a simbolico
  f=matlabFunction(f1); %Funci�n f en formato del lenguaje M
  %arreglo de errores para la gr�fica
  e=[]; i=[];
  
  %se comprueba el teorema de Bolzano
  if (bolzano_teorema(v_inicial,v_final,func)) 
    
    a=v_inicial;  
    b=v_final;
    x0=(v_final-v_inicial)/2;
    
  %Si todavia no se tiene un error aceptable, se evalua si se cumple bolzano en ambos intervalos nuevos
  %y el que cumpla se usa para la siguiente iteraci�n, cuando se alcanza un error aceptable para y devuelve el resultado
    while(x0>=tolerancia)      
        x =(a+b)/2;
        
        error=x0;
        %verificacion del teorema de Bolzano
        if(bolzano_teorema(a, x, func)) 
          b=x;
          
        elseif (bolzano_teorema(x, b, func)) 
           a=x; 
          
        endif
        %se incremental las iteraciones
        itera_max++;
        %formula de la biseccion 
        x0 =(v_final-v_inicial)/(2^itera_max);
        
        %arreglos de la grafica
        e=[e x0];
        i=[i itera_max];
    endwhile

  endif
  
  plot(i,e)
  %impresi�n de la graficaa
  title ("Grafica de Error vs Iteraciones");
  legend(func);
  xlabel("iteraciones");
  ylabel("Error");   
endfunction

%funcion del teorema de Bolzano para realizar la verificaci�n
function [bolzano] = bolzano_teorema(v_inicial, v_final, func)
  %se evaula la funcion para el valor inicial
  x = v_inicial;
  fa = eval(func);
  %se evaula la funcion para el valor final
  x = v_final;
  fb = eval(func);
  %se realiza la comprobacion del teorema
  bolzano = (fa*fb<=0);
endfunction
