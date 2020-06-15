import abc
class Personal():
    __cuil=""
    __apellido=""
    __nombre=""
    __sueldoBasico=0.0
    __antiguedad=0
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera=None,cargo=None,catedra=None,area=None,tipo=None):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldoBasico=sueldobasico
        self.__antiguedad=antiguedad
    def __str__(self):
        return  "Nombre:"+self.__nombre+" Apellido:"+self.__apellido+" Cuil:"+self.__cuil+" Sueldo basico:"+str(self.__sueldoBasico)+" Antigüedad:"+str(self.__antiguedad)
    @abc.abstractmethod
    def calcularSueldo():
        pass
    def retornaParametros(self):
        d=dict(cuil=self.__cuil,apellido=self.__apellido,nombre=self.__nombre,sueldobasico=self.__sueldoBasico,antiguedad=self.__antiguedad)
        return d
    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSueldo(self):
        return self.__sueldoBasico
    def getAntiguedad(self):
        return self.__antiguedad
    def mostrarDatos(self):
        return "Nombre:{0:10s} Apellido:{1:10s} Tipo:{2:9s} Sueldo:{3:.2f}".format(self.__nombre,self.__apellido,self.__class__.__name__,self.calcularSueldo())