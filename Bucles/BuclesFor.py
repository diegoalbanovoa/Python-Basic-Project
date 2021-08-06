# Bucles for 
#imprimir los numeros del 1 al 1000 el rango define las iteraciones
#for contador in range(1,1001):
#    print(contador)

# Tabla del 11
#for i in range(10):
#    print(i*11)

# Se ejecutala un numero de veces que hace referencia a el numero de caracteres del nombre que digites 
def run():
    nombre = input("Escribe tu nombre: ")
    for letra in nombre:
        print(letra)


if __name__ == '__main__':
    run()