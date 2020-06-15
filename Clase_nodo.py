from Clase_personal import Personal
class Nodo():
    __agente=None
    __siguiente=None
    def __init__(self,agente):
        if isinstance(agente,Personal):
            self.__agente=agente
            self.__siguiente=None
        else:
            print("El objeto no era instancia de una clase valida")
            self.__agente=-1
    def modificarSiguiente(self,siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getElemento(self):
        return self.__agente
    def toJSON(self):
        return self.__agente.toJSON()