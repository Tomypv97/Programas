class cliente:
    dni = ""
    apellido = ""
    nombre = ""
    telefono = ""
    patente = ""
    auto = ""
    estado = ""
    
    def __init__(self, dni, apellido, nombre, telefono, patente, auto, estado):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.telefono = telefono
        self.patente = patente
        self.auto = auto
        self.estado = estado
        
        
    def getdni(self):
        return self.dni
    
    def getapellido(self):
        return self.apellido
    
    def getnombre(self):
        return self.nombre
    
    def getpatente(self):
        return self.patente
    
    def getauto(self):
        return self.auto
    
    def getinfo(self):
        print(f"Dni: {self.getdni()}, Apellido y nombre: {self.getapellido()}, {self.getnombre()}")
        print(f"Patente: {self.getpatente()}, Vehiculo: {self.getauto()}")

    def modificar(self):
        self.estado = "T"
        
              