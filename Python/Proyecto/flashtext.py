from tkinter import *
def change(a=0): 
	print (a), ## debug
	lienzo.itemconfigure('amazing', text="Shazzam!" if a%2==0 else 'Hello World... Grafico!')
	lienzo.after(400,change  , a + 1 )
vpadre = Tk()
vpadre.columnconfigure(0, weight=1)
vpadre.rowconfigure(0, weight=1)
lienzo = Canvas(vpadre, bg='white',)
texto=lienzo.create_text((100, 120), text='Hello World... Grafico!', fill='black', tags='amazing')
change()
lienzo.pack()
vpadre.mainloop()