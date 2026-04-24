from datetime import datetime 

def calcular_idade():
    nascimento = int(input("Informe o ano do seu nascimento:"))
    idade = datetime.now().year - nascimento
    return idade
