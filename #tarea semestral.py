#tarea semestral
import random

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
def generarBombas():
    return random.randint(1, int((filas*columnas)/4)) 

#generar tablero



filas, columnas = leeValida(3, 15)
print(generarBombas())