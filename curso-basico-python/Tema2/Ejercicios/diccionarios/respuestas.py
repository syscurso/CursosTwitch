
# Diccionario del que disponemos para los ejercicios
diccionario = {'canal' : 'syslasiGB', 'curso' : 'python', 'integrantes' : ['holou', 'da_chuck', 'pastor']}

# EJERCICIO 1
# Cra una variable que almacene tú nombre de la clave integrantes y printeala (si no está, elige el que quieras)

nombre = diccionario["integrantes"][2]

print(nombre)


# EJERCICIO 2
# Elimina el canal. Luego printea el diccionario para comprobarlo

diccionario.pop('canal')

print(diccionario)


# EJERCICIO 3
# Crea dos variables, una que contenga todas las llaves y otra que contenga todos los valores printealas.

llaves = diccionario.keys()
valores = diccionario.values()

print(llaves)
print(valores)

# EJERCICIO 4
# Utilizando las variables del ejercicio anterior. Crea dos nuevas variables y obten la llave 'curso' y el valor 'python'. Printealo

listaLlave = list(llaves)
print(listaLlave[0])

listaValor = list(valores)
print(listaValor[0])


# EJERCICIO 5
# Con las llaves 'coin' y los valores 'code'. Crea una variable que contenga la creación de un diccionario automático
moneda = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin', 'Dogecoin')

codigo = ('BTC', 'ETH', 'XRP', 'LTC', 'DOGE')

diccionarioAuto = dict(zip(moneda,codigo))

print(diccionarioAuto)

# UNA VEZ AQUÍ. ASEGURATE DE QUE TODOS LOS PRINTS ANTERIORES ESTAN COMENTADOS 
# EJERCICIO EXTRA --VENCER AL MONSTRUO--
#Tenemos dos diccionarios. Uno nuestro personaje y otro el monstruo.

personaje = {'nombre' : 'GameStop', 'fuerza' : 5, 'habilidades' : ['Reddit', 'Comunidad', 'Inversion']}

monstruo = {'nombre' : 'WallStreet', 'vida' : 5, 'habilidades' : ['Apuesta', 'InversionSegura', 'Cagada']}


# En este momento. El monstruo realiza su ataque Cagada
# Crea una variable que contenga la habilidad cagada y printeala
ataqueMonstruo = monstruo["habilidades"][2]

print(ataqueMonstruo)

# Al detectar el ataque de WallStreet. La comunidad se pone manos a la obra.
# De esta manera, obtienen +1 de fuerza. (Haz que el valor de fuerza de tú personaje suba 1)

personaje["fuerza"] += 1

# Printea la fuerza de tu personaje para comprobar que ha subido

print(personaje["fuerza"])

# En este momento tu personaje realiza el ataque Reddit
# Crea una variable que contenga la habilidad Reddit y printeala

ataquePersonaje = personaje["habilidades"][0]

print(ataquePersonaje)

# Crea una variable que compruebe si la fuerza de tu personaje es MAYOR que la vida del monstruo

final = personaje["fuerza"] > monstruo["vida"]

#Printea la variable. En caso de ser True habremos obtenido la VICTORIA!!

print(final)


