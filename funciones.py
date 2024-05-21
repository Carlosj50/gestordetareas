#lista de tareas
tareas = ['tarea 1','tarea 2']


def agregar_tareas(lista):
    
    #Titulo
    print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
    print (('\033[1;31m' + 'Agregar Tarea' + '\33[;0m').center(100,' '))
    print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
   
    #Entrada para la tarea
    tarea = input('\033[;33m' + 'Escriba la tarea a realizar:\n'+ '\33[;36m')
   
    #Añadir la tarea al final de la lista
    lista.append(tarea)
  
    #Informe de la tarea añadida
    print ('\033[1;32m' + '*' * 50 + '\33[;0m')
    print ('\033[1;35mSe agrego una nueva tarea\33[;0m')
   
    #Imprime la tarea añadida
    print ('\033[1;32m' + '*' * 50 + '\33[;0m')
    print ('\033[1;32mSe agrego la siguiente tarea:\n' + tarea + '\33[;0m')
   
    #Informe del número de tarea
    print ('\033[1;32m' + '*' * 50 + '\33[;0m')
    print (f'El número de tareas es:  {len(lista)}')

    #fin de la funcion
    input ('\33[;40;37mpulse una tecla\33[;0m')

def ver_tareas(lista):
    #Titulo
    print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
    print (('\033[1;31m' + 'Ver Tarea' + '\33[;0m').center(100,' '))
    print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))

    #Condicional que evalua si hay algo en la lista
    if lista:
    #Si hay algo en la lista se presenta
        for i, e in enumerate(lista):
            print (f'\033[1;35m {i+1} -. {e}')
            print ('\033[1;33m' + '*' * 30 + '\33[;0m')
        #Mensaje de fin de listado
        print (f'\033[1;34m--- Estas son todas las tareas a realizar el día de hoy ---\n')

    #Si la lista esta vacia se avisa de ello
    else:
        print ('\033[1;33m' + '*' * 30 + '\33[;0m')
        print (f'\33[;31;47m  No hay tareas que realizar.\33[;0m')
        print ('\033[1;33m' + '*' * 30 + '\33[;0m')
    #fin de la funcion
    input ('\33[;40;37m' + 'pulse una tecla' + '\33[;0m')

def completar_tareas(lista):
    #Titulo
    print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
    print (('\033[1;31m' + 'Completar Tarea' + '\33[;0m').center(100,' '))
    print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))

    #fin de la funcion
    input ('\33[;40;37mpulse una tecla\33[;0m')

def eliminar_tarea(lista):
    #Titulo
    print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))
    print (('\033[1;31m' + 'Eliminar Tarea' + '\33[;0m').center(100,' '))
    print (('\033[1;32m' + '*' * 27 + '\33[;0m').center(100,' '))

    #fin de la funcion
    input ('\33[;40;37mpulse una tecla\33[;0m')

def salir():
    salir = input ('\33[;31;47m' + 'Va a salir del programa. ¿Está seguro? s/n \n' + '\33[;0m')
    if salir == 's':
        print ('Adios')
        exit()
    else:
        print ('Continuamos')

    #fin de la funcion
    input ('\33[;40;37mpulse una tecla\33[;0m')