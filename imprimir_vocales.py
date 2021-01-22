# Recorre e imprime el siguiente arreglo donde se encuentren vocales											
											
# Array[	a	b	c	d	e	f	g	h	i	j	k]

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
posicion_vocales = []
vocales = []

for i, valor in enumerate(letras):
    if valor == 'a' or valor == 'e' or valor == 'i' or valor == 'o' or valor == 'u':
        posicion_vocales.append(i)
        vocales.append(valor)

print("Las vocales del arreglo: ")
print(letras)
print("Son: ")
print(vocales)
print("Y se encuentran en las posiciones: ")
print(posicion_vocales)