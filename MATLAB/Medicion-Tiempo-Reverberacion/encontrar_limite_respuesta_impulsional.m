%{
    Encuentra el punto de quiebre donde termina la respuesta
    impulsional propiamente dicha. Se entiende que todo lo que
    hay a la derecha de este punto es "ruido"
    El criterio para seleccionar este punto es algo arbitrario,
    y puede mejorarse posteriormente mediante otros métodos
    Los parámetros n y epsilon representan lo mismo que en la función
    de eliminar un techo constante.
    A prueba y error, elegi 2*10^-10 como el epsilon que mejor se
    ajustaba a mi respuesta impulsional de prueba con n=20, s=10, 
    utilizando el método de promedios.
    Aumentar el epsilon, correrá el límite a la izquierda, mientras que
    disminuirlo lo correrá hacia la derecha.
%}

function i = encontrar_limite_respuesta_impulsional(varargin)

    h = varargin{1};
    n = varargin{2};
    epsilon = varargin{3}; 
    h = h./max(h);
    i = length(h);
    if (nargin == 3) %Método estándar
        for j=1:n:length(h)-n
            if (abs(h(j+n) - h(j)) <= epsilon)
               i = j; 
               break;
            end
        end
    elseif (nargin == 4) %Método de promedios
        semiancho_ventana = varargin{4}; 
        if (semiancho_ventana <= n/2) 
            for j=1:n:length(h)
                if (j - (semiancho_ventana + 1) < 0)
                    padding = zeros(1, j - (semiancho_ventana + 1));
                    data_j = h(j:j+semiancho_ventana);
                    promedio_j = mean(cat(2,padding,data_j));
                    promedio_j_mas_n = mean(h(j+n-(semiancho_ventana+1):j+n+semiancho_ventana));
                elseif (j + n + semiancho_ventana > length(h))
                    padding = zeros(1, (j + n + semiancho_ventana) - length(h));
                    data_j_mas_n = h(j + n - (semiancho_ventana + 1):end);
                    promedio_j = mean(h(j - (semiancho_ventana + 1):j + semiancho_ventana));
                    promedio_j_mas_n = mean(cat(2,data_j_mas_n,padding));
                else
                    promedio_j = mean(h(j - (semiancho_ventana + 1):j + semiancho_ventana));
                    promedio_j_mas_n = mean(h(j + n - (semiancho_ventana + 1):j + n + semiancho_ventana));
                end
                if (abs(promedio_j_mas_n - promedio_j) < epsilon)
                   i = j; 
                   break;
                end
            end
        end
    end

end

