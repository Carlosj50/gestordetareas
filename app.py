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
            system('cls')
            fn.agregar_tareas(fn.tareas)
        case '2':
            system('cls')
            fn.ver_tareas(fn.tareas)
        case '3':
            system('cls')
            fn.completar_tareas(fn.tareas)
        case '4':
            system('cls')
            fn.eliminar_tarea(fn.tareas)
        case '5':
            system('cls')
            fn.salir()
        case _:
            system('cls')
            print ('\033[;31m' + 'no has puesto una opcion valida' + '\033[;0m' )
            input('Pulse una tecla')
inicio()
