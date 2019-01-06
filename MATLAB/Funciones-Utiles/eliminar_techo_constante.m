%{
Dada una cierta curva de decaimiento, esta funcion elimina todo el
'techo' cuya amplitud es aproximadamente constante, dejando unicamente
la parte en la que la intensidad 'decae'. Para eso se toma
la siguiente consideracion: 

Se considerará amplitud constante si en n muestras, la amplitud
ha variado menos que un cierto epsilon.
Esta consideración puede variar; he probado hasta dar con una que
arrojara buenos resultados. (Actualmente utilizo n=10, que equivale a
aproximadamente 226us, y epsilon = 10^-6. Es decir, si en 226us la amplitud
no cambió en al menos la millonésima parte de un dB, considero que es constante). 
Aumentar mucho n conducirá a perder eficiencia, ya que cuando se detecte
el decaimiento, quedarán muchas muestras 'constantes' sin eliminar. 
Tomar un n demasiado pequeño en relación al epsilon de amplitud elegido
(en mi caso 10^-6) puede conducir a errores si el decaimiento 'real'
no es lo suficientemente rápido para quedar fuera de dicha definición.
No he encontrado una definición parecida en
ningún estándar ni en el trabajo de Schroeder.

%}

function s = eliminar_techo_constante(s_db, n, epsilon)

    techo_eliminado = 0;
    i=1;
    while (techo_eliminado == 0)
        
        if (i+10 < length(s_db))
            if (abs(s_db(i+n) - s_db(i)) < epsilon)
           
                s_db = s_db(i+n:end);
               
            else
                
                techo_eliminado = 1;
            
            end
            i = i+n;
            
        end
        
    end
    
    s = s_db;
                
                
        

    