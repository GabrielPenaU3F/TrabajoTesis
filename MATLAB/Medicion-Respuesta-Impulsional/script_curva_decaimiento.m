%Usar con el nombre s_ess los datos grabados de medición de respuesta impulsional ESS, de duracion 10 segundos. 

f_inverso_ess = generar_filtro_inverso_ess(44100,10,20,22050);
h = conv(s_ess, f_inverso_ess);
s_db = obtener_curva_de_decaimiento_en_db(h,fs);

%{
    Opcional: plot

t = 0:1/fs:length(s_db)-1/fs;
plot(t,s_db);

%}