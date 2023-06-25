import tkinter as tk


    
def calculadora():
    # Crear las variables
    vestimenta_c = int(vestimentaEntry1.get())
    vestimenta_b = int(vestimentaEntry2.get())
    vestimenta_a = int(vestimentaEntry3.get())
    alimentos_c = int(alimentosEntry1.get())
    alimentos_b = int(alimentosEntry2 .get())
    alimentos_a = int(alimentosEntry3.get())
    educacion_c = int(educacionEntry1.get())
    educacion_b = int(educacionEntry2 .get())
    educacion_a = int(educacionEntry3.get())
    ipcVest = (vestimenta_c * vestimenta_b) / (alimentos_c * vestimenta_a)
    ipcAlim = (alimentos_c * alimentos_b) / (alimentos_c * alimentos_a)
    ipcEduc = (educacion_c * educacion_b) / (educacion_c * educacion_a)
    IPC_resultado = (ipcAlim + ipcVest + ipcEduc) / 3
    label_resultado.config(text=f"IPC % : {IPC_resultado}")

   # Crear ventana principal
ventana = tk.Tk()
ventana.geometry('535x300')
ventana.title ('Calculadora IPC')  
opts = { 'padx': 5, 'pady': 5 , 'sticky': 'nswe' }  
    
# Crear las variables sin entradas
label_cantidad = tk.Label(ventana, text="Cantidad:")
label_precioB = tk.Label(ventana, text="Precio Año Base:")
label_precioA = tk.Label(ventana, text="Precio Año Actual:")
label_item = tk.Label(ventana, text="item:")
    
 
    
    # Crear los elementos de la interfaz vestimenta
label_vestimenta = tk.Label(ventana, text="Vestimenta:")
vestimentaEntry1 = tk.Entry (ventana)
vestimentaEntry2 = tk.Entry (ventana)
vestimentaEntry3 = tk.Entry (ventana)
    
    # Crear alimentos
label_alimentos = tk.Label(ventana, text="Alimentos:")
alimentosEntry1 = tk.Entry (ventana)
alimentosEntry2 = tk.Entry (ventana)
alimentosEntry3 = tk.Entry (ventana)

# Crear educacicon
label_educacion = tk.Label(ventana, text="Educacion:")
educacionEntry1 = tk.Entry (ventana)
educacionEntry2 = tk.Entry (ventana)
educacionEntry3 = tk.Entry (ventana)

    # Crear el boton y resultado
boton = tk.Button(ventana, text="Calcular IPC", command=calculadora)
botonSalir = tk.Button (ventana, text='Salir', command=ventana.destroy)
label_resultado = tk.Label(ventana, text="IPC %: ")

# Ubicar los elementos en la ventana
# Fila uno
label_item.grid (row=0, column=0)
label_cantidad.grid (row=0, column=1)
label_precioB.grid (row=0, column=2)
label_precioA.grid (row=0, column=3)

# Fila dos
label_vestimenta.grid (row=1, column=0)
vestimentaEntry1.grid (row=1, column=1)
vestimentaEntry2.grid (row=1, column=2)
vestimentaEntry3.grid (row=1, column=3)

# Fila tres
label_alimentos.grid (row=2, column=0)
alimentosEntry1.grid (row=2, column=1)
alimentosEntry2.grid (row=2, column=2)
alimentosEntry3.grid (row=2, column=3)

# FIla cuatro
label_educacion.grid (row=3, column=0)
educacionEntry1.grid (row=3, column=1)
educacionEntry2.grid (row=3, column=2)
educacionEntry3.grid (row=3, column=3)
boton.grid (row=4, column=2)
botonSalir.grid (row=4, column=3)
label_resultado.grid (row=5, column=0)

    # Iniciar el bucle principal de la interfaz
ventana.mainloop()
        












