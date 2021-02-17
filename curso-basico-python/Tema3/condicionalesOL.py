# and   Devuelve True si ambos elementos son True   True and True = True
# or    Devuelve True si al menos un elemento es True   True or False = True
# not   Devuelve el contrario, True si es Falso y viceversa not True = False



eleccionEntrenador = 'pokemonRoca'

eleccionRival = 'pokemonFuego'


if eleccionEntrenador == 'pokemonPlanta' and eleccionRival == 'pokemonTierra':
    print('El entrenador gana.')

elif (eleccionEntrenador == 'pokemonAgua' or eleccionEntrenador == 'pokemonRoca') and eleccionRival == 'pokemonFuego':
    print('El entrenador gana de nuevo')

else:
    print('El entrenador pierde')