function s_db = obtener_curva_de_decaimiento_en_db(h, fs)

    h = eliminar_distorsion_no_lineal(h);
    s_cuadrado = obtener_curva_de_decaimiento_cuadratico(h, fs);
    s_db = 10*real(log10(s_cuadrado./max(s_cuadrado)));
