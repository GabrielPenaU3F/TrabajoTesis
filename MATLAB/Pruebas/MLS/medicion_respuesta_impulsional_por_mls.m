clc;

%{
Esta prueba se realiza con los siguientes datos:
x = Señal mls generada. Es el archivo senal_mls_generada de la carpeta Sonidos
y = Señal mls grabada. Es el archivo senal_mls_grabada de la carpeta Sonidos
fs = Frecuencia de muestreo 44100
Longitud de la secuencia mls: 16 bits, es decir, 2^16 - 1 muestras
Periodos de la secuencia mls: 7 periodos
Senoide: 100 períodos con frecuencia de 100 Hz. Duración 1 segundo
Silencio: 2 segundos
Longitud total de la señal: 1*44100(senoide) + 2*44100(silencio) + 7*(2^16 - 1)(mls)
%}

h = calcular_respuesta_impulsional_mls(x, y, fs, 16, 7);

t = 0:1/fs:length(h)/fs - 1/fs;
plot(t,h);