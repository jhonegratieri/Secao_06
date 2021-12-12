num = 2_000_000
soma = 0
aux = 0

for a in range(3, num + 1, 2):

    for b in range(3, a, 2):
        if a % b == 0:
            aux += 1

    if aux == 0:
        soma += a

    aux = 0

soma += 2  # Acrescenta o único número primo par à soma
print(f"A soma dos números primos até o número {num} é {soma}.")
