function H = calcular_respuesta_frecuencial(X,Y)

    H = zeros(size(X));
    if (length(X) == length(Y))
        
        for i=1:length(X)
            H(i) = Y(i)/X(i);
        end
       
    end
  