function varargout = calcular_edt(s_db,fs)

   [t10, r_xy] = calcular_tx(s_db,fs,10);
   edt = 6 * t10;
   varargout = cell(1, nargout);
   if (nargout == 1)
       varargout{1} = edt;
   elseif (nargout == 2)
       varargout{1} = edt;
       varargout{2} = r_xy;
   end
            
        

    