
def titulo():
    titulo = 'GESTOR DE TAREAS'
    global separadores
    separadores = '*'
    print ((separadores * 27).center(100,' '))
    print ((separadores + '    ' + titulo + '     '+ separadores).center(100,' '))
    print ((separadores * 27).center(100,' '))

def menu():
    menus = ('Añadir tareas','Ver tareas','Completar tarea','Eliminar tarea','Salir del programa')
    print ((separadores * 27).center(100,' ')) 
    print ((f'{separadores}  1. {menus[0]}       {separadores}').center(100,' '))
    print ((f'{separadores}  2. {menus[1]}          {separadores}').center(100,' '))
    print ((f'{separadores}  3. {menus[2]}     {separadores}').center(100,' '))
    print ((f'{separadores}  4. {menus[3]}      {separadores}').center(100,' '))
    print ((f'{separadores}  5. {menus[4]}  {separadores}').center(100,' '))
    print ((separadores * 27).center(100,' ')) 





