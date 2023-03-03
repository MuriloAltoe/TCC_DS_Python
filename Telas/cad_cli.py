from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import items

def open():
  cad_cliente = Tk(className='Cadastrar Cliente')
  cad_cliente.geometry("1366x720")
  ttk.Label(cad_cliente, text='Nome do cliente:').grid(column = 3, row = 1)

  name = ''

  ttk.Entry(cad_cliente, width = 25, textvariable = name).grid(column = 3, row = 2)

  ttk.Combobox(cad_cliente, values=items.meses).grid(column = 4, row = 2)

  ttk.Button(cad_cliente, text='close').grid(column = 8, row = 2)