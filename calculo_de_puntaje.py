def imprimirPuntajeDelNivel(puntajesPorNivel,nivel):
    print("El puntaje en el nivel es: "+str(puntajesPorNivel[nivel-1]))

def calculoPuntajeTotal(puntajesPorNivel):
    puntajeTotal = 0
    for i in puntajesPorNivel:
        puntajeTotal = i+puntajeTotal
    return puntajeTotal

def calculoPuntajeActual(ganoNivel):
    if (ganoNivel):
        return 500

    elif (ganoNivel == False):
        return (-300)


def calcularPuntajePorReinicio(lucesRestantes):
    return (-50*lucesRestantes)

def imprimirPuntajeTotal(puntajesPorNivel):
    puntajeTotal = puntajesPorNivel[0] + puntajesPorNivel[1] + puntajesPorNivel[2] + puntajesPorNivel[3] + puntajesPorNivel[4]
    print("El puntaje total es de: " + str(puntajeTotal))

def imprimirTodosLosPuntajesDeLosNiveles(puntajesPorNivel):
    contadorNivel = 0
    for i in puntajesPorNivel:
        contadorNivel = contadorNivel + 1
        print("El puntaje obtenido en el nivel " + str(contadorNivel) + " es de " + str(i))


