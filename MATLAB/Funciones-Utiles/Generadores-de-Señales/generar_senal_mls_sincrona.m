%Con fs = 44100 Hz, elegir 16 bits y 7 periodos para una señal de 10
%segundos
function mls_sincrono = generar_senal_mls_sincrona(fs, n_bits, cantidad_periodos)

    mls_puro = generar_senal_mls_bits(n_bits, cantidad_periodos);
    
    amplitud_senoide = 2;
    frecuencia_senoide = 100;
    fase_inicial_senoide = 0;
    senoide = generar_senoide(fs, amplitud_senoide, frecuencia_senoide, fase_inicial_senoide, 1);
    silencio = generar_silencio(2,fs); %2 segundos de silencio
    
    mls_sincrono = cat(2, senoide, silencio);
    mls_sincrono = cat(2, mls_sincrono, mls_puro);
    