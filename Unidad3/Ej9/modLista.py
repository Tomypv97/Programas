from modNodo import Nodo
from modInterfaz import Interfaz
from zope.interface import implementer
from modVehiculo import Vehiculo
import json

@implementer(Interfaz)
class Lista:

    def _init_(self):
        
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def getTope(self):
        
        return self.__tope
    
    def _iter_(self):

        self._actual = self._comienzo
        
        return self

    def _next_(self):
        
        if self.__actual is None:
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self._actual = self._actual.getSiguiente()
            return dato
    
    def agregarElemento(self, elemento):
        
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
        
        
    def insertarElemento(self, posicion, elemento):
        
        if posicion < 0 or posicion > self.__tope:
            
            raise ValueError("Posición inválida")
        
        if posicion == 0:
            
            nodo = Nodo(elemento)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
        
        else:
            
            nodo_anterior = None
            nodo_actual = self.__comienzo
            index = 0
            
            while index < posicion and nodo_actual is not None and posicion < self.__tope:
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
                if nodo_actual is None:
                    
                    raise ValueError("Posición inválida")

                nodo = Nodo(elemento)
                nodo.setSiguiente(nodo_actual)
                nodo_anterior.setSiguiente(nodo)
                
        
        self.__tope += 1


    
    def mostrarElemento(self, posicion):
        
        n = None
        band = True
        nodo_anterior = None
        nodo_actual = self.__comienzo
        index = 0
            
        while band and index <= posicion and nodo_actual is not None and posicion < self.__tope:
            
            if index == posicion:
                
                band = False
                print(nodo_actual)
                n = nodo_actual.getDato()
                
            
            else:    
                
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.getSiguiente()
                index += 1
        
        return n