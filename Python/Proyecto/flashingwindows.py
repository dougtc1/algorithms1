"""
Universidad Simon Bolivar
CI-2691 - Laboratorio de Algoritmos y Estructuras I
Fecha: 08/06/2014
Material de Apoyo para tkinter
Nabil J. Marquez 11-10683
"""

from tkinter import *
def change(a=0):
    print (a), ## debug
    lbl.config(bg = "blue" if a & 1 else "purple")
    lbl.after(400,change  , a ^ 1 )
if __name__ == '__main__':
    win= Tk() 
    win.geometry("500x300")
    lbl = Label (win)
    lbl.pack(expand=YES, fill=BOTH)
    change()
    
    win.mainloop()