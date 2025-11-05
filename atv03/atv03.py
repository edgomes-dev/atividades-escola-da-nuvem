from utils.ler_numero import ler_numero

print("============================================")
print("CALCULO DE IMC")
print("============================================")

peso = float(ler_numero("Digite seu peso (kg): "))
altura = float(ler_numero("Digite sua altura (cm): "))

altura_m = altura / 100  # Converte cm ➜ m
imc = peso / (altura_m ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"IMC: {imc:.2f} - {classificacao}")
