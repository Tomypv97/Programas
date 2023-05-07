class viajero:

    def __init__(self, num, dni, nom, apel, millas_acum):
        self.num = num
        self.dni = dni
        self.nom = nom
        self.apel = apel
        self.millas_acum = millas_acum

    def cantidad_total_de_millas(self):
        return self.millas_acum

    def acumular_millas(self, millas):
        self.millas_acum += millas
        

    def canjear_millas(self, millas):
        if self.millas_acum >= millas:
            self.millas_acum -= millas
            return self.millas_acum
        else:
            print("No tiene suficientes millas para canjear.")

per1 = viajero(1, 22123123, "Ricardo", "Paz", 1000)
per2 = viajero(2, 23000000, "Rojas", "Rosas", 2000)
per3 = viajero(3, 24000000, "Raul", "Romero", 3000)
per4 = viajero(4, 25000000, "Roman", "Ruiz", 4000)

lista = [per1, per2, per3, per4]

if __name__=="__main__":


    while True:
        print("Menu")
        numero = input("Ingrese numero de viajero frecuente: ")
        for viajero in lista:
            if viajero.num == int(numero):
                break
            else:
                print("No se encontró el número de viajero frecuente.")
                continue
            print("1. Consultar cantidad de millas")
            print("2. Acumular millas")
            print("3. Canjear millas")
        print("4. Salir")
        opcion = int(input())
        if opcion == 1:
            print("El número de millas que tiene acumuladas son:", viajero.cantidad_total_de_millas())
        elif opcion == 2:
                millas = int(input("Ingrese millas para acumular: "))
                viajero.acumular_millas(millas)
                print("Se han acumulado", millas, "millas. Millas totales:", viajero.cantidad_total_de_millas())
        elif opcion == 3:
                    milla=int(input("Ingrese millas a canjear "))
                    print("Se han canjeado", milla, "millas. Millas restantes:", viajero.canjear_millas(milla))
        
        elif opcion==4:
            exit()