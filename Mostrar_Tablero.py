import operator
def imprimir_Tablero(resultado,dimension_tablero):
    x=0
    y=0
    fila=1
    columna='A'
    recorrido_filas=1
    recorrido_columnas=1
    """
    1 es A  6 es F
    2 es B  7 es G
    3 es C  8 es H
    4 es D  9 es I
    5 es E  10 es J
    """
    while ():
        while (recorrido_filas<=dimension_tablero):
            print(resultado[columna+str(fila)]),
            columna=chr(ord(columna)+1)
        recorrido_filas=1
        columna='A'
        print("\n")

    while resultado[]
    print(resultado[]),
    for i in dimension_tablero:
        print(chr(64+i))
    for i in dimension_tablero:
        print(i)

    fila_0= " A B C D E "
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
    print()

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
resultado = sorted(Diccionario.items(), key=operator.itemgetter(0))
print (resultado)