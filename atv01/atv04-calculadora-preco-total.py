from utils import ler_numero

print("============================================")
print("CALCULADORA PREÇO TOTAL")
print("============================================")

produto = input("Nome do produto: ")
preco_unitario = ler_numero("Preço Unitário: ")
quantidade_produtos = ler_numero("Quantidade de Produtos: ")

valor_total = preco_unitario * quantidade_produtos

print(f'O valor total de {quantidade_produtos} {produto} ficou: {valor_total}')