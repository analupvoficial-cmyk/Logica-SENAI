from datetime import datetime

def exibir_saudacao(nome):
    hora = datetime.now().hour
    minuto = datetime.now().minute
    print(hora,minuto)
    if hora <= 5:
       print(f"Boa Magrugada {nome}! Agora são {hora} horas e {minuto} minutos.")
    elif hora < 12:
        print(f"Bom dia {nome}!Agora são {hora} horas e {minuto} minutos.")
    elif hora <= 19:
        print(f"Boa tarde {nome}! Agora são {hora} horas e {minuto} minutos.")
    else:
        print(f"Boa noite {nome}! Agora são {hora} horas e {minuto} minutos.")
    

nome = input("Informe seu nome: ")


exibir_saudacao(nome)
