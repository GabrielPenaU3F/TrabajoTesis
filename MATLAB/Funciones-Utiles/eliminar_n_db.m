function s_db = eliminar_n_db(s_db,n)

    n_db_eliminados = 0;
    i=2;
    while(n_db_eliminados == 0)
       
        if (i+1 < length(s_db))
            if (abs(s_db(i) - s_db(1)) > n)
           
                s_db = s_db(i:end);
                n_db_eliminados = 1;
                
            end
            i = i+1;
        end
        
    end