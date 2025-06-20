#Tarea Semestral Buscaminas G17
#Nombres: Martin Ignacio Bastias Neira, Matias Ignacio Cabello Carvajal, Felipe Ignacio Castro Castillo
import random

coordjug = [0, 0] #Coordenadas de juego (fila y columna)
posicionb = [] #lista de las posiciones de bombas
tablero = [] #Lista modificable del tablero (para # o *)


def Leevalentero(txt): #Pide un valor entero, repitiendo hasta que la entrada sea válida
    while True:
        try:
            x = input(txt) 
            int(x)
            break
        except ValueError:
            print('Error, valor ingresado debe ser un numero entero')
    return int(x)

def leeValidaGeneral(txt, m, M): #Valida que la entrada sea entera y que este entre m y M (incluyendolos)
    n = Leevalentero(f'Ingrese {txt}: ')
    while not m <= n <= M:
        print(f"Error. Reingresa {txt} y asegurate de que la entrada este entre {m} y {M}")
        n = Leevalentero(f'Ingrese {txt}: ')
    return n

def pb(): #Devuelve una posicion aleatoria dentro del tablero
    return  random.randint(1, filas), random.randint(1, columnas) 

def prepararBombas(): #Coloca bombas y marca "*" en cada posición
    for i in range(cb):
        posicionb.append(pb())
        for p in posicionb:
            tablero[p[0]-1][p[1]-1] = '*'
    
def bombasalrededor(): #Cuenta la cantidad de bombas en las 8 celdas vecinas a la coordenada
    b = 0
    alrededor = [(-1, -1), (-1, 0), (-1, 1), # Translaciones de las celdas cercanas
                 (0, -1),           (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    for i in alrededor:
        rf = (coordjug[0]-1) + i[0] # revisa filas
        rc = (coordjug[1]-1) + i[1] # revisa columnas
        if (0 <= rf <= filas-1) and (0 <= rc <= columnas-1): # Por temas de como se lee la lista se debe restar 1 al rango de posiciones
            if tablero[rf][rc] == '*':
                b +=1
    return b

# Retorna True si la casilla elegida tiene una mina
def perderosguir():
    return tablero[coordjug[0]-1][coordjug[1]-1] == '*'
    
# Retorna True si no quedan casillas ("#") por descubrir
def ganar():
    for fila in tablero:
        if "#" in fila:
            return False
    return True
        

def desplegartablero(): #Imprime el tablero ocultando las bombas (muestra '#' donde hay '*')
    for posicion in tablero:
        f=""
        for i in posicion:
            f+=(str(i).replace('*', '#'))
        print(f)

def crearTablero(): #Inicializa 'tablero' como matriz filas×columnas llena de '#'
    for i in range (filas):
        tablero.append([])
    for i in tablero:
        for j in range(columnas):
            i.append("#")
    
            
#Ingreso de Variables para el Tablero y implementacion de bombas
filas = leeValidaGeneral('Cantidad de filas',3, 15)
columnas = leeValidaGeneral('Cantidad de columnas',3, 15)
crearTablero()
cb = leeValidaGeneral('Cantidad de bombas',1,int(filas*columnas/4))
prepararBombas()

#Previene posiciones duplicadas de bombas
while len(set(posicionb)) < len(posicionb): 
    tablero.clear()
    crearTablero()
    posicionb.clear()
    prepararBombas()
    if len(set(posicionb)) == len(posicionb):
        break

# Debug: conoce ubicación real de las bombas
print(cb) 
print(posicionb)


# Bucle principal:
# 1. Muestra tablero
# 2. Pide fila/columna
# 3. Chequea pérdida (mina)
# 4. Revela número de bombas vecinas
# 5. Chequea victoria
while True:
    desplegartablero()
    coordjug[0] = leeValidaGeneral('fila',1,filas)
    coordjug[1] = leeValidaGeneral('columna',1,columnas)
    
    if perderosguir(): 
        for i in range(filas):
            print(columnas*"*")
        print("Perdiste, Gana el computador!! ")
        break

    tablero[coordjug[0]-1][coordjug[1]-1] = bombasalrededor() 
    if ganar():
        desplegartablero()
        print("Ganaste!!, Completaste el tablero sin que se activara ninguna bomba")
        break