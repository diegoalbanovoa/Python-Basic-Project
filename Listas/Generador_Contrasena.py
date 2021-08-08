import random
# Clas encargada de generar una contraseña al azar usando la clase Random

def password_generator():
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = capital_letters + lowercase + symbols + numbers

    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)

    password = "".join(password)
    return password


def run():
    contrasena = password_generator()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()
