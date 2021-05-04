# -*- coding: iso-8859-15 -*

with open("../Temp/teste.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("Tipo de dado da vari�vel", type(conteudo))
print("\nConte�do do arquivo:\n", conteudo)

# Read + Bytes (r+b)
with open("../Temp/teste.txt", "rb") as arquivo:
    conteudo = arquivo.read()

print("Tipo de dado da vari�vel", type(conteudo))
print("\nConte�do do arquivo:\n", conteudo)

# Read + Bytes (r+b) => ReadLines
with open("../Temp/teste.txt", "rb") as arquivo:
    conteudo = arquivo.readlines()

print("Tipo de dado da vari�vel", type(conteudo))
print("\nConte�do do arquivo:\n", conteudo)

print("\n********************************************")
# Read + Bytes (r+b) => ReadLine
with open("../Temp/teste.txt", "rb") as arquivo:
    conteudo = arquivo.readline()
    conteudos = conteudo

    while conteudo:
        conteudo = arquivo.readline()
        conteudos += conteudo

print("Tipo de dado da vari�vel", type(conteudos))
print("\nConte�do do arquivo:\n", conteudos)
