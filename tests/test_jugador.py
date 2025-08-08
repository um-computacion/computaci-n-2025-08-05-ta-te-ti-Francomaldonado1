import unittest
from modelo.jugador import Jugador

class TestJugador(unittest.TestCase):

    def test_jugador_con_nombre_y_simbolo_X(self):
        jugador = Jugador("Franco", "X")
        self.assertEqual(jugador.obtener_nombre(), "Franco")
        self.assertEqual(jugador.obtener_simbolo(), "X")
        self.assertEqual(str(jugador), "Franco")

    def test_jugador_con_nombre_y_simbolo_O(self):
        jugador = Jugador("Lucía", "O")
        self.assertEqual(jugador.obtener_nombre(), "Lucía")
        self.assertEqual(jugador.obtener_simbolo(), "O")
        self.assertEqual(str(jugador), "Lucía")

    def test_jugador_con_nombre_con_espacios(self):
        jugador = Jugador("Juan Pérez", "X")
        self.assertEqual(jugador.obtener_nombre(), "Juan Pérez")
        self.assertEqual(jugador.obtener_simbolo(), "X")
        self.assertEqual(str(jugador), "Juan Pérez")

if __name__ == '__main__':
    unittest.main()
