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
    
    h = eliminar_distorsion_no_lineal(h);
    h_hilbert = abs(hilbert(h));
    h_cuadrado = h_hilbert.^2;
    lim_superior = estimar_limite_superior_de_integracion_de_schroeder(h_cuadrado, fs);
    s_cuadrado = 0:1/fs:lim_superior/fs - 1/fs;
    dx = 1/fs;
    s_cuadrado(1) = integrar_array(h_cuadrado, lim_superior, dx);
    for i=2:lim_superior
        s_cuadrado(i) = s_cuadrado(i-1) - h_cuadrado(i-1)*dx;
    end
end

function integral = integrar_array(x, lim_superior, dx)

    integral = 0;
    for j=1:lim_superior
        integral = integral + x(j)*dx;
    end
    
end