nome = "Aposentadoria"
print(nome)

# para importar funções externar precisamos usar o import
# from arquivo import nome_das_funcoes
from funcoes import calcular_idade

idade = calcular_idade()
genero = input("Informe seu gênero (MASCULINO/FEMININO): ")
if genero == "Masculino" and idade >= 65:
    print(f"Sua aposentadoria foi concluida!")
elif genero == "Feminino" and idade >= 62:
    print(f"Sua aposentadoria foi concluida!")
else:
    print(f"Sua aposentadoria não é válida!")