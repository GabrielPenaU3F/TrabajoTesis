function xi = calcular_parametro_de_no_linealidad(rxy)

	r_cuadrado = rxy^2;
	xi = 1000 * (1 - r_cuadrado);