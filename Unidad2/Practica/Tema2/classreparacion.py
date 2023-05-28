class reparacion:
    patente = ""
    arreglo = ""
    precio = 0
    manoobra = 0
    estado = ""
    
    def __init__(self, patente, arreglo, precio, manoobra, estado):
        self.patente = patente
        self.arreglo = arreglo
        self.precio = precio
        self.manoobra = manoobra
        self.estado = estado
        
    def getpatente(self):
        return self.patente
    
    def subtotal(self):
        return (self.precio + self.manoobra)
      
    def getarreglo(self):
        return self.arreglo
    
    def getprecio(self):
        return self.precio
        
    def getinfo(self):
        print("Reparacion = " ,self.getarreglo,"Precio propuesto = $",self.getprecio,"Mano de obra = $",self.subtotal())
        
        
