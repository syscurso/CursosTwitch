import random

# Cualquier nombre de variable y/o función debe estár en ingles

# JUEGO DE LOS DADOS. Mayor puntuación GANA!!

# Crea una función que reciba 2 argumentos: El dado de da_chuck y holou
def diceGame(diceDaChuck, diceHolou):
    
# Dentro de la función debe printear un mensaje de que número le ha tocado a cada uno

    print(f'El dado de da_chuck es {diceDaChuck}')
    print(f'El dado de Holou es {diceHolou}')

# Crea un bloque condicional que compruebe si ha habido empate, victoría o derrota y devuelva el mensaje

    if diceDaChuck == diceHolou:
        return 'Empate!!'

    elif diceDaChuck > diceHolou:
        return 'da_chuck gana!!'
        
    else:
        return 'Holou gana!!'


# Dado de da_chuck (número aleatorio del 1 al 9, ambos incluidos)
diceDaChuck = random.randint(1, 9)

# Dado de Holou (número aleatorio del 1 al 9, ambos incluidos)
diceHolou = random.randint(1, 9)

# Llamada a la función
resultGame = diceGame(diceDaChuck, diceHolou)


# Printea el resultado de la función
print(resultGame)