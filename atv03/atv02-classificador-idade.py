from utils.ler_numero import ler_numero

print("============================================")
print("CLASSIFICAR IDADE")
print("============================================")

idade = int(ler_numero("Digite sua idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
