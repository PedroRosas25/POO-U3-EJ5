class ErrorEmpleado(Exception):
    __empleado=None
    __mensaje=None

    def __init__(self,empleado,mensaje=None):
        if mensaje is None:
            print('Ocurrio un error inesperado ')
        super(ErrorEmpleado,self).__init__(mensaje)
        self.__empleado=empleado
        self.__mensaje='ErrorEmpleado: '+mensaje
            