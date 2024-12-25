import pymysql
from pymysql.err import OperationalError, MySQLError

# R E A L I Z A D O  P O R  A R M A N D O  G A R C Í A

def main():
    conexion = None
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        print(" ")

        if opcion == "1":
            conexion = conexionbdd()
        elif opcion == "2":
            if conexion:
                insertar_registros(conexion)
        elif opcion == "3":
            if conexion:
                actualizar_registros(conexion)
        elif opcion == "4":
            if conexion:
                borrar_registros(conexion)
        elif opcion == "5":
            if conexion:
                menuLike(conexion)
        elif opcion == "6":
            if conexion:
                menuJoin(conexion)
        elif opcion == "7":
            if conexion:
                menuGroupBy(conexion)
        elif opcion == "8":
            if conexion:
                conexion.close()
                print("¡Hasta luego! La conexión ha sido cerrada.")
            break
        else:
            print("")
            print("La opción que has indicado no es correcta. Intentalo de nuevo.")


# Función que muestra el menú que verá el usuario en cuestión.

def mostrar_menu():
    print(" ")
    print("Seleccione una opción:")
    print("1. Conectarte a la base de datos BingeBox DB")
    print("2. Insertar registros en una tabla")
    print("3. Actualizar registros en una tabla")
    print("4. Eliminar registros en una tabla")
    print("5. Realización de LIKES")
    print("6. Realización de JOINS")
    print("7. Realización de GROUP BY")
    print("8. Salir")

# Función que muestra el menú de elección de LIKE.

def menuLike(conexion):
    print(" ")
    print("Seleccione el LIKE que quiera")
    print("1. Mostrará los directores con nacionalidad estadounidense.")
    print("2. Series con x número de temporadas")
    print("3. Películas con el rating determinado")
    print("4. Series con el país de origen determinado")
    print("5. Volver al menú principal.")
    
    opcionMenuJoin = input("Ingrese una opción: ")
    
    if opcionMenuJoin == "1":
        primerLike(conexion)
    elif opcionMenuJoin == "2":
        segundoLike(conexion)
    elif opcionMenuJoin == "3":
        tercerLike(conexion)
    elif opcionMenuJoin == "4":
        cuartoLike(conexion)
    elif opcionMenuJoin == "5":
        print("Volviendo al menú principal...")
    else:
        print("Opción no válida. Intenta nuevamente.")

# Función que muestra el menú de elección de JOIN.

def menuJoin(conexion):
    print(" ")
    print("Seleccione el JOIN que quiera")
    print("1. Mostrar las series, capitulos, temporadas y directores de todas las series")
    print("2. Mostrar el título de la película, los actores en ella y los papeles que desempeñan")
    print("3. Mostrar la serie, el creador de esta y la nacionalidad de este.")
    print("4. Mostrar la serie, el ID de la temporada y el titulo de los capitulos.")
    print("5. Volver al menú principal.")
    
    opcionMenuJoin = input("Ingrese una opción: ")
    
    if opcionMenuJoin == "1":
        primerJoin(conexion)
    elif opcionMenuJoin == "2":
        segundoJoin(conexion)
    elif opcionMenuJoin == "3":
        tercerJoin(conexion)
    elif opcionMenuJoin == "4":
        cuartoJoin(conexion)
    elif opcionMenuJoin == "5":
        print("Volviendo al menú principal...")
    else:
        print("Opción no válida. Intenta nuevamente.")

# Función que muestra el menú de elección de GROUP BY.

def menuGroupBy(conexion):
    print(" ")
    print("Seleccione el GROUP BY que quiera")
    print("1. Cuantas películas hay por cada género")
    print("2. Cuantos directores hay de cada género")
    print("3. Cuantos actores hay de cada nacionalidad")
    print("4. Cuantas series hay de cada país")
    print("5. Volver al menú principal.")
    
    opcionMenuJoin = input("Ingrese una opción: ")
    
    if opcionMenuJoin == "1":
        primerGroupBy(conexion)
    elif opcionMenuJoin == "2":
        segundoGroupBy(conexion)
    elif opcionMenuJoin == "3":
        tercerGroupBy(conexion)
    elif opcionMenuJoin == "4":
        cuartoGroupBy(conexion)
    elif opcionMenuJoin == "5":
        print("Volviendo al menú principal...")
    else:
        print("Opción no válida. Intenta nuevamente.")

