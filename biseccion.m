% Metodo de la Biseccion

function biseccion
  %Ejemplo Numérico tomado de las presentaciones
  func='e**x-x-2'; %función (str)
  v_inicial=0; % valor del intervalo inicial (int)
  v_final=2; %valor del intevalo final (int)
  tolerancia=10**-8; %tolerancia (float)
  itera_max=10;  %iteraciones máximas (int)
  %llamar a la función de Bisección principal
  [x,error]=biseccion_metodo(func,v_inicial, v_final, tolerancia, itera_max)
end

function [x,error] = biseccion_metodo(func,v_inicial, v_final, tolerancia, itera_max)
  format long;
  %cargar los paquetes para la grafica
  pkg load symbolic
  syms x
  f1=sym(func); %Convierte el texto a simbolico
  f=matlabFunction(f1); %Función f en formato del lenguaje M
  %arreglo de errores para la gráfica
  e=[]; i=[];
  
  %se comprueba el teorema de Bolzano
  if (bolzano_teorema(v_inicial,v_final,func)) 
    
    a=v_inicial;  
    b=v_final;
    x0=(v_final-v_inicial)/2;
    
  %Si todavia no se tiene un error aceptable, se evalua si se cumple bolzano en ambos intervalos nuevos
  %y el que cumpla se usa para la siguiente iteración, cuando se alcanza un error aceptable para y devuelve el resultado
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
  %impresión de la graficaa
  title ("Grafica de Error vs Iteraciones");
  legend(func);
  xlabel("iteraciones");
  ylabel("Error");   
endfunction

%funcion del teorema de Bolzano para realizar la verificación
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
