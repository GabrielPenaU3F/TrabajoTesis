%{
    El algoritmo es basicamente el mismo que para el cálculo del EDT,
    con la diferencia de que, por estándar ISO, el t20 se calcula
    desde los -5dB.

    t = 10 para el caso edt
    t = 20 para el caso t20
    t = 30 para el caso t30

%}


function tx = calcular_tx(s_db, fs, t, graficar)

    %{
        Primero, eliminamos la parte de la curva que no es util
        Utilizo como parámetros n=10 muestras y epsilon = 10^-6 dB,
        lo que implica que si pierdo información útil de la señal,
        la duración temporal de esta será como máximo 226us y su
        contenido de amplitud no excederá la millonésima parte de un dB.
        Estos parámetros se pueden ajustar, pero definidos de esta manera
        me aseguro que produzcan una pérdida despreciable.
    
    %}

    s_db = eliminar_techo_constante(s_db,10,10^-6);
    
    %Si no es EDT, se eliminan los primeros 5dB
    if (t ~= 10) 
        s_db = obtener_segmento_de_curva(s_db,5,t+5); 
    elseif (t~= 60)
        s_db = obtener_segmento_de_curva(s_db,5,35);
    else
        s_db = obtener_segmento_de_curva(s_db,0,10);
    end
    
    y = s_db;
    x = 0:1/fs:length(y)/fs - 1/fs;
    
    media_x = mean(x); media_y = mean(y);
    media_x_cuadrado = mean(x.^2); media_y_cuadrado = mean(y.^2);
    media_cuadrada_x = media_x^2; media_cuadrada_y = media_y^2;
    desviacion_estandar_x = sqrt(media_x_cuadrado - media_cuadrada_x); 
    desviacion_estandar_y = sqrt(media_y_cuadrado - media_cuadrada_y);
    covarianza = mean(x .* y) - media_x * media_y;
    r = covarianza / (desviacion_estandar_x * desviacion_estandar_y);
    pendiente = r * desviacion_estandar_y  / desviacion_estandar_x;
    ordenada_al_origen = -(pendiente * media_x) + media_y;
    
    if (nargin==4) 
        if (graficar==1)
            y_recta = (pendiente .* x) + ordenada_al_origen;
            plot(x, y, x, y_recta);
        end
    end
    
    tx = -(ordenada_al_origen + t)/pendiente;
    