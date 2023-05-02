while True:
    try:
        texto = input()
        
        aberturaI = False
        aberturaB = False
        novoTexto = ""

        for letra in texto:
            if letra == "_":
                if aberturaI:
                    letra = "</i>"
                    aberturaI = False
                else:
                    letra = "<i>"
                    aberturaI = True

            if letra == "*":
                if aberturaB:
                    letra = "</b>"
                    aberturaB = False
                else:
                    letra = "<b>"
                    aberturaB = True
            
            novoTexto += letra

        print (novoTexto)
    except EOFError:
        break