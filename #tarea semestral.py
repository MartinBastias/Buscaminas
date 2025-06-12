#tarea semestral
import random
coordjug = [0, 0]
cb = 0
posicionb = []
tablero = []

def leeValidaTablero(m, M):
    f = int(input("Ingresa cantidad de filas: "))
    while not m <= f <= M:
        f = int(input(f"Reingresa la cantidad de filas entre {m} y {M}: "))
    c = int(input("Ingresa cantidad de columnas: "))
    while not m <= c <= M:
        c = int(input(f"Reingresa la cantidad de columnas entre {m} y {M}: "))
    return f,c

def leeValidaCoordenadas(f, c):
    fila = int(input("Ingresa fila: "))
    while not 1 <= fila <= f:
        fila = int(input(f"Valor fuera de rango, debes ingresar un valor entre 1 y {f}: "))
    columna = int(input("Ingresa columna: "))
    while not 1 <= columna <= c:
        columna = int(input(f"Valor fuera de rango, debes ingresar un valor entre 1 y {c}: "))
    return fila, columna

def generarCantidadBombas():
    return random.randint(1, int((filas*columnas)/4)) #cantidad de bombas aleatorias entre 1 y f,c / 4

#generar posicion de bobmbas
def pb():
    return  random.randint(1, filas), random.randint(1, columnas) 

def prepararBombas():
    for i in range (cb):
        posicionb.append(pb())
        for p in posicionb:
            tablero[p[0]-1][p[1]-1] = "b"
    
def bombasalrededor():
    b = 0
    alrededor = [(-1, -1), (-1, 0), (-1, 1), # estas son todas las traslaciones alrededor, les mande un dibujo con la idea
                 (0, -1),           (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    for i in alrededor:
        rf = (coordjug[0]-1) + i[0] # revisar filas
        rc = (coordjug[1]-1) + i[1] # columnas
        if (0 <= rf <= filas-1) and (0 <= rc <= columnas-1): # por temas de com ose lee la lista se debe restar 1 al rango de posiciones
            if tablero[rf][rc] == "b":
                b +=1
    return b

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
#como el tablero original son varias listas, las pase a string, si alguien lo puede optimizar mejor, adeelante
#basicamente convierte cada lista en una string por separado y luego las despliega 1 por 1, dando el efecto de que fuera
#un solo tablero grande
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
def crearTablero():
    for i in range (filas):
        tablero.append([])
    for i in tablero:
        for x in range(columnas):
            i.append("#")

filas, columnas = leeValidaTablero(3, 15)
crearTablero()
cb = generarCantidadBombas()
prepararBombas()
while len(set(posicionb)) < len(posicionb): #previene que se juegue una partida con bombas repetidas
    tablero.clear
    crearTablero()
    posicionb.clear
    cb = generarCantidadBombas()
    prepararBombas()
    if len(set(posicionb)) == len(posicionb):
        break
print(cb) #esto es informacion para nosotros, la cantuidad de bombas u sus posiciones
print(posicionb)

while True:#bucle del juego
    desplegartablero()
    coordjug[0],coordjug[1] = leeValidaCoordenadas(filas, columnas)
    
    if perderosguir() == False:
        desplegartablerobombas()
        print("perdiste, gana el pc ! ! ! ")
        break

    tablero[coordjug[0]-1][coordjug[1]-1] = bombasalrededor() # ssta linea hay que dejarla si o si despues de verificar si se pierde
    if ganar() == False:
        desplegartablero()
        print("ganaste ! ! ! elpepe elpepe i hate ")
        break