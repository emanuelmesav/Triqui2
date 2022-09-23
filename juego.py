from jugadores import Jugador
from tablero import Tablero


class Juego:


    def __init__(self):
         
         self.miJugador= Jugador()
         self.miTablero= Tablero()
    
    def jugarTriqui(self):
       
        self.miJugador.miFicha.simbolo="x"

        self.miJugador.realizar_jugada(self.miTablero)  
        self.miJugador.realizar_jugada(self.miTablero)  

        print(self.miJugador.realizar_jugada)



miJuego=Juego()
        