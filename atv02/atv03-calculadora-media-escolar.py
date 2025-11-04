from utils import ler_numero

print("============================================")
print("MÉDIA ESCOLAR")
print("============================================")

var_a = ler_numero("Nota A: ")
var_b = ler_numero("Nota B: ")
var_c = ler_numero("Nota C: ")

resultado = (var_a + var_b + var_c) / 3

print(f'Sua média ficou por: {resultado:.2f}')
