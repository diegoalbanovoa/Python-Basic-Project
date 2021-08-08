# Palindro: palabra que se lee igual al derecho y al reves
def palindrome(word):
    word = word.replace(' ','')
    word = word.lower()
    inverted_word = word[::-1]
    if word == inverted_word:
        return True
    else:
        return False


# Funcion Principal, Estandar (Buena Practica)


def run():
    word = input("Escribe una palabra: ")
    is_palindrome = palindrome(word)
    if is_palindrome == True :
        print("Es palindromo")
    else:
        print("No es palindromo")

# Estandar (Buena Practica), punto de entrada de un programa de python
if __name__ == '__main__':
    run()
