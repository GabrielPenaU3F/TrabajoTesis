function [A, rho] = efectuar_regresion_exponencial(x, y)

        z = log(y);
        [pendiente, ordenada] = efectuar_regresion_lineal(x,z);
        rho = pendiente;
        A = exp(ordenada);

end