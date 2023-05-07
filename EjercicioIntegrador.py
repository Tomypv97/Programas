

class Alumno:
    
        def __init__(self, dni, apellido, nombre, notas, anio):
            self.dni = dni
            self.apellido = apellido
            self.nombre = nombre
            self.notas = notas
            self.anio = anio


        def promedio(self):
            return self.notas / 2

if __name__=="__main__":
    
    alumnos = []
    for i in range(3):
        dni = input("Ingrese el DNI del alumno {}: ".format(i+1))
        nombre = input("Ingrese el nombre del alumno {}: ".format(i+1))
        apellido = input("Ingrese el apellido del alumno {}: ".format(i+1))
        notas = input("Ingrese la notas del alumno {}: ".format(i+1))
        anio = input("Ingrese el año de la carrera que cursa el alumno {}: ".format(i+1))
    
        alumnos = Alumno(dni, apellido, nombre, notas, anio)
        Alumno.append(alumnos)
        
        
    i=0
    while i==0:
        print("Menu")
        print("1. Leer por teclado el número de dni de un alumno, e informar su promedio con aplazos y sin aplazos. ")
        print("2. Salir")
        opcion = int(input())
        if opcion == 1:
            numero = input("Ingrese dni: ")
            for Alumno in alumnos:
                if Alumno.dni == int(numero):
                    break
                else:
                    print("No se encontró el dni.")
                    continue
            print("El promedio del alumno es: ", Alumno.promedio())
        elif opcion == 2:
            exit()
    














