import json
from urllib.request import urlopen
from tkinter import *
from tkinter import ttk, messagebox
from functools import partial


class Conversor:
    __ventana: None
    __pesos = None
    __dolares = None

    def __init__(self) -> None:
        self.__ventana = Tk()
        self.__ventana.geometry('355x139')
        self.__ventana.title('Conversor de moneda')
        opts = { 'padx': 5, 'pady': 5 , 'sticky': 'nswe' }
        marco = ttk.Frame (self.__ventana, padding="3 10 3 10")
        marco.grid(row=0, column=0, **opts)
        marco.columnconfigure(0, weight=1)
        marco.rowconfigure(0, weight=1)
        marco['borderwidth'] = 2
        marco['relief'] = 'sunken'

        # Obtener valor dolar oficial desde la API

        url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        response = urlopen (url)
        data = json.loads(response.read())
        for d in data:
            if d['casa']['nombre'] == 'Oficial':
                dolarstr = d['casa']['compra']
                dolar = float (dolarstr.replace(',','.'))

        self.__pesos = StringVar()
        self.__dolares = StringVar()
        self.__dolares.trace('w', partial(self.calcular, dolar))
        self.dolaresEntry = ttk.Entry (marco, textvariable=self.__dolares, width=10)
        self.dolaresEntry.grid (row=0, column=1, **opts)
        self.dolaresLbl = ttk.Label (marco, text='Dólares').grid (row=0, column=2, **opts)
        self.equiLbl = ttk.Label (marco, text='es equivalente a').grid (row=1, column=0, **opts)
        self.resultLbl = ttk.Label (marco, textvariable=self.__pesos).grid (row=1, column=1, **opts)
        self.pesosLbl = ttk.Label (marco, text='pesos').grid (row=1, column=2, **opts)
        self.botonSalir = ttk.Button (marco, text='Salir', command=self.__ventana.destroy).grid (row=2, column=3, **opts)
        self.dolaresEntry.focus()

    def ejecutar (self):
        self.__ventana.mainloop()

    def calcular (self, dolar, *args):
        if self.dolaresEntry.get() != '':
            
            try:
                value = float (self.dolaresEntry.get())
                self.__pesos.set(f"{dolar*value:.2f}") 
            except ValueError:
                messagebox.showerror(title='Error de valor', message='Ingrese un valor valido')
                self.__pesos.set('')
                self.dolaresEntry.focus()
        else:
            self.__pesos.set('')