class viajero:
    num = 0
    dni = ""
    nom = ""
    apel = ""
    millas_acum = 0


    def __init__(self, num, dni, nom, apel):
        self.num = num
        self.dni = dni
        self.nom = nom
        self.apel = apel
        
    
    def option1(self):
        print("Sus millas acumuladas son: ", self.millas_acum)


    def option2(self):
        millas = int(input("Ingrese millas para acumular: "))
        self.millas_acum += millas
        print("Se han acumulado", millas, "millas. Millas totales:", self.millas_acum)

    def option3(self):
        milla = int(input("Ingrese millas a canjear "))
        if self.millas_acum >= milla:
            self.millas_acum -= milla
            print("Las millas que le quedan son: ",self.millas_acum)
        else:
            print("No tiene suficientes millas para canjear.")