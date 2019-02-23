function h = calcular_respuesta_impulsional_mls(mls_generada, mls_grabada, fs, n_bits, cantidad_periodos)

    mls_suave = aplicar_filtro_media_movil(mls_grabada, 50);
    [x, y] = recuperar_mls_puro(mls_generada, mls_suave, fs, 100, 100, 2);
    %y_suave = aplicar_filtro_media_movil(y,50);
    periodo_promediado_y = obtener_respuesta_mls_promediada(y, fs, n_bits, cantidad_periodos);
    periodo_promediado_suave = aplicar_filtro_media_movil(periodo_promediado_y, 50);
    longitud_periodo = 2^n_bits - 1;
    periodo_x = x(1:longitud_periodo);
    h = xcorr(periodo_promediado_suave, periodo_x);