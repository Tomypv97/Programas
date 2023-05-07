class Numero:
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        
        self.c = c
        self.d = d
    def __add__(self, otro):    
        if isinstance(otro, Numero):
                suma_a = self.a + otro.a
                suma_b = self.b + otro.b
                suma_c = self.c + otro.c
                suma_d = self.d
                suma_a = self.a + otro.a

                return Numero(suma_a, suma_b, suma_c, suma_d)

    def __add__(self, otro):    
         if isinstance(otro, Numero):
                resta_a = self.a - otro.a
                resta_b = self.b - otro.b
                resta_c = self.c - otro.c
                resta_d = self.d
                resta_a = self.a - otro.a
                
                return Numero(suma_a, suma_b, suma_c, suma_d)

     def __eq__(self, otro):
         for Numero in lista:
             if self.a == otro.a , self.b == otro.b, self.c == otro.c , self.d == otro.d, :  
             
                 print("Los numeros son iguales ")
             else:
                 print("Los numeros no son iguales")

if __name__ == "__main__":
    e = Numero(1,2,3,4)
    f = Numero(3,6,9)
    lista = [e,f]
    suma = e + f 
    print("Suma de e + f es: ",suma)
    resta = e - f
    print("Resta de e y f es: ",resta)
    igual = e == f
    print(e==f)















