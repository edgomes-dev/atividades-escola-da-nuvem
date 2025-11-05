from utils import ler_numero

print("============================================")
print("CONVERSOR DE MOEDAS")
print("============================================")

taxa = 0
moeda = ler_numero("Escolha Moeda: 1(Dolar) | 2(Euro): ")

if(moeda == 1) {
    moeda = "Dólar"
    taxa = 5.60
} else if (moeda == 2) {
    moeda = "Euro"
    taxa = 6.60
} else {
    print("Opção inválida")
    moeda = ler_numero("Escolha Moeda: 1(Dolar) | 2(Euro)")
}

real = ler_numero("Valor em Real: ")

resultado = real / taxa

print(f'Convertendo o valor de R${real}, para {moeda}, fica por: {resultado}')