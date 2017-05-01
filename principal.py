import menu_de_inicio
import ingreso_de_casilla
import modificadorTablero
import mostrar_tablero
import niveles_predeterminados
import niveles_aleatorios

def principal():
    modoYDimension=menu_de_inicio.menu_de_inicio()
    if(modoYDimension[0]=="Predeterminado"):
        diccionario_tablero=niveles_predeterminados.niveles_predeterminados(1)
        mostrar_tablero.imprimir_Tablero(diccionario_tablero,modoYDimension[1])
    elif(modoYDimension[0]=="Aleatorio"):
        diccionario_tablero=niveles_aleatorios.generarTablerosConLuces(modoYDimension[1])
        mostrar_tablero.imprimir_Tablero(diccionario_tablero,modoYDimension[1])

principal()