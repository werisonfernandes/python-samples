with open("../Temp/teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open("../Temp/teste.txt", "a") as arquivo:
    arquivo.write("\nContinuação do texto.")

with open("../Temp/teste.txt", "r") as arquivo:
    print(arquivo.read())

with open("../Temp/teste.txt", "r+t") as arquivo:
    print(arquivo.read())

with open("../Temp/teste.txt", "r+b") as arquivo:
    print(arquivo.read())

with open("../Temp/teste2.txt", "x") as arquivo:
    arquivo.write("Continuação do texto.")

with open("../Temp/teste2.txt", "r+b") as arquivo:
    print(arquivo.read())