from Clase_docente import Docente
from Clase_investigador import Investigador
from Clase_apoyo import Apoyo
from Clase_docenteInvestigador import DocenteInvestigador
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            7:self.opcion7,
                            8:self.opcion8,
                            9:self.test,
                            10:self.salir
                         }
    def opcion(self,op,manejador):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if(op<1 or op>9):    
            func()
        else:
            func(manejador)
    def salir(self):
        print('Usted salio del programa')
    def CargaDeDatos(self):
        cuil=input("Ingrese cuil:")
        apellido=input("Ingrese apellido:")
        nombre=input("Ingrese nombre:")
        sueldobas=float(input("Ingrese sueldo básico:"))
        antiguedad=int(input("Ingrese antigüedad:"))
        print("A continuación si desea registrar docente ingrese 1, 2 para personal de apoyo,3 investigador y 4 docente investigador. ")
        opcion=int(input("Ingrese opcion:"))
        while(opcion>4 or opcion<1):
            print("Opción incorrecta")
            opcion=int(input("Ingrese 1 para docente, 2 para personal de apoyo,3 para investigador o 4 para docente investigador."))
        if opcion==1:
            carrera=input("Ingrese carrera:")
            cargo=input("Ingrese cargo:")
            catedra=input("Ingrese cátedra:")
            agente=Docente(cuil, apellido, nombre, sueldobas, antiguedad, carrera, cargo, catedra)
        elif opcion==2: 
            categoria=int(input("Ingrese número de categoría:"))
            while(categoria>22 or categoria<1):
                print("Número incorrecto rango 1-22")
                categoria=int(input("Ingrese número de categoría:"))
            agente=Apoyo(cuil, apellido, nombre, sueldobas, antiguedad, categoria)   
        elif opcion==3:
            area=input("Ingrese el área:")
            tipo=input("Ingrese el tipo de investigación:")
            agente=Investigador(cuil, apellido, nombre, sueldobas, antiguedad,None,None,None, area, tipo)
        else:
            carrera=input("Ingrese carrera:")
            cargo=input("Ingrese cargo:")
            catedra=input("Ingrese cátedra:")
            area=input("Ingrese el área:")
            tipo=input("Ingrese el tipo de investigación:")
            categoriadeprograma=int(input("Ingrese número de categoría de investigación 1-5:"))
            while(categoriadeprograma>5 or categoriadeprograma<1):
                print("Número incorrecto rango 1-5")
                categoriadeprograma=int(input("Ingrese número de categoría de investigación:"))
            importeextra=float(input("Ingrese importe extra:"))
            investigacion=input("Ingrese investigación:")
            agente=DocenteInvestigador(cuil, apellido, nombre, sueldobas, antiguedad, carrera, cargo, catedra, area, tipo, categoriadeprograma, importeextra, investigacion)
        return agente
    def opcion1(self,manejador):
        agente=self.CargaDeDatos()
        pos=int(input("Ingrese la posición a añadir en la lista:"))
        error=manejador.insertarEnLista(agente,pos)
        while(error==-1):
            pos=int(input("Ingrese posicion a añadir en la lista que resulte correcta:"))
            error=manejador.insertarEnLista(agente,pos)
    def opcion2(self,manejador):
        agente=self.CargaDeDatos()
        manejador.agregarEnLista(agente)
    def opcion3(self,manejador):
        pos=int(input("Ingrese la posición:"))
        manejador.mostrarElemento(pos)
    def opcion4(self,manejador):
        carrera=input("Ingrese el nombre de la carrera:")
        manejador.MostrarDIConCarrera(carrera)
    def opcion5(self,manejador):
        area=input("Ingrese el área :")
        manejador.contarPorArea(area)
    def opcion6(self,manejador):
        manejador.ListadoPorApellido()
    def opcion7(self,manejador):
        categoriadeprograma=int(input("Ingrese número de categoría de investigación 1-5:"))
        while(categoriadeprograma>5 or categoriadeprograma<1):
            print("Número incorrecto,rango 1-5")
            categoriadeprograma=int(input("Ingrese número de categoría de investigación:"))
        manejador.listarPorCategoria(categoriadeprograma)
    def opcion8(self,manejador):
        manejador.guardarenJson()
    def test(self,manejador):
        manejador.test()