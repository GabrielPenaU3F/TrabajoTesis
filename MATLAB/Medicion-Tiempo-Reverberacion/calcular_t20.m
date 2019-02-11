function varargout = calcular_t20(s_db,fs)

   [t20, r_xy] = calcular_tx(s_db, fs, 20);
   varargout = cell(1, nargout);
   if (nargout == 1)
       varargout{1} = t20;
   elseif (nargout == 2)
       varargout{1} = t20;
       varargout{2} = r_xy;
   end