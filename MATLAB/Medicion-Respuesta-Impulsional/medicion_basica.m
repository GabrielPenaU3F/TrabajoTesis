function rta = medicion_basica(x, fs, tiempo_duracion)

%Reproducir la señal de medicion
audio_player = audioplayer(x, fs);
play(audio_player);

%Grabar la respuesta
audio_recorder = audiorecorder(fs, 24, 1); %16 bits, canal mono
recordblocking(audio_recorder, tiempo_duracion); %Grabo por tantos segundos como dure la señal y bloqueo el programa
y = getaudiodata(audio_recorder);


%GRAFICOS

%Señal de medicion en tiempo
eje_t = 0:1/fs:tiempo_duracion-1/fs; 
subplot(3,2,1);
plot(eje_t,x);
axis([0 15 0 15]);
xlabel('t(seg)');
ylabel('Amplitud(V)');
title('Señal de medición x(t)');

%Señal de medicion en frecuencia
eje_f = 0:fs/length(x):fs/2-fs/length(x);
xfft = fft(x);
xfft_graf = xfft(1:length(x)/2);
subplot(3,2,2);
plot(eje_f, abs(xfft_graf), eje_f, angle(xfft_graf));
axis([0 22050 0 8000]);
xlabel('f(Hz)');
legend('Modulo', 'Fase');
title('Señal de medición X(f)');

%Señal grabada en tiempo
eje_t = 0:1/fs:length(y)/fs-1/fs; 
subplot(3,2,3);
plot(eje_t,y);
axis([0 15 0 0.5]);
xlabel('t(seg)');
ylabel('Amplitud(V)');
title('Señal grabada y(t)');

%Señal grabada en frecuencia
eje_f = 0:fs/length(y):fs/2-fs/length(y);
yfft = fft(y);
yfft_graf = yfft(1:length(y)/2);
subplot(3,2,4);
plot(eje_f, abs(yfft_graf), eje_f, angle(yfft_graf));
axis([0 22050 0 100]);
xlabel('f(Hz)');
legend('Modulo', 'Fase');
title('Señal grabada Y(f)');

%H(f) = Y(f)/X(f)
hfft = calcular_respuesta_frecuencial(xfft, yfft);
h_t = ifft(hfft);

%Respuesta impulsional
eje_t = 0:1/fs:length(h_t)/fs-1/fs; 
subplot(3,2,5);
plot(eje_t,real(h_t));
axis([0 15 0 0.001]);
xlabel('t(seg)');
ylabel('Amplitud(V)');
title('R. impulsional h(t)');

%Respuesta frecuencial
eje_f = 0:fs/length(hfft):fs-fs/length(hfft);
subplot(3,2,6);
plot(eje_f, abs(hfft), eje_f, angle(hfft));
axis([0 22050 0 10]);
xlabel('f(Hz)');
legend('Modulo', 'Fase');
title('Respuesta frecuencial H(f)');