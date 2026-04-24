nome = str(input("Informe o nome do produto: "))
preco = float(input("Informe o preço do produto: "))
desconto = preco * 5
desconto1 = desconto / 100
desconto2 = preco + desconto1
print(f"O valor final do produto {nome} será {desconto2} , com diferença de {desconto1} $")