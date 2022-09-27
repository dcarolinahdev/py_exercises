# -*- coding: utf-8 -*-

monedas = ["pesos", "dólares", "libras"]

def get_coin_value(moneda_origen, moneda_destino):
	# order: colombian pesos, dollar, pound
	coin_value = [
		[1, 0.00029, 0.00021],
		[3493, 1, 0.72],
		[4856, 1.39, 1]]
	return coin_value[moneda_origen][moneda_destino]

def conversor(pos_origen, pos_destino):
    origen = float(input("¿Cuántos " + monedas[pos_origen] + " tienes?: "))
    destino = round(origen * get_coin_value(pos_origen, pos_destino) , 2)
    print("Tienes $" + str(destino) + " " + monedas[pos_destino])

menu = """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Dólares americanos
3 - Libra exterlina

Elige la moneda de origen: """

opcion_o = int(input(menu))

if opcion_o in [1, 2, 3]:
    menu_2 = """
    Ahora elige la moneda destino

    1 - Pesos colombianos
    2 - Dólares americanos
    3 - Libra exterlina
    """
    opcion_d = int(input(menu_2))
    if opcion_d in [1, 2, 3]:
        conversor(opcion_o-1, opcion_d-1)
    else:
        print('[destino] Ingresa una opción correcta por favor')
else:
    print('[origen] Ingresa una opción correcta por favor')
