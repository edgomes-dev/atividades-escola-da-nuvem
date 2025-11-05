from utils.ler_numero import ler_numero

print("============================================")
print("CONVERSOR TEMEPRATURA")
print("============================================")


valor = float(ler_numero("Digite a temperatura: "))
origem = ler_numero("Unidade de origem (C/F/K): ").upper()
destino = ler_numero("Converter para (C/F/K): ").upper()

temp_c = valor

if origem == "F":
    temp_c = (valor - 32) * 5/9
elif origem == "K":
    temp_c = valor - 273.15

if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = (temp_c * 9/5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

print(f"Resultado: {resultado:.2f} °{destino}")
