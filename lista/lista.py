# Etapa 1 - Criar uma lista com 5 itens
objetos = ["rede","bola","manguito","tenis","joelheira"]
print("Lista de 5 objetos de vôlei criada com sucesso!")

# Etapa 2 - Adicionar um objeto ao final da lista
objetos.append("quadra")
print("O item Quadra foi adicionado ao final da lista.")

# Etapa 3 - Acessar o objeto que está na 2° posição e exibi-lo
objetos[1]
print(objetos[1])

# Etapa 4 - Remover um objeto da lista e exibi-lo
objetos.pop(3)
print(objetos.pop(3))

# Etapa 5 - Exibir o tamamho da lista
len(objetos)
print(len(objetos))


# Etapa 6 - Mostrar todos os itens
for objeto in objetos:
    print(objeto)
    
# Etapa 7 - Verificar se "cadeira" está na lista. Se sim remove-la, senão adiciona-la
if "cadeira" in objetos:
    objetos.remove("cadeira")
    print("O item foi removido com sucesso!")
else:
    objetos.append("cadeira")
    print("O item foi adicionado na lista!")

# Etapa 8 - Colocar em ordem alfabética e exibir Antes/Depois
print(objetos)
objetos.sort()
print(objetos)

# Etapa 9 - Acessar o 1° e o último objeto e exibi-los
objetos[0]
print(objetos[0])
objetos[4]
print(objetos[4])

# Lista de números
idades = [5, 18, 1, 64]
print(f"Maior idade {max(idades)}")
print(f"Menor idade {min(idades)}")
print(f"A soma das idades é {sum(idades)}")

# Etapa 10 - Limpar toda lista
objetos.clear()
print("A lista foi esvaziada")
