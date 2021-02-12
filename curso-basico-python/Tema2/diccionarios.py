
# Un diccionario, es una estructura de datos. Este se define con llaves {}
# Su estructura se compone de Llave-Valor  Key-Value
# La llave no puede estar repetida

#CREAR DICCIONARIO
diccionario = {'nombre' : 'holou', 'edad' : 22, 'curso' : ['Pygame', 'Tkinter', 'Flask']}

#OBTENER VALOR DE LA CLAVE NOMBRE
nombre = diccionario["nombre"]
#OBTENER VALOR DE LA CLAVE CURSO
curso = diccionario["curso"]

#VARIABLE ALFABETO
letras = 'abcdefghijklmnñopqrstuvwxyz'

#VARIABLE POSICIONES ALFABETO
posiciones = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

#CREAR UN DICCIONARIO DEL ALFABETO
diccionarioAutomatico = dict(zip(letras, posiciones))

letrasGriego = ('Alfa', 'Beta', 'Gamma')
posicionesGriego = ('PosicionUno', 'PosicionDos', 'PosicionTres')

diccionarioAutomatico1 = dict(zip(letrasGriego,posicionesGriego))

diccionario["edad"] += 1

edad = diccionario["edad"]

print(edad)


#OBTENER VALOR DE LA CLAVE NOMBRE
valor = diccionario.get('nombre')

#ELIMINAR clave-valor de EDAD
valor1 = diccionario.pop('edad')

#OBTENER TODAS LAS CLAVES DEL DICCIONARIO (EN OBJETO)
llaves = diccionario.keys()

#CONVERTIR EL OBJETO A LISTA PARA SU MANEJO
llavesLista = list(llaves)

#OBTENER TODOS LOS VALORES DEL DICCIONARIO (EN OBJETO)
valores = diccionario.values()

#CONVERTIR EL OBJETO A LISTA PARA SU MANEJO
valoresLista = list(valores)

#COPIAR EL DICCIONARIO EN UNA VARIABLE NUEVA
copiaDiccionario = diccionario.copy()

#LIMPIAR EL DICCIONARIO PRINCIPAL
diccionario.clear()

# EJERCFICIO 
# Obtener el nombre 'holou' por consola, teniendo en cuenta los diccionarios anteriores
nombreHolou = copiaDiccionario.get('nombre')

print(nombreHolou)
