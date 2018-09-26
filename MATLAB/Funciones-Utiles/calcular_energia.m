%Realiza la integral del valor absoluto de la señal al cuadrado en el
%período T indicado.
%Como la señal sera siempre real, se omite el valor absoluto
function energia_total = calcular_energia(data, Ts, indice_inicial, indice_final)

    data_periodo = data(indice_inicial:indice_final);
    suma = 0;
    for i=1:length(data_periodo)
        suma = suma + (data_periodo(i)^2)*Ts;
    end
    energia_total = suma;
    
end