import random
from mostrar_tablero import imprimirTablero

def generarTableroAleatorio(dimensionTablero):
    tablero = {}
    estadosAleatoriosDeLuces=[]
    posiblesEstadosDeLuces=['O','.']
    indiceEstadosAleatoriosDeLuces=0
    cantidadTotalDeCasillas= dimensionTablero ** 2

    for i in range(cantidadTotalDeCasillas):
        estadoDefinidoDeLaLuz=random.choice(posiblesEstadosDeLuces)
        estadosAleatoriosDeLuces.append(estadoDefinidoDeLaLuz)
    random.shuffle(estadosAleatoriosDeLuces)
    letraDeLaUltimaColumnaDelTablero = str(chr(dimensionTablero + 64))
    numeroDeLaFilaAnalizada = 1
    letraDeLaColumnaAnalizada = 'A'

    while (letraDeLaColumnaAnalizada <= letraDeLaUltimaColumnaDelTablero):  # Columna vale A
        while (numeroDeLaFilaAnalizada <= dimensionTablero):
            tablero[letraDeLaColumnaAnalizada + str(numeroDeLaFilaAnalizada)] = estadosAleatoriosDeLuces[indiceEstadosAleatoriosDeLuces]
            indiceEstadosAleatoriosDeLuces=indiceEstadosAleatoriosDeLuces+1
            numeroDeLaFilaAnalizada = numeroDeLaFilaAnalizada + 1
        numeroDeLaFilaAnalizada = 1
        letraDeLaColumnaAnalizada = ord(letraDeLaColumnaAnalizada) + 1
        letraDeLaColumnaAnalizada = chr(letraDeLaColumnaAnalizada)

    return (tablero)

