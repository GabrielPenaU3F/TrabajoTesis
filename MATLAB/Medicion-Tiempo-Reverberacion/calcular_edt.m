function [edt, r_xy] = calcular_edt(s_db,fs)

    [t10, r_xy] = calcular_tx(s_db,fs,10);
    edt = 6 * t10;
            
        

    