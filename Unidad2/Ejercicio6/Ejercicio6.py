class Viajero:

    def __init__(self, num, dni, nom, apel, millas_acum):
        self.num = num
        self.dni = dni
        self.nom = nom
        self.apel = apel
        self.millas_acum = millas_acum

    def __gt__(self, otro):
        return self.millas_acum > otro.millas_acum

    def __add__(self, otro):
        if isinstance(otro, int):
            return Viajero(None, None, None, None, self.millas_acum + otro)
        elif isinstance(otro, Viajero):
            return Viajero(None, None, None, None, self.millas_acum + otro.millas_acum)
        else:
            raise TypeError("Tipo de objeto no soportado para la suma")

    def __sub__(self, otro):
        if isinstance(otro, int):
            return Viajero(None, None, None, None, self.millas_acum - otro)
        elif isinstance(otro, Viajero):
            return Viajero(None, None, None, None, self.millas_acum - otro.millas_acum)
        else:
            raise TypeError("Tipo de objeto no soportado para la resta")

if __name__ == "__main__":
    per1 = Viajero(1, 22123123, "Ricardo", "Paz", 1000)
    per2 = Viajero(2, 23000000, "Rojas", "Rosas", 2000)
    per3 = Viajero(3, 24000000, "Raul", "Romero", 3000)
    per4 = Viajero(4, 25000000, "Roman", "Ruiz", 4000)

    lista = [per1, per2, per3, per4]

    mayor = max(lista, key=lambda x: x.millas_acum)
    print("El mayor número de millas acumuladas es de:", mayor.millas_acum)

    x = 100
    suma = sum(lista) + x
    print("La suma de millas acumuladas es: ", suma.millas_acum)

    y = 100
    restas = sum(lista) - y
    print("La resta de millas acumuladas es: ", restas.millas_acum)





















