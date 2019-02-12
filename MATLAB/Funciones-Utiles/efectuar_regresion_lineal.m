function [pendiente, ordenada_al_origen] = efectuar_regresion_lineal(x, y)
    
    media_x = mean(x); media_y = mean(y);
    media_x_cuadrado = mean(x.^2); media_y_cuadrado = mean(y.^2);
    media_cuadrada_x = media_x^2; media_cuadrada_y = media_y^2;
    desviacion_estandar_x = sqrt(media_x_cuadrado - media_cuadrada_x); 
    desviacion_estandar_y = sqrt(media_y_cuadrado - media_cuadrada_y);
    covarianza = mean(x .* y) - media_x * media_y;
    r = covarianza / (desviacion_estandar_x * desviacion_estandar_y);
    pendiente = r * desviacion_estandar_y  / desviacion_estandar_x;
    ordenada_al_origen = -(pendiente * media_x) + media_y;

end

