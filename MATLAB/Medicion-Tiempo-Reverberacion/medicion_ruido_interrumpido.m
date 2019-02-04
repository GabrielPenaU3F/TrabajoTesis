fs = 44100;
tiempo_grabacion = 10;
tiempo_ruido = 5;
potencia = 50;
ruido = generar_ruido_blanco_gaussiano(tiempo_ruido, fs, potencia);

%Reproducir la señal de medicion
audio_player = audioplayer(ruido, fs);
play(audio_player);

%Grabar la respuesta
audio_recorder = audiorecorder(fs, 24, 1); %24 bits, canal mono
recordblocking(audio_recorder, tiempo_grabacion); %Grabo por tantos segundos como dure la señal y bloqueo el programa
y = getaudiodata(audio_recorder);
audiowrite('E:\Universidad\Tesis\Codigo y Recursos\TrabajoTesis\Sonidos\Pruebas\ruido_interrumpido_10seg.wav',y,fs);
