from Clase_menu import Menu
from Clase_manejador import Manejador
from Clase_ObjectEncoder import ObjectEncoder
if __name__=='__main__':
    jsonf=ObjectEncoder()
    diccionario=jsonf.leerArchivo("personal.json")
    if diccionario!=-1:
        manejador=jsonf.DecodificarDiccionario(diccionario)
        print("Se cargaron agentes de archivo")
    else:    
        manejador=Manejador()
    menu=Menu()
    op=None
    print("Bienvenido al programa:")
    while(op!=10):
        print("Ingrese 1 para  Insertar a agentes a la colección.")
        print("Ingrese 2 para agregar agentes a la colección.")
        print("Ingrese 3 para mostrar por pantalla que tipo de agente se encuentra almacenado en una posición.")
        print("Ingrese 4 para dada una carrera mostrar un listado de docentes investigadores.")
        print("Ingrese 5 para conocer la cantidad de docentes investigadores e investigadores en un área.")
        print("Ingrese 6 para mostrar un listado de agentes por apellido.")
        print("Ingrese 7 para dada una categoria de investigación,conocer los docentes investigadores que se encuentran en ella y el presupuesto para solicitar.")
        print("Ingrese 8 para guardar en el archivo json")
        print("Ingrese 9 para realizar test.")
        print("Ingrese 10 para salir.")
        op=int(input("Ingrese opcion:"))
        menu.opcion(op,manejador)