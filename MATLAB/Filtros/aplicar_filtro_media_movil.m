function y = aplicar_filtro_media_movil(x, n)

    %n es la cantidad de puntos a promediar, o el ancho
    %de la ventana móvil
    
    kernel = ones(1, n) / n;
    y = filter(kernel, 1, x);