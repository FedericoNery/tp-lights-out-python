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
    puntajeTotal=0
    for i in puntajesPorNivel:
        puntajeTotal=i+puntajeTotal
    return puntajeTotal

def calculoPuntajeActual(ganoNivel,reinicioNivel,lucesRestantes):
    if (ganoNivel):
        return 500

    elif (ganoNivel==False):
        return (-300)

    if (reinicioNivel):
        return (-50*lucesRestantes)

def imprimirEncabezadoTablaPuntajesFinales(puntajeTotal):
    print("")
    print("TABLA DE PUNTAJES FINALES: ")
    print("El puntaje total es de: " + str(puntajeTotal))

def imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel,contadorNivel):
    for i in puntajesPorNivel:
        contadorNivel = contadorNivel + 1
        print("El puntaje obtenido en el nivel " + str(contadorNivel) + " es de " + str(i))


