from ficha import Ficha

class Jugador:


    def __init__(self):

        self.miFicha=Ficha()
    x=-1
    y=-1
    def realizar_jugada(self,unTablero):
     while unTablero.verificarJugada(x,y)==False:
        
        while x>2 and x<0:
          x=int(input("Ingresa la fila:"))
        
        while y>2 and y<0:
          y=int(input("Ingresa la columna:"))

        
        unTablero.matriz[x][y]= self.miFicha.simbolo 

        return unTablero
        
        