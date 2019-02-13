function graficar_respuestas_impulsionales(h, fs)

    h = eliminar_distorsion_no_lineal(h);
    h_hilbert = abs(hilbert(h));
    h_hilbert_suave_51 = aplicar_filtro_media_movil(h_hilbert, 51);
    h_hilbert_suave_501 = aplicar_filtro_media_movil(h_hilbert, 501);
    h_hilbert_suave_5001 = aplicar_filtro_media_movil(h_hilbert, 5001);
    e_t = 20*real(log10(h_hilbert./max(h_hilbert)));
    e_t_suave_51 = 20*real(log10(h_hilbert./max(h_hilbert_suave_51)));
    e_t_suave_501 = 20*real(log10(h_hilbert./max(h_hilbert_suave_501)));
    e_t_suave_5001 = 20*real(log10(h_hilbert./max(h_hilbert_suave_5001)));
    t = 0:1/fs:length(h)/fs - 1/fs;
    plot(t,e_t, t, e_t_suave_51, t, e_t_suave_501, t, e_t_suave_5001);