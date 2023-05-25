import tkinter as tk
from tkinter import ttk
class Convertir(tk.Frame):
    def __init__(self,parent,posy):
        super().__init__(parent)
        self.Guia=ttk.Label(parent,text="Ingrese metros"
               ,font=('Algerial',18))
        self.Guia.place(x=20,y=posy)
        self.Metros=ttk.Entry(parent,font=('Algerial',20))
        self.Metros.place(x=220,y=posy,width=100)
        self.Boton=ttk.Button(parent,command=self.Accion)
        self.Boton.place(x=340,y=posy)
        self.Resultado=ttk.Label(parent
                    ,font=('Algerial',20))
        self.Resultado.place(x=20,y=posy+80)
    def Accion(self):
        Cent=float(self.Metros.get())*100
        self.Resultado.configure(text=str(Cent))
Ventana=tk.Tk()
Ventana.title("Convertidor")
Ventana.configure(width=600,height=600)
Conver1=Convertir(Ventana,30)
Conver1=Convertir(Ventana,200)
Conver1=Convertir(Ventana,300)
Ventana.mainloop()
