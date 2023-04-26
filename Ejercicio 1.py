class email:
    def __int__(self, id, dom, tip, contra):
        self.id = id
        self.dom = dom
        self.tip = tip
        self.contra = contra


def modificarcontra(self):
    contrase = input(" Ingrese contraseña actual ")
    if self.contra==contrase:
        print("Contrasela correcta ")
        nueva = input("Ingrese nueva contraseña ")
        self.contra==nueva
        print("Su nueva contraseña es: " ,self.contra )
    else:
        print("Contraseña incorrecta")


nombre = input("Ingrese su nombre ")
ids = input("Ingrese su id de email ")
dominio = input("Ingrese el dominio de su email ")
tipo = input("Ingrese el tipo de dominio de su email ")
contraseña =str(input("Ingrese la contraseña de su email "))
emails = ids + dominio + tipo
print("Estimado " + nombre + " te enviaremos un mensaje a la dirreccion " , emails)

unaclase = email(ids,dominio,tipo,contraseña)
unaclase.modificarcontra()
