%{
    El margen indica la cantidad de decibeles que se deben dejar
    por encima del punto de cruce estimado anteriormente. En el punto que
    cumpla esa condición se establece el nuevo limite para calcular
    el ruido de fondo.
    El porcentaje mínimo indica la cantidad mínima de muestras a la que
    se puede reducir la RI real durante la estimación. 
%}

function lim = buscar_limite_ruido_de_fondo(senal, muestra_cruce, margen_de_db, porcentaje_minimo_ri)

    minima_muestra_posible = floor(length(senal)*porcentaje_minimo_ri/100);
    lim = minima_muestra_posible;
    if (muestra_cruce > minima_muestra_posible && muestra_cruce < length(senal))
        for i=1:muestra_cruce - minima_muestra_posible
            if (muestra_cruce - i >= length(senal) || muestra_cruce - i < 0)
                continue;
            end
            if (abs(senal(muestra_cruce - i) - senal(muestra_cruce)) > margen_de_db)
                lim = muestra_cruce - i;
                break;
            end
        end
    end

end