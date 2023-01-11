BBDD_actores = {}
fichero = "BBDD_actores.txt"
# creación/comprobación existencia de fichero para DB
# operador with permite abrir archivo y cerrar a final de bloque
try:
    with open(fichero,"r") as f:
        ...
except FileNotFoundError:
    with open(fichero,"w") as f:
        print("No existe el fichero BBDD_actores.txt. Creando...\n")

with open(fichero,"r") as f:
    for linea in f:
        linea = linea.strip()
        datos = linea.split(";")
        actor_dict = datos[0]
        datos_actores = {
            datos[0]: {
                "birthday": datos[1],
                "sexo": datos[2],
                "peliculas": datos[3]
            }
        }

        BBDD_actores.update(datos_actores)

def menu_inicio():
    print("Base de datos de Actores")
    print("por Miguel Ramón Alonso\n")

    print("Opciones:")
    print("1) Inserta una nueva entrada")
    print("2) Lista el nombre de los actores presentes en la BBDD")
    print("3) Muestra los datos de un actor determinado")
    print("4) Muestra el nombre de aquellos actores nacidos en un rango de años especificado")
    print("5) Muestra aquellos actores del sexo especificado")
    print("6) Muestra aquellos actores que hayan aparecido en una película determinada")
    print("7) Borrar una entrada de la BBDD")
    print("8) Muestra la BBDD")
    print("\n0) Sal del programa\n")
    
# Funciones
# F) Comprobación de entrada como INT
def es_int(mensaje):
    try:
        ret_opcion = int(input(mensaje))
        return ret_opcion
    except:
        print("Inserta una opción válida ")
        return es_int(mensaje)  
    
# Insertar entrada y guardar en fichero
def insertar_entrada():
    # Recogida de datos
    nombre_actor = input("Nombre del actor/actriz: ")
    birthday_actor = es_int("Año de nacimiento: ")
    sexo_actor = input("Sexo (M/F): ")
    # Guardo en un conjunto para no tener repeticiones
    l_peliculas = []
    while True:
        peliculas_actor = input("Inserte una película. Inserte un 0 para salir: ")
        if peliculas_actor == "0":
            print("\tPelículas introducidas: ", ', '.join(l_peliculas))
            break
        else:
            l_peliculas.append(peliculas_actor)
            continue          
    # Añadir a BBDD_actores
    BBDD_actores[nombre_actor] = {
        "birthday": birthday_actor,
        "sexo": sexo_actor,
        "peliculas": l_peliculas
    }
    # Añadir a fichero BBDD_actores.txt
    with open(fichero, "w") as f:
        for actor in BBDD_actores:
            # guardo en fichero en formato pseudo-CSV (películas separadas por ,)
            f.write(actor + ";" + str(BBDD_actores[actor]['birthday']) + ";" \
+ BBDD_actores[actor]['sexo'] + ";" + ", ".join(BBDD_actores[actor]['peliculas']))
            f.write("\n")

# Listado actores
def listar_actores(mensaje):
    print(f"\n{mensaje}")
    for actor in BBDD_actores:
        print(actor)

# Función general BBDD
def mostrar_BBDD(actor):
    print(f"\n\tNombre: {actor}")
    print(f"\tAño de nacimiento: {BBDD_actores[actor]['birthday']}")
    print(f"\tSexo: {BBDD_actores[actor]['sexo']}")
    print(f"\tPelículas: {BBDD_actores[actor]['peliculas']}")      

# Subfunción muestra de actores individuales
def mostrar_datos_actor():
    actor = input("¿De qué actor deseas ver los datos? ")
    if actor in BBDD_actores:
        mostrar_BBDD(actor) 
    else:
        print(f"\n\tEl actor {actor} no se encuentra en la base de datos")    
                    
