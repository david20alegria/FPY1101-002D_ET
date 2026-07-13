#EXAMEN - DAVID ALEGRIA

diccionario_peliculas =  {
    "P101":["Luz de otoño", "Drama", 110, "B", "Español", False],
    "P102":["Noche neon", "Accion", 125, "C", "Ingles", True],
    "P103":["Planeta agua", "Documental", 90, "A", "Español", False],
    "P104":["Risa total", "Comedia", 105, "A", "Español", True],
    "P105":["Codigo Zero", "Thriller", 118, "C", "Ingles", True],
    "P106":["Viaje lunar", "Ciencia Ficcion", 132, "B", "Ingles", False]

}

diccionario_cartelera = {
    "P101":[5990, 40],
    "P102":[7990, 0],
    "P103":[4990, 25],
    "P104":[6990, 12],
    "P105":[8990, 8],
    "P106":[7490, 3]

}

#---------------------------------------------------------------------------

def validar_numeros_enteros_positivos(mensaje:str) -> int:
    while(True):
        try:
            valor = int(input(mensaje))
            if valor == 0:
                print("El valor debe ser distinto de 0")
            elif valor < 0:
                print("El valor debe ser un NUMERO ENTERO POSITIVO")
            else:
                return valor
        except Exception as e:
            print("Solo se permiten NUMEROS ENTEROS POSITIVOS")

        
def validar_numeros_decimales_positivos(mensaje:str) -> float:
    while(True):
        try:
            valor = float(input(mensaje))
            if valor == 0:
                print("El valor debe ser distinto de 0")
            elif valor < 0:
                print("El valor debe ser un NUMERO ENTERO O DECIMAL POSITIVO")
            else:
                return valor
        except Exception as e:
            print("Solo se permiten NUMEROS ENTEROS O DECIMALES POSITIVOS")


def validar_strings(mensaje:str):
    while(True):
            valor = input(mensaje)
            if len(valor) == 0:
                print("El valor no debe quedar vacio")
            elif len(valor) < 3:
                print("El valor debe contener al menos 3 caracteres")
            else:
                return valor
            
#---------------------------------------------------------------------------

def validar_codigo(mensaje:str):
    while(True):
        valor = input(mensaje)
        if len(valor) == 0:
            print("El valor no debe quedar vacio")
        elif len(valor) != 4:
            print("Los codigos son de 4 caracteres")
        else:
            return valor.upper()
        

def validar_cupos(mensaje:str):
    while(True):
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("El valor debe ser un NUMERO ENTERO POSITIVO")
            else:
                return valor
        except Exception as e:
            print("Solo se permiten NUMEROS ENTEROS POSITIVOS")


def validar_si_es_3d(mensaje:str):
    while(True):
        valor = input(mensaje).upper()
        if valor == "S":
            return True
        elif valor == "N":
            return False
        else:
            print("Solo se permite S o N")


def validar_repetir(mensaje:str):
    while(True):
        valor = input(mensaje).upper()
        if valor == "S":
            return True
        elif valor == "N":
            return False
        else:
            print("Solo se permite S o N")


def validar_clasificacion(mensaje:str):
    while(True):
        valor = input(mensaje).upper()
        if valor != "A" and valor != "B" and valor != "C":
            print("Solo se permiten A / B / C")
        else:
            return valor.upper()

#---------------------------------------------------------------------------

def agregar_pelicula():
    codigo = validar_codigo("Ingrese el codigo de la Pelicula: ")

    if codigo in diccionario_peliculas:
        print("El codigo ingresado ya se encuentra registrado")
    else:
        titulo = validar_strings("Ingrese el Titulo de la Pelicula: ")
        genero = validar_strings("Ingrese el Genero de la Pelicula: ")
        duracion = validar_numeros_enteros_positivos("Ingrese la Duracion de la Pelicula en minutos: ")
        clasificacion = validar_clasificacion("Ingrese la Clasificacion de la Pelicula (A / B / C): ")
        idioma = validar_strings("Ingrese el Idioma de la Pelicula: ")
        es_3d = validar_si_es_3d("¿La Pelicula es en formato 3D? (S/N): ")
        precio = validar_numeros_enteros_positivos("Ingrese el Precio de la Pelicula: ")
        cupos = validar_cupos("Ingrese los Cupos de la Pelicula: ")


        diccionario_peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d]
        diccionario_cartelera[codigo] = [precio, cupos]

        print("Pelicula Agregada Correctamente")

#---------------------------------------------------------------------------

