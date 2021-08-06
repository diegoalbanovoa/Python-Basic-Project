
def run():
    numero = int(input("Escribe numero: "))
    if es_primo(numero):
        print("Es Primo")
    else:
        print("No es primo")

# Metodo encargado de validar si un numero es primo o no
def es_primo(numero):
    contador = 0
    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    run()
