class PosOcupadaException(Exception):
    def __init__(self, mensaje="Esa posición ya está ocupada. Por favor, elija otra."):
        super().__init__(mensaje)

class PosicionInvalidaException(Exception):
    def __init__(self, mensaje="Posición fuera del tablero."):
        super().__init__(mensaje)


class FichaInvalidaException(Exception):
    def __init__(self, mensaje="Ficha inválida. Debe ser 'X' o 'O'."):
        super().__init__(mensaje)


class TurnoInvalidoException(Exception):
    def __init__(self, mensaje="No es el turno de este jugador."):
        super().__init__(mensaje)


class JuegoFinalizadoException(Exception):
    def __init__(self, mensaje="El juego ya terminó."):
        super().__init__(mensaje)

class CaracterNoNumericoException(Exception):
    def __init__(self, mensaje="Debe ingresar un número. No se permiten letras ni símbolos."):
        super().__init__(mensaje)
