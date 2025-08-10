from modelo.tateti import Tateti
from modelo.jugador import Jugador
from modelo.excepciones import PosicionInvalidaException, PosOcupadaException, CaracterNoNumericoException

def main():
    print("Bienvenidos al Tateti")
    
    nombre1 = input("Ingrese el nombre del Jugador 1 (X): ")
    nombre2 = input("Ingrese el nombre del Jugador 2 (O): ")

    while True:  # Bucle para repetir el juego
        jugador_x = Jugador(nombre1, "X")
        jugador_o = Jugador(nombre2, "O")
        tateti = Tateti(jugador_x, jugador_o) 

        while True:
            print("\nTablero:")
            print(tateti)
            print(f"\nTurno de {tateti.turno.obtener_nombre()} ({tateti.turno.obtener_simbolo()})")
            
            try:
                fil_str = input("Ingrese la fila (1 a 3): ")
                col_str = input("Ingrese la columna (1 a 3): ")
                
                if not (fil_str.isdigit() and col_str.isdigit()):
                    raise CaracterNoNumericoException()
                
                fil = int(fil_str) - 1
                col = int(col_str) - 1
                
                tateti.ocupar_posicion(fil, col)
                ganador = tateti.obtener_ganador()
                if ganador:
                    print("\nTablero final:")
                    print(tateti)
                    nombre_ganador = jugador_x.obtener_nombre() if ganador == jugador_x.obtener_simbolo() else jugador_o.obtener_nombre()
                    print(f"\n¡Ganó {nombre_ganador} ({ganador})!")
                    break
                
                if not tateti.tablero.hay_espacios_libres():
                    print("\nTablero final:")
                    print(tateti)
                    print("\n¡Empate! No hay más espacios libres.")
                    break

            except PosicionInvalidaException as e:
                print(e)
            except PosOcupadaException as e:
                print(e)
            except CaracterNoNumericoException as e:
                print(e)
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
        
    
        repetir = input("\n¿Quieren jugar otra partida? (s/n): ").strip().lower()
        if repetir != "s":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break


if __name__ == '__main__':
    main()
