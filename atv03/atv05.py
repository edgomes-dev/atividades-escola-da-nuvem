from utils.ler_numero import ler_numero

print("============================================")
print("ANO BISSEXTO")
print("============================================")

ano = int(ler_numero("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não é bissexto")
