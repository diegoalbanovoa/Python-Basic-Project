import random
# Clase contiene el codigo que hace refencia a un juego de adivinar un numero del 1-100, el cual es jenerado con un clase especial llamada Random


def run():
    number = random.randint(1, 100)
    chosen_number = int(input("Elige un numero del 1 al 100: "))
    while chosen_number != number:
        if chosen_number < number:
            print("Busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño")
        chosen_number = int(input("Elige un numero del 1 al 100: "))
        print("Ganaste!!!!!!")


if __name__ == '__main__':
    run()
