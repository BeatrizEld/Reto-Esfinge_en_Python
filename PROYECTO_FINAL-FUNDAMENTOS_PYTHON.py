#PROYECTO FINAL - FUNDAMENTOS DE PYTHON
#Beatiz Cogollo - Última modificación: 11-abr-22

#Clase 1 Proyecto: Definiendo la aventura
#Reto 1 - Equipamiento
from operator import length_hint


print("ESFINGE: Este es el equipo disponible y su valor en trekjuls:")
mapa = 70.67
botas = 120.23
bateria = 11.69
linterna = 28
agua = 73
botella = 20.5
snacks = 8.8
brujula = 60.99
reloj = 83.75
lentes_sol = 53.28
print("""mapa = 70.67
    botas = 120.23
    bateria = 11.69
    linterna = 28
    agua = 73
    botella = 20.5
    snacks = 8.8
    brujula = 60.99
    reloj = 83.75
    lentes_sol = 53.28""")

#Reto 2 - Pon tu respuesta después de cada print
print("ESFINGE: Lista tres objetos del equipamiento: Nombre y valor")
print("mapa:", mapa)
print("snacks:", snacks)
print("reloj:", reloj)

print("ESFINGE: ¿Puedes combinar elementos de tu equipo para prepararte mejor?")
agua_embotellada=botella+agua
linterna_funcional=linterna+bateria
print("agua_embotellada=botella+agua", agua_embotellada)
print("linterna_funcional=linterna+bateria", linterna_funcional)

print("ESFINGE: ¿El precio del agua en botella es menor al de la linterna funcional?")
print(agua_embotellada<linterna_funcional)

print("ESFINGE: ¿Cuanto valdría comprar unos snacks y una brujula?")
print(snacks+brujula)

print("ESFINGE: ¿Si tienes 100 puntos, te alcanza para comprar unas botas?")
print(botas<100)

#Clase 2 Proyecto: Tomando decisiones
#Reto 3 - Pon tu respuesta después del print
print("ESFINGE: No debes colocar más de 5 objetos en tu mochila, y tampoco pasarte de 200 trekjuls: ¿Cuales elementos colocarías?")
print("Escribe con el teclado el objeto que deseas agregar a la mochila. Si ya terminaste escribe FIN para calcular el valor total.")
compra = "ON"
num_items = 0
objetos = []
total = 0
while compra == "ON":
    while num_items <= 5:
        item = input("Selecciona un objeto: ")
        objetos.append(item)
        if item == "mapa":
            total = total + mapa
            num_items = num_items + 1
        elif item == "botas":
            total = total + botas
            num_items = num_items + 1
        elif item == "bateria":
            total = total + bateria
            num_items = num_items + 1
        elif item == "linterna":
            total = total + linterna
            num_items = num_items + 1
        elif item == "agua":
            total = total + agua
            num_items = num_items + 1
        elif item == "botella":
            total = total + botella
            num_items = num_items + 1
        elif item == "snacks":
            total = total + snacks
            num_items = num_items + 1
        elif item == "brujula":
            total = total + brujula
            num_items = num_items + 1
        elif item == "reloj":
            total = total + reloj
            num_items = num_items + 1
        elif item == "lentes_sol":
            total = total + lentes_sol
            num_items = num_items + 1
        elif item == "agua_embotellada":
            total = total + agua_embotellada
            num_items = num_items + 1
        elif item == "linterna_funcional":
            total = total + linterna_funcional
            num_items = num_items + 1
        elif item == "FIN":
            objetos.pop()
            break
        else:
            print("No seleccionaste una opcion valida")
            objetos.pop()
    else:
        print("Alcanzaste el numero maximo de objetos permitidos")
    if total <= 200:
        print("El valor de la compra no excede los 200 TJS:", total)
        compra = "OFF"
    else:
        print("Selecciona nuevos objetos, porque tu compra excedio el limite de 200 TJS:", total)
        num_items = 0
        objetos.clear()
        total = 0

#Reto 4 - Pon tu respuesta después del print
print ("ESFINGE: Es tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")
print("A la nueva mochila le caben", int(200/agua_embotellada))

#Clase 3 Proyecto: Almacenando equipamimento
#Reto 5 - Pon tu respuesta después del segundo print
print("ESFINGE: Le hice una actualización a tu mochila te dice la esfinge, porque solo podias conocer el valor de los objetos que tenias")
print("ESFINGE: Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")

unicos = []
for i in objetos:
    if i not in unicos:
        unicos.append(i)

mochila_1 = {}
for i in unicos:
    mochila_1[i] = {"cantidad": objetos.count(i), "valor": eval(i)}
print(mochila_1)

mochila_2 = {
    "agua_embotellada": {"cantidad": int(200/agua_embotellada), "valor": agua_embotellada}
}
print(mochila_2)

#Reto 6 - Pon tu respuesta después del print
print("ESFINGE: Ahora, en esta aventura te van a acompañar 8 integrantes más, y te voy a pedir que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")

vehiculo = []

for compartimiento in range(8):
    vehiculo.append(mochila_1)
    print("Así quedo la mochila de compartimiento", compartimiento + 1)
    print(vehiculo[compartimiento])

#Clase 4 Proyecto: Organizandonos un poco
#Reto 7 - Pon tu respuesta después del segundo print
print("ESFINGE: Te pido que para cuatro integrantes recolectes 3 elementos sin importar las cantidades que quieras adicionarles")
print("ESFINGE: Estas son las opciones: brujula, linterna_funcional, snacks y agua_embotellada")
print("ESFINGE: Pero necesito que calcules el total de elementos que hay en tu equipo")

def cambio_mochilas():
    nueva_mochila = {}
    print("Indica los tres elementos que deseas colocar en las mochilas: ")
    for i in range(3):
        objeto = input("Objeto: ")
        cantidad = input("Cantidad: ")
        nueva_mochila[objeto] = {"cantidad": int(cantidad), "valor": eval(objeto)}
    cant = input("Indica la cantidad de mochilas a modificar: ")
    for compartimiento in range(int(cant)):
        vehiculo[compartimiento] = nueva_mochila
    print(vehiculo)
    total_equipaje(vehiculo)


def total_equipaje(vehiculo):
    total_objetos = {}
    for mochila in vehiculo:
        for objeto, cantidad in mochila.items():
            if objeto not in total_objetos:
                total_objetos[objeto] = cantidad["cantidad"]
            else:
                total_objetos[objeto] += cantidad["cantidad"]
    print(total_objetos)

cambio_mochilas()