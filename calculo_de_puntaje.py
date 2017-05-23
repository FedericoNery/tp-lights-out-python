def imprimirPuntajeDelNivel(puntajesPorNivel,nivel):
    print("El puntaje en el nivel es: "+str(puntajesPorNivel[nivel-1]))

def calculoPuntajeTotal(puntajesPorNivel):
    puntajeTotal = 0
    for i in puntajesPorNivel:
        puntajeTotal = i+puntajeTotal
    return puntajeTotal

def calculoPuntajeActual(ganoNivel,reinicioNivel,lucesRestantes):
    if (ganoNivel):
        return 500

    elif (ganoNivel == False):
        return (-300)

    if (reinicioNivel):
        return (-50*lucesRestantes)

def imprimirPuntajeTotal(puntajeTotal):
    print("El puntaje total es de: " + str(puntajeTotal))

def imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel,contadorNivel):
    for i in puntajesPorNivel:
        contadorNivel = contadorNivel + 1
        print("El puntaje obtenido en el nivel " + str(contadorNivel) + " es de " + str(i))


