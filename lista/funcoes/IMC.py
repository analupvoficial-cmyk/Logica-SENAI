def calcular_imc():
    altura = float(input("Informe sua altura: "))
    peso = float(input("Informe seu peso: "))
    imc = peso / (altura * altura)
    if imc <= 18.5:
        print(f"Seu Índice de Massa Corporal é {imc} e está abaixo do recomendado.")
    elif imc <= 24.9:
        print(f"Parabéns! Seu Índice de Massa Corporal é {imc} e está adequado.")
    elif imc <= 29.9:
        print(f"Seu Índice de Massa Corporal é {imc} e está acima do recomendado.")
    else:
        print(f"Seu Índice de Massa Corporal é {imc}, você está imenso! Procure ajuda imediatamente!")

calcular_imc()