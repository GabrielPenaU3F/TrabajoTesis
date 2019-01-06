function y = calcular_envolvente_energetica(x, fs, periodo)

    y = zeros(1,length(x));
    Ts = 1/fs;
    duracion = length(x)/fs;
    
    for i=1:length(y)
       tiempo_actual = calcular_tiempo_muestra(i,fs); 
       if ((tiempo_actual + periodo) <= duracion) 
           y(i) = calcular_potencia_eficaz(x, Ts, tiempo_actual, periodo);  
       else
           y(i) = calcular_potencia_eficaz(x, Ts, tiempo_actual, duracion-tiempo_actual);
       end
    end