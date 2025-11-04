from utils.ler_numero import ler_numero

print("============================================")
print("CALCULADORA DE COMISSÃO")
print("============================================")

nome = input("Nome do vendedor: ")
salario_fixo = float(ler_numero("Salário fixo: R$ "))
total_vendas = float(ler_numero("Total de vendas: R$ "))

comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao

print(f"TOTAL = R$ {total_receber:.2f}")
