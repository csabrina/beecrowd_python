while True:
    try:
        sentencaDancante = ""
        sentenca = input()

        maiuscula = True

        for letra in sentenca:
            if letra == " ":
                sentencaDancante += " "
                continue
            if maiuscula:
                sentencaDancante += letra.upper()
                maiuscula = False
            else:
                sentencaDancante += letra.lower()
                maiuscula = True
        print(sentencaDancante)
    except EOFError:
        break