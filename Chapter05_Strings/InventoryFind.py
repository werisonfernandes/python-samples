from Functions.FileFunctions import *
inventario = {}
opcao = chamarMenu()
while 0 < opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
    for linha in resultado:
        print(linha[linha.find(";") + 1:-1])
    opcao = chamarMenu()