class registro:

    def __init__(self, temp, hum, pre):
        self.temp = temp
        self.hum = hum
        self.pre = pre

    def mayor(self):
        for registro in lista:
            mayor = max(self.hum,self.temp,self.pre)
            print("El mayor numero en la primer hora es: ",mayor)
            menor = min(self.hum,self.temp,self.pre)
            print("El menor numero en la primer hora es: ",menor)
        

    def promedio(self):
        for registro in lista:
            prom=sum(self.hum,self.temp,self.pre)/3
            print("El promedio de la primer hora es: ",prom)
            
            
    def mostrar(self):
        for registro in lista:
            print("La temperatura es: {self.temp} ,humedad: {self.hum}, presion: {self.pre}")
            
if __name__ =="__main__":
    
    dia1_hora0 =registro(10,11,12)
    dia1_hora1 =registro(13,14,15)
    dia1_hora2 =registro(16,17,18)
    lista = [dia1_hora0,dia1_hora1,dia1_hora2]
    i=0
    while i==0:
        print("Menu")
        print("1. Mostrar para cada variable el día y hora de menor y mayor valor.")
        print("2. Indicar la temperatura promedio mensual por cada hora")
        print("3. Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.")
        print("4. Salir")
        opcion = int(input())
        if opcion == 1:
           registro.mayor(lista)
        elif opcion == 2:
            registro.promedio(lista)
        elif opcion == 3:
            registro.mostrar(lista)    
        elif opcion==4:
            exit()












