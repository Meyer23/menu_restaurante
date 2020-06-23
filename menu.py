import sqlite3 

from tkinter import *


root = Tk()
root.title("Bar Don Costa - Menú")
root.resizable(0,0)
root.config(bd=25, relief="sunken")


Label(root, text="   Bar Don Costa   ", fg="darkgreen", font=("Consolas", 28, "bold")).pack()
Label(root, text="   Menú del día   ", fg="green", font=("Consolas", 20, "bold")).pack()

#Separacion de titulos y categorias
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.bd")
cursor = conexion.cursor()


#Buscar categorias y los platos
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
	Label(root, text=categoria[1], fg="black", font=("Consolas", 18, "bold") ).pack()
	platos = cursor.execute("SELECT * FROM plato WHERE categoria_id = {}".format(categoria[0]) ).fetchall()
	for plato in platos:
		Label(root, text=plato[1], fg="grey", font=("Consolas", 15, "bold italic") ).pack()
		

	#Separacion entre categorias 
	Label(root, text="")

conexion.close()

Label(root, text="12.000 GS (IVA inc.)", fg="darkgreen", font=("Consolas", 15, "bold italic") ).pack(side="right")

#Precio del menu



root.mainloop()