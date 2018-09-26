%Nivel de potencia en decibeles relativo a una potencia de referencia.
%Si la potencia es potencia de la presion sonora, con una presion de
%referencia que por defecto es de 20uPa, se obtiene el nivel de presion
%sonora en decibeles relativo al umbral auditivo
function nivel_potencia_equivalente = calcular_nivel_de_potencia_equivalente(data, Ts, t_comienzo, periodo, presion_referencia)

    potencia_eficaz = calcular_potencia_eficaz(data,Ts,t_comienzo,periodo);
    nivel_potencia_equivalente = 20 * log10(potencia_eficaz / presion_referencia);

end