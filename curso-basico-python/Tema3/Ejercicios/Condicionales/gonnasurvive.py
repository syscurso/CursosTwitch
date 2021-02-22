def hero(bullets, dragons):
    
    killOneDragon = bullets // 2

    if killOneDragon >= dragons:
        return True

    return False

opcion1 = hero(10, 5) # DEVUELVE TRUE
opcion2 = hero(7, 4) # DEVUELVE FALSE
opcion3 = hero(4, 5) # DEVUELVE FALSE
opcion4 = hero(100, 40) # DEVUELVE TRUE
opcion5 = hero(1500, 751) # DEVUELVE FALSE
opcion6 = hero(0, 1) # DEVUELVE FALSE

print(opcion6)