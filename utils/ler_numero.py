"""
    Lê um número digitado pelo usuário e valida a entrada.
    Retorna um int válido.
"""
def ler_numero(mensagem):

    while True:
        valor = input(mensagem)
        try:
            return int(valor)
        except ValueError:
            print("Erro: Digite um número válido!")
