from utils import ler_numero

print("============================================")
print("CALCULADORA NÚMERO INTEIRO")
print("============================================")

var_a = ler_numero("Valor A: ")
var_b = ler_numero("Valor B: ")
var_c = ler_numero("Valor C: ")
var_d = ler_numero("Valor D: ")

diferenca = (var_a * var_b - var_c * var_d)

print(f'O valor total ficou: {diferenca}')