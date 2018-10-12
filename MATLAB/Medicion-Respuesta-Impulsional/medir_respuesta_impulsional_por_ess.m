function h = medir_respuesta_impulsional_por_ess(fs, T, f1, f2)

    x = generar_senal_ess(fs,T,f1,f2);
    filtro_inverso = generar_filtro_inverso_ess(fs,T,f1,f2);
    tiempo_duracion = length(x)/fs;

    %Reproducir la señal de medicion
    audio_player = audioplayer(x, fs);
    play(audio_player);

    %Grabar la respuesta
    audio_recorder = audiorecorder(fs, 24, 1); %24 bits, canal mono
    recordblocking(audio_recorder, tiempo_duracion); %Grabo por tantos segundos como dure la señal y bloqueo el programa
    y = getaudiodata(audio_recorder);
    
    %Procesar
    h = conv(y,filtro_inverso);