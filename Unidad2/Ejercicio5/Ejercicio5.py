import csv

class plan_ahorro:
    def __init__(self,cod=None, mod=None, ver=None, val=None, cant=12, cuot=6):
        self.codigo = cod
        self.modelo = mod
        self.version = ver
        self.valor = val
        self.cant_cuotas = cant
        self.cuotas_pagas = cuot
      
class coleccion_planes:
    def __init__(self):
        self.lista_planes = []

    def agregar_plan(self,unPlan):
        self.lista_planes.append(unPlan)
        
    def __str__(self):
        return f"Código: {self.codigo}, Modelo: {self.modelo}, Versión: {self.version}, Valor: {self.valor}, Cuotas Pagas: {self.cuotas_pagas}/{self.cant_cuotas}"       
        
    def plan_ahorros(self):
        with open('autos5.csv') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            bandera = True
            for fila in reader:
                if bandera:
                    '''saltear cabecera '''
                    bandera = False
                else:
                    codigo = int(fila[0])
                    modelo = fila[1]
                    version = fila[2]
                    valor = int(fila[3])
                    unPlan = plan_ahorro(codigo,modelo,version,valor)
                    self.agregar_plan(unPlan)
                    
    def modificar(self):
         for plan in planes.lista_planes:
             print(plan)
             nuevo_valor =float(input("Ingrese nuevo valor de vehiculo"))
             self.valor = nuevo_valor
     
    def inferior(self):
         for plan in planes.lista_planes:
             inf =float(input("Ingrese valor de vehiculo"))
             if inf < self.valor:
                 print(plan)
            
    
if __name__==("__main__"):
    planes = coleccion_planes()
    planes.plan_ahorros()
    i=0
    while i==0:
        print("Menu")
        print("1. Actualizar el valor del vehículo de cada plan")
        print("2. Mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.")
        print("3. Mostrar el monto que se debe haber pagado para licitar el vehículo")
        print("4. Modificar la cantidad cuotas que debe tener pagas para licitar")
        print("5. Salir")
        opcion = int(input())
        if opcion == 1:
            planes.modificar()
        elif opcion == 2:
            planes.inferior()
     
        elif opcion==5:
            exit()
        
        
