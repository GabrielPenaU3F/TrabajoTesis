fs = 44100;
T = 10;
f1 = 20;
f2 = 22050;


filtro_inverso_ess = generar_filtro_inverso_ess(fs, T, f1, f2);
h_ess = conv(y_ess, filtro_inverso_ess);

f_scuadrado = @() obtener_curva_de_decaimiento_cuadratico(h_ess,fs);
t_scuadrado = timeit(f_scuadrado);