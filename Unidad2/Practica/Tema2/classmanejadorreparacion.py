from classreparacion import reparacion
import csv

class manejadorreparacion:
    
    def carga(reparaciones):
        with open("reparaciones.csv","r") as archivoreparaciones:
            next(archivoreparaciones)
            for file in archivoreparaciones:
                file = file.split(";")
                rep = reparacion(file[0], file[1], float(file[2]), float(file[3]), file[4])
                reparaciones.append(rep)
            print("Carga reparaciones exitosa")   
            
    def modificar(clientes,patente):
        i = 0
        bandera = False
        while i < len(clientes) and bandera == False:
            if clientes[i].getpatente() == patente:
                clientes[i].modificar()
                bandera = True
            else:
                i +=1
            
    def mostrar(clientes,reparaciones,patente):
        return 0
            
            
    def option2(clientes,reparaciones):
        patente = "AB000BA"
        bandera = False
        i = 0
        while i < len(reparaciones) and bandera == False:
                if reparacion[i].getestado() == "T":
                    if ((reparaciones[i].getpatente() == patente) and (reparaciones[i].getestado() == "T")):
                        bandera = True
                    else:
                        i+=1
                if bandera == True:
                    print("No tiene reparaciones pendiente ")
                    manejadorreparacion.modificar(clientes,patente)
                    print("Se modifico el estado")
                    manejadorreparacion.mostrar(clientes,reparaciones,patente)
                else:
                    print("Tiene reparaciones pendiente")
                    
    def option4(clientes,reparaciones):
        j = 0
        t = -1
        band = False
        for i in range(len(reparaciones)):
            while j < len(reparaciones) and band == False:
                if reparaciones[j].getpatente() == reparaciones[t+1].getpatente():
                    print("El cliente con patente: ",reparaciones[j].getpatente(),",Tiene mas de una reparacion ")
                    band = True
                else:
                    t +=1
                j+1
                
        










