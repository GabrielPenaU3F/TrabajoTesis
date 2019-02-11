function varargout = calcular_t30(s_db,fs)

   [t30, r_xy] = calcular_tx(s_db, fs, 30);
   varargout = cell(1, nargout);
   if (nargout == 1)
       varargout{1} = t30;
   elseif (nargout == 2)
       varargout{1} = t30;
       varargout{2} = r_xy;
   end