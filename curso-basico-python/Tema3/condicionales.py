


edad = input('Que edad tienes: ')

edad = int(edad)

if edad < 18:
    print('Eres menor de edad')
elif edad == 18:
    print('Acabas de llegar a la mayoría de edad. BIENVENIDO')
else:
    print('Ya tienes más de 18')

# Crea una estructura de control que determine que beben según su edad
# Si tienen menos de 18 años beben zumito
# Si tienen 18 beben tequila
# Si tienen más de 18, beben cerveza
# Y sino, el valor no es correcto
# EN CADA CONDICION HAY QUE PRINTEAR UN MENSAJE DE LO QUE BEBEN

edad = input('Que edad tienes: ')
edad = int(edad)

if edad < 18:
    print('Solo puedes beber zumito de naranja')
elif edad == 18:
    print('Te puedo servir un chupito de tequila')
elif edad > 18:
    print('Como ya eres mayor te puedo dar una buena jarra de cerveza')
else:
    print('La edad introducida no corresponde a ninguna de este universo, vuelva a intentar')