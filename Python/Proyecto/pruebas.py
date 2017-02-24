from tkinter import *

def MarcarLinea(event):
    
    r = 4
       
    clickx,clicky = event.x,event.y

    for i in range(filas):
        for j in range(columnas):

            starthx = 48+(50*i+((150-(filas*10))*2.5))+r # >= for any i in range (filas-1)
            starthy = 48+(50*j+((100-(columnas*10))*2.5))+r  # == for any j in range (columnas-1)
            
            startvx = 48+(50*i+((150-(filas*10))*2.5))+r # == for any i in range (filas-1)
            startvy = 48+(50*j+((100-(columnas*10))*2.5))+r  # >= for any j in range (columnas-1)

            if ((clickx-int(starthx)<=50) and int(starthy-r)<=clicky<=int(starthy+r)):
                return canvas.create_line(starthx,starthy,starthx+50,starthy,width=3,fill="red")
                
            
            elif((clicky-int(startvy)<=50) and int(startvx-r)<=clickx<=int(startvx+r)):
                return canvas.create_line(startvx,startvy,startvx,startvy+50,width=3,fill="red")
                

def Salir():
    quit()

filas = int(input('Escribe el numero de filas del tablero: '))
columnas = int(input('Escribe el nuemro de columnas del tablero: '))
root = Tk()
root.title = ("Connect the dots")
root.configure(background='white')
root.geometry("800x800")

canvas = Canvas(root, bg='white',width = 800, height = 800)


salir = Button(canvas, text="Salir",command = Salir,font= ("Agency FB",14),\
                   width=10).place(x=150,y=535)

#guardar = Button(canvas,text="Guardar",command = GuardarPartida("archivo.txt"),\
 #                    font= ("Agency FB",14),width=10).place(x= 500,y=535)

x = 150-(filas*10)
y = 100-(columnas*10)
        
for i in range (filas):
    for j in range (columnas):
        canvas.create_oval(50 +(50*i+x*2.5),50 +(50*j+y*2.5),\
                               (x*2.5)+(50*i+50+2*2),\
                               (y*2.5)+(50*j+50+2*2),fill="black")
        canvas.pack()

canvas.bind("<Button-1>",MarcarLinea)
        
NombreJugador1 = "Douglas"
NombreJugador2 = "Roberto"
#TableroHorizontal,TableroVertical,\
 #   TableroCuadros = Inicializacion(filas,columnas)
TipoJugador = 2
PuntajeJugador1 = 0
PuntajeJugador2 = 0
TurnoActual = 0
        #NombreJugador1 = ""
        #NombreJugador2 = ""

nombre1 = Label(canvas, text=NombreJugador1,font= ("Agency FB",14),\
                    width=10).place(x=25,y=150)

nombre2 = Label(canvas, text=NombreJugador2,font= ("Agency FB",14),\
                    width=10).place(x=665,y=150)


root.mainloop()