def eliminar_pelicula():
    codigo = validar_codigo("Ingrese el Codigo de la Pelicula a eliminar: ")

    if codigo in diccionario_peliculas:
        diccionario_peliculas.pop(codigo)

        if codigo in diccionario_cartelera:
            diccionario_cartelera.pop(codigo)  

        print("Pelicula Eliminada Correctamente")

    else:
        print("No se encontro el Codigo de la Pelicula a Eliminar")     
        
#---------------------------------------------------------------------------

def buscar_pelicula_por_rango_precio():
    precio_minimo = validar_numeros_enteros_positivos("Ingrese un Precio minimo: ")
    precio_maximo = validar_numeros_enteros_positivos("Ingrese un Precio Maximo: ")

    if precio_minimo > precio_maximo:
        print("El precio minimo no puede ser mayor que el precio maximo")
    else:
        pelicula_encontrada = 0
        for codigo in diccionario_cartelera:
            precio = diccionario_cartelera[codigo][0]

            if precio >= precio_minimo and precio <= precio_maximo:
                titulo = diccionario_peliculas[codigo][0]
                print(f"CODIGO: {codigo} - TITULO: {titulo} - PRECIO: {precio}")

                pelicula_encontrada += 1

        if pelicula_encontrada == 0:
            print("No se encontraron Peliculas con el Rango de Precios ingresados")

#---------------------------------------------------------------------------

def actualizar_precio():
    while(True):
        codigo = validar_codigo("Ingrese el Codigo de la Pelicula a Actualizar: ")
    
        if codigo in diccionario_peliculas:
            precio = validar_numeros_enteros_positivos("Ingrese el Nuevo Precio de la Pelicula: ")
            cupos = diccionario_cartelera[codigo][1]

            diccionario_cartelera[codigo] = [precio, cupos]

            print("Precio de Pelicula Actualizada Correctamente")
            print("")
            respuesta = validar_repetir("¿Desea Actualizar otro precio? (S/N): ")

            if respuesta == True:
                continue
            else:
                break

        else:
            print("No se encontro el Codigo de la Pelicula a Actualizar")
            break

#---------------------------------------------------------------------------

def mostrar_cupos_por_genero():
    genero = validar_strings("Ingrese el Genero a Buscar: ").capitalize()

    pelicula_encontrada = 0
    contador_cupos = 0
    
    for genero in diccionario_peliculas:
        cupos = diccionario_cartelera[genero][1]

        if genero in diccionario_peliculas:
            titulo = diccionario_peliculas[genero][0]
            print(f"GENERO: {diccionario_peliculas[genero][1]} - TITULO: {titulo} - CUPOS: {cupos}")
            pelicula_encontrada += 1
            contador_cupos += cupos

    print("")
    print(f"El total de cupos disponibles es de: {contador_cupos}")

    if pelicula_encontrada == 0:
        print("No existen Peliculas con el Genero Ingresado")


# No logre hacer que solo identificara los del genero Ingresado
# Logre hacer que se sumaran todos los cupos de toda la cartelera

#---------------------------------------------------------------------------

def menu():
    while(True):
        print("")
        print("---------- MENU ----------")
        print("")
        print("(1) - Cupos por Genero")
        print("(2) - Busqueda de Peliculas por Rango de Precio")
        print("(3) - Actualizar Precio Pelicula")
        print("(4) - Agregar Pelicula")
        print("(5) - Eliminar Pelicula")
        print("(6) - Salir")
        print("")


        opc = validar_numeros_enteros_positivos("Ingrese una opcion: ")


        if opc == 1:
            print("- OPCION 1 -")
            print("- CUPOS POR GENERO -")
            print("")
            mostrar_cupos_por_genero()


        elif opc == 2:
            print("- OPCION 2 -")
            print("- BUSQUEDA DE PELICULAS POR RANGO DE PRECIO -")
            print("")
            buscar_pelicula_por_rango_precio()


        elif opc == 3:
            print("- OPCION 3 -")
            print("- ACTUALIZAR PRECIO PELICULA -")
            print("")
            actualizar_precio()



        elif opc == 4:
            print("- OPCION 4 -")
            print("- AGREGAR PELICULA -")
            print("")
            agregar_pelicula()


        elif opc == 5:
            print("- OPCION 5 -")
            print("- ELIMINAR PELICULA -")
            print("")
            eliminar_pelicula()


        elif opc == 6:
            print("- OPCION 6 -")
            print("- SALIR -")
            print("")
            print("Finalizando Programa...")
            break

        else:
            print("Opcion no Valida")
            print("Intente Nuevamente")

    
menu()