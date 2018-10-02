function y = recortar_senal(senal, fs, t_inicial, t_final)

    duracion = length(senal)/fs; %En segundos
    nro_muestra_t_inicial = 1 + t_inicial*fs;
    nro_muestra_t_final = 1 + t_final*fs;
    y = senal(nro_muestra_t_inicial:nro_muestra_t_final);