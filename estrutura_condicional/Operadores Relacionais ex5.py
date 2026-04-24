nome = "Dias da semana"
print(nome)
dia_semana = int(input("Selecione um número entre 1 e 7: "))
if dia_semana == 1:
    print("Domingo")
elif dia_semana == 2:
    print("Segunda-feira")
elif dia_semana == 3:
    print("Terça-feira")
elif dia_semana == 4:
    print("Quarta-feira")
elif dia_semana == 5:
    print("Quinta-feira")
elif dia_semana == 6:
    print("Sexta-feira")
elif dia_semana == 7:
    print("Sábado")
if dia_semana >7:
    print("Ops! A semana contém apenas 7 dias...")