%Los tiempos se indican en segundos
function valor_eficaz = calcular_potencia_eficaz(data, Ts, t_comienzo, periodo) 

    T_duracion_total = (length(data) - 1) * Ts;
    t_final = t_comienzo + periodo - Ts;

    if (t_comienzo > T_duracion_total) 
        fprintf('El tiempo de inicio del periodo excede la duracion del audio %.4f \n', T_duracion_total);
    elseif (t_final > T_duracion_total + 1) 
        fprintf('El periodo indicado excede la duracion del audio \n');
    elseif (periodo < Ts)
        fprintf('El periodo indicado es mas corto que el periodo de muestreo \n');
        valor_eficaz = 0; 
        %{
            Este return est� porque en el c�lculo de la envolvente
            energ�tica, puede pedirse integrar sobre un per�odo menor al 
            per�odo de muestreo. En dicho caso, efectivamente no se agrega
            energ�a ninguna en dicho per�odo de integraci�n.
        %}
    else
    
        muestra_inicial = calcular_muestra(t_comienzo,Ts);
        muestra_final = calcular_muestra(t_final,Ts);

        energia_total = calcular_energia(data, Ts, muestra_inicial, muestra_final);
        valor_eficaz = sqrt(energia_total/periodo);

    end
    
end