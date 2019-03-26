from tkinter import ttk
s = ttk.Style()
s.theme_use('classic')
pb = ttk.Progressbar(None, orient="horizontal")
bClass = pb.winfo_class()
print(bClass)
layout = s.layout('Horizontal.TProgressbar')
print(layout)