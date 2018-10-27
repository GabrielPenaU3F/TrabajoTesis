%{ 
Uso el algoritmo de Schroeder para obtener la curva de
decaimiento cuadratico. Para cada t, el valor s^2(t) es directamente
proporcional a la integral desde t a infinito de la respuesta impulsional
cuadrada. (Ignoramos la constante de proporcionalidad porque nos interesa
la relación, no los valores exactos). Esto se traduce en sumar los valores
de la respuesta impulsional original, desde la muestra del instante t
hasta el final de la señal.
%}


function s_cuadrado = obtener_curva_de_decaimiento_cuadratico(h,fs)

    h_cuadrado = h.^2;
    s_cuadrado = 0:1/fs:length(h_cuadrado)/fs - 1/fs;
    
    s_cuadrado(1) = sumar_array(h_cuadrado);
    for i=2:length(s_cuadrado)
        s_cuadrado(i) = s_cuadrado(i-1) - h_cuadrado(i-1);
    end
    
end

function suma = sumar_array(x)

    suma = 0;
    for j=1:length(x) 
        suma = suma + x(j);
    end
    
end