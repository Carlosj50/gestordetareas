#lista de tareas
tareas = ['tarea 1','tarea 2','tarea 3','tarea 4','tarea 5','tarea 6']


def agregar_tareas(lista):
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

def ver_tareas(lista):
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


def completar_tareas(lista):
    # llamamos a la funcion ver_tareas()
    ver_tareas(lista)
    # Entrada para que el usuario introduzca una tarea
    completada = int(input('Introduzca el número de la tarea que ha sido completada:\n'))
    # condicional para marcar como tarea finalizada.
    if completada > 0 and completada <= len(lista):
        #si la tarea esta finalizada
        indice = completada-1
        if 'Completada' in lista[indice]:
            print ('Esa tarea ya fue completada')
        #si no esta finalizada
        else:
            indice = completada-1
            lista[indice] = lista[indice] + ' - (Completada)'
            
    # Avisar si la opcion es incorrecta.
    else:
        print ('No hay ninguna tarea con ese número')


def eliminar_tarea(lista):
    # llamamos a la funcion ver_tareas()
    ver_tareas(lista)
    # Entrada para que el usuario introduzca una tarea
    eliminar = int(input('Introduzca el número de la tarea que quiere eliminar:\n'))
    # condicional para marcar como tarea finalizada.
    if eliminar > 0 and eliminar <= len(lista):
        #se elimina la tarea indicada.
        indice = eliminar - 1
        tarea_eliminada = lista[indice]
        del lista[indice]  
        print (f'La tarea {tarea_eliminada} fue eliminada con exito')
    # Avisar si la opcion es incorrecta.
    else:
        print ('No hay ninguna tarea con ese número')


def salir():
    salir = input ('\33[;31;47m' + 'Va a salir del programa. ¿Está seguro? s/n \n' + '\33[;0m')
    if salir == 's':
        print ('Adios')
        exit()
    else:
        print ('Continuamos')

    #fin de la funcion
    input ('\33[;40;37mpulse una tecla\33[;0m')