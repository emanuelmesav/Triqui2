


class Tablero:


    def __init__(self):
        #Definir nuestra matriz de 3x3
        self.matriz=[
            ["","",""],
            ["","",""],
            ["","",""]

        ]
        for fila in self.matriz:

         print(fila)
    def verificar_Jugada(self,x,y):
       if x==-1:
         return False
       
       if self.matriz[x][y]=="":
        return True
       

       else:
        return False
    
    def verificar_triqui(self):
       for fila in range (3):
         if self.matriz[fila][0]==self.matriz[fila][1] and self.matriz[fila][0]==self.matriz[fila][2] and not self.matriz[fila][0]=="":
            return True
       for columna in range (3):
         if self.matriz[0][columna]==self.matriz[1][columna] and self.matriz[0][columna]==self.matriz[2][columna] and not self.matriz[0][columna]=="":
            return True
       if self.matriz[0][0]==self.matriz[1][1] and self.matriz[0][0]==self.matriz[2][2] and not self.matriz[1][1]=="":
            return True
       if self.matriz[0][2]==self.matriz[1][1] and self.matriz[0][2]==self.matriz[2][0] and not self.matriz[1][1]=="":
            return True
            
       return False

       
    def mostrar_tablero(self):

      for fila in self.matriz:

       print(fila)
      
       

       
        