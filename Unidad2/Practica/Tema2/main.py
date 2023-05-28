from classmanejadorcliente import manejadorcliente
from classmanejadorreparacion import manejadorreparacion

def menu():
    clientes = []
    manejadorcliente.carga(clientes)
    
    reparaciones = []
    manejadorreparacion.carga(reparaciones)
    
    print("Menu")
    print("1- Leer un Dni de un cliente y mostrar informacion")
    print("2- Leer una patente, si las reparaciones están terminadas,cambiar el estado en el Cliente y mostrar nombre y apellido del cliente, el teléfono, el vehículo y el total a pagar. ")
    
    option = int(input("Ingrese opcion elegida: "))
    while option !=0:
        if option ==1:
            manejadorcliente.option1(clientes,reparaciones)
        elif option ==2:
            manejadorreparacion.option2(clientes,reparaciones)
        elif option ==4:
            manejadorreparacion.option4(clientes,reparaciones)
    option = int(input("Ingrese opcion elegida: "))
    

if __name__  == "__main__":
    menu()

