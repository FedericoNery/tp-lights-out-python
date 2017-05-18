def calculoPuntaje(ganoNivel, nivel, lucesRestantes, reinicioNivel, puntajeActual, puntajesPorNivel):
    puntajeTotal=0
    if(ganoNivel):
         puntajeActual=puntajeActual+500

    elif(ganoNivel==False):
         puntajeActual=puntajeActual-300

    if(reinicioNivel):
         puntajeActual=puntajeActual-50*lucesRestantes

    puntajesPorNivel[nivel-1]=puntajeActual+puntajesPorNivel[nivel-1]

    for i in puntajesPorNivel:
        puntajeTotal=i+puntajeTotal

    return(puntajesPorNivel[nivel-1],puntajeTotal,puntajesPorNivel)


def calculoPuntajeTotal(puntajesPorNivel):
    for i in puntajesPorNivel:
        puntajeTotal=i+puntajeTotal
    return puntajeTotal

def calculoPuntajeActual(ganoNivel,reinicioNivel,lucesRestantes):
    if (ganoNivel):
        return 500

    elif (not ganoNivel):
        return (-300)

    if (reinicioNivel):
        return (-50*lucesRestantes)




