%Para efectuar esta prueba, cargar los archivos de la se�al mls generada y
%grabada que est�n en la carpeta Sonidos. La se�al generada deber� ser
%llamada 'x' y la se�al grabada deber� ser llamada 'y'. 

lag = finddelay(x,y); %Computa el delay exacto entre el comienzo de cada se�al

y_align = y(lag+1:end); %Eliminamos la parte nula al principio de la se�al grabada
x_align = x(1:end-lag); %Eliminamos la parte sobrante al final de la se�al generada, que no tendr� correspondencia con ninguna parte de la se�al grabada

%Ahora, x_align y y_align tienen la misma longitud y est�n alineadas
%muestra a muestra.

%Graficamos las cuatro se�ales
t_duracion = length(x)/fs;
t = 0:1/fs:t_duracion - 1/fs;
t_duracion_align = length(x_align)/fs;
t_align = 0:1/fs:t_duracion_align - 1/fs;
subplot(2,2,1);
plot(t,x);
title('Se�al MLS');
subplot(2,2,2);
plot(t_align,x_align);
title('Se�al MLS sincronizada');
subplot(2,2,3);
plot(t,y);
title('Se�al grabada');
subplot(2,2,4);
plot(t_align,y_align);
title('Se�al grabada sincronizada');

