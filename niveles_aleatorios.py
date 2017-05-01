import random
from mostrar_tablero import imprimir_Tablero
def generarTablerosConLuces(dimension_tablero):
    Diccionario = {}
    listaValoresAleatorios=[]
    listaPosiblesValores=['O','.']
    j=0
    cantidadDeCasillas=dimension_tablero**2
    for i in range(cantidadDeCasillas):
        valor=random.choice(listaPosiblesValores)
        listaValoresAleatorios.append(valor)
    random.shuffle(listaValoresAleatorios)
    ultima_fila_numero = dimension_tablero
    ultima_columna_letra = str(chr(dimension_tablero + 64))
    fila = 1
    columna = 'A'
    while (columna <= ultima_columna_letra):  # Columna vale A
        while (fila <= dimension_tablero):
            Diccionario[columna + str(fila)] = listaValoresAleatorios[j]
            j=j+1
            fila = fila + 1
        fila = 1
        columna = ord(columna) + 1
        columna = chr(columna)

    return (Diccionario)


dimension_tablero=6
Diccionario=generarTablerosConLuces(dimension_tablero)
print(imprimir_Tablero(Diccionario,dimension_tablero))
