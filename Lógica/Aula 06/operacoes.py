import math

opcao = ""
while opcao != "0":
    print("Selecione uma opção.")
    print("[0] Sair")
    print("[1] Raiz Quadrada")
    print("[2] Quadrado")
    print("[3] Cubo")
    print("[4] Tabuada")
    opcao = input("Informe a opção escolhida: ")
    if opcao != "0":
        numero = int(input("Digite o número que deseja calcular: "))
    
    if opcao == "1":
        raiz = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {raiz}")
    elif opcao == "2":
        quadrado = numero * numero
        print(f"O Quadrado de {numero} é {quadrado}.")
    elif opcao == "3":
        cubo = numero * numero * numero
        print(f"O Cubo de {numero} é {cubo}")
    elif opcao == "4":
        print(numero * 1)
        print(numero * 2)
        print(numero * 3)
        print(numero * 4)
        print(numero * 5)
        print(numero * 6)
        print(numero * 7)
        print(numero * 8)
        print(numero * 9)
        print(numero * 10)
        