from Extenso import Extenso

class Cheque:

    def extenso(self, valor):
        
        real, cent = valor.split(".")
        real = int(real)
        cent = int(cent)
        saida=""

        if(real != 0):
            saida += Extenso.escrever(Extenso,real)
            saida += "reais" 
            
            if(cent !=0):
                saida += " e " 
        
        
        if(cent != 0):
            saida += Extenso.escrever(Extenso, cent)
            saida += "centavos" 
            
        return saida
    
    