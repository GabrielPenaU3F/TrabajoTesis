h = calcular_respuesta_impulsional_mls(x,y,fs,n_bits,periodos);
h_lineal = eliminar_distorsion_no_lineal(h);
s_db = obtener_curva_de_decaimiento_en_db(h_lineal, fs);
t = 0:1/fs:length(h_lineal)/fs - 1/fs;
t_s = 0:1/fs:length(s_db)/fs - 1/fs;
t30 = calcular_t30(s_db, fs);
t60 = calcular_t60(s_db, fs);
t20 = calcular_t20(s_db, fs);
h_db = 20*real(log10(h_lineal./max(h_lineal)));
figure;
plot(t(1:24001), h_db(1:24001));
hold on;
plot(t_s, s_db);