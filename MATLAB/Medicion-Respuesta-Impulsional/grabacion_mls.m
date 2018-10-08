fs =  44100; %Hertz
n_bits = 16;
periodos = 7;
x = generar_senal_mls_sincrona(fs,n_bits,periodos);
tiempo_duracion = length(x)/fs;

%Guardo en archivo
audiowrite('E:\Universidad\Tesis\Codigo y Recursos\TrabajoTesis\Sonidos\senal_mls_generada.wav',x,fs);

%Reproducir la señal de medicion
audio_player = audioplayer(x, fs);
play(audio_player);

%Grabar la respuesta
audio_recorder = audiorecorder(fs, 24, 1); %24 bits, canal mono
recordblocking(audio_recorder, tiempo_duracion); %Grabo por tantos segundos como dure la señal y bloqueo el programa
y = getaudiodata(audio_recorder);
audiowrite('E:\Universidad\Tesis\Codigo y Recursos\TrabajoTesis\Sonidos\senal_mls_grabada.wav',y,fs);
