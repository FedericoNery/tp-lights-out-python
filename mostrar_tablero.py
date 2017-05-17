import operator
import string
def sacarCaracteresResiduales(estadosDeLucesDeLaFilaAnalizada):
    filaConLucesEncendidasApagadas = ""
    for i in estadosDeLucesDeLaFilaAnalizada:
        filaConLucesEncendidasApagadas = filaConLucesEncendidasApagadas + i +" "
    return (filaConLucesEncendidasApagadas)

def imprimirFilaSuperiorDelTablero(dimensionTablero):
    lineaSuperiorDelTablero=""
    for i in range (0, dimensionTablero):
        lineaSuperiorDelTablero=lineaSuperiorDelTablero+" "+chr(65+i)
    lineaSuperiorDelTablero=" "+lineaSuperiorDelTablero
    print(lineaSuperiorDelTablero)

def imprimir_Tablero(tableroConLuces, dimensionTablero):
    """
       1 es A  6 es F
       2 es B  7 es G
       3 es C  8 es H
       4 es D  9 es I
       5 es E  10 es J
       """
    estadosDeLucesDeLaFilaAnalizada=[]
    numeroDeFilaQueAnalizo=1
    numeroDeColumnaQueAnalizo=1
    imprimirFilaSuperiorDelTablero(dimensionTablero)
    while(numeroDeFilaQueAnalizo<=dimensionTablero):
        while (numeroDeColumnaQueAnalizo<=dimensionTablero):#Columna 1 Columna 2 Columna 3
            fila=str(numeroDeFilaQueAnalizo)
            columna=chr(numeroDeColumnaQueAnalizo+64)
            estadoDeLuzDeLaCasillaAnalizada=tableroConLuces[(columna+fila)]
            estadosDeLucesDeLaFilaAnalizada.append(estadoDeLuzDeLaCasillaAnalizada)
            if(numeroDeColumnaQueAnalizo==dimensionTablero):
                sacarCaracteresResiduales(estadosDeLucesDeLaFilaAnalizada)
                print(str(numeroDeFilaQueAnalizo)+"|"+sacarCaracteresResiduales(estadosDeLucesDeLaFilaAnalizada))
            numeroDeColumnaQueAnalizo=numeroDeColumnaQueAnalizo+1#Paso a la segunda columna
        estadosDeLucesDeLaFilaAnalizada=[]
        numeroDeFilaQueAnalizo=numeroDeFilaQueAnalizo+1
        numeroDeColumnaQueAnalizo=1
    return("")

