%{
    Encuentra el punto de quiebre donde termina la respuesta
    impulsional propiamente dicha. Se entiende que todo lo que
    hay a la derecha de este punto es "ruido"
    El criterio para seleccionar este punto es algo arbitrario,
    y puede mejorarse posteriormente mediante otros métodos
    Los parámetros n y epsilon representan lo mismo que en la función
    de eliminar un techo constante.
    A prueba y error, elegi 5*10^-6 como el epsilon que mejor se
    ajustaba a mi respuesta impulsional de prueba con n=10
%}

function i = encontrar_limite_respuesta_impulsional(h, n, epsilon)

    h = h./max(h);
    i = length(h);
    for j=1:length(h)-n
        if (abs(h(j+n) - h(j)) <= epsilon)
           i = j; 
           break;
        end
    end

end

