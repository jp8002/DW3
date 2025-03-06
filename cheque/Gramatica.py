class Gramatica:
    erros = {
        "e reais" : "reais",
        "e centavos" : "centavos",
        "e mil" : "mil",
        "e bil" : "bil",
        "cem e" : "cento e",
        "um milhões" : "um milhão",
        "milhão reais" : "milhão de reais",
        "milhões reais" : "milhões de reais",
        "um bilhões" : "um bilhão",
        "bilhão reais" : "bilhão de reais",
        "bilhões reais" : "bilhões de reais",
        " e cen" : " cen",
        " e du" : " du",
        " e trezen" : " trezen",
        " e quatroc" : " quatroc",
        " e quinh" : " quinh",
        " e seisc" : " seisc",
        " e setec" : " setec",
        " e oitoc" : " oitoc",
        " e novec" : " novec",
    }
    def corrigir(self, frase):
        
        if frase.startswith("um e reais"):
            frase = frase.replace("um e reais", "um real")
            
        for x in list(self.erros) :
            if x in frase:
                frase = frase.replace(x, self.erros[x])
        
        return frase
                