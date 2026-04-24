from time import sleep
times = {
    "Nome": "Sociedade Esportiva Palmeiras",
    "Títulos_Nacionais": "18 títulos",
    "Mundias": 1,
    "Estádio": "Allianz Parque"
    }

#adicionar um campo
times["Jogador mais gato"] = "Piquerez"
times["Treinador"] = "Abel Frreira"
times["Ano de fundação"] = 1914
times["Copa Libertadores"] = "3 títulos"

#exibir um dicionario
for chave, valor in times.items():
    print(f"{chave}: {valor}")

print(times["Jogador mais gato"])
opcao = ""
while opcao != 2:
    print("Gostaria de adicionar um novo campo?")
    print("[1] sim")
    print("[2] não")
    opcao = int(input("Informe sua opção: "))
    if opcao == 1:
        campo = input("Adicione um campo: ")
        valor = input("Valor do campo: ")
        times[campo] = valor
        print("Campo criado!")
        
        for chave, valor in times.items():
            print(f"{chave}: {valor}")
    else:
        print("Ok!")
        sleep(1)
        print("Saindo...")
        sleep(2)
        print("Você saiu!")
