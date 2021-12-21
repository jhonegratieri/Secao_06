print("Informe um intervalo de números")
n1 = int(input("Número inicial: "))
n2 = int(input("Número final: "))
aux = 0
qt = 0

for a in range(n1, n2 + 1):

    for b in range(3, a, 2):
        if a % b == 0 or a % 2 == 0:
            aux += 1

    if aux == 0:
        qt += 1

    aux = 0

print(f"Entre o número {n1} e o número {n2} existem {qt} números primos")
