import menu_de_inicio
import ingreso_de_casilla
import modificadorTablero
import mostrar_tablero
import niveles_predeterminados
import niveles_aleatorios
import calculo_de_puntaje
import prueba_solo_por_turnos
import sys

def principal():
    modoYDimension=menu_de_inicio.menu_de_inicio()
    if(modoYDimension[0]=="Predeterminado"):
        prueba_solo_por_turnos.principalPredeterminado()
    elif(modoYDimension[0]=="Aleatorio"):
        prueba_solo_por_turnos.principalAleatorio(modoYDimension)

principal()