nome = "Maioridade"
print(nome)
data_nascimento = int(input("Informe o ano do seu nascimento: "))
idade = 2026 - data_nascimento
if idade >= 18:
    print(f"Você nasceu em {data_nascimento} e tem {idade} anos então já atingiu a maioridade")
else:
    print(f"Você nasceu em {data_nascimento} e tem {idade} anos então ainda não atingiu a maioridade")