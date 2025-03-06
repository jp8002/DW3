import math
class Decompor:
    decomposto = []
    
    def decompor(self, valor):
        while(valor != 0):
            if 10 < valor < 20:
                self.decomposto.append(valor)
                break            
            posicao = int(math.log10(valor))
            numero = (valor//10**posicao)*(10**posicao) 
            valor -= (valor//10**posicao)*(10**posicao)
            self.decomposto.append(numero)
        self.decomposto.reverse()
   
        
            