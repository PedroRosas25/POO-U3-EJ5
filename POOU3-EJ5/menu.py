from claseempleado import Empleado
class Menu:
    __opcion=0

    def __init__(self):
        self.__opcion=0

    def opciones(self,m):
        while self.__opcion!=4:
            print('1--Ingresar elemento por posicion\n2--Ingresar elemento al final\n3--Mostrar elemento por posicion\n')
            self.__opcion=int(input('Ingrese una opcion '))
            if self.__opcion==1:
                dni=int(input('Ingrese dni de la persona '))
                nombre=str(input('Ingrese nombre de la persona '))
                direccion=str(input('Ingrese direccion de la persona '))
                telefono=str(input('Ingrese telefono de la persona '))
                unempleado=Empleado(dni,nombre,direccion,telefono)
                posicion=int(input('Ingrese posicion donde insertar el elemento '))
                m.insertarelemento(unempleado,posicion)
            elif self.__opcion==2:
                dni=int(input('Ingrese dni de la persona '))
                nombre=str(input('Ingrese nombre de la persona '))
                direccion=str(input('Ingrese direccion de la persona '))
                telefono=str(input('Ingrese telefono de la persona '))
                unempleado=Empleado(dni,nombre,direccion,telefono)
                m.agregarelemento(unempleado)
            elif self.__opcion==3:
                posicion=int(input('Ingrese posicion del elemento a mostrar '))
                m.mostrarelemento(posicion)
            elif self.__opcion==4:
                print('SALIENDO DEL PROGRAMA')  
            else:
                print('Opcion ingresada incorrecta ')                  
