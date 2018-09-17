%La potencia debe darse en watts, el tiempo en segundos
function y = generar_ruido_blanco_gaussiano(tiempo_duracion, fs, potencia)

    P_dbW = 10*log10(potencia);
    Ts = 1/fs;
    cantidad_muestras = tiempo_duracion/Ts;

    %Primer par�metro: filas de la matriz de ruido
    %Segundo par�metro: columnas de la matriz de ruido
    %Tercer par�metro: potencia en dBW (referida a 1W en 0dBW)
    y = wgn(1,cantidad_muestras,P_dbW); 

    %Devuelve una se�al de ruido blanco. La amplitud de las muestras se expresa en Volts. 