clc;

%100 periodos de senoide de 100 Hz, 2 segundos de silencio 
[x_mls, y_mls] = recuperar_mls_puro(x,y,fs,100,100,2);

z = obtener_respuesta_mls_promediada(y_mls,fs,16,7);
Rxx = xcorr(z, z);
t = 0:1/fs:length(Rxx)/fs - 1/fs;
plot(t,Rxx);