class PosOcupadaException(Exception):
    def __init__(self, mensaje="Esa posición ya está ocupada. Por favor, elija otra."):
        super().__init__(mensaje)

class PosicionInvalidaException(Exception):
    def __init__(self, mensaje="Posición fuera del tablero."):
        super().__init__(mensaje)

class CaracterNoNumericoException(Exception):
    def __init__(self, mensaje="Debe ingresar un número. No se permiten letras ni símbolos."):
        super().__init__(mensaje)
