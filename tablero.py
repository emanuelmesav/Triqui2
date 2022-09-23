


class Tablero:


    def __init__(self):
        #Definir nuestra matriz de 3x3
        self.matriz=[
            ["","",""],
            ["","",""],
            ["","",""]

        ]
    def verificarJugada(x,y,self,):

     if x==-1:

        if not self.matriz[x][y]=="":
            return False
        else:
            return True    
        