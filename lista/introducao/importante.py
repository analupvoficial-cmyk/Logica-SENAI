# 1- como salvar dados/informações
 # Usando variável
nome = "Ana"
salario = 1500.50

# 2- como solicitar informações
 # Usando input
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))

# 3- Como exibir informações
 # Usando o print
print(f"Seu nome é {nome} e seu salário é {salario}")

# 4- Como fazer verificações
 # usando if/else
if salario >= 1600:
    print("Salário maior que o mínimo")
else:
    print("Salário menor que o mínimo")
    
# 5- Como solicitar informações complexas
 # Usando um menu
print("Selecione seu gênero: ")
print("1 - Masculino")
print("2 - Feminino")
genero_escolha = input("Digite a opção: ")

if genero_escolha == "1" :
    genero = "Masculino"
elif genero_escolha == "2":
    genero = "Feminino"
else:
    print("Opção inválida")
    
    
