from utils.ler_numero import ler_numero

print("============================================")
print("ATIVIDADE 01")
print("============================================")


while True:
    try:
        num1 = float(ler_numero("Digite o primeiro número: "))
        num2 = float(ler_numero("Digite o segundo número: "))
        op = input("Digite a operação (+, -, *, /): ")

        if op not in ['+', '-', '*', '/']:
            print("Erro: operação inválida! Tente novamente.")
            continue

        if op == '+':
            resultado = num1 + num2
        elif op == '-':
            resultado = num1 - num2
        elif op == '*':
            resultado = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Erro: divisão por zero não é permitida!")
                continue
            resultado = num1 / num2

        print(f"Resultado: {resultado}")
        break  # operação concluída com sucesso, encerra
    except ValueError:
        print("Erro: Digite apenas números!")
