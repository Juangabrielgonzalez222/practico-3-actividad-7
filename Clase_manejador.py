from Clase_lista import Lista
from Clase_ObjectEncoder import ObjectEncoder
from Clase_docente import Docente
from Clase_docenteInvestigador import DocenteInvestigador
from Clase_investigador import Investigador
from Clase_apoyo import Apoyo
class Manejador():
    __lista=None   
    __jsonf=None
    __archivo=""
    def __init__(self):
            self.__lista=Lista()
            self.__jsonf=ObjectEncoder()
            self.__archivo="personal.json"
    def insertarEnLista(self,elemento,pos):
        error=self.__lista.insertarElemento(elemento,pos)
        return error
    def agregarEnLista(self,elemento):
        self.__lista.agregarElemento(elemento)
    def mostrarElemento(self,pos):
        self.__lista.mostrarElemento(pos)
    def MostrarDIConCarrera(self,carrera):
        print("Agentes que se desempeñan como Docentes Investigadores en la carrera:")
        dic={}
        for agente in self.__lista:
            if type(agente)==DocenteInvestigador:    
                if(agente.getCarrera()==carrera):
                    dic[agente.getNombre()]=agente
        if(len(dic)!=0):
            dic=sorted(dic.items())
            for agente in dic:
                print(agente[1])
        else:
            print("No se encontro a ningun agente con la carrera ingresada")
    def contarPorArea(self,area):
        dic=dict(DocenteInvestigador=0,Investigador=0)
        for agente in self.__lista:
            if(type(agente)==DocenteInvestigador or type(agente)==Investigador):
                if(agente.getArea()==area):
                    dic[agente.__class__.__name__]+=1
        print("La cantidad de docentes investigadores es:{} y la cantidad de investigadores es:{}".format(dic["DocenteInvestigador"],dic["Investigador"]))
    def ListadoPorApellido(self):
        print("Agentes:")
        dic={}
        for agente in self.__lista:
                dic[agente.getApellido()]=agente
        if(len(dic)!=0):
            dic=sorted(dic.items())
            for agente in dic:
                print(agente[1].mostrarDatos())
        else:
            print("No hay ningun agente en la colección")
    def listarPorCategoria(self,categoria):
        print("{0:10s} {1:10s} {2:}".format("Apellido:","Nombre:","Importe Extra:"))
        acum=0
        for agente in self.__lista:
            if(agente.__class__.__name__=="DocenteInvestigador"):
                if(agente.getCategoriaDePrograma()==categoria):
                    print(agente.mostrarDatos2())
                    acum+=agente.getImporteExtra()
        if(acum!=0):
            print("Dindero que debe ser solicitado en función de importes extras es:{:.2f}".format(acum))
        else:
            print("No se encontraron docentes investigadores en la categoría ingresada.")
    def cambiarArchivo(self,archivo):
        self.__archivo=archivo
    def toJson(self):
        d=dict(__class__=self.__class__.__name__,agentes=[agente.toJSON() for agente in self.__lista])
        return d
    def guardarenJson(self):
            dic=self.toJson()
            self.__jsonf.guardarEnArchivo(dic,self.__archivo)
            print("Se guardo con exito en el archivo")
    def test(self):
        manejador2=Manejador()
        docente=Docente("20-30445324-5","Fernandez", "Jose", 30000.40, 6,"LSI","exclusivo", "Matemática Básica")
        apoyo=Apoyo("20-38234246-6","Flores", "Ignacio",9000.21,3, 7)
        investigador=Investigador("27-41345398-5","Cevallos","Martin",15000, 7,None,None, None,"Investigación computacional","pruebas")
        docentein=DocenteInvestigador("20-36239842-5","Gomez","Fernanda",22000.12, 5,"LCC","Semiexclusico","Programacion","Investigación computacional","pruebas", 4, 9000,"Relacionada a la inteligencia artificial")
        docentein2=DocenteInvestigador("20-45313453-5","Sanchez","Ines",20000.22, 6,"LCC","simple","Programacion","Investigación computacional","pruebas", 4, 8000,"Relacionada a la inteligencia artificial")
        manejador2.agregarEnLista(docente)
        manejador2.agregarEnLista(apoyo)
        manejador2.insertarEnLista(investigador,1)
        manejador2.agregarEnLista(docentein)
        manejador2.insertarEnLista(docentein2,3)
        print("tipo del primer elemento:")
        manejador2.mostrarElemento(1)
        print("Prueba de docentes investigadores en carrera lcc:")
        manejador2.MostrarDIConCarrera("LCC")
        print("Cantidad de investigadores y docentes investigadores en Investigación computacional:")
        manejador2.contarPorArea("Investigación computacional")
        print("5 agentes ordenados por apellido: ")
        manejador2.ListadoPorApellido()
        print("Test para categoía de investigación 4: ")
        manejador2.listarPorCategoria(4)
        print("Testeando guardado de archivo en pruebas.json:")
        manejador2.cambiarArchivo("pruebas.json")
        manejador2.guardarenJson()