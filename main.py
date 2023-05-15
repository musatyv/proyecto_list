def imprimir_nombres():
    print ("Imprimiendo nombres")
    for item in lista:
        print (item["nombre"])
def hacer_grandioso():
    print ("Haciendo grandiosos")
    for mago in magos:
        mago["nombre"] = "el gran "+ mago["nombre"]
lista=[{"nombre":"Harry Houdini","rol":"mago"},{"nombre":"Newton","rol":"cientifico"},{"nombre":"David Blaine","rol":"mago"},{"nombre":"Howking","rol":"cientifico"},{"nombre":"Messi","rol":"otros"},{"nombre":"Teller","rol":"mago"},{"nombre":"Einstein","rol":"cientifico"},{"nombre":"Pele","rol":"otros"},{"nombre":"Juanes","rol":"otros"}]
magos=[]
cientifico=[]
otros=[]
#print(lista)
for item in lista:
    #print (item)
    rol=item.get ("rol")
    #print (rol)
    if rol == "mago":
        #print ("Este es mago") 
        magos.append(item)
    elif rol=="cientifico":
        #print ("Este es cientifico")
        cientifico.append(item)
    else: 
        otros.append(item)
        #print ("Este no es mago ni cientifico")
#print("magos>")
#print(magos)
#print("cientifico>")
#print(cientifico)
#print("otros>")
#print(otros)
imprimir_nombres()
hacer_grandioso()
imprimir_nombres()
#print(magos)


