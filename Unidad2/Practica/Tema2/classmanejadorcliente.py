from classcliente import cliente
import csv

class manejadorcliente:
    
    def carga(clientes):
        with open("clientes.csv","r") as archivoclientes:
            next(archivoclientes)
            for file in archivoclientes:
                file = file.split(";")
                cli = cliente(file[0],file[1],file[2],file[3],file[4],file[5],file[6])
                clientes.append(cli)
            print("Carga de clientes exitosa")
                
            
    def getpatente(clientes,dni):
        patente = ""
        for i in range(len(clientes)):
            if clientes[i].getdni() == dni:
                patente = clientes[i].getpatente()
        return patente
    
    
    def getcliente(clientes,dni):
        i=0
        bandera = False
        valorRetorno = 0
        while i < len(clientes) and bandera == False:
            if clientes[i].getdni() == dni:
                valorRetorno = i
                bandera = True
            else:
                i +=1
        return valorRetorno
    
    
        
    
    
    def option1(clientes,reparaciones):
        dni = 21111223
        patente = manejadorcliente.getpatente(clientes, dni)
        i = 0
        bandera = False
        
            
                
                    
            
                
            




