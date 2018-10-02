function y = aplicar_filtro_octava(data, fs, f_central)

    %Las bandas de octava se caracterizan por las siguientes formulas,
    %donde f1 y f2 son las frecuencias inferior y superior de la banda y 
    %fc la frecuencia central
    
    %fc = sqrt(f1*f2) (Frecuencia central)
    %f2 = 2f1 (Relación de 2)
    
    %Se deduce entonces que f1 = fc/sqrt(2)
    
    f1 = f_central/sqrt(2);
    f2 = 2*f1;
    
    %Se utilizan frecuencias de corte un 1% por debajo y por encima de las
    %frecuencias de paso necesarias
    filtro = construir_filtro_pasabanda(fs, f1-f1*0.01, f1, f2, f2+f2*0.01, 60, 1, 60);
    y = filter(filtro, data);