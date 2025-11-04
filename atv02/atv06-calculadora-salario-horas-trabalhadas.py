from utils import ler_numero

print("============================================")
print("SÁLARIO HORAS TRABALHADAS")
print("============================================")

cod_funcionario = ler_numero("Identificador do funcionário: ")
horas_trabalhadas = ler_numero("Horas trabalhadas: ")
valor_hora = ler_numero("Valor da hora: ")

salario = horas_trabalhadas * valor_hora

print(f'Número do funcionário: {cod_funcionario}')
print(f'Salário: R${salario:.2f}')
