#tarea semestral
import random


coordjug = [0, 0]
posicionb = []
tablero = []
tablerovisual = []
#tamaño tablero
def leeValida(m, M):
    f = int(input("Ingresa cantidad de filas: "))
    while not m <= f <= M:
        f = int(input(f"Reingresa la cantidad de filas entre {m} y {M}: "))
    c = int(input("Ingresa cantidad de columnas: "))
    while not m <= c <= M:
        c = int(input(f"Reingresa la cantidad de columnas entre {m} y {M}: "))
    return f,c

#cantidad de bombas aleatorias entre 1 y f,c / 4
def generarCBombas():
    return random.randint(1, int((filas*columnas)/4)) 

#generar tablero
filas, columnas = leeValida(3, 15)

for i in range (filas):
    tablero.append([])
for i in tablero:
    for x in range(columnas):
        i.append("#")

#generar posicion de bobmbas
def pb():
    return  random.randint(1, filas), random.randint(1, columnas) 

def perderosguir():
    if tablero[coordjug[0]-1][coordjug[1]-1] == "b":
        return False
    
def ganar():
        c = 0
        for filast in tablero:
            if "#" not in filast: # filas del ciclo for
                c +=1
        if c == filas:  #filas del tablero en general
            return False
def bombasalrededor():
    b = 0
    alrededor = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),           (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    for i in alrededor:
        rf = (coordjug[0]-1) + i[0] # revisar filas
        rc = (coordjug[1]-1) + i[1] # columnas
        if (0 <= rf <= filas-1) and (0 <= rc <= columnas-1): # por temas de com ose lee la lista se debe restar 1 al rango de posiciones
            if tablero[rf][rc] == "b":
                b +=1
    return b

def desplegartablero():
    for posicion in tablero:
        f=""
        for i in posicion:
            f+=(str(i).replace("b", "#"))
        print(f)
def desplegartablerobombas():
    for posicion in tablero:
            f=""
            for i in posicion:
                f+=(str(i))
            print(f) 

cb = generarCBombas()

for i in range (cb):
    posicionb.append(pb())
    for p in posicionb:
        tablero[p[0]-1][p[1]-1] = "b"
    

#print tablero codigo
print(cb)
print(posicionb)


while True:
    desplegartablero()
    fj = int(input("Ingresa la fila: "))
    cj = int(input("Ingresa la columna: "))
    coordjug[0] = fj
    coordjug[1] = cj
    
    
    if perderosguir() == False:
        desplegartablerobombas()
        print("perdiste, gana el pc ! ! ! ")
        break

    tablero[coordjug[0]-1][coordjug[1]-1] = bombasalrededor() # ssta linea hay que dejarla si o si despues de verificar si se pierde
    if ganar() == False:
        desplegartablero()
        print("ganaste ! ! ! elpepe elpepe i hate ")
        break