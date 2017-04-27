import sys
def mensaje_de_bienvenida():
    print("|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|")
    print("| B B B    I   E E E  NN    N V       V E E E  NN    N  I  D D D     O O O          A     |")
    print("| B   B    I   E      N N   N  V     V  E      N N   N  I  D     D  O     O        A A    |")
    print("| B B B B  I   E E E  N  N  N   V   v   E E E  N  N  N  I  D     D  O     O       A   A   |")
    print("| B     B  I   E      N   N N    V V    E      N   N N  I  D     D  O     O      A A A A  |")
    print("| B B B B  I   E E E  N    NN     V     E E E  N    NN  I  D D D     O O O      A       A |")
    print("|                                                                                         |")
    print("| L      U     U   C C C  E E E   S S S      F F F  U     U  E E E  R R R       A         |")
    print("| L      U     U  C       E      S           F      U     U  E      R    R     A A        |")
    print("| L      U     U  C       E E E   S S S      F F F  U     U  E E E  R R R     A   A       |")
    print("| L      U     U  C       E            S     F      U     U  E      R   R    A A A A      |")
    print("| L L L   U U U    C C C  E E E   S S S      F       U U U   E E E  R    R  A       A     |")
    print("|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|\n")





def menu_de_inicio():
    """ Interfaz de inicio del juego para seleccionar entre modo aleatorio o predeterminado. Dentro del modo
    aleatorio se podrá seleccionar la dimension del tablero"""
    dimension_tablero=0
    sub_validacion = False
    sub_valor=0
    valor=0
    modo=0
    validacion=False
    mensaje_de_bienvenida()
    print("1.JUGAR ")
    print("2.SALIR \n")
    while(validacion==False):
        valor=input("Ingrese el valor numerico de lo que desea hacer ")
        if(valor=='1'):
            validacion=True
        elif(valor=='2'):
            validacion=False
            sys.exit()
        else:
            validacion=False
            print ("Error")
    print ("1.MODO ALEATORIO")
    print ("2.MODO PREDETERMINADO\n")
    validacion=False
    while(validacion==False):
        valor=input("Ingrese el numero correspondiente a la accion que desea realizar ")
        if(valor=='1'):
            validacion=True
            modo = "Aleatorio"
            print ("5. Tablero de 5x5")
            print ("6. Tablero de 6x6")
            print ("7. Tablero de 7x7")
            print ("8. Tablero de 8x8")
            print ("9. Tablero de 9x9")
            print ("10. Tablero de 10x10\n")
            while(sub_validacion==False):
                sub_valor=str(input("Ingrese el numero correspondiente a la dimension del tablero en la que desea jugar "))
                if((sub_valor=='5') or (sub_valor=='6')or (sub_valor == '7') or (sub_valor == '8') or (sub_valor == '9')or (sub_valor=='10')):
                    sub_validacion=True
                    dimension_tablero=sub_valor
                    print ("Se determino jugar al modo aleatorio "+",la dimension sera de: "+str(dimension_tablero)+" x "+str(dimension_tablero))
                else:
                    sub_validacion=False
                    print ("Error")
        #Llamar a la funcion modo aleatorio
        elif(valor=='2'):
            validacion=True
            print ("Se determino jugar al modo predeterminado \n")
            modo = "Predeterminado"
            dimension_tablero=5
        #Llamar a la funcion modo predeterminado
        else:
            validacion=False
            print ("Error")
    return (modo,dimension_tablero)
menu_de_inicio()

