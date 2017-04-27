import operator
import string
def sacarCaracteresResiduales(linea_acumulada):
    """t = []
    for i in range(fila):
        t.append([0] * columna)

    for i in t:
        print
        i"""

    linea_final=[]
    for i in linea_acumulada:
        linea_final.append([0]*columna)
    print(linea_final)

def imprimir_Primer_Fila(dimension):
    if(dimension==5):
        print('A','B','C','D','E')
    elif(dimension==6):
        print('A', 'B', 'C', 'D','E','F')
    elif(dimension==7):
        print('A', 'B', 'C', 'D', 'E','F','G')
    elif(dimension==8):
        print('A', 'B', 'C', 'D', 'E','F','G','H')
    elif(dimension==9):
        print('A', 'B', 'C', 'D', 'E','F','G','H','I')
    elif(dimension==10):
        print('A', 'B', 'C', 'D', 'E','F','G','H','I','J')

def imprimir_Tablero(resultado,dimension_tablero):
    """
       1 es A  6 es F
       2 es B  7 es G
       3 es C  8 es H
       4 es D  9 es I
       5 es E  10 es J
       """
    linea_acumulada=[]
    recorrido_filas=1
    recorrido_columnas=1
    Diccionario=resultado
    dimension=dimension_tablero
    imprimir_Primer_Fila(dimension)
    while(recorrido_filas<=dimension):

        while (recorrido_columnas<=dimension):#Columna 1 Columna 2 Columna 3
            fila=str(recorrido_filas)
            columna=chr(recorrido_columnas+64)
            elemento=Diccionario[(columna+fila)]
            linea_acumulada.append(elemento)
            if(recorrido_columnas==dimension):
                sacarCaracteresResiduales(linea_acumulada)
               # linea_acumulada=sacarCaracteresResiduales(linea_acumulada)
               # print(linea_acumulada)
            #print(Diccionario[(columna+fila)])#Imprimo el elemento del diccionario con clave A1
            recorrido_columnas=recorrido_columnas+1#Paso a la segunda columna
        linea_acumulada=[]
        recorrido_filas=recorrido_filas+1
        recorrido_columnas=1

    """
        x0  x1  x2  x3  x4  x5  x6
    y0      A   B   C   D   E   F

    y1  1|

    y2  2|

    y3  3|

    y4  4|

    y5  5|

    y6


    """
    return (0)

def modo_Predeterminado_LV1(dimension_tablero):
    Diccionario={}
    ultima_fila_numero=dimension_tablero
    ultima_columna_letra=str(chr(dimension_tablero+64))
    fila=1
    columna='A'
    while(columna<=ultima_columna_letra):#Columna vale A
        while(fila<=dimension_tablero):
            Diccionario[columna+str(fila)]='O'
            fila=fila+1
        fila=1
        columna=ord(columna)+1
        columna=chr(columna)

    #print(str(ultima_fila_numero)+ultima_columna_letra)
    return(Diccionario)

dimension_tablero=5
Diccionario=modo_Predeterminado_LV1(dimension_tablero)
#resultado = sorted(Diccionario.items(), key=operator.itemgetter(0))
#print (resultado)
#print(Diccionario)
imprimir_Tablero(Diccionario,dimension_tablero)