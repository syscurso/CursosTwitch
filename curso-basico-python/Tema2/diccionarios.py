
# Un diccionario, es una estructura de datos. Este se define con llaves {}
# Su estructura se compone de Llave-Valor  Key-Value
# La llave no puede estar repetida

diccionario = {'nombre' : 'holou', 'edad' : 22, 'curso' : ['Pygame', 'Tkinter', 'Flask']}

nombre = diccionario["nombre"]
curso = diccionario["curso"]

letras = 'abcdefghijklmnñopqrstuvwxyz'
posiciones = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

diccionarioAutomatico = dict(zip(letras, posiciones))


valor = diccionario.get('nombre')
valor1 = diccionario.pop('edad')


llaves = diccionario.keys()
llavesLista = list(llaves)

valores = diccionario.values()
valoresLista = list(valores)


copiaDiccionario = diccionario.copy()

diccionario.clear()

# EJERCFICIO 
# Obtener el nombre 'holou' por consola, teniendo en cuenta los diccionarios anteriores
nombreHolou = copiaDiccionario.get('nombre')

print(nombreHolou)
