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
            #Titulo
            print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
            print (('\033[1;31m' + 'Agregar Tarea' + '\33[;0m').center(100,' '))
            print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
            fn.agregar_tareas(fn.tareas)
            #fin de la funcion
            input ('\33[;40;37mpulse una tecla\33[;0m')
        case '2':
            system('cls')
            #Titulo
            print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
            print (('\033[1;31m' + 'Ver Tarea' + '\33[;0m').center(100,' '))
            print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
            fn.ver_tareas(fn.tareas)
            #fin de la funcion
            input ('\33[;40;37mpulse una tecla\33[;0m')
        case '3':
            system('cls')
            #Titulo
            print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
            print (('\033[1;31m' + 'Completar Tarea' + '\33[;0m').center(100,' '))
            print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
            fn.completar_tareas(fn.tareas)
            #fin de la funcion
            input ('\33[;40;37mpulse una tecla\33[;0m')
        case '4':
            system('cls')
            #Titulo
            print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
            print (('\033[1;31m' + 'Eliminar Tarea' + '\33[;0m').center(100,' '))
            print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
            fn.eliminar_tarea(fn.tareas)
            #fin de la funcion
            input ('\33[;40;37mpulse una tecla\33[;0m')
        case '5':
            system('cls')
            fn.salir()
        case _:
            system('cls')
            print ('\033[;31m' + 'no has puesto una opcion valida' + '\033[;0m' )
            input('Pulse una tecla')
inicio()
