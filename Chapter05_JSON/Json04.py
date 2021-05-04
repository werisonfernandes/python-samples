# -*- encoding: utf-8
from Functions.JsonFunctions import *
inventario = ler_arquivo("../Temp/inventario_json.json")
opcao=chamarMenu()
while 0 < opcao < 3:
    if opcao==1:
        print(registrar(inventario, "../Temp/inventario_json.json"))
    elif opcao==2:
        exibir("../Temp/inventario_json.json")
    opcao = chamarMenu()
