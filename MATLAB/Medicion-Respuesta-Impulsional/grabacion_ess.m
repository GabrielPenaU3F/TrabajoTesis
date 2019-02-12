fs = 44100;
T = 12;
f1 = 20;
f2 = 22050;

x = generar_senal_ess(fs,T,f1,f2);
tiempo_duracion = length(x)/fs;

%Guardo en archivo
audiowrite('E:\Universidad\Tesis\Codigo y Recursos\TrabajoTesis\Sonidos\Pruebas\senal_ess_generada_12seg_vol_alto.wav',x,fs);

%Reproducir la señal de medicion
audio_player = audioplayer(x, fs);
play(audio_player);

%Grabar la respuesta
audio_recorder = audiorecorder(fs, 24, 1); %24 bits, canal mono
recordblocking(audio_recorder, tiempo_duracion); %Grabo por tantos segundos como dure la señal y bloqueo el programa
y = getaudiodata(audio_recorder);
audiowrite('E:\Universidad\Tesis\Codigo y Recursos\TrabajoTesis\Sonidos\Pruebas\senal_ess_grabada_12seg_vol_alto.wav',y,fs);
