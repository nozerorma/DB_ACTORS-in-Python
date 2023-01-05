# Realice el ejercicio dentro del cuadro a continuación de esta línea 

# Os dejo un ejemplo de inicialización de la base de datos para que veáis la estructura (vuestra base de datos inicialmente estará vacía).
#BBDD_actores = {
#    'Keanu Reeves' : {
#        'año' : 1964, 
#        'sexo' : 'masculino', 
#        'peliculas' : ['Speed', 'The Matrix', 'Constantine']
#    }
#}

# Pseudo first approach
 
# 1)  First dict. k:actor name

# First dict

#this is a try of how git on android looks like
#second try
#thirdiesss
import re

'''
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
'''
    
BBDD_actores = {
    'Actor One' : {
        'año' : 2020,
        'sexo' : 'masculino',
        'peliculas' : ['Película 1', 'Película 2', 'Película 3']
    },
    'Actor Two' : {
        'año' : 2022,
        'sexo' : 'femenino',
        'peliculas' : ['Película 4', 'Película 5', 'Película 6']
    }
}
# CSV FORMAT: 
# Actor One; 2020; Masculino; Película 1; Película 2; Película 3

# #2)  Second dict (embeded) three keys
#         a)  Date of birth yyyy
#         b)  Sex
#         c)  [Films in which he has appeared]

# 3)  Crear un menú que permita:
print('Base de datos de Actores')
print('por Miguel Ramón Alonso\n')

print('Opciones:')
print('1) Inserta una nueva entrada')
print('2) Lista el nombre de los actores presentes en la BBDD')
print('3) Muestra los datos de un actor determinado')
print('4) Muestra el nombre de aquellos actores nacidos en un rango de años especificado')
print('5) Muestra aquellos actores del sexo especificado')
print('6) Muestra aquellos actores que hayan aparecido en una película determinada')
print('\n0) Sal del programa\n')

while True:
    

    opcion = int(input('¿Qué deseas hacer? '))
    if opcion == 0:
        fichero = ('BBDD_actores.txt', 'w')
        for actor in BBDD_actores.txt:
            actor_guardado = actor
            # skip until further understanding BANG BANG BANG!!!

#    1)  Insertar nuevo actor
#       -   Si existe, se sobreescribirá
    elif opcion == 1:
        # recogida de datos
        nombre_actor = input('Nombre del actor/actriz: ')
        año_actor = int(input('Año de nacimiento (yyyy): '))
        sexo_actor = input('Sexo del actor/actriz (H/M): ')
        l_peliculas = []
        # gotta make this last as list so can append
        while True :
            peliculas_actor = input('Inserte una película. Si desea continuar añadiendo películas, pulse Enter. \
En caso contrario, por favor, pulse 0.\n')
            if peliculas_actor == '0': # cambiar esto por logica escape
                break
            else:
                l_peliculas.append(peliculas_actor)
                print(l_peliculas)
                continue
        # creo un diccionario
        dict_actor = {
            nombre_actor : {
                'año' : año_actor,
                'sexo' : sexo_actor,
                'peliculas' : l_peliculas   
            } 
        }
        # añadir diccionario a BD_actor
        BBDD_actores.update(dict_actor)

#    2)  Listar nombre (solo) actores. Formateado.
    elif opcion == 2: 
        l_actores = list(BBDD_actores.keys())     
        """
        or we could create an empty list
        l_actores = []
        for actor in l_actores:
            l_actores.append(actor)
        """   
        print(l_actores)
#    3)  Datos de actor dtdo. Formateado.
    elif opcion == 3 :
        # pedir al usuario un actor
        while True:
            req_actor = input("¿Qué actor quieres buscar? ")
            # caso de no encontrar el actor en la base de datos (check keys????? PVAJJHAVLSJKH)
            if req_actor not in BBDD_actores :
                print("No se ha encontrado al actor, inserta otro.")
                continue
            else:
                # para dicho actor, mostrar todos sus pares key-val
                for req_actor 
                print()

                """outer_dict = {'dict1': {'a': 1, 'b': 2}, 'dict2': {'c': 3, 'd': 4}, 'dict3': {'e': 5, 'f': 6}}

string = input("Enter a string: ")

if string in outer_dict:
    inner_dict = outer_dict[string]
    for key, value in inner_dict.items():
        print(f"{key}: {value}")
else:
    print(f"The string '{string}' is not present in the dictionary. Please input another one.")
"""
#    4)  Actores en rango años (userinput)
#    5)  Actores determinado sexo
#    6)  Actores que hayan participado en x película
#    0)  Salir del programa

"""

# Access sample: print(BBDD_actores['Actor One']['año'])
      

Dict inside dict access
my_nested_dictionary = {'mydict': {'A': 'Letter A', 'B': 'Letter C', 'C': 'Letter C'}}
print(my_nested_dictionary['mydict']['A'])'''

"""