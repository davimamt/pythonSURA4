mes=input("Ingrese el mes: ")
mes_min= mes.lower()

if(mes_min=="enero" or mes_min=="febrero" or mes_min=="marzo"):
    print(f'Estas en INVIERNO')
elif(mes_min=="abril" or mes_min=="mayo" or mes_min=="junio"):
    print(f'Estas en PRIMAVERA')
elif(mes_min=="julio" or mes_min=="agosto" or mes_min=="septiembre"):
    print(f'Estas en VERANO')
elif(mes_min=="octubre" or mes_min=="noviembre" or mes_min=="diciembre"):
    print(f'Estas en OTOÑO')
else:
    print(f'ingresa un mes valido')
