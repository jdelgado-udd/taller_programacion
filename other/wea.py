"""
with open("ventas.csv", "r", encoding="utf-8") as archivo:
    leer = archivo.readlines()
listaT = []
for i in leer[1::]:
    i=i.strip().split(", ")
    fecha = i[0]
    tienda = i[1]
    producto = i[2]
    cantidad = int(i[3])
    precio_unitario = float(i[4])
    
    listaT.append((fecha, tienda, producto, cantidad, precio_unitario))
    f"fecha: {fecha}, tienda: {tienda}, producto: {producto}, cantidad: {cantidad}, precio_unitario:{precio_unitario}"
    #print(listaT)

diccion = {}
def ventas_por_tienda(lista):
    for i in lista:
        multiplicar = i[3]*i[4]
        diccion[i[2]]= (multiplicar)
ventas_por_tienda(listaT)
print(diccion)

def producto_mas_vendido(producto):
    for i in producto:
        print(i)
producto_mas_vendido(diccion)

"""
"""
ventas_por_tienda(listaT)

dick = {}
cewfydjwfuydewguydgwj = [("hola",2,3)]
def funcion(x):
    for i in x:
        
        dick[i[0]]=(i[1],i[2])
    



funcion(cewfydjwfuydewguydgwj)
"""


diccion = {
    "hola":[
            1,
            {
                "malo": [2,8],
                "exotico": [3,4]
            }
        ],
        "hola1": [
            2,
            {
                "bueno": [6,3],
                "binchilin": [1,2]
            }
        ]
    }

for i in diccion:
    for j in diccion[i][1]:
        for k in diccion[i][1][j]:
            print(k)
           


