function s_db = obtener_curva_de_decaimiento_de_ruido_interrumpido_sin_latencia(data)

    i = 1;
    while (abs((data(i+1) - data(i)) < 0.05)) 
        i = i+1;
    end
    data = data(i+1:end);

    data_norm = data ./ max(data);
    s_db = 10*real(log10(data_norm));
    
        
        