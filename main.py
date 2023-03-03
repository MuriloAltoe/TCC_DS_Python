from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import items

main = Tk(className='Cadastrar festa')

main.geometry("700x400")

def open_cad_festa():
  cad_festa = Tk(className='Cadastrar festa')
  cad_festa.geometry("700x400")
  ttk.Button(cad_festa, text='close').pack(pady= 20)

def open_cad_cliente():
  cad_cliente = Tk(className='Cadastrar Cliente')
  cad_cliente.geometry("700x400")
  ttk.Label(cad_cliente, text='Nome do cliente:').grid(column = 3, row = 1)

  name = ''

  ttk.Entry(cad_cliente, width = 25, textvariable = name).grid(column = 3, row = 2)

  ttk.Combobox(cad_cliente, values=items.meses).grid(column = 4, row = 2)

  ttk.Button(cad_cliente, text='close').grid(column = 8, row = 2)


ttk.Button(main, text= "Cadastrar festa", command=open_cad_festa).pack(pady= 20)
ttk.Button(main, text= "Cadastrar Cliente", command=open_cad_cliente).pack(pady= 20)
ttk.Button(main, text= "Sair", command=lambda: main.quit()).pack(pady= 20)



main.mainloop()