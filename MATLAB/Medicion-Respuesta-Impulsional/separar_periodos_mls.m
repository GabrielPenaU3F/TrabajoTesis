function matriz_periodos = separar_periodos_mls(mls, n_bits, cantidad_periodos);

    longitud_periodo = 2^n_bits - 1;
    longitud_necesaria = cantidad_periodos*longitud_periodo;
    mls = dar_longitud_exacta(mls, longitud_necesaria);
    matriz_periodos = zeros(longitud_periodo,1);
    
    for i=1:cantidad_periodos
        periodo_actual = mls(1:longitud_periodo);
        matriz_periodos = [matriz_periodos, periodo_actual']; %Concatena a derecha todos los vectores columna
        %Nota: la comilla ' indica matriz transpuesta. Es para que lo
        %considere con las mismas dimensiones que el otro vector
        mls = mls(longitud_periodo+1:end); %Eliminamos el período ya agregado a la matriz
    end
    
    matriz_periodos(:,1) = []; %Eliminamos la primer columna de la matriz, la de ceros

end

%Aseguramos que la longitud de la señal mls sea exactamente la cantidad de
%periodos por la longitud de un período. Para eso, rellenamos con ceros si
%la señal real es mas corta y la truncamos si es más larga. (Esto último,
%teóricamente, no debería ocurrir nunca pero le da mayor robustez al
%algoritmo)
%IMPORTANTE: Rellenar con ceros el último período no alterará
%significativamente el resultado, puesto que estos valores se promedian punto a punto con
%todos los demás períodos
function y = dar_longitud_exacta(x, longitud_necesaria)

    if (length(x) < longitud_necesaria)
        y = zeros(1,longitud_necesaria);
        for i=1:longitud_necesaria
            if (i <= length(x))
                y(i) = x(i);
            else
                y(i) = 0;
            end
        end
    elseif (length(x) > longitud_necesaria)
        y = zeros(1,longitud_necesaria)
        for i=1:longitud_necesaria
            y(i) = x(i);
        end
    end
    
end
         
          
                

    