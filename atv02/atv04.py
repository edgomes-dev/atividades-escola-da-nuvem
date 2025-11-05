from utils import ler_numero

print("============================================")
print("CONSUMO DE COMBUSTÍVEL")
print("============================================")

var01 = ler_numero("Distância percorrida: ")
var02 = ler_numero("Combustível gasto: ")

resultado = var01 / var02

print(f'Consumo médio: {resultado:.2f} km/l')
