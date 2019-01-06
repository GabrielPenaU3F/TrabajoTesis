function s_db = obtener_curva_de_decaimiento_en_db(h, fs)

    s_cuadrado = obtener_curva_de_decaimiento_cuadratico(h,fs);
    max_s = max(s_cuadrado);
    s_cuadrado_norm = s_cuadrado./max_s;
    s_cuadrado_db = 10*real(log10(s_cuadrado_norm));
    s_db = s_cuadrado_db./2; 