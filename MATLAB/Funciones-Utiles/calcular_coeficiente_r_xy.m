function r_xy = calcular_coeficiente_r_xy(x,y)

    n = length(x); 
    
    %Primero, calculamos las medias muestrales
    x_media = mean(x);
    y_media = mean(y);
    
    %Calculamos la suma-producto de las desviaciones de x e y
    numerador = 0;
    for i=1:n
        numerador = numerador + (x(i) - x_media)*(y(i) - y_media);  
    end
    
    %Calculamos la suma de las desviaciones cuadradas de x y de y, y sus
    %respectivas raices cuadradas
    suma_desv_cuadradas_x = 0;
    suma_desv_cuadradas_y = 0;
    for i=1:n
       suma_desv_cuadradas_x = suma_desv_cuadradas_x + ((x(i) - x_media)^2); 
       suma_desv_cuadradas_y = suma_desv_cuadradas_y + ((y(i) - y_media)^2); 
    end
    denominador = sqrt(suma_desv_cuadradas_x)*sqrt(suma_desv_cuadradas_y);
    
    %Resultado
    r_xy = numerador / denominador;
    