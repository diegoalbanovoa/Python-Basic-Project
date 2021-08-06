# Palindro: palabra que se lee igual al derecho y al reves
def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


# Funcion Principal, Estandar (Buena Practica)


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True :
        print("Es palindromo")
    else:
        print("No es palindromo")

# Estandar (Buena Practica), punto de entrada de un programa de python
if __name__ == '__main__':
    run()
