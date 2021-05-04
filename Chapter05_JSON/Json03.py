# -*- encoding: utf-8
import json
import os

inventario={}
if os.path.exists("../Temp/inventario_json.json"):
    with open("../Temp/inventario_json.json", "r") as arq_json:
        inventario = json.load(arq_json)

opcao=int(input("Digite: \n<1> para registrar ativo"
 "\n<2> para exibir ativos armazenados: "))

while 0 < opcao < 3:
    if opcao==1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
            resp = input("Digite <S> para continuar.").upper()
        with open("../Temp/inventario_json.json", "w") as arq_json:
            json.dump(inventario, arq_json)
        print("JSON gerado!!!!")
    elif opcao==2:
        for chave, dado in inventario.items():
            print("Data.........: ", dado[0])
            print("Descrição....: ", dado[1])
            print("Departamento.: ", dado[2])
    opcao = int(input("Digite: "
    "\n<1> para registrar ativo"
    "\n<2> para exibir ativos armazenados: "))