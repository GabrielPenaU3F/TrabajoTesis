%{
    Encuentra el punto de quiebre donde termina la respuesta
    impulsional propiamente dicha. Se entiende que todo lo que
    hay a la derecha de este punto es "ruido"
    El criterio para seleccionar este punto es algo arbitrario,
    y puede mejorarse posteriormente mediante otros métodos
    Los parámetros n y epsilon representan lo mismo que en la función
    de eliminar un techo constante.
    A prueba y error, elegi 10^-7 como el epsilon que mejor se
    ajustaba a mi respuesta impulsional de prueba con n=10, 
    utilizando el método de promedios.
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
    elseif (nargin == 4) 
        flag = varargin{4};
        if (flag == 1) %Método de promedios
            n_muestras_primer_intervalo = round(n/2);
            for j=1:n:length(h)-n
                promedio_primer_intervalo = mean(h(j:j+n_muestras_primer_intervalo));
                promedio_segundo_intervalo = mean(h(j+n_muestras_primer_intervalo:j+n));
                if (abs(promedio_segundo_intervalo - promedio_primer_intervalo) <= epsilon)
                   i = j; 
                   break;
                end
            end
        end
    end

end

