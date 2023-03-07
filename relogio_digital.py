#!/usr/bin/env python

# Carregando Bibliotecas
from tkinter import *
import tkinter
import pyglet
from datetime import datetime

# Definição de Cores
cinza_escuro = "#3d3d3d"
verde_opaco = "#21c25c"

# Definição Fonte
pyglet.font.add_file('digital-7.ttf')

# Criando a interface
root = Tk()
root.title("Relógio Digital feito em Python")
root.geometry('430x190')
root.resizable(width=False,height=False)
root.configure(background=cinza_escuro)

# Cria lógica do relógio
def clock():
  time = datetime.now()
  hour = time.strftime("%H:%M:%S")
  weekday = time.strftime("%A")
  day = time.day
  month = time.strftime("%b")
  year = time.strftime("%Y")
  lblclock.config(text=hour)
  lblclock.after(200, clock)
  lblweek.config(text=" " + weekday + "                          " + str(day) + "/" + str(month) + "/" + str(year))

# Criando os labels
lblclock = Label(root, font=('digital-7 80'), bg=cinza_escuro, fg=verde_opaco)
lblclock.grid(row=0, column=0, sticky=NW)

lblweek = Label(root, font=('Arial 20'), bg=cinza_escuro, fg=verde_opaco)
lblweek.grid(row=1, column=0, sticky=NW)

# Executa a função
clock()
root.mainloop()
