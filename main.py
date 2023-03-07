from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import Telas.cad_festa
import Telas.cad_cli


main = Tk(className='Cadastrar festa')

main.geometry("1366x720")


ttk.Button(main, text= "Cadastrar festa", command=Telas.cad_festa.open).pack(pady= 20)
ttk.Button(main, text= "Cadastrar Cliente", command=Telas.cad_cli.open).pack(pady= 20)
ttk.Button(main, text= "Sair", command=lambda: main.quit()).pack(pady= 20)

main.mainloop()