%La frecuencia de la senoide, por supuesto, deberá ser menor que fs
function senoide = generar_senoide(fs, amplitud, frecuencia, fase_inicial, cantidad_periodos)

    %Genero un periodo
    %En 1 segundo entran fs muestras
    %Un periodo dura 1/frecuencia, en segundos
    %Luego, hay tantas muestras por periodo como m = fs/frecuencia
    periodo_senoide = 0:1/fs:1/frecuencia - 1/fs;
    for i=1:length(periodo_senoide)
        periodo_senoide(i) = amplitud * sin(2*pi*frecuencia*periodo_senoide(i) + fase_inicial);
    end
    
    %Genero todos los periodos
    senoide = 0;
    for i=1:cantidad_periodos
        senoide = cat(2, senoide, periodo_senoide);
    end
    senoide = senoide(2:end);
        
    