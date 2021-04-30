# lista preenchida estaticamente
lista_estatica = ["xpto", True]
# lista preenchida dinamicamente
lista_dinamica = [input("Digite o usuário: "), bool(int(input("Está logado? ")))]
# lista vazia
lista_vazia = []
# lista nula
list1 = None
print(list1)

if list1 is None:
    list1 = [10]

list1.append(20)

print(list1)