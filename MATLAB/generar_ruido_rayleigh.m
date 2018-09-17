%La potencia debe darse en watts, el
function y = generar_ruido_rayleigh(tiempo_duracion, fs, potencia, sigma) 

    Ts = 1/fs;
    cantidad_muestras = tiempo_duracion/Ts;

    %Vector fila de números aleatorios rayleigh
    vector_ray = 1:cantidad_muestras;

    %A cada posicion del vector le asigno numeros aleatorios Rayleigh
    for i=1:length(vector_ray)
            vector_ray(i) = rayrnd(sigma);
    end

    energia_total = calcular_energia (vector_ray, Ts, 1, length(vector_ray));
    potencia_total = energia_total/tiempo_duracion;
    %Si se supone que los números aleatorios representan amplitudes en Volt, y
    %se asume como hace MATLAB una carga de 1 Ohm, entonces esta potencia esta
    %en Watts. 

    %Calculo la constante K necesaria para que la potencia total sea la
    %requerida. 
    K = sqrt(potencia/potencia_total);

    %Procedo a multiplicar cada muestra por K y devuelvo
    y = vector_ray.*K;

end

%Devuelve un número aleatorio Rayleigh con parámetro sigma
function rayleigh = rayrnd(sigma)

    num_uni = rand();
    rayleigh = sqrt(-2*(sigma^2)*log(1-num_uni));
end