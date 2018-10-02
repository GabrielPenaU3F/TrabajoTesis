function y = aplicar_filtro_tercio_octava(data, fs, f_central)

    %Las bandas de tercio de octava se caracterizan por las siguientes formulas,
    %donde f1 y f2 son las frecuencias inferior y superior de la banda y 
    %fc la frecuencia central
    
    %fc = sqrt(f1*f2) (Frecuencia central)
    %f2 = f1*2^(1/3) (Relación de 2^(1/3))
    
    %Se deduce entonces que f1 = fc/2^(1/6)
    
    f1 = f_central/(2^(1/6));
    f2 = (2^(1/3))*f1;
    
    %Se utilizan frecuencias de corte un 1% por debajo y por encima de las
    %frecuencias de paso necesarias
    filtro = construir_filtro_pasabanda(fs, f1-f1*0.01, f1, f2, f2+f2*0.01, 60, 1, 60);
    y = filter(filtro, data);