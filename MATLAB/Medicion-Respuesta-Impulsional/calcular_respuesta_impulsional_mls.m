function h = calcular_respuesta_impulsional_mls(mls_generada, mls_grabada, fs, n_bits, cantidad_periodos)

    [x, y] = recuperar_mls_puro(mls_generada, mls_grabada, fs, 100, 100, 2);
    periodo_promediado_y = obtener_respuesta_mls_promediada(y, fs, n_bits, cantidad_periodos);
    longitud_periodo = 2^n_bits - 1;
    periodo_x = x(1:longitud_periodo);
    h = xcorr(periodo_x, periodo_promediado_y);
    