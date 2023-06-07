from clasenodo import Nodo

class Lista:
    __comienzo=Nodo

    def __init__(self):
        self.__comienzo=None
    def agregarEmpleadoFinal(self,empleado):
        nuevonodo = Nodo(empleado)
        if self.__comienzo == None:
            self.__comienzo = nuevonodo
        else:
            temporal = self.__comienzo
            while temporal.getSiguiente() is not None:
                temporal = temporal.getSiguiente()
            temporal.setSiguiente(nuevonodo)    

    def agregarEmpleadoIndice(self,empleado,indice):
        nuevonodo=Nodo(empleado)
        if indice == 1:
            nuevonodo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevonodo
        else:
            temporal = self.__comienzo
            contador = 1 
            while temporal:
                if contador + 1 == indice:
                    nuevonodo.setSiguiente(temporal.getSiguiente())
                    temporal.setSiguiente(nuevonodo)
                    break
                temporal = temporal.getSiguiente()
                contador += 1

    def mostrarEmpleadoIndice(self, indice):
        temporal = self.__comienzo
        contador = 0
        while temporal:
            if contador+1 == indice:
                return temporal.getDato()
            temporal = temporal.getSiguiente()
            contador += 1
        


        
