from Clase_personal import Personal
class Docente(Personal):
    __carrera=""
    __cargo=""
    __catedra=""
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area="",tipo=""):
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo)
    def __str__(self):
        return super().__str__()+" Carrera:"+self.__carrera+" Cargo:"+self.__cargo+" Catedra:"+self.__catedra
    def calcularSueldo(self):
        basico=self.getSueldo()
        sueldo=basico+((self.getAntiguedad()*basico)/100)
        if(self.__cargo=="simple"):
            sueldo+=(10*basico)/100
        elif(self.__cargo=="semiexclusivo"):
            sueldo+=(20*basico)/100
        elif(self.__cargo=="exclusivo"):
            sueldo+=(50*basico)/100
        return sueldo
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def retornaParametros(self):
        d=dict(carrera=self.__carrera,cargo=self.__cargo,catedra=self.__catedra)
        return d
    def toJSON(self):
        dic=super().retornaParametros()
        dic2=dict(carrera=self.__carrera,cargo=self.__cargo,catedra=self.__catedra,area=None,tipo=None)
        d=dict(__class__=self.__class__.__name__,__atributos__=dic)
        d["__atributos__"].update(dic2)
        return d   