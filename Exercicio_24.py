num = int(input("Informe um número inteiro positivo: "))
soma = 0
for i in range(1, num):
    if num % i == 0:
        soma += i

print(f"A soma dos divisores do número informado é {soma}")
