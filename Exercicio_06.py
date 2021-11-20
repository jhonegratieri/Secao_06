print("Informe 10 números inteiros, retornaremos a média deles:")

soma = 0

for i in range(1, 11):
    num = int(input(f"Número {i}:"))
    soma += num

print(f"A média dos números é {soma / 10}")
