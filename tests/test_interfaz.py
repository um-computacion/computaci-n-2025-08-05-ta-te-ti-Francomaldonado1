import unittest
from unittest.mock import patch
from interfaz.interfaz import main

class TestInterfaz(unittest.TestCase):

    @patch("builtins.input", side_effect=[
    "Jugador1", "Jugador2",  # nombres
    "a", "2",                # entrada no numérica (debe tirar excepción)
    "1", "1",                # después ingresa bien
    "1", "2",                # jugada siguiente
    "2", "2",                # sigue la partida para terminar
    "1", "3",
    "3", "3"
    ])
    def test_caracter_no_numerico(self, mock_input):
        try:
           main()
        except Exception as e:
           self.fail(f"main() lanzó una excepción inesperada: {e}")


    @patch("builtins.input", side_effect=[
        "Jugador1", "Jugador2",  # nombres
        "1", "1",  # X
        "1", "2",  # O
        "2", "2",  # X
        "1", "3",  # O
        "3", "3"   # X gana
    ])
    def test_ganador_jugador1(self, mock_input):
        try:
            main()
        except Exception as e:
            self.fail(f"main() lanzó una excepción inesperada: {e}")

    @patch("builtins.input", side_effect=[
        "Jugador1", "Jugador2",  # nombres
        "1", "1",  # X
        "1", "2",  # O
        "1", "3",  # X
        "2", "1",  # O
        "2", "3",  # X
        "2", "2",  # O
        "3", "1",  # X
        "3", "3",  # O
        "3", "2"   # X - tablero lleno sin ganador
    ])
    def test_empate(self, mock_input):
        try:
            main()
        except Exception as e:
            self.fail(f"main() lanzó una excepción inesperada: {e}")
