def Modo_Predeterminado_LV1(dimension_tablero):
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
print(Modo_Predeterminado_LV1(dimension_tablero))
