n = int(input("Informe um número inteiro positivo:"))
soma = 0

if n > 0:
    for i in range(n):
        soma += i
else:
    print("Não é um número inteiro positivo.")

print(f"O somatório dos {n} primeiros números naturais é {soma}")
