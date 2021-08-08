name = "Francisco"
# Esto es un slices(Rebanada)
print(name[0:3])
# Si no especificas tomara como comienzo el caracter eu especificaste
print(name[3:])
# Este tercer hace referencia a los pasos que quiero hacer para llegar ahi, lo que quiere decir es que nos devolvera la cadena de a pasos de dos en dos.  
print(name[1:7:2])
# Lo que quiere decir es que tomaresmos pasos negativos, lo que pasara es que comenzara desde el caracter final hasta el del comienzo 
print(name[::-1])