# Mostrar actores en función del parámetro seleccionado
def mostrar_actores_param(keyword,mensaje,mensaje2,param_buscado):
    l_actores = []
    # separamos la edad del resto de parámetros
    if keyword != "birthday":
        param_buscado = input(mensaje)
        for actor, d_actor in BBDD_actores.items():
            # sexo
            if d_actor[keyword] == param_buscado:
                l_actores.append(actor)
            # pelicula
            elif param_buscado in d_actor[keyword]:
                l_actores.append(actor)
        if len(l_actores) > 0:
            print(f"\n{mensaje2} {param_buscado}: {', '.join(l_actores)}")
        else:
            print(f"\nNo existen actores con los parámetros especificados.")
    # especificamos para rango de edades
    else:
        print(mensaje)
        edad_min = 0
        edad_max = 0
        # si rango de edad fuera del especifico, vuelvo a pedir datos
        while (edad_min < 1900 or edad_max > 2023):
            edad_min = es_int("\nIngrese el año mínimo: ")
            edad_max = es_int("Ingrese el año máximo: ")
            if edad_min < 1900 or edad_max > 2023:
                print("\nInserta un rango de edades válido (entre 1900 y 2023)")
        # añado a lista y muestro en consola
        for actor, d_actor in BBDD_actores.items():
            if edad_min <= int(d_actor[keyword]) <= edad_max:
                l_actores.append(actor)  
        if len(l_actores) > 0:
            print(f"\n{mensaje2} {edad_min}-{edad_max}: {', '.join(l_actores)}")
        else:
            print(f"\nNo existen actores dentro del rango de edad especificado.")
            
def borrar_entrada():
    actor_borrar = input("Nombre del actor a borrar: ")
    if actor_borrar in BBDD_actores:
        BBDD_actores.pop(actor_borrar)
        with open(fichero, "r+") as f:
            # Creo una lista con las líneas del archivo que no corresponden al actor borrado
            # lista de comprehension
            fichero_temporal = [line for line in f if actor_borrar not in line]
            # Muevo el puntero al principio del archivo
            f.seek(0)
            # Sobrescribo el archivo con el nuevo contenido
            f.writelines(fichero_temporal)
            f.truncate()
    print(f"\nLa entrada de {actor_borrar} ha sido eliminada de la base de datos.")
            
# Programa

# muestra menú
menu_inicio()
# De manera que el menú no cierre hasta que se lo pida
while True:
    # Elección de opciones, solo aceptará INT
    opcion = es_int("\n¿Qué deseas hacer? ")
    
    # op0: Salir
    if opcion == 0:
        print("Cerrando programa...")
        break
    
    # op 1: insertar nuevo valor en BBDD_actores y guarda en fichero
    elif opcion == 1:
        insertar_entrada()

    # op2: listar actores
    elif opcion == 2: 
        listar_actores("Actores presentes en la base de datos: \n")
        
    # op3: mostrar datos actor
    elif opcion == 3:
        mostrar_datos_actor()
        
    # op4: mostrar actores por rango de años
    elif opcion == 4:
        mostrar_actores_param("birthday","¿De que rango de edad deseas ver los actores? ", \
"Actores en el rango de edad",opcion)
        
    # op5: mostrar actores por sexo
    elif opcion == 5:
        # Inicializar variable param_buscado
        param_buscado = None
        mostrar_actores_param("sexo","¿De qué sexo deseas ver los actores? (M/F) ", \
"Actores del sexo",param_buscado)
        
    # op6: mostrar actores por película
    elif opcion == 6:
        # Inicializar variable param_buscado
        param_buscado = None
        mostrar_actores_param("peliculas","¿De qué película deseas ver los actores? ", \
"Actores presentes en el reparto de",param_buscado )
        
    # op7: borrar entrada? No pedido pero util
    elif opcion == 7:
        borrar_entrada()
        
    #op8: mostrar base de datos formateada
    elif opcion == 8:
        count = 1
        for actor in BBDD_actores:
            print(f"\nEntrada número {count}")
            mostrar_BBDD(actor)
            count += 1
    
    # Caso entrada INT pero no válida
    else:
        print("La opción indicada no se encuentra en el menú.")  
    