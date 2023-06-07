from claseempleado import Empleado
import numpy as np
from interface import IEmpleado
from claseerrorempleado import ErrorEmpleado
from claselista import Lista
class Manejador(IEmpleado):
    __lista=Lista()

    def __init__(self):
        self.__lista=Lista()
        self.__len=3

    def insertarelemento(self,empleado,posicion):
        if posicion<=0:
            raise ErrorEmpleado(self,'No se puede insertar un elemento de una lista en una posicion menor que 0 ')
        if posicion>self.__len:
            raise ErrorEmpleado(self,'No se puede insertar un elemento en una posicion mayor a la del tamaño de la lista  ')
        self.__lista.agregarEmpleadoIndice(empleado,posicion)
        print('Elemento insertado correctamente ')

    def agregarelemento(self,elemento):
        self.__lista.agregarEmpleadoFinal(elemento)

    def mostrarelemento(self,posicion):
        if posicion<=0:
            raise ErrorEmpleado(self,'No se puede mostrar un elemento de una lista en una posicion menor que 0 ')
        if posicion>self.__len:
            raise ErrorEmpleado(self,'No se puede mostrar un elemento en una posicion mayor a la del tamaño de la lista  ')  
        print('{}'.format(self.__lista.mostrarEmpleadoIndice(posicion)))         



