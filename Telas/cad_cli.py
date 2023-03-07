from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import items

class entry():
  id = ''
  nome_cli = ''
  data_nasc = ''
  cpf_cnpj = ''
  celular = ''



def open():
  cad_cliente = Tk(className='Cadastrar Cliente')
  cad_cliente.geometry("1366x720")
  ttk.Label(cad_cliente, text='Nome do cliente:').grid(column = 3, row = 1)

  cadastro = entry()

  cadastro.id = ttk.Entry(cad_cliente, width = 25).grid(column = 3, row = 2)

  ttk.Label(cad_cliente, text=cadastro.id)

  ttk.Combobox(cad_cliente, values=items.meses).grid(column = 4, row = 2)

  ttk.Button(cad_cliente, text='close').grid(column = 8, row = 2)