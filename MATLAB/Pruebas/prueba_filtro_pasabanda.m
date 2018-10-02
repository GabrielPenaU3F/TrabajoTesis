%Para esta prueba se utiliza como dato la señal conformada por los tonos
%440, 480 y 1760, que se encuentra en la carpeta 'Sonidos' Se permiten pasar los primeros dos y se observa que en la
%señal de salida no hay ninguna componente en frecuencia alrededor de
%1.7khZ. 

clc

f_pasabanda_400_500 = construir_filtro_pasabanda(fs,399,400,500,501,60,1,60);
%[b,a] = tf(f_pasabanda_400_500); %Funcion de transfrerencia del filtro. b
%son los coeficientes del numerador, a son los coeficientes del denominador.
filtered_signal = filter(f_pasabanda_400_500,data);

f = 0: fs/length(filtered_signal) : fs/2;
data_freq = fft(filtered_signal);
ydft = data_freq(1:length(filtered_signal)/2+1);
plot(f,abs(ydft));