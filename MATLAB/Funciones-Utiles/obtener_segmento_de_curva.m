%Los decaimientos son positivos, ejemplo: 0  y 10 para calcular EDT, 5 y 35 para calcular T30

function s = obtener_segmento_de_curva(s_db,decaimiento_inicial,decaimiento_final)

     %{
        Primero, eliminamos la parte de la curva que no es util
        Utilizo como par�metros n=10 muestras y epsilon = 10^-6 dB,
        lo que implica que si pierdo informaci�n �til de la se�al,
        la duraci�n temporal de esta ser� como m�ximo 226us y su
        contenido de amplitud no exceder� la millon�sima parte de un dB.
        Estos par�metros se pueden ajustar, pero definidos de esta manera
        me aseguro que produzcan una p�rdida despreciable.
    
    %}

    s_db = eliminar_techo_constante(s_db,10,10^-6);
    
    %Eliminamos por izquierda
    if (decaimiento_inicial > 0)
       s_db = eliminar_n_db(s_db, decaimiento_inicial); 
    end
    
    decaimiento_requerido = decaimiento_final - decaimiento_inicial;
    [y_max,x_max] = max(s_db);

    %{ 
        Desde la localizacion del maximo (la parte anterior
        es ruido producto de que la respuesta impulsional
        no estaba centrada y conten�a tambi�n ruido) se
        busca el punto donde el sonido ha deca�do t db
    %}
    
    decaimiento = 0;
    i = x_max+1;
    while (decaimiento < decaimiento_requerido) 
       
        if (i+1 < length(s_db))
            i = i+1;
            decaimiento = abs(s_db(i) - y_max);
        else
            break;
        end
        
    end
    
    %{
        Cuando superamos el decaimiento requerido, se elimina todo
        lo que resta a la derecha    
    %}
    
    s = s_db(x_max:i-1);