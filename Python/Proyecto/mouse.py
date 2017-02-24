#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Universidad Simon Bolivar
CI-2691 - Laboratorio de Algoritmos y Estructuras I
Fecha: 08/06/2014
Material de Apoyo para tkinter
Nabil J. Marquez 11-10683
"""

from tkinter import *


TOL = 8
CELLSIZE = 50
OFFSET = 50
CIRCLERAD = 2
DOTOFFSET = 50
GAME_H = 400
GAME_W = 400

x2=50
y2=50

def mostrar_coordenadas(event):
    x, y = event.x, event.y
    mensaje = 'Clic en la posición (%d, %d)' % (x, y)
    #canvas.create_line(x,x2,y,y2, width=2)
    print(mensaje)
    return x,y

###########################################################

def create_line(x, y, orient):
	startx = CELLSIZE * ((x-OFFSET)//CELLSIZE) + DOTOFFSET
	starty = CELLSIZE * ((y-OFFSET)//CELLSIZE) + DOTOFFSET
	tmpx = (x-OFFSET)//CELLSIZE
	tmpy = (y-OFFSET)//CELLSIZE
	if orient == HORIZONTAL:
		endx = startx + CELLSIZE
		endy = starty
                #print("line drawn: %d,%d to %d,%d"%(startx,starty,endx,endy))
	else:
		endx = startx
		endy = starty + CELLSIZE
                #print ("line drawn: %d,%d to %d,%d" % (startx,starty,endx,endy))
	return canvas.create_line(startx,starty,endx,endy)

def isclose(x,y):

    x -= OFFSET
    y -= OFFSET
    dx = x - (x//CELLSIZE)*CELLSIZE
    dy = y - (y//CELLSIZE)*CELLSIZE
    
    if abs(dx) < TOL:
        if abs(dy) < TOL:
            return None  # mouse in corner of box; ignore
        else:
            return VERTICAL
    elif abs(dy) < TOL:
        return HORIZONTAL
    else:
        return None









############################################################

root = Tk()
root.geometry("800x800")
#root.columnconfigure(0, weight=560)
#root.rowconfigure(0, weight=560)

canvas = Canvas(root, bg='white',height = 800, width = 800)
#canvas.grid(column=0, row=0, sticky=(N, W, E, S))

filas = int(input("Filas: "))

columnas = int(input("Columnas: "))

#print (par)

#x,y = mostrar_coordenadas	

i = 0
j = 0

A = 150-(10*filas)
B = 100-(10*columnas)


for i in range (filas):
    for j in range (columnas):
        coordenadax = 50 +(50*i+A*2.5)
        coordenaday = 50 +(50*j+B*2.5)
        print(coordenadax,coordenaday)
        canvas.create_oval(coordenadax,coordenaday,(A*2.5)+(50*i+50+2*2),\
                               (B*2.5)+(50*j+50+2*2),fill="black")
        canvas.pack()


canvas.bind("<Button-1>", mostrar_coordenadas)
canvas.pack()
canvas.create_text((300, 300), text='Haga clic en el lienzo', tags='leyenda')


#################################print (cerca)
#cerca = isclose(x)


root.mainloop()
