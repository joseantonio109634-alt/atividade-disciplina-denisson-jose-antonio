alunos[]

while True:
    print("\n=== Menu ===")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        alunos.append(nome)
        print("Aluno cadastrado")

    elif opcao == "2":
        print("\nLista de alunos:")
        for aluno in alunos:
            print("-", aluno)

    elif opcao == "3":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")