class Email:
    def __init__(self, id, dom, tip, contra):
        self.id = id
        self.dom = dom
        self.tip = tip
        self.contra = contra

    def retorna_email(self): # Agregar self como primer parámetro
        emailss = self.id + self.dom + self.tip # Agregar self antes de cada atributo
        return emailss

    def modificar_contra(self):
        contrase = input("Ingrese contraseña actual: ")
        if self.contra == contrase:
            print("Contraseña correcta")
            nueva = input("Ingrese nueva contraseña: ")
            self.contra = nueva
            print("Su nueva contraseña es:", self.contra)
        else:
            print("Contraseña incorrecta")

if __name__ == '__main__':
    nombre = input("Ingrese su nombre: ")
    ids = input("Ingrese su id de email: ")
    dominio = input("Ingrese el dominio de su email: ")
    tipo = input("Ingrese el tipo de dominio de su email: ")
    contraseña = input("Ingrese la contraseña de su email: ")
    emails = Email(ids, dominio, tipo, contraseña) # Cambiar el nombre de la variable según convenciones de Python
    print("Estimado " + nombre + ", te enviaremos un mensaje a la dirección:", emails.retorna_email())
    emails.modificar_contra()