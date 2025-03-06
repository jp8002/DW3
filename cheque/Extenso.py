from Decompor import Decompor
import math
class Extenso:
    unicos = {
            1: "um",
            2: "dois",
            3: "três",
            4: "quatro",
            5: "cinco",
            6: "seis",
            7: "sete",
            8: "oito",
            9: "nove",
            10: "dez",
            11: "onze",
            12: "doze",
            13: "treze",
            14: "quatorze",
            15: "quinze",
            16: "dezesseis",
            17: "dezessete",
            18: "dezoito",
            19: "dezenove",
            20: "vinte",
            30: "trinta",
            40: "quarenta",
            50: "cinquenta",
            60: "sessenta",
            70: "setenta",
            80: "oitenta",
            90: "noventa",
            100: "cem",
            200: "duzentos",
            300: "trezentos",
            400: "quatrocentos",
            500: "quinhentos",
            600: "seiscentos",
            700: "setecentos",
            800: "oitocentos",
            900: "novecentos",
            1000: "mil",

        }
    
    @staticmethod
    def escrever(self, valor):
        posicao = math.log10(valor)
        saida = ""
        dec = Decompor()
        
        
        if(9 <= posicao < 12):
            nvalor = valor//1000000000
            valor -= nvalor * 1000000000
            saida += self.escrever(Extenso, nvalor) + "bilhões e "
        
        if(valor == 0):
            return saida
        
        posicao = math.log10(valor)
            
        if(6 <= posicao < 9):
            nvalor = valor//1000000
            valor -= nvalor * 1000000
            saida += self.escrever(Extenso, nvalor) + "milhões e "
            
        if(valor == 0):
            return saida
        
        posicao = math.log10(valor)

        if(3 <= posicao < 6 and valor >=2000):
            nvalor = valor//1000
            valor -= nvalor * 1000
            saida += self.escrever(Extenso, nvalor) + "mil e "
        
        
        dec.decompor(valor)
        while len(dec.decomposto) != 0 :
            saida +=  self.unicos[dec.decomposto.pop()] + " "
            saida += "e "
        return saida