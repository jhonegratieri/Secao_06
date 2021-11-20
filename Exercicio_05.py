print("Informe dez números, retornaremos à soma de todos eles.")
soma = 0
for i in range(1, 11):
    num = float(input(f"Número {i}:"))
    soma += num
print(f"A soma dos números informados é {soma}")
