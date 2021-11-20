print("Informe 10 números inteiros positivos, retornaremos a média deles:"
      "\nOBS: serão ignorados os números negativos.")

soma = 0
counter = 0

for i in range(1, 11):
    num = int(input(f"Número {i}:"))
    if num >= 0:
        soma += num
        counter += 1

print(f"A média dos {counter} números positivos é {soma / counter}")
