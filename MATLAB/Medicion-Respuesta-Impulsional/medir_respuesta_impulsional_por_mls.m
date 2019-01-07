function h = medir_respuesta_impulsional_por_mls(fs, n_bits, periodos)

    x = generar_senal_mls_sincrona(fs,n_bits,periodos);
    tiempo_duracion = length(x)/fs;

    %Reproducir la señal de medicion
    audio_player = audioplayer(x, fs);
    play(audio_player);

    %Grabar la respuesta
    audio_recorder = audiorecorder(fs, 24, 1); %24 bits, canal mono
    recordblocking(audio_recorder, tiempo_duracion); %Grabo por tantos segundos como dure la señal y bloqueo el programa
    y = getaudiodata(audio_recorder);
    
    %Procesar
    h = calcular_respuesta_impulsional_mls(x, y, fs, n_bits, periodos);

