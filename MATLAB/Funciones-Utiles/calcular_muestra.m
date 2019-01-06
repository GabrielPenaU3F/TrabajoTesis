%Obtiene el indice de la muestra mas cercana al tiempo t
function indice_muestra = calcular_muestra(t,Ts)
    indice_muestra = 1 + round(t/Ts);
end