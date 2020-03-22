# -*- coding: utf-8 -*-
import os
import sqlite3
import sys
from tkinter import *
from tkinter import ttk
 
from sqlite3 import Error
#crea conexion con base de datos 
def sql_connection():
 
    try:
 
        con = sqlite3.connect('miBase.db')
 
        return con
 
    except Error:
 
        print(Error)
#inserta registro nuevo en la tabla
def sql_table(con,codigo,nombre,mail):
 
    cursorObj = con.cursor()
 
 
    
    cursorObj.execute("INSERT INTO productores VALUES('"+codigo+"', '"+nombre+"', '"+mail+"')")
    
    con.commit()
   

    os.makedirs(os.path.join('C:','\\Users','Franco','Documents','archivosproductores',nombre))



window = Tk()
import tkinter as tk

window.title("GG Seguros")

# gives weight to the cells in the grid
rows = 0
while rows < 50:
    window.rowconfigure(rows, weight=1)
    window.columnconfigure(rows, weight=1)
    rows += 1
        
# Defines and places the notebook widget
nb = ttk.Notebook(window)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Registrar')

def salir():
    try:
        return os._exit(0)
    except SystemExit as er :
        print(er)
    
def aceptarRegi():
    con = sql_connection()      
    sql_table(con,cajacodigo.get(),cajanombre.get(),cajamail.get())
    con.close() 
    
    cajacodigo.delete(0,'end')
    cajamail.delete(0,'end')
    cajanombre.delete(0,'end')
    
tk.Label(page1,text = "Codigo",borderwidth = 20).grid(row =10,column =10)
cajacodigo = tk.Entry(page1)
cajacodigo.grid(row = 10 , column = 11)

tk.Label(page1,text = "Nombre",borderwidth = 20).grid(row = 11 , column = 10)
cajanombre = tk.Entry(page1)
cajanombre.grid(row = 11 , column = 11)

tk.Label(page1, text = "Mail",borderwidth = 20).grid(row = 12 , column = 10)
cajamail = tk.Entry(page1)
cajamail.grid(row = 12 , column = 11) 

botonaceptarregi =tk.Button(page1,text = "Aceptar", borderwidth = 3,command = aceptarRegi)
botonaceptarregi.grid(row = 19,column =10)
botonsalirregi = tk.Button(page1,text = "Salir", borderwidth = 3,command = salir)
botonsalirregi.grid(row = 19,column = 12)

window.mainloop()