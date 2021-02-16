# Personajes

tanque = {'nombre': 'Braun', 'defensa': 5, 'vida': 15, 'mana': '9',
          'habilidades': ['Escudo de Odin', 'Muralla Asgardiana']}

tirador = {'nombre': 'Legolas', 'ataque': 10, 'vida': 9, 'mana': '8',
           'habilidades': ['Lluvia de flechas', 'Disparo certero', 'Ira elfica']}

sanadora = {'nombre': 'Freya', 'vida': 10, 'mana': 10,
            'habilidades': ['Armadura', 'Aumento de ataque', 'Gota de Vida']}

# Monstruos


jefe = {'nombre': 'Alpha', 'vida': 25, 'ataque': 15,
        'habilidades': ['Zarpazo de Hel', 'Mordisco Infernal']}

# Un grupo de tres aventureros estan de camino a una mision en la cual tienen que derrotar
# al Alpha de los lobos.
# Los aventureros son un tanque, un tirador y un sanador.

# Imprime el nombre de los tres aventureros.
nombre1 = tanque['nombre']
nombre2 = tirador['nombre']
nombre3 = sanadora['nombre']

print(nombre1)
print(nombre2)
print(nombre3, '\n')

# Crea tres variables para imprimir las habilidades de cada aventurero.

habilidadesTanque = tanque['habilidades']
habilidadesTirador = tirador['habilidades']
habilidadesSanadora = sanadora['habilidades']

print(habilidadesTanque)
print(habilidadesTirador)
print(habilidadesSanadora, '\n')

# Los aventureros se encuentran con el Aplha y dos lobos.
# El alpha ataca primero con zarpazo de Hel  y el tanque se pone delante para aguantar el golpe.
# El alpha ataca con Mordico infernal cuyo daño es igual a su ataque

# Imprime la habilidad zarpazo de hel y el daño.
habilidadJefe = jefe['habilidades'][0]
ataqueJefe = jefe['ataque']

print('Alpha uso:', habilidadJefe)
print('Daño de ataque:', ataqueJefe, '\n')


# El tanque usa Escudo de odin que duplica su defensa.
# Imprime la habilidad de Escudo de odin y calcula cuanto de vida le sobra al
# tanque tras recibir el ataque. La vida total es igual a la vida mas la defensa

defensa = tanque['defensa']
vidaTotal = tanque['vida'] + (defensa * 2)
vidaRestante = vidaTotal - ataqueJefe

print('Braun uso:', habilidadesTanque[0])
print('Vida restante de Braun:', vidaRestante, '\n')


# El tirador aprovecha y ataca al jefe usando disparo certero
# Imprime la habilidad disparo certero y la vida restante de alpha
# despues del ataque.


jefe['vida'] = jefe['vida'] - tirador['ataque']


print('Legolas uso:', habilidadesTirador[1])
print('Vida restante de Alpha:', jefe['vida'], '\n')

# El jefe ataca de nuevo, esta vez usa mordisco infernal
# Imprime el daño de la habilidad y su nombre.

habilidadJefe = jefe['habilidades'][1]

print('Alpha uso:', habilidadJefe)
print('Daño de ataque:', ataqueJefe, '\n')

# El ataque del jefe va contra el tanque y su vida
# no es suficiente para aguantar el ataque.
# Por lo cual sanadora decide aumentar la vida y armadura del tanque
# Tanto la armadura como la vida seran aumentadas en la misma
# cantidad que mana tenga sanadora.

# Imprime la habilidad de gota de vida y armadura.
# Calcula la vida total del tanque para ver si sobrevive al ataque


vidaTotal = vidaRestante + 20
vidaRestante = vidaTotal - ataqueJefe

print('Sanadora uso:', habilidadesSanadora[0], 'y',
      habilidadesSanadora[2])
print('Vida restante de Braun:', vidaRestante, '\n')

# Legolas vuelve a atacar usando lluvia de flechas
# imprime la habilidad de lluvia de flechas y la vida restante
# del jefe.

jefe['vida'] = jefe['vida'] - tirador['ataque']

print('Legolas uso:', habilidadesTirador[0])
print('Vida restante de Alpha:', jefe['vida'], '\n')

# Ya que el tanque no tiene suficiente vida para soportar otro ataque
# el tirador decide usar furia elfica que le permite atacar rapido

# Imprime la habilidad de furia elfica y si la vida de alpha
# es menor de cero significa que lso aventureros an ganado.

jefe['vida'] = jefe['vida'] - tirador['ataque']

ganador = jefe['vida'] < 0

print(habilidadesTirador[2])
print('Alpha esta muerto?:', ganador, '\n')