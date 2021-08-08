# def imprimir_mensaje():
#    print("Mensaje Especial")
#    print("Estoy Aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()
def conversation(message):
    print("Hola")
    print("Como estas")
    print(message)
    print("adios")


option = int(input('Elege opcion(1,2,3): '))
if option == 1:

    conversation("Elegiste la Opcion 1")

elif option == 2:

    conversation("Elegiste la Opcion 2")

elif option == 3:

    conversation("Elegiste la Opcion 3")

else:
    print("Elige un opcion correcta")
