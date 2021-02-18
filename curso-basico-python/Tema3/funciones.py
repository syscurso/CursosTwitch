

def saludo():

    return 'Hola que tal'

saludillo = saludo()



def saludoCortana(nombre):

    return f'Hola {nombre}, como va eso'


saludilloCortana = saludoCortana('Julian')



def controladorMenores(edad):

    if edad < 18:
        return 'No puedes pasar, eres menor'
    else:
        return 'Puedes pasar'

controlador = controladorMenores(16)

print(controlador)