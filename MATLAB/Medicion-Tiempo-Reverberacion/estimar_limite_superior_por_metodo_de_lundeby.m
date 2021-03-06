function [lim, pendiente, ordenada_al_origen] = estimar_limite_superior_por_metodo_de_lundeby(h, fs)

    h_cuadrado = h.^2;
    
    %Paso 1
    longitud_filtro = 0.030 * fs; %Cantidad de muestras correspondes a 30ms de se�al.
    %Nota: para bandas de baja frecuencia conviene tomar filtros m�s largos
    h_cuadrado_suave = aplicar_filtro_media_movil(h_cuadrado, longitud_filtro);
    h_cuadrado_db = 20*real(log10(h_cuadrado_suave./max(h_cuadrado_suave)));
    
    %Paso 2
    porcentaje_de_cola = 10; %El ultimo 10% de duracion de la se�al ser� la 'cola'
    nivel_de_ruido_de_fondo = estimar_nivel_de_ruido_de_fondo(h_cuadrado_db, porcentaje_de_cola);
    
    %Paso 3
    tope_de_estimacion = nivel_de_ruido_de_fondo + 10;
    decaimiento = obtener_segmento_de_curva(h_cuadrado_db, 0, abs(tope_de_estimacion));
    t = 0:1/fs:length(decaimiento)/fs - 1/fs;
    [pendiente, ordenada_al_origen] = efectuar_regresion_lineal(t, decaimiento, 0);
    
    %Paso 4
    t_cruce = nivel_de_ruido_de_fondo/pendiente;
    muestra_cruce = calcular_muestra(t_cruce, 1/fs);
    
    %Paso 5
    valor_decaimiento = abs(h_cuadrado_db(muestra_cruce));
    intervalos_por_10_db = 5;
    cantidad_intervalos = valor_decaimiento * intervalos_por_10_db / 10;
    longitud_intervalo = floor(muestra_cruce / cantidad_intervalos);
    
    %Paso 6
    h_cuadrado_nuevo = aplicar_filtro_media_movil(h_cuadrado_db, longitud_intervalo);
    
    for i=0:5
        
        %Paso 7
        porcentaje_minimo_ri = 10;
        margen_de_db = 5;
        limite_ruido_de_fondo = buscar_limite_ruido_de_fondo(h_cuadrado_nuevo, muestra_cruce, margen_de_db, porcentaje_minimo_ri);
        nivel_de_ruido_de_fondo = mean(h_cuadrado_nuevo(limite_ruido_de_fondo:end));

        %Paso 8
        decaimiento_tardio = obtener_segmento_de_curva(h_cuadrado_nuevo, abs(nivel_de_ruido_de_fondo + 20), abs(nivel_de_ruido_de_fondo + 7));
        t = 0:1/fs:length(decaimiento_tardio)/fs - 1/fs;
        [pendiente, ordenada_al_origen] = efectuar_regresion_lineal(t, decaimiento_tardio);

        %Paso 9
        t_cruce = (nivel_de_ruido_de_fondo - ordenada_al_origen)/pendiente;
        muestra_cruce = calcular_muestra(t_cruce, 1/fs);
        
    end
    lim = muestra_cruce;
    
end