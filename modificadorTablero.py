from niveles_aleatorios import generarTablerosConLuces
from ingreso_de_casilla import validacionIngresoDeCasillero
from mostrar_tablero import imprimir_Tablero
def modificoTablero(Diccionario,Casilla):
    #Cuatro casilleros alrededor del central
    filaCasillaCentral=Casilla[1]
    columnaCasillaCentral=Casilla[0]
    """ Casilla Central"""
    if(Diccionario.get(Casilla,[])=='O'):
        Diccionario[Casilla]='.'
    else:
        Diccionario[Casilla]='O'
    """ Casilla a la izquierda de la Central """
    casillaALaIzquierda= chr(ord(columnaCasillaCentral)-1)+filaCasillaCentral
    if(Diccionario.get(casillaALaIzquierda,[])=='O'):
        Diccionario[casillaALaIzquierda]='.'
    else:
        Diccionario[casillaALaIzquierda]='O'
    """ Casilla a la derecha de la Central """
    casillaALaDerecha = chr(ord(columnaCasillaCentral)+1)+filaCasillaCentral
    if(Diccionario.get(casillaALaDerecha,[])=='O'):
        Diccionario[casillaALaDerecha]='.'
    else:
        Diccionario[casillaALaDerecha]='O'
    """Casilla superior a la Central"""
    casillaSuperior= columnaCasillaCentral + str(int(filaCasillaCentral)-1)
    if(Diccionario.get(casillaSuperior,[])=='O'):
        Diccionario[casillaSuperior]='.'
    else:
        Diccionario[casillaSuperior]='O'
    """Casilla inferior a la Central"""
    casillaInferior = columnaCasillaCentral + str(int(filaCasillaCentral)+1)
    if(Diccionario.get(casillaInferior, [])=='O'):
        Diccionario[casillaInferior]='.'
    else:
        Diccionario[casillaInferior]='O'
    return (Diccionario)



