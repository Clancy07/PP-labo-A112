import os
from funciones import *

ejecutando = True

opciones_menu_principal = ['1. Cargar archivo CSV',
                           '2. Imprimir lista',
                           '3. Asignar rating',
                           '4. Asignar género',
                           '5. Filtrar por género',
                           '6. Ordenar películas',
                           '7. Informar Mejor Rating',
                           '8. Guardar películas',
                           '9. Salir']

elecciones_validas_menu_principal = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9']

while ejecutando:
    os.system('cls')

    opcion_elegida_menu_principal = crear_menu(opciones_menu_principal)
    while not verificar_opcion(opcion_elegida_menu_principal, elecciones_validas_menu_principal):
        print('\n',
              'Opcion invalida. Reingrese la opcion (1-9): \n')
        opcion_elegida_menu_principal = crear_menu(
            opciones_menu_principal)

    match(opcion_elegida_menu_principal):

        case '1':
            nombre_archivo = input('Ingrese el nombre del archivo a cargar: ')
            try:
                peliculas = cargar_peliculas(nombre_archivo)
                print('\nArchivo cargado\n')
                os.system('pause')
            except FileNotFoundError:
                print(
                    '\nNo se econtraron archivos con ese nombre. Debera reingresarlo.\n')
                os.system('pause')

        case '2':
            print()
            mostrar_valores_por_claves(
                peliculas, ['id', 'titulo', 'genero', 'rating'], 30)
            print()
            os.system('pause')

        case '3':
            peliculas = mapear_lista(asignar_rating, peliculas)
            print('\nRatings asignados con exito\n')
            os.system('pause')

        case '4':
            peliculas = mapear_lista(asignar_genero, peliculas)
            print('\nGeneros asignados con exito\n')
            os.system('pause')

        case '5':
            genero_solicitado = input(
                'Ingrese el genero por el que desea filtrar: ')

            peliculas_genero_solicitado = filtrar_lista_diccionarios(
                peliculas, 'genero', genero_solicitado)

            escribir_peliculas_genero_solicitado(
                peliculas_genero_solicitado, genero_solicitado)

            print(
                f'Se genero un archivo con las peliculas filtradas por el genero de {genero_solicitado}')
            os.system('pause')

        case '6':
            peliculas_copia = duplicar_lista(peliculas)
            peliculas_ordenadas = []

            dramas = filtrar_lista_diccionarios(
                peliculas_copia, 'genero', 'drama')
            comedias = filtrar_lista_diccionarios(
                peliculas_copia, 'genero', 'comedia')
            de_accion = filtrar_lista_diccionarios(
                peliculas_copia, 'genero', 'accion')
            de_terror = filtrar_lista_diccionarios(
                peliculas_copia, 'genero', 'terror')

            ordenar_diccionarios(
                lambda film1, film2: film1["rating"] < film2["rating"], dramas)

            ordenar_diccionarios(
                lambda film1, film2: film1["rating"] < film2["rating"], comedias)

            ordenar_diccionarios(
                lambda film1, film2: film1["rating"] < film2["rating"], de_accion)

            ordenar_diccionarios(
                lambda film1, film2: film1["rating"] < film2["rating"], de_terror)

            peliculas_ordenadas.extend(dramas)
            peliculas_ordenadas.extend(comedias)
            peliculas_ordenadas.extend(de_accion)
            peliculas_ordenadas.extend(de_terror)

            mostrar_valores_por_claves(
                peliculas_ordenadas, ['id', 'titulo', 'genero', 'rating'], 30)

            os.system('pause')

        case '7':
            ratings = mapear_diccionarios(peliculas, ["rating"])

            rating_maximo = calcular_maximo_en_clave_diccionarios(
                ratings, 'rating')

            peliculas_con_mejor_rating = agrupar_valores_iguales_diccionarios(
                peliculas, 'rating', rating_maximo)

            mostrar_valores_por_claves(peliculas_con_mejor_rating, [
                'titulo', 'rating'], 20)

            os.system('pause')

        case '8':
            pass

        case '9':
            if input('CONFIRMAR SALIDA? ').lower() == 'si':
                ejecutando = False
