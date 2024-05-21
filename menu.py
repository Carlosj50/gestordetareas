
def titulo():
    titulo = 'GESTOR DE TAREAS'
    global separadores
    separadores = '*'
    print (('\033[1;32m' + separadores * 27 + '\33[;0m').center(100,' '))
    print (('\033[1;32m' + separadores + '   \033[1;31m ' + titulo + '    \033[1;32m '+ separadores + '\33[;0m').center(113,' '))
    print (('\033[1;32m' + separadores * 27 + '\33[;0m').center(100,' '))

def menu():
    menus = ('Añadir tareas','Ver tareas','Completar tarea','Eliminar tarea','Salir del programa')
    print (('\033[1;35m' + separadores* 27).center(93,' ')) 
    print ((f'\033[1;35m {separadores}\033[1;34m  1. {menus[0]}\033[1;35m       {separadores}').center(107,' '))
    print ((f'\033[1;35m {separadores}\033[1;34m  2. {menus[1]}\033[1;35m          {separadores}').center(107,' '))
    print ((f'\033[1;35m {separadores}\033[1;34m  3. {menus[2]}\033[1;35m     {separadores}').center(107,' '))
    print ((f'\033[1;35m {separadores}\033[1;34m  4. {menus[3]}\033[1;35m      {separadores}').center(107,' '))
    print ((f'\033[1;35m {separadores}\033[1;34m  5. {menus[4]}\033[1;35m  {separadores}').center(107,' '))
    print (('\033[1;35m      ' + separadores * 27 + '\33[;0m').center(93,' ')) 

