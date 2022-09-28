from typing_extensions import Self
from Ficha import Ficha
import random

class Jugador:


    def __init__(self):

        self.miFicha=Ficha()
   
    def realizar_jugada(self,untablero):
        x=int(input("Ingrese una fila"))

        y=int(input("Ingrese una columna"))

        untablero.matriz[x],[y]=self.miFicha.simbolo
        return untablero

    def seleccionar_simbolo(self):
        x=random.randint(0,1)
        if x== 0:
          self.miFicha.simbolo='O'
        else:
          self.miFicha.simbolo='X'

                      
        