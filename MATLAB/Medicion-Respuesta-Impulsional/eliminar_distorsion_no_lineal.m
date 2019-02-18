function h_trim = eliminar_distorsion_no_lineal(h)
   
    [y, x] = max(h);
    h_trim = h(x:end);
    