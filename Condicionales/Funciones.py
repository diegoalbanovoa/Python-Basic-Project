# def imprimir_mensaje():
#    print("Mensaje Especial")
#    print("Estoy Aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()
def conversacion(message):
    print("Hola")
    print("Como estas")
    print(message)
    print("adios")


opcion = int(input('Elege opcion(1,2,3): '))
if opcion == 1:

    conversacion("Elegiste la Opcion 1")

elif opcion == 2:

    conversacion("Elegiste la Opcion 2")

elif opcion == 3:

    conversacion("Elegiste la Opcion 3")

else:
    print("Elige un opcion correcta")
