# Operadores Relacionais

# Maior >
# Menor <
# Igual ==
# Diferente !=

num1 = 5
num2 = 7
#print(num1 > num2)
#print(num1 < num2)
#print(num1 == num2)
#print(num1 != num2)

# Solicitar uma temperatura
temperatura = float(input("Informe a temperatura: "))

temp_amena = 25

# Verificar se a temperatura é maior que a amena
if temperatura > temp_amena:
    print("Ta calor")
elif temperatura == temp_amena:
    print("Ta ameno")
else:
    print("Ta frio")
    