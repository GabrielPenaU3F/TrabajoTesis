%{
    El algoritmo es basicamente el mismo que para el cálculo del EDT,
    con la diferencia de que, por estándar ISO, el t20 se calcula
    desde los -5dB.

    t = 10 para el caso edt
    t = 20 para el caso t20
    t = 30 para el caso t30
    t = 60 para el caso t60

%}


function [tx, r_xy] = calcular_tx(s_db, fs, t, graficar)
    
    %Si es EDT, el intervalo va entre 0 y -10
    %Si es T60, se utiliza el intervalo de T30 y se extrapola
    %Para T20 y T30, se utiliza el intervalo -5, -25 y -3, -35
    %respectivamente
    if (t == 10) 
        s_db = obtener_segmento_de_curva(s_db,0,10);
    elseif (t == 60)
        s_db = obtener_segmento_de_curva(s_db,5,25);
    else
        s_db = obtener_segmento_de_curva(s_db,5,t+5);
    end
    
    x = 0:1/fs:length(s_db)/fs - 1/fs;
    
    r_xy = calcular_coeficiente_r_xy(x, s_db); %Coeficiente de correlación lineal; este se devuelve
    
    [pendiente, ordenada_al_origen] = efectuar_regresion_lineal(x, s_db);
    
    if (nargin==4) 
        if (graficar==1)
            y_recta = (pendiente .* x) + ordenada_al_origen;
            plot(x, s_db, x, y_recta);
        end
    end
    %longitud_senal_estimulo = (length(s_db) + 1)/2;
    %tx = (-(ordenada_al_origen + t)/pendiente)/(longitud_senal_estimulo/fs);
    tx = -(ordenada_al_origen + t)/pendiente;