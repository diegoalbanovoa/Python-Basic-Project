
def run():
    number = int(input("Escribe numero: "))
    if is_cousin(number):
        print("Es Primo")
    else:
        print("No es primo")

# Metodo encargado de validar si un numero es primo o no
def is_cousin(number):
    contador = 0
    for i in range(1, number+1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    run()
