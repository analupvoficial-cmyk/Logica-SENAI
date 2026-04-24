from time import sleep
lista_times = []
opcao = ""
while opcao !=4:
    print()
    print("Olá! Bem-vindo (a) ao site da CBF!")
    sleep(1)
    print()
    print("[1] Cadastrar time.")
    sleep(0.5)
    print("[2] Listar todos os times.")
    sleep(0.5)
    print("[3] Quantidade de times.")
    sleep(0.5)
    print()
    sleep(1)
    opcao = int(input("Selecione uma opcão: "))
    print()
    if opcao == 1:
        time = {}
        time["nome"] = input("Informe o nome do time: ")
        time["titulos"] = input("Informe a quantidade de títulos do time: ")
        time["mundiais"] = input("Informe quantos Mundiais o time possui: ")
        time["estadio"] = input("Informe o nome do Estádio do time: ")
        lista_times.append(time)
        sleep(1)
        print()
        print("Gostaria de adicionar um novo campo?")
        print("[1] sim")
        print("[2] não")
        opcao = int(input("Informe sua opção: "))
        if opcao == 1:
            chave = input("Adicione um campo: ")
            valor = input("Valor do campo: ")
            time[chave] = valor
            print()
            print("Campo criado!")
        
    elif opcao == 2:
        for time in lista_times:
            for chave, valor in time.items():
                print(f"{chave}: {valor}")
            print()
        print()
    elif opcao == 3:
        len(lista_times)
        print(f"Times: {len(lista_times}")
       
    else:
        print("Ok!")
        sleep(1)
        print("Saindo...")
        sleep(2)
        print("Você saiu!")
 


        
       