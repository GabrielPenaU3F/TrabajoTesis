function [x_mls, y_mls] = recuperar_mls_puro(x, y, fs, frecuencia_senoide, cant_periodos_senoide, tiempo_silencio)

    [x_align, y_align] = alinear_senales(x,y);

    %Eliminación de la senoide
    tiempo_senoide = (1/frecuencia_senoide)*cant_periodos_senoide; %Duracion de la senoide
    muestras_senoide = tiempo_senoide*fs; %Cantidad de muestras que conforman la senoide
    x_sin_senoide = x_align(muestras_senoide+1:end);
    y_sin_senoide = y_align(muestras_senoide+1:end);
    
    %Eliminación del silencio
    muestras_silencio = tiempo_silencio*fs;
    x_mls = x_sin_senoide(muestras_silencio+1:end);
    y_mls = y_sin_senoide(muestras_silencio+1:end);

    