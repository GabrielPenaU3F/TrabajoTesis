%{
    f1 y f2 son los limites inferior y superior respectivamente de la banda
    de frecuencias que cubre la señal. T es la duracion en segundos
%}
function ess = generar_senal_ess(fs, T, f1, f2)
    
    %{
        La señal ESS está dada por la expresión:

            s(t) = sin[K.(exp(t/L) - 1)] = sin[(2pi.f1.T/R).(exp(tR/T) - 1)]

        Las constantes K, L, R son como sigue:

            K = 2pi.f1.L
            L = T/R
            R = ln(f2/f1)

        Se indican las dos notaciones equivalentes porque en distintas fuentes
        aparecen ambas.

        Esta señal es una senoide cuya frecuencia fundamental crece
        exponencialmente. Su contenido frecuencial está comprendido en la
        banda entre f1 y f2.
   %}

   ess = 0:1/fs:T - 1/fs;
   R = log(f2/f1);
   for i=1:length(ess)
       ess(i) = sin((2*pi*f1*T/R)*(exp(ess(i)*R/T) - 1));
   end
   
   
   
    
    