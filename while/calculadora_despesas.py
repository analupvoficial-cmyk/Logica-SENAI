opcao = 1
quantidade = 0
valor_total = 0
while opcao > 0:
    print("Selecione a tarefa que deseja realizar.")
    print("[0] Sair")
    print("[1] Adicionar valor da despesa.")
    print("[2] Mostrar a quantidade de despesas e o valor total.")
    print("[3] Dividir com mais pessoas.")
    opcao = int(input("Selecione uma opção: "))
    if opcao == 1:
        valor = float(input("Selecione o valor da despesa: "))
        valor_total = valor_total + valor
        quantidade += 1
    elif opcao == 2:
        print(f"Você possui {quantidade} despesas e seu valor total é {valor_total}")
    elif opcao == 3:
        pessoas = int(input("Deseja dividir com quantas pessoas?: "))
        valor_dividido = valor_total / pessoas
        print(f"Cada pessoa irá pagar {valor_dividido}$")
     