def c_para_k(celsius):
    kelvin = celsius + 273
    return kelvin

def c_para_f(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

celsius = float(input("Informe a temperatura em graus celsius: "))


print(f"{celsius} graus celsius correspondem a {c_para_k(celsius)} kelvin.")
print(f"{celsius} graus celsius correspondem a {c_para_f(celsius)} fahrenheit.")