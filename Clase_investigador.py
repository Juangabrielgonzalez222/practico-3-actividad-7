from Clase_personal import Personal
class Investigador(Personal):
    __area=""
    __tipo=""
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo):
        self.__area=area
        self.__tipo=tipo
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo)
    def calcularSueldo(self):
        basico=self.getSueldo()
        return basico+((self.getAntiguedad()*basico)/100)        
    def __str__(self):
        return super().__str__()+" Área:"+self.__area+" Tipo:"+self.__tipo
    def getArea(self):
        return self.__area
    def retornaParametros(self):
        d=dict(area=self.__area,tipo=self.__tipo)
        return d
    def getTipo(self):
        return self.__tipo
    def toJSON(self):
        dic=super().retornaParametros()
        dic2=dict(carrera=None,cargo=None,catedra=None,area=self.__area,tipo=self.__tipo)
        d=dict(__class__=self.__class__.__name__,__atributos__=dic)
        d["__atributos__"].update(dic2)
        return d