## Notas: iba a intentar hacer búsquedas insensitivas dentro de los diccionarios,
## para buscar sobretodo actores, pero creo que no merece la pena codificarlo viendo
## que hay módulos (CaseInsensitiveDict) que hacen esto mismo, lo cual ya se sale del
## scope del trabajo.
### Idem con búsqueda de actores por contexto ("Cruz" buscaría todo actor presente
### cuyo apellido sea "Cruz"

BBDD_actores = {}

fichero = "BBDD_actores.txt"
# Creación/comprobación existencia de fichero para DB
# Operador *with* permite abrir archivo y cerrar a final de bloque sin necesidad de close()
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
        # Especificar separación campo películas
        # separado con "" ya que ciertas películas pueden contener , en su interior
        # no se debe usar ";" ya que es separador general de campo
        peliculas = datos[3].split(", ")
        # Quitar dobles comillas
        peliculas = [pelicula.strip('"') for pelicula in peliculas]
        datos_actores = {
            datos[0]: {
                "birthday": datos[1],
                "sexo": datos[2],
                "peliculas": peliculas
            }
        }

        BBDD_actores.update(datos_actores)

# Funciones

# Presentación del menú de inicio
def menu_inicio():
    print("Base de datos de Actores para módulo de Pyhton\n\
del Máster de Bioinformática 2022/23.")
    print("\npor Miguel Ramón Alonso\n")

    print("Opciones:")
    print("1) Insertar una nueva entrada")
    print("2) Listar el nombre de los actores presentes en la BBDD")
    print("3) Mostrar los datos de un actor determinado")
    print("4) Mostrar el nombre de aquellos actores nacidos en un rango de años específico")
    print("5) Mostrar aquellos actores de un sexo específico")
    print("6) Mostrar aquellos actores que hayan aparecido en una película determinada")
    print("7) Borrar una entrada de la BBDD")
    print("8) Mostrar la BBDD")
    print("\n10) Volver a mostrar este menú")
    print("\n0) Salir del programa\n")
    
# Comprobación de entrada como *Int*
def es_int(mensaje):
    try:
        ret_opcion = int(input(mensaje))
        return ret_opcion
    except:
        print("Inserte una opción válida ")
        return es_int(mensaje)  

# Formatear películas entre comillas y separadas por comas para su visualización y guardado
## Actor inicializado como parámetro, devuelto por las funciones correspondientes
def l_peliculas_comillado(actor):
    # Uso de lista de comprehensión
    # formato : obj = [{operacion con entrada n} for n in {python iterable}]
    ### En este caso {operacion con entrada n}: "película" como str entrecomillado
    ### luego listado de todas las películas, y luego separado por ", "
    peliculas = ", ".join([f'"{pelicula}"' for pelicula in BBDD_actores[actor]["peliculas"]])
    # Devulevo "Película 1", "Película 2", "etc"
    return peliculas
            
# Insertar entrada y guardar en fichero
def insertar_entrada():
# Recogida de datos
    nombre_actor = input("Nombre del actor/actriz: ")
    # Inicialización de variable tipo Int
    birthday_actor = 0
    # Comprobación edad en rango deseado
    while (birthday_actor < 1900 or birthday_actor > 2023):
        birthday_actor = es_int("Año de nacimiento: ")
        if birthday_actor < 1900 or birthday_actor > 2023:
            print("\nInserte un rango de edades válido (entre 1900 y 2023)")
    sexo_actor = input("Sexo (M/F): ")
    # Inicializo lista vacía para almacenar peliculas
    peliculas_actor = []
    while True:
        pelicula = input("Inserte una película. Inserte un 0 para salir: ")
        # Si no más películas, mostrar películas insertadas
        if pelicula == "0":
            print("\tPelículas introducidas: ", '; '.join(peliculas_actor))
            break
        else:
            peliculas_actor.append(pelicula)
            continue          
    # Añadir a BBDD_actores
    BBDD_actores[nombre_actor] = {
        "birthday": birthday_actor,
        "sexo": sexo_actor,
        "peliculas": peliculas_actor
    }
    # Añadir a fichero BBDD_actores.txt en formato pseudoCSV (películas separadas
    # de acuerdo al formato descrito en l_peliculas_comillado)
    with open(fichero, "w") as f:
        for actor in BBDD_actores:
            peliculas = l_peliculas_comillado(actor)
            # Todo debe tener la misma clase para ser concatenado
            f.write(actor + ";" + str(BBDD_actores[actor]["birthday"]) +\
";" + BBDD_actores[actor]["sexo"] + ";" + peliculas)
            f.write("\n")

# Listado simple de actores
def listar_actores(mensaje):
    print(f"\n{mensaje}")
    for actor in BBDD_actores:
        print(actor)

# Función general de muestra de BBDD
## Actor inicializado como parámetro a recibir/devolver 
## de/a funciones correspondientes/anidadas
def mostrar_BBDD(actor):
    print(f"\n\tNombre: {actor}")
    print(f"\tAño de nacimiento: {BBDD_actores[actor]['birthday']}")
    print(f"\tSexo: {BBDD_actores[actor]['sexo']}")
    print(f"\tPelículas: {l_peliculas_comillado(actor)}")


