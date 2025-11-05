from utils import ler_numero

print("============================================")
print("CALCULADORA DE VOLUME")
print("============================================")

comprimento = ler_numero("Comprimento: ")
largura = ler_numero("Largura: ")
altura = ler_numero("Altura: ")

volume = comprimento * largura * altura

print(f'O volume da caixa é: {volume}')