# Funcion para realizar la conexión a nuestra base de datos

def conexionbdd():
    try:
        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            database='bdpeliculasyseries'
        )
        print("Te has conectado exitosamente a la base de datos BingeBox DB")
        return conexion
    except OperationalError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Funcion para realizar la inserción de registros en cualquier tabla de nuestra base de datos.

def insertar_registros(conexion):
    try:
        cursor = conexion.cursor()
        
        # Solicitamos que el usuario en cuestión nos introduzca el nombre de la tabla que quiera.
        tablaIndicada = input("¿En qué tabla deseas insertar valores?: ")
        
        # Ahora, solicitamos el nombre de las columnas, separados estos por comas, mediante el método split.
        columnasIndicadas = input(f"A continuación introduce el nombre de las columnas de {tablaIndicada}, siendo estos separados por comas: ")
        listaColumnas = columnasIndicadas.split(",")
        
        # Solicitamos los valores para las columnas correspondientes
        valores = []
        for columna in listaColumnas:
            valor = input(f"Introduce el valor para {columna.strip()}: ")
            valores.append(valor)
        
        # Realizamos la consulta en cuestión.
        columnasIntroducidas = ", ".join(listaColumnas)
        placeholders = ", ".join(["%s"] * len(listaColumnas))
        consultaInsert = f"INSERT INTO {tablaIndicada} ({columnasIntroducidas}) VALUES ({placeholders})"
        
        # Ejecutamos la consulta correspondiente, en este caso Insert.
        cursor.execute(consultaInsert, valores)
        conexion.commit()
        print("Registro insertado correctamente en la base de datos BingeBoxDB.")
        
    except MySQLError as e:
        print(f"Error al insertar registros: {e}")

# Función para actualizar registros de una tabla.

def actualizar_registros(conexion):
    try:
        cursorUpdate = conexion.cursor()

        tablaIndicada = input("¿En qué tabla deseas actualizar registros? ").strip()

        columnas = input(f"¿Cuáles son los nombres de las columnas de la tabla: {tablaIndicada}? (Separalos por comas) (Ej: nombre, nacionalidad, genero): ").strip().split(',')
        valores = input(f"¿Cuáles son los valores correspondientes para las columnas (Separalos por comas)? (Ej: Rowan, Británico, Masculino): ").strip().split(',')

        # Si se introducen mal las columnas y los valores saltará esto por consola.
        
        if len(columnas) != len(valores):
            print("El número de columnas y valores no coincide.")
            return

        actualizacionDeLosRegistros = ', '.join([f"{col.strip()}=%s" for col in columnas])
        valores_tupla = tuple(val.strip() for val in valores)

        condicionColumna = input(f"Introduzca el nombre de la columna en cuestión para la condición de la consulta UPDATE. (Ej: ID): ").strip()

        valordecondicionColumna = input(f"Introduzca el valor de la condición en cuestión para la condición de la consulta UPDATE. (Ej: 7): ").strip()

        # Se realiza el UPDATE.
        consultaUpdate = f"UPDATE {tablaIndicada} SET {actualizacionDeLosRegistros} WHERE {condicionColumna}=%s"

        cursorUpdate.execute(consultaUpdate, valores_tupla + (valordecondicionColumna,))
        conexion.commit()

        print('Registros actualizados correctamente.')

    except MySQLError as e:
        print(f"Error al actualizar registros: {e}")

# Función para eliminar registros de una tabla.

def borrar_registros(conexion):
    try:
        cursor = conexion.cursor()

        # Solicitamos que el usuario nos indique el nombre de la tabla en la que desea borrar el registro.
        tablaIndicada = input("¿En qué tabla deseas borrar valores?: ")

        # Solicitamos la condicion que queremos para que se produzca el DELETE.

        condicion = input(f"¿Qué condición (Ej: nombre=nombre) deseas introducir para la eliminación de registros de la tabla: {tablaIndicada} ")

        # Indicamos la consulta en cuestión.

        consultaDelete = f"DELETE FROM {tablaIndicada} WHERE {condicion}"

        # Ejecutamos la consulta.

        cursor.execute(consultaDelete)
        conexion.commit()

        print('Registros eliminados correctamente de la tabla indicada.')

    except MySQLError as e:
        print(f"Error al insertar registros: {e}")

