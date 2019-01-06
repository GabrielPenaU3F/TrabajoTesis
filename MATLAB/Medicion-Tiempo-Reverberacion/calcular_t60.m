function [r_xy, t60] = calcular_t60(s_db,fs)

    %{

        El cálculo del T60 es más complejo que los otros
        Como la intensidad del sonido desciende mucho y
        la medición directa se dificulta, se estima realizando
        una regresión lineal sobre los puntos de la curva comprendidos
        entre -5db y -35db.

    %}

    %Guardo una copia de la señal original sin el techo constante
    s_db_original_real = eliminar_techo_constante(s_db,10,10^-6);
    
    s_db = obtener_segmento_de_curva(s_db,5,35);
    y_matriz = s_db';
    x = 0:1/fs:length(y_matriz)/fs - 1/fs;
    
    r_xy = calcular_coeficiente_r_xy(x,s_db); %Coeficiente de correlación lineal; este se devuelve
    
    x_columna = x';
    x_matriz = cat(2,ones(length(y_matriz),1),x_columna);
    
    %Con los puntos (x,y) se realiza el ajuste lineal
    coeficientes = x_matriz\y_matriz; %El operador \ ajusta por minimos cuadrados
    
    ordenada_al_origen = coeficientes(1);
    pendiente = coeficientes(2);
    
    %{
        
        %Descomentar esta parte para observar graficas
    
        recta_estimada = x_matriz*coeficientes;
        t = 0:1/fs:length(s_db_original_real)/fs-1/fs;
        recta_completa = t.*pendiente + ordenada_al_origen;
        
        subplot(1,2,1);
        scatter(x,s_db);
        hold on;
        plot(x, recta_estimada);
        title('Datos vs recta estimada');
        
        subplot(1,2,2);
        plot(t,s_db_original_real,t,recta_completa);
        title('Curva de decaimiento real vs recta estimada');
    
    %}
    
    %{
        Para obtener el t60, evaluo la función inversa de la recta estimada
        en y=-60.
        Si y=ax+b, la función inversa es x=(y-b)/a
    %}
    
    t60 = (-60 - ordenada_al_origen)/pendiente;
        
    
    
    