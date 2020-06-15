from Clase_personal import Personal
class Apoyo(Personal):
    __categoria=0
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__categoria=categoria
    def calcularSueldo(self):
        basico=self.getSueldo()
        sueldo=basico+((self.getAntiguedad()*basico)/100)
        if(self.__categoria>0 and self.__categoria<11):
            sueldo+=(10*basico)/100
        elif(self.__categoria>10 and self.__categoria<21):
            sueldo+=(20*basico)/100
        elif(self.__categoria>20 and self.__categoria<23):
            sueldo+=(30*basico)/100
        return sueldo
    def __str__(self):
        return super().__str__()+" Categoría:"+self.__categoria
    def getCategoria(self):
        return self.__categoria
    def toJSON(self):
        dic=super().retornaParametros()
        d=dict(__class__=self.__class__.__name__,__atributos__=dic)
        d["__atributos__"]["categoria"]=self.__categoria
        return d