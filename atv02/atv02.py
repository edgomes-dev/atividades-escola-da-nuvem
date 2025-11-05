from utils.ler_numero import ler_numero

print("============================================")
print("CALCULADORA DE DESCONTO")
print("============================================")

produto = input("Nome do produto: ")
var01 = ler_numero("Preço original: ")
var02 = ler_numero("Porcentagem de desconto: ")

desconto = var01 * (var02 / 100)
resultado = var01 - desconto

print(f'{produto} com desconto de {var02}, com valor original de {var01}, ficou por: {resultado} com {desconto} de desconto')
