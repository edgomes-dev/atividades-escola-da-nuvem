print("============================================")
print("ATIVIDADE 04")
print("============================================")

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == "sair":
        print("Encerrando programa...")
        break

    if len(senha) < 8:
        print("Senha muito curta! Deve ter pelo menos 8 caracteres.")
        continue

    if not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número.")
        continue

    print("Senha forte cadastrada com sucesso!")
    break
