fs =  44100; %Hertz
tiempo = 10; %Segundos
potencia = 8; %Watts
x = generar_ruido_blanco_gaussiano(tiempo, fs, potencia);

medicion_basica(x,fs,tiempo);