# Función que realiza el primer JOIN sobre las series, las temporadas, los capítulos y sus correspondientes directores

def primerJoin(conexion):
    try:
        cursor = conexion.cursor()
        joinSeriesTemporadasCapitulosDirectores = """
        SELECT series.titulo, temporadas.num_temporada, capitulos.titulo_capitulo, capitulos.director_episodio
        FROM series
        JOIN temporadas ON series.id_serie = temporadas.series_id
        JOIN capitulos ON temporadas.id_temporada = capitulos.temporada_id;
        """
        cursor.execute(joinSeriesTemporadasCapitulosDirectores)
        resultadosPrimerJoin = cursor.fetchall()
        print("")
        for fila in resultadosPrimerJoin:
            print(fila)
        cursor.close()
    except MySQLError as e:
        print(f"Error al ejecutar la consulta: {e}")

# Función que realiza el segundo JOIN, que muestra una lista con el título de la película, el nombre de los actores involucrados y el papel que desempeñaron.

def segundoJoin(conexion):
    try:
        cursor = conexion.cursor()
        joinTituloNombrePapel = """
        SELECT peliculas.titulo, actors.nombre_actor, participacion_actor_pelicula.papel_realiza
        FROM peliculas 
        JOIN participacion_actor_pelicula ON peliculas.id_pelicula = participacion_actor_pelicula.peliculas_id
        JOIN actors ON participacion_actor_pelicula.actors_id = actors.id_actor;
        """
        cursor.execute(joinTituloNombrePapel)
        resultadosSegundoJoin = cursor.fetchall()
        print("")
        for fila in resultadosSegundoJoin:
            print(fila)
        cursor.close()
    except MySQLError as e:
        print(f"Error al ejecutar la consulta: {e}")

# Función que realiza el tercer JOIN, que muestra el titulo de la serie, el creador y su nacionalidad.

def tercerJoin(conexion):
    try:
      cursor = conexion.cursor()
      joinSerieCreadorNacionalidad = """
      SELECT series.titulo, creador_serie.nombre, creador_serie.nacionalidad
      FROM series
      JOIN creacion_series ON series.id_serie = creacion_series.series_id
      JOIN creador_serie ON creacion_series.creador_id = creador_serie.idcreador_serie;    
      """
      cursor.execute(joinSerieCreadorNacionalidad)
      resultadosTercerJoin = cursor.fetchall()
      print("")
      for fila in resultadosTercerJoin:
        print(fila)
      cursor.close()
    except MySQLError as e:
        print(f"Error al ejecutar la consulta: {e}")

# Función que realiza el cuarto y último JOIN, que muestra el titulo de la serie, el ID de la temporada más el titulo de todos los capitulos de la serie.

def cuartoJoin(conexion):
    try:
        cursor = conexion.cursor()
        joinTituloNumeroTituloCapitulos = """
        SELECT series.titulo, temporadas.num_temporada, capitulos.titulo_capitulo
        FROM series
        JOIN temporadas ON series.id_serie = temporadas.series_id
        JOIN capitulos ON temporadas.id_temporada = capitulos.temporada_id;
        """

        cursor.execute(joinTituloNumeroTituloCapitulos)
        resultadosCuartoJoin = cursor.fetchall()
        print("")
        for fila in resultadosCuartoJoin:
            print(fila)
        cursor.close()
    except MySQLError as e:
        print(f"Error al ejecutar la consulta: {e}")

# Función que nos mostrara los directores de nacionalidad Estadounidense

