fs =  44100; %Hertz
tiempo = 10; %Segundos
potencia = 8; %Watts
x_ruido = generar_ruido_blanco_gaussiano(tiempo/2, fs, potencia);
x_silencio = generar_silencio(tiempo/2, fs);
x = cat(2,x_ruido,x_silencio); %El 2 especifica que concateno por la segunda dimension, columnas

medicion_basica(x,fs,tiempo);

