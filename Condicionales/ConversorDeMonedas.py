# """ con tre comillas dobles me permite que python me reconosca las lineas que estas colocoando
menu = """
Bienvenido al conversor de monedas 💕
1 - Pesos Colombianos 
2 - Pesos Argentinos 
3 - Pesos Mexicanos 

Elige una opción:  """

option = int(input(menu))

if option == 1:
    pesos = input('Cuantos pesos colombianos tienes?: ')
    pesos = float(pesos)
    value_dolar = 3875
    dolar = pesos / value_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print("Tienes $"+dolar + " dolares")
elif option == 2:
    pesos = input('Cuantos pesos argentinos tienes?: ')
    pesos = float(pesos)
    value_dolar = 65
    dolar = pesos / value_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print("Tienes $"+dolar + " dolares")
elif option == 3:
    pesos = input('Cuantos pesos Mexicanos tienes?: ')
    pesos = float(pesos)
    value_dolar = 24
    dolar = pesos / value_dolar
    dolar = round(dolar, 2)
    dolar = str(dolar)
    print("Tienes $"+dolar + " dolares")
else:
    print("Ingrese una opcion correcta")
