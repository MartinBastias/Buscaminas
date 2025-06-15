#Tarea Semestral Buscaminas G17
#Nombres: Martin Ignacio Bastias Neira, Matias Ignacio Cabello Carvajal, Felipe Ignacio Castro Castillo
import random
coordjug = [0, 0] #Coordenadas iniciales
posicionb = [] #Posicion de las bombas en el tablero
tablero = [] #Lista que se modifica dentro del programa que produce el tablero


def Leevalentero(txt): #Asegura que la entrada sea un valor entero, mostrando error si no lo es
    while True:
        try:
            x = input(txt) 
            int(x) #Pasar el input a entero, si marca error, despliega un mensaje y se renicia
            break
        except ValueError:
            print('Error, valor ingresado debe ser un numero entero')
    return int(x)

def leeValidaGeneral(txt, m, M): #Valida que la entrada sea entera y que este en el rango deseado.
    n = Leevalentero(f'Ingrese {txt}: ')
    while not m <= n <= M:
        print(f"Error. Reingresa {txt} y asegurate de que la entrada este entre {m} y {M}")
        n = Leevalentero(f'Ingrese {txt}: ')
    return n



#Generar posicion de bobmbas
def pb():
    return  random.randint(1, filas), random.randint(1, columnas) 

def prepararBombas(): #Añade una bomba en una posicion aleatoria hasta que se ingresen la cantidad maxima de bombas
    for i in range (cb):
        posicionb.append(pb())
        for p in posicionb:
            tablero[p[0]-1][p[1]-1] = '*'
    
def bombasalrededor(): #Chequea la cantidad de bombas alrededor de una posicion dada
    b = 0
    alrededor = [(-1, -1), (-1, 0), (-1, 1), # estas son todas las traslaciones alrededor, les mande un dibujo con la idea
                 (0, -1),           (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    for i in alrededor:
        rf = (coordjug[0]-1) + i[0] # revisar filas
        rc = (coordjug[1]-1) + i[1] # columnas
        if (0 <= rf <= filas-1) and (0 <= rc <= columnas-1): # por temas de com ose lee la lista se debe restar 1 al rango de posiciones
            if tablero[rf][rc] == '*':
                b +=1
    return b

def perderosguir():
    if tablero[coordjug[0]-1][coordjug[1]-1] == '*':
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
            f+=(str(i).replace('*', '#'))
        print(f)

def crearTablero():
    for i in range (filas):
        tablero.append([])
    for i in tablero:
        for x in range(columnas):
            i.append("#")
            
#Ingreso de Variables para el Tablero y implementacion de bombas
filas = leeValidaGeneral('Cantidad de filas',3, 15)
columnas = leeValidaGeneral('Cantidad de columnas',3, 15)
crearTablero()
cb = leeValidaGeneral('Cantidad de bombas',1,int(filas*columnas/4))
prepararBombas()

#Previene que existan bombas repetidas, "loopeando" hasta que no se repitan
while len(set(posicionb)) < len(posicionb): 
    tablero.clear()
    crearTablero()
    posicionb.clear()
    prepararBombas()
    if len(set(posicionb)) == len(posicionb):
        break

#Esto es informacion para nosotros, sirve como un 'debug' de la cantidad de bombas u sus posiciones
#print(cb) 
#print(posicionb)

#Bucle del juego
while True:
    desplegartablero()
    coordjug[0],coordjug[1] = leeValidaGeneral('fila',1,filas),leeValidaGeneral('columna',1,columnas)
    
    if perderosguir() == False: #Evalua que se haya pisado una bomba, entregando False si se hizo y True cuando no.
        for i in range(filas):
            print(columnas*"*")
        print("Perdiste, Gana el computador!! ")
        break

    tablero[coordjug[0]-1][coordjug[1]-1] = bombasalrededor() # Esta linea hay que dejarla si o si despues de verificar si se pierde
    if ganar() == False:
        desplegartablero()
        print("Ganaste!!, Completaste el tablero sin que se activara ninguna bomba")
        break