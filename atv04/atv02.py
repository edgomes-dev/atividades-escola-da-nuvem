from utils.ler_numero import ler_numero

print("============================================")
print("ATIVIDADE 02")
print("============================================")


notas = []

while True:
    entrada = ler_numero("Digite uma nota (0-10) ou 'fim' para encerrar: ")

    if entrada.lower() == "fim":
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite um número ou 'fim'.")

if notas:
    print(f"Média da turma: {sum(notas) / len(notas):.2f}")
else:
    print("Nenhuma nota válida foi registrada.")