# Subfunción muestra de actores individuales
## Actor como parámetro a devolver a funciones anidadas
def mostrar_datos_actor():
    actor = input("¿De qué actor desea ver los datos? ")
    if actor in BBDD_actores:
        mostrar_BBDD(actor) 
    else:
        print(f"\n\tEl actor {actor} no se encuentra en la base de datos")    
                    
# Búsqueda parametrizada de actores
def mostrar_actores_param(keyword,mensaje,mensaje2,param_buscado):
    l_actores = []
    # Separamos la edad del resto de parámetros
    if keyword != "birthday":
        param_buscado = input(mensaje) 
        for actor, d_actor in BBDD_actores.items():
        # No muy lógico, demasiado explícito?    
            # Búsqueda por sexo
            if d_actor[keyword] == param_buscado:
                l_actores.append(actor)
            # Búsqueda por película
            elif param_buscado in d_actor[keyword]:
                l_actores.append(actor)
        if len(l_actores) > 0:
            print(f"\n{mensaje2} {param_buscado}: {', '.join(l_actores)}")
        else:
            print(f"\nNo existen actores con los parámetros especificados.")
    # Especificamos para rango de edades
    else:
        print(mensaje)
        # Inicialización variables edad tipo Int
        edad_min = 0
        edad_max = 0
        # Si rango de edad fuera del deseado, vuelvo a pedir datos
        while (edad_min < 1900 or edad_max > 2023):
            edad_min = es_int("\nIngrese el año mínimo: ")
            edad_max = es_int("Ingrese el año máximo: ")
            if edad_min < 1900 or edad_max > 2023:
                print("\nInserte un rango de edades válido (entre 1900 y 2023)")
        # Añado a lista y muestro en consola
        for actor, d_actor in BBDD_actores.items():
            if edad_min <= int(d_actor[keyword]) <= edad_max:
                l_actores.append(actor)  
        if len(l_actores) > 0:
            print(f"\n{mensaje2} {edad_min}-{edad_max}: {', '.join(l_actores)}")
        else:
            print(f"\nNo existen actores dentro del rango de edad especificado.")
            
def borrar_entrada():
    actor_borrar = input("Nombre del actor cuya entrada desea eliminar: ")
    if actor_borrar in BBDD_actores:
        BBDD_actores.pop(actor_borrar)
        with open(fichero, "r+") as f:
            # Creo una lista con las líneas del archivo que no corresponden al actor borrado
            ## lista de comprehension
            fichero_temporal = [line for line in f if actor_borrar not in line]
            # Muevo el puntero al principio del archivo
            f.seek(0)
            # Sobrescribo el archivo con el nuevo contenido
            f.writelines(fichero_temporal)
            f.truncate()
            print(f"\nLa entrada de {actor_borrar} ha sido eliminada de la base de datos.")
    else:
        print("\nNo existe ninguna entrada con el nombre especificado.")
            
# Programa

# Muestra menú de forma que no se cierre hasta que se lo pida
menu_inicio()

while True:
    # Elección de opciones, solo aceptará INT
    opcion = es_int("\n¿Qué deseas hacer? ")
    
    # op0: Salir
    if opcion == 0:
        print("Cerrando la base de datos...")
        break
    
    # op 1: Insertar nuevo valor en BBDD_actores y guarda en fichero
    elif opcion == 1:
        insertar_entrada()

    # op2: Listar actores
    elif opcion == 2: 
        listar_actores("Actores presentes en la base de datos: \n")
        
    # op3: Mostrar datos actor
    elif opcion == 3:
        mostrar_datos_actor()
        
    # op4: Mostrar actores por rango de años
    elif opcion == 4:
        mostrar_actores_param("birthday","¿De que rango de edad desea ver los actores? ",\
"Actores en el rango de edad",opcion)
        
    # op5: Mostrar actores por sexo
    elif opcion == 5:
        # Inicializar variable param_buscado sin tipo en particular
        param_buscado = None
        mostrar_actores_param("sexo","¿De qué sexo desea ver los actores? (M/F) ",\
"Actores del sexo",param_buscado)
        
    # op6: Mostrar actores por película
    elif opcion == 6:
        # Inicializar variable param_buscado sin tipo en particular
        param_buscado = None
        mostrar_actores_param("peliculas","¿De qué película desea ver los actores? ",\
"Actores presentes en el reparto de",param_buscado )
        
    # op7: Borrar entrada. No pedido pero util
    elif opcion == 7:
        borrar_entrada()
        
    #op8: Mostrar base de datos formateada
    # Función no necesaria debido a la simplicidad del código y su no reutilización
    elif opcion == 8:
        # Primera entrada = 1
        count = 1
        for actor in BBDD_actores:
            print(f"\nEntrada número {count}")
            mostrar_BBDD(actor)
            # Tantas entradas como actores en BBDD
            count += 1
    
    # Vuelve a mostrar el menú de inicio
    elif opcion == 10:
        menu_inicio()
        
    # Caso entrada INT pero no válida
    else:
        print("La opción indicada no se encuentra en el menú.")  
    