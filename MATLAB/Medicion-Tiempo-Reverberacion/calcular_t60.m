function varargout = calcular_t60(s_db,fs)

   [t60, r_xy] = calcular_tx(s_db, fs, 60);
   varargout = cell(1, nargout);
   if (nargout == 1)
       varargout{1} = t60;
   elseif (nargout == 2)
       varargout{1} = t60;
       varargout{2} = r_xy;
   end
        
    
    
    