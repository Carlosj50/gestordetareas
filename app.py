import funciones as fn
import menu as mn
from os import system

#titulo y menu
def inicio():
    while True:
        system('cls')
        mn.titulo()
        mn.menu()
        opciones(opciones)
#opciones con match
def opciones(opcion):
    opcion = input('\033[;33m' +'Selecione una opción del menu: \n' + '\33[;36m')
    match opcion:
        case '1':
            fn.agregar_tareas(fn.tareas)
        case '2':
            fn.ver_tareas(fn.tareas)
        case '3':
            fn.completar_tareas(fn.tareas)
        case '4':
            fn.eliminar_tarea(fn.tareas)
        case '5':
            fn.salir()
        case _:
            print ('no has puesto una opcion valida')
inicio()
