equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for equipamento in equipamentos:
    print("Equipamento: ", equipamento)

for valor in valores:
    print("Valor: ", valor)

for serial in seriais:
    print("Serial: ", serial)

for departamento in departamentos:
    print("Departamento: ", departamento)
