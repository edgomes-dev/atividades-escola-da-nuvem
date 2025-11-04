import math
from utils.ler_numero import ler_numero

print("============================================")
print("ÁREA CIRCUNFERENCIA")
print("============================================")


raio = float(ler_numero("Digite o valor do raio: "))
area = 3.14159265 * (raio ** 2)

print(f"A={area:.4f}")
