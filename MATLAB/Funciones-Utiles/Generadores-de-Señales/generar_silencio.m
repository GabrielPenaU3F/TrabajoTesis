function y = generar_silencio(tiempo_duracion, fs)

    Ts = 1/fs;
    cantidad_muestras = tiempo_duracion/Ts;
    y = zeros(1, cantidad_muestras);
    
    