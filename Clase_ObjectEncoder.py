from pathlib import Path
import json
class ObjectEncoder():
    def DecodificarDiccionario(self,d):
        from Clase_manejador import Manejador
        from Clase_apoyo import Apoyo
        from Clase_docente import Docente
        from Clase_investigador import Investigador
        from Clase_docenteInvestigador import DocenteInvestigador
        if "__class__" not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                agentes=d['agentes']
                dAgente=None
                manejador=class_()
                for i in range(len(agentes)):
                    dAgente=agentes[i]
                    class_name=dAgente.pop('__class__')
                    class_=eval(class_name)
                    atributos=dAgente['__atributos__']
                    trabajador=class_(**atributos)
                    manejador.agregarEnLista(trabajador)
                return manejador 
    def guardarEnArchivo(self,diccionario,archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()
    def leerArchivo(self,archivo):
        try:
            with Path(archivo).open(encoding="UTF-8") as fuente:
                diccionario=json.load(fuente)
                fuente.close()
        except:
            diccionario=-1
        return diccionario