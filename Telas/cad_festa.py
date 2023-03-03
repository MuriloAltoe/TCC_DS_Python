from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def open():
  cad_festa = Tk(className='Cadastrar festa')
  cad_festa.geometry("1366x720")
  ttk.Button(cad_festa, text='close').pack(pady= 20)