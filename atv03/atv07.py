from utils.ler_numero import ler_numero

print("============================================")
print("MÉDIA")
print("============================================")

N1 = float(ler_numero("Digite o N1: "))
N2 = float(ler_numero("Digite o N2: "))
N3 = float(ler_numero("Digite o N3: "))
N4 = float(ler_numero("Digite o N4: "))

media = (N1*2 + N2*3 + N3*4 + N4*1) / 10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input("Nota do exame: "))
    print(f"Nota do exame: {exame:.1f}")
    
    media_final = (media + exame) / 2
    
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_final:.1f}")
