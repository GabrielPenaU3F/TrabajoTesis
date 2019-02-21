%{ 
Uso el algoritmo de Schroeder para obtener la curva de
decaimiento cuadratico. Para cada t, el valor s^2(t) es directamente
proporcional a la integral desde t a infinito de la respuesta impulsional
cuadrada. (Ignoramos la constante de proporcionalidad porque nos interesa
la relaci�n, no los valores exactos). Esto se traduce en sumar los valores
de la respuesta impulsional original, desde la muestra del instante t
hasta el final de la se�al.
%}

function s_cuadrado = obtener_curva_de_decaimiento_cuadratico(h, fs)

    h_cuadrado_original = h.^2;
    %h_hilbert = abs(hilbert(abs(h)));
    h_suave = aplicar_filtro_media_movil(h,100);
    coef_ajuste = max(h)/max(h_suave);
    h_suave = h_suave.*coef_ajuste;
    %h_cuadrado = abs(hilbert(h_cuadrado_original));
    h_cuadrado = h.^2;
    lim_superior = estimar_limite_superior_de_integracion_de_schroeder(h_suave.^2, fs);
    c_corr = calcular_termino_de_correccion(h_suave, fs, lim_superior);
    s_cuadrado = 0:1/fs:lim_superior/fs - 1/fs;
    
    dx = 1/fs;
    s_cuadrado(1) = integrar_array(h_cuadrado, lim_superior, dx);
    for i=2:lim_superior
        s_cuadrado(i) = s_cuadrado(i-1) - h_cuadrado(i-1)*dx;
    end
    %Si se utiliza la trasnformada de Hilbert, se calcula 
    %el ruido de fondo sobre la respuesta impulsional original,
    %ya que la envolvente de Hilbert tiene una r�plica del pico inicial
    %al final de la se�al y esta destruye el c�lculo.
    s_cuadrado = sustraer_ruido_de_fondo(s_cuadrado, h_cuadrado, fs, lim_superior);
    s_cuadrado = s_cuadrado + c_corr;
    
end

function integral = integrar_array(x, lim_superior, dx)

    integral = 0;
    for j=1:lim_superior
        integral = integral + x(j)*dx;
    end
    
end

function s = sustraer_ruido_de_fondo(s_cuadrado, h, fs, lim_superior)
    
    s = 0:1/fs:length(s_cuadrado)/fs - 1/fs;
    nivel_ruido_de_fondo_cuadrado = mean(h(lim_superior:end))^2;
    for i=1:length(s_cuadrado)
        distancia_temporal = (lim_superior - i)/fs;
        s(i) = s_cuadrado(i) - nivel_ruido_de_fondo_cuadrado * distancia_temporal;
    end
end

function c_corr = calcular_termino_de_correccion(h, fs, lim_superior)
    c_corr = 0;
    if (lim_superior < length(h))
        h_db = 10*real(log10(h./max(h)));
        nivel_limite = h_db(lim_superior);
        decaimiento_final = abs(nivel_limite)-10;
        decaimiento_inicial = abs(nivel_limite)-20;
        [muestra_inicial, muestra_final] = obtener_segmento_de_curva(h_db, decaimiento_inicial, decaimiento_final);
        t = muestra_inicial/fs:1/fs:muestra_final/fs;
        y = h(muestra_inicial:muestra_final);
        [A, rho] = efectuar_regresion_exponencial(t,y);
        
        %{
        t = 0:1/fs:length(h)/fs - 1/fs;
        exponencial = A*exp(rho.*t);
        exp_db = 10*log10(exponencial./max(exponencial));
        figure;
        plot(t,h,t,exponencial);
        figure;
        plot(t,h_db,t,exp_db);
        %}
        
        c_corr = (A^2/(2*rho))*exp(2*rho*lim_superior/fs);
    end
end