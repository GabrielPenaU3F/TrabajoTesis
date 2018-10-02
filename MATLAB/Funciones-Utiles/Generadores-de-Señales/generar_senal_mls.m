%Implementacion de secuencia aleatoria de 1 y -1. No resulta tener las
%propiedades deseadas.

function mls = generar_senal_mls(fs, periodo_mls, cantidad_periodos)
    
    x = ones(1,periodo_mls*fs);
    for i=1:length(x)
        if (rand() > 0.5)
            x(i) = -1;
        end
    end
    
    mls = 0;
    for i=1:cantidad_periodos
        mls = cat(2, mls, x);
    end
    mls = mls(2:end);
    
end