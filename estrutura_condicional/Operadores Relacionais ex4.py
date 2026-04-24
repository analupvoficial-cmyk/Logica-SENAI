nome = "Qual número é maior?"
print(nome)
num1 = float(input("Selecione um número: "))
num2 = float(input("Selecione outro número: "))
if num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print(f"{num2} é maior que {num1}")
    