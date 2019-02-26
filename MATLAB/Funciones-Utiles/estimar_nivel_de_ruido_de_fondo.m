function n_ruido = estimar_nivel_de_ruido_de_fondo(senal_db, porcentaje_de_cola)

    muestras_cola = round(length(senal_db) * porcentaje_de_cola / 100);
    inicio_cola = length(senal_db) - muestras_cola;
    cola = senal_db(inicio_cola:end);
    n_ruido = mean(cola);

end