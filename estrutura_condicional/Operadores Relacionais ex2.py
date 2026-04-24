nome = "Média"
print(nome)
nota1 = float(input("Selecione a primeira nota: "))
nota2 = float(input("Selecione a segunda nota: "))
soma = nota1 + nota2
media = soma / 2
if media < 70:
    print(f"Sua média foi {media}, REPROVADO")
else:
    print(f"Sua média foi {media}, parabéns! Você foi aprovado!")