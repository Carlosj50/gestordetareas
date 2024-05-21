#lista de tareas
tareas = []


def agregar_tareas(lista):
    print ('\33[;30;47m' + 'agregar')
    input ('\33[;40;37m' + 'pulse una tecla' + '\33[;0m')

def ver_tareas(lista):
    print ('ver')
    input ('pulse una tecla')

def completar_tareas(lista):
    print ('completar')
    input ('pulse una tecla')

def eliminar_tarea(lista):
    print ('eliminar')
    input ('pulse una tecla')

def salir():
    salir = input ('\33[;31;47m' + 'Va a salir del programa. ¿Está seguro? s/n \n' + '\33[;0m')
    if salir == 's':
        print ('Adios')
        exit()
    else:
        print ('Continuamos')
        input ('pulse una tecla')
        