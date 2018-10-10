function y = obtener_respuesta_mls_promediada(mls, fs, n_bits, cantidad_periodos)

    periodos_x = separar_periodos_mls(mls,n_bits,cantidad_periodos);
    longitud_periodo = 2^n_bits - 1;
    sumatoria_periodos = zeros(1,longitud_periodo);

    %Itero sobre todos los periodos 
    for i=1:cantidad_periodos

        periodo_actual = periodos_x(:,i);
        %Recorro el periodo y sumo sus valores punto a punto al vector
        %sumatoria
        for j=1:longitud_periodo
            sumatoria_periodos(j) = sumatoria_periodos(j) + periodo_actual(j);
        end
    end

    y = sumatoria_periodos ./ cantidad_periodos; %Divido punto a punto por la cantidad de periodos para obtener el promedio