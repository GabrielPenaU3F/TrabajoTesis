function mls = generar_senal_mls_bits(n_bits, cantidad_periodos)

    x = ones(1, 2^n_bits - 1);
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