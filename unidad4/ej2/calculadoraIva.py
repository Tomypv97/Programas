from tkinter import *
from tkinter import ttk, messagebox

class calculadoraIva:
    __ventana: None

    def __init__(self) -> None:
        self.__ventana = Tk()
        self.__ventana.geometry('325x261')
        self.__ventana.title('Calculo de IVA')
        self.__ventana.resizable(0,0)
        self.marco = ttk.Frame(self.__ventana, borderwidth=30, relief="raised", padding=(10,10))
        self.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))
        self.marco.columnconfigure(0, weight=1)
        self.marco.rowconfigure(0, weight=1)
        self.marco['borderwidth'] = 30
        self.marco['relief'] = 'sunken'
        opts = { 'padx': 5, 'pady': 5 , 'sticky': 'nswe' }

        self.precioLbl = ttk.Label (self.marco, text='Precio sin IVA').grid(row=0, column=0, **opts)
        self.precio = StringVar()
        self.precioEntry = ttk.Entry (self.marco, textvariable=self.precio).grid(row=0, column=1, **opts)
        
        self.ivaRadio = IntVar()
        self.iva21 = ttk.Radiobutton (self.marco, text='IVA 21 %', value=0, variable=self.ivaRadio).grid(row=1, column=0)
        self.iva10 = ttk.Radiobutton (self.marco, text='IVA 10.5 %', variable=self.ivaRadio).grid(row=2, column=0)
        
        self.ivaLbl = ttk.Label (self.marco, text='IVA').grid(row=3, column=0, **opts)
        self.iva = StringVar()
        self.ivaEntry = ttk.Entry (self.marco, textvariable=self.iva).grid(row=3, column=1, **opts)

        self.precioIvaLbl = ttk.Label (self.marco, text='Precio Con IVA').grid(row=4, column=0, **opts)
        self.precioIva = StringVar()
        self.precioIvaEntry = ttk.Entry (self.marco, textvariable=self.precioIva).grid(row=4, column=1)

        self.calcularBoton = ttk.Button (self.marco, text='Calcular', command=self.calcular).grid(row=5, column=0, **opts)
        self.salirBoton = ttk.Button (self.marco, text='Salir', command=self.__ventana.destroy).grid(row=5, column=1, **opts)

        #self.calcularBoton.focus()
        self.__ventana.mainloop()

    def calcular (self):
        try:
            value = float (self.precio.get())
            if self.ivaRadio.get() == 0:
                iva = (value * 21) / 100
                self.iva.set(iva)
                self.precioIva.set(iva + value)
            elif self.ivaRadio.get() == 1:
                iva = (value * 10.5) / 100
                self.iva.set(iva)
                self.precioIva.set(iva + value)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Ingrese un valor valido')
            self.precio.set('')