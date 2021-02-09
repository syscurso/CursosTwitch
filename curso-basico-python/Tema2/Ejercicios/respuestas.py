
# Lista de la que disponemos para los ejercicios
lista = [5, 30, 17, 4, 24]

# EJERCICIO 1
# Crea una variable que almacene la longitud de la lista y printeala

longitud = len(lista)

# EJERCICIO 2
# Crea una variable que almacene el último valor de la lista y printeala

#Ambas son correctas
ultimoVal = lista[longitud-1]
ultimoVal1 = lista[-1]


# EJERCICIO 3
# Añade un número a la lista y luego printeala para certificarlo

lista.append(4)


# EJERCICIO 4
# Elimina el último valor de la lista y luego printeala para certificarlo

lista.pop()


# EJERCICIO 5
# Ordena la lista y luego printeala para certificarlo

lista.sort()



# EJERCICIO EXTRA
# Sabiendo que nosotros somos la 'X' y es nuestro turno...
# Añade tú valor X en esta matriz para obtener la victoria!!!

matriz = [['X',' ','O'],
          ['O','X',' '],
          [' ',' ',' ']]

#Se aceptará ya que es el que expliqué.
matriz[2].insert(2, 'X')

# Correcto y lo explico hoy antes de comenzar
matriz[2][2] = 'X'

# Para que se vea en consola correctamente.
print(matriz[0])
print(matriz[1])
print(matriz[2])