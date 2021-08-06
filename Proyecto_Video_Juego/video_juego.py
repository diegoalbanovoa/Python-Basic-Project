import random
# Clase contiene el codigo que hace refencia a un juego de adivinar un numero del 1-100, el cual es jenerado con un clase especial llamada Random


def run():
    numero = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    while numero_elegido != numero:
        if numero_elegido < numero:
            print("Busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño")
        numero_elegido = int(input("Elige un numero del 1 al 100: "))
        print("Ganaste!!!!!!")


if __name__ == '__main__':
    run()
