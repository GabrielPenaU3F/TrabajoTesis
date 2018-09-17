%La potencia debe darse en watts, el
function y = generar_ruido_exponencial(tiempo_duracion, fs, potencia, mu) 

    Ts = 1/fs;
    cantidad_muestras = tiempo_duracion/Ts;

    %Vector fila de números aleatorios exponenciales
    %Tambien pueden ser generados directamente por la formula:
    %x = -mu*ln(1-u) donde u es un número aleatorio uniforme
    vector_exp = exprnd(mu, 1, cantidad_muestras);

    energia_total = calcular_energia (vector_exp, Ts, 1, length(vector_exp));
    potencia_total = energia_total/tiempo_duracion;
    %Si se supone que los números aleatorios representan amplitudes en Volt, y
    %se asume como hace MATLAB una carga de 1 Ohm, entonces esta potencia esta
    %en Watts. 

    %Calculo la constante K necesaria para que la potencia total sea la
    %requerida. 
    K = sqrt(potencia/potencia_total);

    %Procedo a multiplicar cada muestra por K y devuelvo
    y = vector_exp.*K;