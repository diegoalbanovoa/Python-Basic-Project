# Un diccionario es un estructura de datos de llave valor
# las {} hacen la funcion de definir diccionarios
def run():
    my_dictionary = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # Forma de imprimir llaves
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    countries_population = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }
    # este for nos permite ver el valor de las llaves del diccionario 
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # Este ciclo for nos permite ver el valor almacenado en las llaves
    # for pais in poblacion_paises.values():
    #     print(pais)

    # Este for nos permite ver la clave con su respectivo valor
    for country, population in countries_population.items():
        print(country + ' tiene ' + str(population) + ' habitantes')


if __name__ == '__main__':
    run()
