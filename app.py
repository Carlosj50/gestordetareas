import funciones as fn
from menu import *

#titulo y menu
def inicio():
    while True:
        titulo()
        menu()
        opciones(opciones)
#opciones con match
def opciones(opcion):
    opcion = input('Selecione una opción del menu: \n')
    match opcion:
        case '1':
            print ('Añadir tarea')
        case '2':
            print ('Ver Tareas')
        case '3':
            print ('Completar Tareas')
        case '4':
            print ('Eliminar tarea')
        case '5':
            salir = input ('Va a salir del programa. ¿Está seguro? s/n \n')
            if salir == 's':
                print ('Adios')
                exit()
            else:
                inicio()
        case _:
            print ('no has puesto una opcion valida')
inicio()
