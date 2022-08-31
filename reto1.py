# ENTARDAS = Variables = referencias en memoria
nivelAgua = int(input("Digite el nivel de agua: ")) 




#PROCESO
if (nivelAgua>=0 and nivelAgua<20):
    print (f'El nivel de agua es: {nivelAgua} y este es BAJO') #SALIDA

elif(nivelAgua>=20 and nivelAgua<400):
    print (f'El nivel de agua es: {nivelAgua} y este es NORMAL') #SALIDA
elif(nivelAgua>=400):
    print (f'El nivel de agua es: {nivelAgua} ¡ALERTA!') #SALIDA
else:
  print (f'El nivel de agua {nivelAgua} no es valido')  #SALIDA