def primerLike(conexion):
    try:
        cursor = conexion.cursor()
        nacionalidadquerida = 'Estadounidense'
        consultaconLike1 = "SELECT * FROM directors WHERE nacionalidad LIKE %s"
        cursor.execute(consultaconLike1, (f"%{nacionalidadquerida}%",))
        resultados = cursor.fetchall()

        print("Directores con la nacionalidad Estadounidense")
        for resultado in resultados:
            print(resultado)
            cursor.close()
    except MySQLError as e:
        print (f"Error al ejecutar la consulta: {e}")

# Función que nos mostrará las series con X número de temporadas

def segundoLike(conexion):
    try:
        cursor = conexion.cursor()
        temporadasIndicadas = '6'   
        consultaconLike2 = "SELECT * FROM series WHERE num_temporadas LIKE %s"
        cursor.execute(consultaconLike2, (f"%{temporadasIndicadas}%",))

        resultados = cursor.fetchall()

        print(f"Series con '{temporadasIndicadas}' temporadas:")
        for resultado in resultados:
            print(resultado)
            cursor.close()
    except MySQLError as e:
        print (f"Error al ejecutar la consulta: {e}")

# Funcion que nos mostrará las películas con el rating determinado

def tercerLike(conexion):
    try:
        cursor = conexion.cursor()
        ratingDeterminado = 'R'
        consultaconLike3 = "SELECT * FROM peliculas WHERE rating LIKE %s"
        cursor.execute(consultaconLike3, (f"%{ratingDeterminado}%",))

        resultados = cursor.fetchall()

        print(f"Películas con rating: '{ratingDeterminado}': ")
        for resultado in resultados:
            print(resultado)
        cursor.close()
    except MySQLError as e:
        print (f"Error al ejecutar la consulta: {e}")

# Función que nos mostrará las series por el país de origen

def cuartoLike(conexion):
    try:
        cursor = conexion.cursor()
        paisDeterminado = 'España'
        consultaconLike4 = "SELECT * FROM series WHERE pais_serie LIKE %s"
        cursor.execute(consultaconLike4, (f"%{paisDeterminado}%",))

        resultados = cursor.fetchall()

        print(f"Series de '{paisDeterminado}' :")
        for resultado in resultados:
            print (resultado)
        cursor.close()
    except MySQLError as e:
        print (f"Error al ejecutar la consulta: {e}")

# F U N C I O N E S  G R O U P   B Y

def primerGroupBy(conexion):

    cursor = conexion.cursor()

    consultaGroupBy1 = """
    SELECT genero, COUNT(*) as num_peliculas
    FROM peliculas
    GROUP BY genero;
    """
    cursor.execute(consultaGroupBy1)
    resultados1 = cursor.fetchall()
    print("Películas agrupadas por género:")
    for fila in resultados1:
        print(f"Género: {fila[0]}, Número de películas: {fila[1]}")
    cursor.close()

def segundoGroupBy(conexion):

    cursor = conexion.cursor()

    consultaGroupBy2 = """
        SELECT genero, COUNT(*) as num_directores
        FROM directors
        GROUP BY genero;
    """
    cursor.execute(consultaGroupBy2)
    resultados2 = cursor.fetchall()
    print("\nDirectores agrupados por género:")
    for fila in resultados2:
        print(f"Género: {fila[0]}, Número de directores: {fila[1]}")

def tercerGroupBy(conexion):

    cursor = conexion.cursor()

    consultaGroupBy3 = """
    SELECT nacionalidad_actor, COUNT(*) as num_actores
    FROM actors
    GROUP BY nacionalidad_actor;
    """
    cursor.execute(consultaGroupBy3)
    resultados3 = cursor.fetchall()
    print("\nActores agrupados por nacionalidad:")
    for fila in resultados3:
        print(f"Nacionalidad: {fila[0]}, Número de actores: {fila[1]}")

def cuartoGroupBy(conexion):

    cursor = conexion.cursor()
    consultaGroupBy4 = """
    SELECT pais_serie, COUNT(*) as num_series
    FROM series
    GROUP BY pais_serie;
    """
    cursor.execute(consultaGroupBy4)
    resultados4 = cursor.fetchall()
    print("\nSeries agrupadas por país:")
    for fila in resultados4:
        print(f"País: {fila[0]}, Número de series: {fila[1]}")


if __name__ == "__main__":
    main()
