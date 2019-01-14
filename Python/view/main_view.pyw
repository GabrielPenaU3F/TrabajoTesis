from tkinter import *

root = Tk()

# ----- Configuracion del root ------
root.title("Medidor Acústico por Gabriel Pena")
root.iconbitmap("../resources/icons/mic_icon.ico")
root.tk_setPalette(background='#f4f3f3')

# ----- Configuracion del frame principal de la ventana -----
main_frame = Frame(root)
main_frame.config(width="1200", height="600")
main_frame.pack(fill="both", expand="True", padx=20, pady=20)


# ----- Dividiré el frame principal en un grid de 3x2 -----

frame_titulos = Frame(main_frame)
frame_titulos.grid(row=0, column=0)

frame_graficas = Frame(main_frame)
frame_graficas.grid(row=1, column=0)

frame_medicion = Frame(main_frame)
frame_medicion.grid(row=2, column=0, sticky="w", pady=(10, 0))

frame_resultados = Frame(main_frame)
frame_resultados.grid(row=0, column=1, sticky="n", padx=(20, 0))


# ----- Frame de títulos -----

frame_titulo_rta_impulsional = Frame(frame_titulos)
frame_titulo_rta_impulsional.config(width=500, height=20, borderwidth=2, relief="groove")
frame_titulo_rta_impulsional.pack_propagate(False)
frame_titulo_rta_impulsional.grid(row=0, column=0)
label_titulo_rta_impulsional = Label(frame_titulo_rta_impulsional)
label_titulo_rta_impulsional.config(text="Respuesta impulsional", background="#dfdfdf")
label_titulo_rta_impulsional.pack(fill="both", expand="True", ipadx=3, ipady=3)

frame_titulo_curva_decaimiento = Frame(frame_titulos)
frame_titulo_curva_decaimiento.config(width=500, height=20, borderwidth=2, relief="groove")
frame_titulo_curva_decaimiento.pack_propagate(False)
frame_titulo_curva_decaimiento.grid(row=0, column=1)
label_titulo_curva_decaimiento = Label(frame_titulo_curva_decaimiento)
label_titulo_curva_decaimiento.config(text="Curva de decaimiento", background="#dfdfdf")
label_titulo_curva_decaimiento.pack(fill="both", expand="True", ipadx=3, ipady=3)


# ----- Frame de gráficas -----

frame_graf_rta_impulsional = Frame(frame_graficas)
frame_graf_rta_impulsional.config(width=500, height=300, borderwidth=2, relief="groove")
frame_graf_rta_impulsional.pack_propagate(False)
frame_graf_rta_impulsional.grid(row=0, column=0)

frame_graf_curva_decaimiento = Frame(frame_graficas)
frame_graf_curva_decaimiento.config(width=500, height=300, borderwidth=2, relief="groove")
frame_graf_curva_decaimiento.pack_propagate(False)
frame_graf_curva_decaimiento.grid(row=0, column=1)


# ----- Frame de medicion -----

boton_instrucciones = Button(frame_medicion, text="Instrucciones")
boton_instrucciones.grid(row=0, column=0, padx=(0, 10))

boton_medir = Button(frame_medicion, text="Medir")
boton_medir.grid(row=0, column=1, padx=10)

radiob_metodo_var = StringVar(value="ESS")

radiob_ess = Radiobutton(frame_medicion, text="Método ESS", variable=radiob_metodo_var, value="ESS")
radiob_ess.grid(row=0, column=2, padx=10)

radiob_mls = Radiobutton(frame_medicion, text="Método MLS", variable=radiob_metodo_var, value="MLS")
radiob_mls.grid(row=0, column=3, padx=10)


# ----- Frame de resultados -----

frame_titulo_resultados = Frame(frame_resultados)
frame_titulo_resultados.config(width=100, height=20, borderwidth=2, relief="groove")
frame_titulo_resultados.pack_propagate(False)
frame_titulo_resultados.grid(row=0, column=1)
label_titulo_resultados = Label(frame_titulo_resultados)
label_titulo_resultados.config(text="Resultados")
label_titulo_resultados.pack(fill="both", expand="True", ipadx=3, ipady=3)



root.mainloop()
