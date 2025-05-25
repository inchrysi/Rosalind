with open("qualcosa.txt", "r") as input, open("risultato.txt", "w") as output:
    for riga in input:
        filamento = riga.strip()
        print(filamento)
        output.write(filamento + "\n")

