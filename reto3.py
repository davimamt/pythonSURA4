
edad = int(input("Ingrese su edad"))




if (edad>=0 and edad<14):
    print (f'su edad es: {edad} y eres catalogado como niño')
elif (edad>=14 and edad<28):
    print (f'su edad es: {edad} y eres catalogado como Joven')
elif (edad>=28 and edad<60):
    print (f'su edad es: {edad} y eres catalogado como Adulto')
elif (edad>=60):
    print (f'su edad es: {edad} y eres catalogado como Adulto Mayor')
else:
    print (f'la edad: {edad} no es una edad valida')