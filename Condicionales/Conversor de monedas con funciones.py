def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos" + tipo_pesos + "tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $"+dolares + " dolares")


menu = """
Bienvenido al conversor de monedas 💕
1 - Pesos Colombianos 
2 - Pesos Argentinos 
3 - Pesos Mexicanos 

Elige una opción:  """

option = int(input(menu))

if option == 1:
    conversor("Colombiano", 3875)
elif option == 2:
    conversor("Argentinos", 65)
elif option == 3:
    conversor("Mexicanos", 24)
else:
    print("Ingrese una opcion correcta")
