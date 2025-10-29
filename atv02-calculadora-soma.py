from utils import ler_numero

print("============================================")
print("APLICATIVO DE SOMA")
print("============================================")

var01 = ler_numero("Digite o primeiro número: ")
var02 = ler_numero("Digite outro número: ")

soma = var01 + var02

print(f'Resultado da soma entre {var01} + {var02} = {soma}')