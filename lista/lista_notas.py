import time
from colorama import Fore
print(Fore.LIGHTMAGENTA_EX + "Olá! Como podemos ajudar?")
print("")
opcao = ""
notas = []
while opcao != 0 :
    time.sleep(1)
    print("[1] Cadastrar notas")
    print("[2] Exibir notas em ordem crescente")
    print("[3] Média das notas")
    print("[4] Maior e menor nota")
    print("[5] Quantidade de notas") 
    print("[0] Sair")
    opcao = input("Informe o que deseja realizar: ")
    if opcao == "1":
        nota = float(input("Informe sua nota: "))
        print(f"Sua notas é {nota} e foi cadastrada!")
        notas.append(nota)
    elif opcao == "2":
        notas.sort()
        print(f"Suas notas em ordem crescente {notas}")
    elif opcao == "5":
        qnt = print(f"Você tem {len(notas)} notas.")
    elif opcao == "3":
        media = sum(notas) / len(notas)
        print(f"Sua média de notas é {media}")
        acima = 0
        abaixo = 0
        for nota in notas:
            if nota <= media:
                abaixo += 1
            else:
                acima += 1 
        print(f"Você possui {acima} de notas acima da média!")
        print(f"Você possui {abaixo} de notas abaixo da média.")
    elif opcao == "4":
        print(f"Sua maior nota é {max(notas)}!")
        print(f"Sua menor nota é {min(notas)}.")
  