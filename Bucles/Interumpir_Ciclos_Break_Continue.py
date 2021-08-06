# Interumpir ciclos Break Continue

# El siguiente metodo nos permite imprimir el numor del 1-1000, donde solo va a mostrarse por consola los numeros pares
# def run():
#     for contador in range(1000):
#         if contador % 2 != 0:
#             continue
#         print(contador)

# El siguiente metodo nos permite imprimir todos lod numero del 1-500
def run():
    for i in range(1000):
        print(i)
        if i == 500:
            break
if __name__ == '__main__':
    run()
