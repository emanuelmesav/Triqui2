


class Tablero:


    def __init__(self):
        #Definir nuestra matriz de 3x3
        self.matriz=[
            ["","",""],
            ["","",""],
            ["","",""]

        ]
    def verificar_Jugada(x,y,self):
       if self.matriz[x][y]=="":
        return True

       else:
        return False
    
    def verificar_triqui(self):
       pass
    def mostrar_tablero(self):
       print(self.matriz)
      
       

       
        