def calculoPuntaje(ganonivel,nivel,lucesRestantes,reset,puntajeActual,puntajesPorNivel):
    puntajeTotal=0
    if(ganonivel==True):
         puntajeActual=puntajeActual+500
    elif(ganonivel==False):
         puntajeActual=puntajeActual-300
    if(reset==True):
         puntajeActual=puntajeActual-50*lucesRestantes#Asegurarse que lucesRestantes sea un entero
    puntajesPorNivel[nivel-1]=puntajeActual+puntajesPorNivel[nivel-1]
    for i in puntajesPorNivel:
        puntajeTotal=i+puntajeTotal
    return(puntajesPorNivel[nivel-1],puntajeTotal,puntajesPorNivel)
