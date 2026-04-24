import random

palpite = ""
opcao = ""
while True:
    print("Olá! Gostaria de participar do JOGO DA ADIVINHAÇÃO?")
    print("[SIM!] Digite 1")
    print("[NÃO!] Digite 2")
    opcao = int(input("Selecione se deseja continuar: "))
    if opcao == 1:
        print("A máquina irá selecionar um número aleatório entre 1 e 100, tente adivinha-lo de acordo com suas respostas.")
        numero = random.randint(0, 100)
        while opcao != 0 :
            palpite = int(input("Dê seu palpite: "))
            if numero < palpite:
                    print("O número é menor...")
            elif numero > palpite:
                    print("O número é maior...")
            elif numero == palpite :
                print("Você acertou! Parabéns!")
                break
    else:
        print("Ahh, que pena... :(")
        break