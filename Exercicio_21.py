num1 = int(input("Informe o primeiro número inteiro: "))
num2 = int(input("Informe o segundo número inteiro: "))

soma = 0
multiplicacao = 1

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma += i
    else:
        multiplicacao *= i

print(f"A soma dos números pares desse intervalo é {soma}\n"
      f"A multiplicação dos números ímpares desse intervalo é {multiplicacao}")
