%Recuperamos la señal MLS pura

%100 periodos de senoide de 100 Hz, 2 segundos de silencio 
[x_mls, y_mls] = recuperar_mls_puro(x,y,fs,100,100,2);

%Grafico
t_mls_puro = 0:1/fs:length(x_mls_puro)/fs - 1/fs;
subplot(2,2,1);
plot(t_mls_puro, x_mls_puro);
title('Señal MLS pura generada');
subplot(2,2,2);
plot(t_mls_puro, y_mls_puro);
title('Señal MLS pura grabada');
subplot(2,2,[3,4]);
Rxy = xcorr(x_mls,y_mls);
t_corr = 0:1/fs:length(Rxy)/fs - 1/fs;
plot(t_corr, Rxy);