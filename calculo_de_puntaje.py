def calculo_de_puntaje(puntaje_acumulado,nivel_actual,movimientos_restantes,estado_nivel,luces_prendidas,dimension_tablero):
    puntaje_nivel=[]
    if(movimientos_restantes==0):
        puntaje_acumulado=puntaje_acumulado-300
    if(estado_nivel=="Ganado"):
        puntaje_acumulado=puntaje_acumulado+500
        puntaje_nivel[nivel_actual]=puntaje_acumulado
    elif(estado_nivel=="Reiniciado"):
        puntaje_acumulado=puntaje_acumulado-50*luces_prendidas
        movimientos_restantes=3*dimension_tablero

    return (puntaje_acumulado,puntaje_nivel[nivel_actual])

a=calculo_de_puntaje(100,1,0,"Ganado",0,5)
print (a)
a=calculo_de_puntaje(a,2,0,"Ganado",0,5)
print (a)
a=calculo_de_puntaje(a,3,0,"Ganado",0,5)
print (a)
a=calculo_de_puntaje(a,4,0,"Ganado",0,5)
print (a)
a=calculo_de_puntaje(a,5,0,"Ganado",0,5)
