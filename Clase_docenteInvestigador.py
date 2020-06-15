from Clase_docente import Docente
from Clase_investigador import Investigador
class DocenteInvestigador(Docente,Investigador):
    __categoriaDePrograma=0
    __importeExtra=0.0
    __investigacion=""
    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo,categoriadeprograma,importeextra,investigacion):
        self.__categoriaDePrograma=categoriadeprograma
        self.__importeExtra=importeextra
        self.__investigacion=investigacion
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo)
    def calcularSueldo(self):
        sdocente=Docente.calcularSueldo(self)
        return sdocente+self.__importeExtra
    def getCategoriaDePrograma(self):
        return self.__categoriaDePrograma
    def getImporteExtra(self):
        return self.__importeExtra
    def getInvestigacion(self):
        return self.__investigacion
    def __str__(self):
        return super().__str__()+" Categoría de programa:"+str(self.__categoriaDePrograma)+" Importe Extra:"+str(self.__importeExtra)+" Investigación:"+self.__investigacion
    def mostrarDatos(self):
        return "Nombre:{0:10s} Apellido:{1:10s} Tipo:{2:9s} Sueldo:{3:.2f}".format(super().getNombre(),super().getApellido(),"Docente Investigador",self.calcularSueldo())
    def mostrarDatos2(self):
        return "{0:10s} {1:10s} {2:.2f}".format(self.getApellido(),self.getNombre(),self.__importeExtra)
    def toJSON(self):
        dic1=Docente.retornaParametros(self)
        dic2=Investigador.retornaParametros(self)
        dic3=dict(categoriadeprograma=self.__categoriaDePrograma,importeextra=self.__importeExtra,investigacion=self.__investigacion)
        d=dict(__class__=self.__class__.__name__,__atributos__=dict(cuil=super().getCuil(),apellido=super().getApellido(),nombre=super().getNombre(),sueldobasico=super().getSueldo(),antiguedad=super().getAntiguedad()))
        d["__atributos__"].update(dic1)
        d["__atributos__"].update(dic2)
        d["__atributos__"].update(dic3)
        return d