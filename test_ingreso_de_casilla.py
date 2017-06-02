import unittest
import ingreso_de_casilla


class ValidacionIngresoDeCasilleroTestCase(unittest.TestCase):
    def test_ingresoDimensionDelTablero(self):
        self.assertTrue(ingreso_de_casilla.validacionIngresoDeCasillero(5))

    def test_ingresoDimensionDelTablero(self):
        self.assertTrue(ingreso_de_casilla.validacionIngresoDeCasillero(-1))

    def test_ingresoDimensionDelTablero(self):
        self.assertTrue(ingreso_de_casilla.validacionIngresoDeCasillero([]))

    def test_ingresoDimensionDelTablero(self):
        self.assertTrue(ingreso_de_casilla.validacionIngresoDeCasillero(0))

    def test_ingresoDimensionDelTablero(self):
        self.assertTrue(ingreso_de_casilla.validacionIngresoDeCasillero(""))

    def test_ingresoDimensionDelTablero(self):
        self.assertTrue(ingreso_de_casilla.validacionIngresoDeCasillero("AAA"))




class LongitudDeCoordenadaValidaTestCase(unittest.TestCase):
    def test_pasoComoParametroUnSoloNumero(self):
        self.assertFalse(ingreso_de_casilla.longitudDeCoordenadaValida(5))

    def test_pasoComoParametroUnaListaVacia(self):
        self.assertFalse(ingreso_de_casilla.longitudDeCoordenadaValida([]))

    def test_pasoComoParametroUnNumeroNegativo(self):
        self.assertFalse(ingreso_de_casilla.longitudDeCoordenadaValida(-1))

    def test_pasoComoParametroUnStringVacio(self):
        self.assertFalse(ingreso_de_casilla.longitudDeCoordenadaValida(""))

    def test_pasoComoParametroUnStringDeLongitudTres(self):
        self.assertFalse(ingreso_de_casilla.longitudDeCoordenadaValida("AAA"))

    def test_pasoComoParametroUnStringDeLongitudDosConDosCifras(self):
        self.assertFalse(ingreso_de_casilla.longitudDeCoordenadaValida("11"))

    def test_pasoComoParametroUnStringDeLongitudDosConDosLetras(self):
        self.assertFalse(ingreso_de_casilla.longitudDeCoordenadaValida("AA"))

class IngresoDeCoordenadaValidaTestCase(unittest.TestCase):
    def test_pasoComoParametroUnNumero(self):
        self.assertEquals(ingreso_de_casilla.ingresoDeCoordenadaEsReinicio(1))

    def test_pasoComoParametroUnaListaVacia(self):
        self.assertEquals(ingreso_de_casilla.ingresoDeCoordenadaEsReinicio([]))

    def test_pasoComoParametroUnStringDeLongitud3(self):
        self.assertEquals(ingreso_de_casilla.ingresoDeCoordenadaEsReinicio("AAA"))

    def test_pasoComoParametroUnNumeroNegativo(self):
        self.assertEquals(ingreso_de_casilla.ingresoDeCoordenadaEsReinicio(-1))

class letraDeCoordenadaValidaTestCase(unittest.TestCase):
    def test_pasoComoParametroUnNumero(self):
        self.assertEquals(ingreso_de_casilla.letraDeCoordenadaValida(1,1))

    def test_pasoComoParametroUnNumero(self):
        self.assertEquals(ingreso_de_casilla.letraDeCoordenadaValida(1,1))

    def test_pasoComoParametroUnNumero(self):
        self.assertEquals(ingreso_de_casilla.letraDeCoordenadaValida(1,1))

    def test_pasoComoParametroUnNumero(self):
        self.assertEquals(ingreso_de_casilla.letraDeCoordenadaValida(1,1))

    def test_pasoComoParametroUnNumero(self):
        self.assertEquals(ingreso_de_casilla.letraDeCoordenadaValida(1,1))

    def test_pasoComoParametroUnNumero(self):
        self.assertEquals(ingreso_de_casilla.letraDeCoordenadaValida(1,1))

    def test_pasoComoParametroUnNumero(self):
        self.assertEquals(ingreso_de_casilla.letraDeCoordenadaValida(1,1))

    def test_pasoComoParametroUnNumero(self):
        self.assertEquals(ingreso_de_casilla.letraDeCoordenadaValida(1,1))
