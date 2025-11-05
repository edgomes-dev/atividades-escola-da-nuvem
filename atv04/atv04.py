print("============================================")
print("ATIVIDADE 03")
print("============================================")


while True:
    valor = input("Digite um número inteiro ou 'fim' para encerrar: ")

    if valor.lower() == "fim":
        break

    try:
        numero = int(valor)
        if numero % 2 == 0:
            print("Par ✅")
            pares += 1
        else:
            print("Ímpar ✅")
            impares += 1
    except ValueError:
        print("Erro: Digite apenas números inteiros!")

print(f"Total de pares: {pares}")
print(f"Total de ímpares: {impares}")
