usuarios = {}
opcao = input("O que deseja realizar?\n" +
              "<I> - Para Inserir um usuário\n" +
              "<P> - Para Pesquisar um usuário\n" +
              "<E> - Para Excluir um usuário\n" +
              "<L> - Para Listar um usuário: ").upper()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        chave = input("Digite o login: ").upper()
        nome = input("Digite o nome: ").upper()
        data = input("Digite a última data de acesso: ")
        estacao = input("Qual a última estação acessada: ").upper()
        usuarios[chave] = [nome, data, estacao]
        opcao = input("O que deseja realizar?\n" +
                      "<I> - Para Inserir um usuário\n" +
                      "<P> - Para Pesquisar um usuário\n" +
                      "<E> - Para Excluir um usuário\n" +
                      "<L> - Para Listar um usuário: ").upper()
