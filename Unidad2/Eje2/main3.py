from classviajero_ import viajero
import csv
import sys

def menu(viajeros,numero):
                 
    print("Menu")
    print("1- Consultar cantidad de millas ")
    print("2- Acumular millas ")
    print("3- Canjear millas ")   
    print("4- Salir")
    option = int(input(" Ingrese opcion "))

    while option !=4:
        if option == 1:
            viajeros[numero].option1()
        elif option == 2:
            viajeros[numero].option2()
        elif option == 3:
            viajeros[numero].option3()

        option = int(input(" Ingrese opcion "))

if __name__=="__main__":
     viajeros = []
     with open("dataviajeros.csv", "r") as archivoviajeros:
         next(archivoviajeros)
         for file in archivoviajeros:
             file = file.split(";")
             via = viajero(file[0],file[1],file[2],file[3])
             viajeros.append(via)
         print("Info de viajeros cargada con éxito.")
           
             
     numero = int(input("Ingrese numero de vijaero frecuente  "))
     menu(viajeros,numero)