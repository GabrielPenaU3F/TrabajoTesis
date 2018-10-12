function [x_align, y_align] = alinear_senales(x,y)

    lag = finddelay(x,y); %Computa el delay exacto entre el comienzo de cada se�al
    y_align = y(lag+1:end); %Eliminamos la parte nula al principio de la se�al grabada
    x_align = x(1:end-lag); %Eliminamos la parte sobrante al final de la se�al generada, que no tendr� correspondencia con ninguna parte de la se�al grabada