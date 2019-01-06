%{
    El algoritmo es basicamente el mismo que para el cálculo del EDT,
    con la diferencia de que, por estándar ISO, el t20 se calcula
    desde los -5dB.

    t = 10 para el caso edt
    t = 20 para el caso t20
    t = 30 para el caso t30

%}


function tx = calcular_tx(s_db, fs, t)

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
    else
        s_db = obtener_segmento_de_curva(s_db,0,10);
    end
    
    tx = length(s_db)/fs;
    