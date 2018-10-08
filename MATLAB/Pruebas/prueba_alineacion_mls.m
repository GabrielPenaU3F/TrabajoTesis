%Para efectuar esta prueba, cargar los archivos de la señal mls generada y
%grabada que están en la carpeta Sonidos. La señal generada deberá ser
%llamada 'x' y la señal grabada deberá ser llamada 'y'. 

lag = finddelay(x,y); %Computa el delay exacto entre el comienzo de cada señal

y_align = y(lag+1:end); %Eliminamos la parte nula al principio de la señal grabada
x_align = x(1:end-lag); %Eliminamos la parte sobrante al final de la señal generada, que no tendrá correspondencia con ninguna parte de la señal grabada

%Ahora, x_align y y_align tienen la misma longitud y están alineadas
%muestra a muestra.

Rxy = xcorr(x_align,y_align);

%Graficamos las cinco señales
t_duracion = length(x)/fs;
t = 0:1/fs:t_duracion - 1/fs;
t_duracion_align = length(x_align)/fs;
t_align = 0:1/fs:t_duracion_align - 1/fs;
t_r = 0:1/fs:length(Rxy)/fs - 1/fs;
subplot(3,2,1);
plot(t,x);
title('Señal MLS');
subplot(3,2,2);
plot(t_align,x_align);
title('Señal MLS sincronizada');
subplot(3,2,3);
plot(t,y);
title('Señal grabada');
subplot(3,2,4);
plot(t_align,y_align);
title('Señal grabada sincronizada');
subplot(3,2,[5,6]);
plot(t_r, Rxy);
title('Correlación cruzada entre las señales sincronizadas');

