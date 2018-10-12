%Los parámetros son los mismos que para la señal ESS correspondiente
function h = generar_filtro_inverso_ess(fs, T, f1, f2);

    %{

        El filtro inverso es tal que al pasar la señal por él, se obtiene
        como resultado una delta
        Está dado por la función
 
            h(t) = s_i(t)/k

        Donde s_i(t) es la señal ESS invertida en el tiempo, y k es como
        sigue

            k = exp(tR/T)
            R = ln(f2/f1)

        El resultado es una versión con amplitud modulada de la señal ESS
        invertida en el tiempo.

    %}

    ess = generar_senal_ess(fs,T,f1,f2);
    s_i = flip(ess); %Señal ESS invertida
    h = 0:1/fs:T-1/fs;
    R = log(f2/f1);
    for i=1:length(h)
        k = exp(h(i)*R/T);
        h(i) = s_i(i)/k;
    end
    
   
    