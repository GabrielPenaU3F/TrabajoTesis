%{ 
Uso el algoritmo de Schroeder para obtener la curva de
decaimiento cuadratico. Para cada t, el valor s^2(t) es directamente
proporcional a la integral desde t a infinito de la respuesta impulsional
cuadrada. (Ignoramos la constante de proporcionalidad porque nos interesa
la relación, no los valores exactos). Esto se traduce en sumar los valores
de la respuesta impulsional original, desde la muestra del instante t
hasta el final de la señal.
%}

function s_cuadrado = obtener_curva_de_decaimiento_cuadratico(h, fs)

    h_cuadrado_original = h.^2;
    %h_hilbert = abs(hilbert(abs(h)));
    h_suave = aplicar_filtro_media_movil(h, 100);
    %h_cuadrado = abs(hilbert(h_cuadrado_original));
    [lim_superior, pendiente, ordenada_al_origen] = estimar_limite_superior_por_metodo_de_lundeby(h, fs);
    h_sin_ruido = sustraer_ruido_de_fondo(h, fs, lim_superior);
    h_cuadrado = h_sin_ruido.^2;
    c_corr = calcular_termino_de_correccion(h_suave, fs);
    s_cuadrado = 0:1/fs:lim_superior/fs - 1/fs;
    
    dx = 1/fs;
    s_cuadrado(1) = integrar_array(h_cuadrado, lim_superior, dx);
    for i=2:lim_superior
        s_cuadrado(i) = s_cuadrado(i-1) - h_cuadrado(i-1)*dx;
    end
    %Si se utiliza la trasnformada de Hilbert, se calcula 
    %el ruido de fondo sobre la respuesta impulsional original,
    %ya que la envolvente de Hilbert tiene una réplica del pico inicial
    %al final de la señal y esta destruye el cálculo.
    %s_cuadrado = sustraer_ruido_de_fondo(s_cuadrado, h_cuadrado, fs, lim_superior);
    s_cuadrado = s_cuadrado + c_corr;
    
end

function integral = integrar_array(x, lim_superior, dx)

    integral = 0;
    for j=1:lim_superior
        integral = integral + x(j)*dx;
    end
    
end

function h_sin_ruido = sustraer_ruido_de_fondo(h, fs, lim_superior)
  
    h_sin_ruido = 0:1/fs:length(h)/fs - 1/fs;
    ruido_de_fondo = mean(abs(h(lim_superior:end)));
    for i=1:length(h)
        if (h(i) > 0)
            h_sin_ruido(i) = h(i) - ruido_de_fondo;
        elseif (h(i) < 0)
            h_sin_ruido(i) = h(i) + ruido_de_fondo;
        end
    end
end

function c_corr = calcular_termino_de_correccion(h, fs)

   exponencial = @(x,xdata)(x(1)*exp(-x(2)*xdata)+x(3));
   x0 = [1,1,0];
   t = 0:1/fs:length(h)/fs - 1/fs;
   parametros = lsqcurvefit(exponencial,x0,t,abs(h));
   amplitud = parametros(1);
   tasa_decaimiento = parametros(2);
   ruido = parametros(3);
   
   %{
   z = amplitud * exp(-tasa.*t) + ruido;
   plot(t,h,t,z);
   %}
   tiempo_truncado_modelo = -(log(ruido/amplitud))/tasa_decaimiento;
   c_corr = (1/(2*tasa_decaimiento))*exp(-2*tasa_decaimiento*tiempo_truncado_modelo);
   
   %{
   N = calcular_energia(h, 1/fs, lim_superior, length(h)) / ((length(h) - lim_superior) / fs);
   B = pendiente;
   tiempo_truncado = calcular_tiempo_muestra(lim_superior, fs);
   A = log(N / B) / tiempo_truncado;
   c_corr = - (B / A) * exp(A * tiempo_truncado);
   %}
end