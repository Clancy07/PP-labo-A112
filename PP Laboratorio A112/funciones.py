import random


def crear_menu(opciones):
    """
    Crea un menu de opciones con las opciones recibidas y devuelve la opcion elegida por el usuario.

    Args:
        opciones (list): Son las opciones del menu

    Returns:
        char: Es la opcion elegida por el usuario
    """
    for opcion in opciones:
        print(f'{opcion}')

    return input('ingrese una opcion: ')


def verificar_opcion(opcion: str, opciones_validas: list) -> True | False:
    """Recibe por parametros una opcion solicitada y una lista con opcione validas y comprueba que la opcion solicitada este dentro de las validas.

    Args:
        opcion (str): Opcion solicitada.
        opciones_validas (list): Lista de opciones validas

    Returns:
        True | False: Si la opcion solicitada es valida: True | Si la opcion solicitada es invalida: False.
    """
    return opcion in opciones_validas


def get_path_actual(nombre_archivo: str) -> str:
    """Recive el nombre de un archivo y retorna su path

    Args:
        nombre_archivo (str): Nombre del archivo cuyo path se retornara

    Returns:
        str: Path del archivo solicitado
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)


def cargar_peliculas(nombre_archivo: str) -> list:
    """Carga las peliculas de un archivo a una lista de diccionarios

    Args:
        nombre_archivo (str): Nombre del archivo del que se obtendran las peliculas

    Returns:
        list: Lista de diccionarios de peliculas.
    """
    with open(get_path_actual(nombre_archivo), 'r', encoding='utf-8') as archivo:
        peliculas = []

        encabezado = archivo.readline()
        encabezado = encabezado.strip('\n')
        encabezado = encabezado.split(',')

        for linea in archivo.readlines():
            pelicula = {}

            linea = linea.strip('\n')
            linea = linea.split(',')

            id = linea[0]
            titulo = linea[1]
            genero = linea[2]
            rating = linea[3]

            pelicula["id"] = int(id)
            pelicula["titulo"] = titulo
            pelicula["genero"] = genero
            pelicula["rating"] = int(rating)

            peliculas.append(pelicula)

    return peliculas


def mostrar_valores_por_claves(diccionarios: list, claves: list, espaciado: int = 12):
    """Recive una lista de diccioarios e imprime los valores que se encuentran en las claves solicitadas

    Args:
        diccionarios (list): Diccionarios que se imprimiran
        claves (list): Las claves de los diccionarios cuyos valores asociados se imprimiran
        espaciado (int, optional): Espaciado entre columnas. Defaults to 12.
    """
    encabezados = []
    for clave in claves:
        encabezados.append(clave)

    for encabezado in encabezados:
        print(f'{encabezado.capitalize():^{espaciado}}', end='')

    print()
    print('=' * (len(encabezados) * espaciado))

    for diccionario in diccionarios:
        for clave in claves:
            print(f'{diccionario[clave]:^{espaciado}}', end='')

        print()


def mapear_lista(mapeadora, lista: list) -> list:
    """Mapea una lista acorde a un criterio recibido en la forma de una funcion

    Args:
        mapeadora (_type_): Funcion que determinara el criterio del mapeo
        lista (list): Lista que se mapeara

    Returns:
        list: Lista mapeada acorde al criterio recivido 
    """
    lista_retorno = []

    for el in lista:
        lista_retorno.append(mapeadora(el))

    return lista_retorno


def asignar_rating(elemento: dict) -> dict:
    """Asigna un valor aleatorio entre 1 y 10 a un diccionario en la clave "rating"

    Args:
        elemento (dict): diccionario

    Returns:
        dict: Diccionario con el rating asignado
    """
    elemento["rating"] = random.randint(10, 100) / 10
    return elemento


def asignar_genero(elemento: dict) -> dict:
    """Asigna un genero al diccionario dependiendo de su valor inicial

    Args:
        elemento (dict): diccionario al que se le asignara el genero

    Returns:
        dict: Diccionario con el genero asignado en la clave "genero"
    """
    elemento["genero"] = random.randint(1, 4)

    if elemento["genero"] == 1:
        elemento["genero"] = 'drama'

    elif elemento["genero"] == 2:
        elemento["genero"] = 'comedia'

    elif elemento["genero"] == 3:
        elemento["genero"] = 'accion'

    elif elemento["genero"] == 4:
        elemento["genero"] = 'terror'

    return elemento


def mapear_diccionarios(diccionarios: list, claves: list) -> list:
    """Mapea una lista de diccionarios acorde a las claves recibidas

    Args:
        diccionarios (list): Lista de diccionarios a mapear
        claves (list): Lista de las claves segun las cuales se mapearan los diccionarios

    Returns:
        list: Diccionarios mapeados acorde a las claves recividas
    """
    diccionarios_mapeados = []
    diccionario_mapeado = {}
    for diccionario in diccionarios:
        for clave in claves:
            diccionario_mapeado = {clave: diccionario[clave]}
            diccionarios_mapeados.append(diccionario_mapeado)

    return diccionarios_mapeados


def filtrar_lista_diccionarios(lista: list, clave: str, valor_buscado: any) -> list:
    """Filtra la lista de diccionarios recivida de acuerdo al valor buscado en la clave recivida

    Args:
        lista (list): diccionarios a filtrar
        clave (str): Clave en cuyos valores asociados se buscara el valor recivido
        valor_buscado (any): Valor segun el cual se filtraran los diccionarios

    Returns:
        list: Diccionarios filtrados
    """
    lista_filtrada = []
    for elemento in lista:
        if elemento[clave] == valor_buscado:
            lista_filtrada.append(elemento)

    return lista_filtrada


def escribir_peliculas_genero_solicitado(peliculas: list, genero: str) -> None:
    """Escribe las peliculas del genero solicitado en un archivo CSV

    Args:
        peliculas (list): lista de peliculas original
        genero (str): genero solicitado
    """
    with open(get_path_actual(f'{genero}.csv'), 'w', encoding='utf-8') as archivo:
        encabezado = ','.join(list(peliculas[0].keys())) + '\n'
        archivo.write(encabezado)

        for pelicula in peliculas:
            values = list(pelicula.values())
            lista = []

            for value in values:
                if isinstance(value, int):
                    lista.append((str(value)))
                elif isinstance(value, float):
                    lista.append(str(value))
                else:
                    lista.append(value)
            linea = ','.join(lista) + '\n'
            archivo.write(linea)


def calcular_maximo_en_clave_diccionarios(diccionarios: list, clave: str) -> int:
    """Calcula el valor maximo asociado a una clave en una lista de diccionarios

    Args:
        diccionarios (list): Lista de diccionarios en la que se buscara el valor maximo asociado a la clave recivida
        clave (str): clave en cuyos valores asociados se buscara el maximo 

    Returns:
        int/float: valor maximo encontrado
    """
    maximo = diccionarios[0][clave]

    for diccionario in diccionarios:
        if diccionario[clave] > maximo:
            maximo = diccionario[clave]

    return maximo


def agrupar_valores_iguales_diccionarios(diccionarios: list, clave: str, valor: any) -> list:
    """Busca en los valores asociados a una clave recivida en una lista de diccionarios los iguales al valor recivido

    Args:
        diccionarios (list): Lista de diccionarios en la que se buscaran los iguales al valor recivido
        clave (str): Clave en cuyos valores asociados se buscara el valor recivido
        valor (any): Valor que se buscara en la lista de diccionarios

    Returns:
        list: _description_
    """
    coincidentes = []
    for diccionario in diccionarios:
        if diccionario[clave] == valor:
            coincidentes.append(diccionario)

    return coincidentes


def ordenar_diccionarios(criterio, diccionarios: list) -> None:
    """Ordena una lista de diccionarios segun el criterio recivido

    Args:
        criterio (_type_): Criterio segun el cual se ordenara la lista
        diccionarios (list): Lista de diccionarios a ordenar
    """
    tam = len(diccionarios)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if criterio(diccionarios[i], diccionarios[j]):
                swap_lista(diccionarios, i, j)


def swap_lista(lista: list, i: int, j: int) -> None:
    """Swapea dos elementos de la lista recivida

    Args:
        lista (list): Lista cuyos elementos se swapearan
        i (int): indice del primer elemento del swap
        j (int): Indice del segundo elemento del swap
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def duplicar_lista(lista_original: list) -> list:
    """Recive una lista y crea una copia

    Args:
        lista_original (list): Lista a duplicar

    Returns:
        list: Copia de la lista original
    """
    lista_duplicada = []
    for elemento in lista_original:
        lista_duplicada.append(elemento)

    return lista_duplicada
