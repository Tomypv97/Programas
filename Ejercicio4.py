import tkinter

class Ventana:
    def __init__(self, titulo, valorxsup, valorysup, valorxinf, valoryinf):
        self.titulo = titulo
        self.valorxsup = valorxsup
        self.valorysup = valorxsup
        self.valorxinf = valorxinf
        self.valoryinf = valoryinf
        
        
    def mostrar(self):
        ventanaInicio=tkinter.Tk()
        ventanaInicio.title(self.titulo)
        ventanaInicio.geometry(str(self.valorxinf) + "x" + str(self.valoryinf))
        ventanaInicio.resizable(self.valorxsup,self.valorysup)
        ventanaInicio.mainloop()
        self.ventanaInicio = ventanaInicio
        
        
    def getTitulo(self):
        return self.titulo
        
    def alto(self):
        return self.valorxinf
    
    def ancho(self):
        return self.valoryinf
    
    #def moverDerecha(self,10):
     #   x=10
      #  self.valorxinf+=x
       # ventanaCargar.geometry(str(self.valorxinf) + "x" + str(self.valoryinf) ) 
        
    
if __name__== '__main__':

    print('==== Ventana Inicio ====')

    ventanaInicio= Ventana('Inicio', 0, 0, 500, 500)

    ventanaInicio.mostrar()
    
    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))

   #print('==== Ventana Cargar ====')

    #ventanaCargar= Ventana("Cargar",10,20,500,500)

    #ventanaCargar.mostrar()

    #print('*** Mueve a la derecha ***')

    #ventanaCargar.moverDerecha(10)

    #ventanaCargar.mostrar()

 #   print('*** Mueve a la izquierda ***')

  #  ventanaCargar.moverIzquierda(10)

   # ventanaCargar.mostrar()

    #print('*** Bajar ***')

    #ventanaCargar.bajar(10)

    #ventanaCargar.mostrar()

    #print('==== Ventana Borrar ====')

    #ventanaBorrar = Ventana('Borrar', 10,20,100,200)

    #ventanaBorrar.mostrar()

    #print('*** Subir ***')

    #ventanaBorrar.subir(5)   

    #ventanaBorrar.mostrar()

    #print('*** Subir ***')

    #ventanaBorrar.subir()

    #ventanaBorrar.mostrar()

    #print('*** Bajar ***')

    #ventanaBorrar.bajar()

    #ventanaBorrar.mostrar()
    
    














