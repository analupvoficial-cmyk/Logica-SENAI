print(f"A viagem possui 800km de duração")
print(f"O carro consome 1 litro de gasolina a cada 7km")
print(f"Restam apenas 10 litros no carro e o motorista já percorreu 90km do trajéto")
distancia_total = 800
distancia_percorrida = 90
distancia_faltante = distancia_total - distancia_percorrida

km_l = 7
litros = 10
espaço_percorrido = km_l * litros

litros_faltantes = (distancia_faltante - espaço_percorrido) / km_l

gasolina = 6.90 

total = litros_faltantes * gasolina

print(f"O motorista irá abastecer mais {litros_faltantes} litros, que lhe custarão {total}")
