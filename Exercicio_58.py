print("Informe um intervalo de números")
n1 = int(input("Número inicial: "))
n2 = int(input("Número final: "))
aux = 0
soma = 0

for a in range(n1, n2 + 1):

    for b in range(3, a, 2):
        if a % b == 0 or a % 2 == 0:
            aux += 1

    if aux == 0:
        soma += a

    aux = 0

print(f"A soma dos números primos que estão entre o número {n1} e o número {n2} é {soma}")
