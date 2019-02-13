function s_db = obtener_curva_de_decaimiento_en_db(h, fs)

    s_cuadrado = obtener_curva_de_decaimiento_cuadratico(h,fs);
    s = sqrt(s_cuadrado);
    max_s = max(s);
    s_norm = s./max_s;
    s_db = 20*real(log10(s_norm));
