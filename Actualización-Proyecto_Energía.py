consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84}
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Manta': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32}
    },
}

plantas = {
    'Quito': ('Coca Codo Sinclair', 'Sopladora'),
    'Guayaquil': ('Coca Codo Sinclair', 'Sopladora'),
    'Loja': ('Sopladora'),
    'Tena': ('Sopladora'),
    'Manta': ('Sopladora')
}

informacion = {
    'Costa': ('Guayaquil', 'Manta'),
    'Sierra': ('Quito', 'Ambato', 'Loja'),
    'Oriente': ('Tena', 'Nueva Loja')
}

def total_consumo_por_planta_ciudad(planta, ciudad):
    if planta not in consumo_energia.keys():
        return 'La planta ' + planta + ' no existe o no se encuentra registrada'

    if ciudad not in consumo_energia[planta].keys():
        return 'La planta ' + planta + ' no proveé energía a la ciudad de ' + ciudad

    total_consumo = sum(consumo_energia[planta][ciudad]['consumos'])
    return total_consumo

def ciudad_plantas():
    for dato in plantas:
        if ciudad in dato:
            for dato in consumo_energia['Coca Codo Sinclair']:
                if dato == ciudad:
                    total_coca = (sum(consumo_energia['Coca Codo Sinclair']['{}'.format(ciudad)]['consumos']))
                    print('Coca Codo Sinclair entregó: ',total_coca, 'MWh de energía')
                    continue
            for dato in consumo_energia['Sopladora']:
                if dato == ciudad:
                    total_sopladora = (sum(consumo_energia['Sopladora']['{}'.format(ciudad)]['consumos']))        
                    print('Sopladora entregó: ',total_sopladora, 'MWh de energía')
        if ciudad not in plantas:
            print ('La ciudad que ingresó no cuenta con registros aún')
            break

def recaudacion ():
    ciudades_region_digitada = informacion[region_digitada]
    total_consumo = 0
    
    for ciudad_region_digitada in ciudades_region_digitada:
        for planta in consumo_energia.keys():
            for ciudad in consumo_energia[planta].keys():
                if ciudad_region_digitada == ciudad:
                    total_consumo += sum(consumo_energia[planta][ciudad]['consumos'])*consumo_energia[planta][ciudad]['tarifa']
    print("La región " +region_digitada, 'cuenta con :','$', total_consumo)


opción = 1
while opción != 0:

    print("<1> Consultar el total de MWh consumidos en una planta eléctrica")
    print("<2> Consultar información de plantas en una ciudad")
    print("<3> Consultar información de dinero recaudado en una región")
    print("<4> Salir")

    op = int(input('Ingrese opción: '))
    print("....................................................................................")

    while op == 1:
       
        planta = input('Ingrese el nombre de la planta (Coca Codo Sinclair, Sopladora): ')
        ciudad = input('Ingrese el nombre de la ciudad: ')

        total = total_consumo_por_planta_ciudad(planta, ciudad)

        if type(total) == int:
            print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total, planta))
        else:
            print(total)
        print("....................................................................................")
        break
    while op == 2:
        ciudad =  input('Ingrese el nombre de la ciudad: ')
        ciudad_plantas()
        print("....................................................................................")
        break
    while op == 3:
        region_digitada = input('Ingrese el nombre de una región: ')
        if region_digitada not in informacion.keys():
            print ('La región no se encuentra registrada o no existe')
            print("....................................................................................")
            break
        if region_digitada in informacion.keys():
            recaudacion()
            print("....................................................................................")
            break
    if op==4:
        print("Programa finalizado....")
        exit()
