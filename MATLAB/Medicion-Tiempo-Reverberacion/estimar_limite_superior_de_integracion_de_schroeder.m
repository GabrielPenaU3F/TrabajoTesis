function lim = estimar_limite_superior_de_integracion_de_schroeder(h, fs)
    
    %{
        Para estimar, primero se calcula un umbral inicial
        Luego, se aplica el método de dividir la señal en dos, una a
        cada lado del umbral. Los dos grupos de puntos resultantes
        se ajustan a dos respectivas rectas. Se selecciona como
        límite superior de integración el punto de intersección
        entre las mismas.
    %}

    n = 40;
    semiancho_ventana = 20;
    %epsilon = 5*10^-7; %Valor adecuado para la medición MLS con un solo filtro
    %epsilon = 5*10^-5;  %Valor adecuado para la medición MLS con doble filtro
    epsilon = 5*10^-10; %Valor adecuado para la medición ESS
    umbral_inicial = encontrar_limite_respuesta_impulsional(h, n, epsilon, semiancho_ventana);
    if (umbral_inicial < length(h))
        h_abs = abs(h); %Porque queremos encontrar una 'recta envolvente'
        h_izquierda = h_abs(1:umbral_inicial);
        h_derecha = h_abs(umbral_inicial+1:end);
        t_izquierda = 0:1/fs:umbral_inicial/fs - 1/fs;
        t_derecha = (umbral_inicial+1)/fs:1/fs:length(h_abs)/fs; 
        [m_izquierda, b_izquierda] = efectuar_regresion_lineal(t_izquierda, h_izquierda);
        [m_derecha, b_derecha] = efectuar_regresion_lineal(t_derecha, h_derecha);
        t_interseccion = (b_derecha - b_izquierda) / (m_izquierda - m_derecha);
        lim = calcular_muestra(t_interseccion, 1/fs);
    else
        lim = umbral_inicial;
    end
    
    %{
        %Graficar (opcional)
        t = 0:1/fs:length(h_abs)/fs - 1/fs;
        t_izquierda = 0:1/fs:umbral_inicial/fs - 1/fs;
        t_derecha = (umbral_inicial+1)/fs:1/fs:length(h_abs)/fs;
        recta_izquierda = m_izquierda*t_izquierda + b_izquierda;
        recta_derecha = m_derecha*t_derecha + b_derecha;
        plot(t, h_abs, t_izquierda, recta_izquierda, t_derecha, recta_derecha);
    %}
    
end

