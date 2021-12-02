n = int(input("Informe um número inteiro positivo par:"))

if n % 2 == 0:
    print("Os números ímpares do número escolhido até 1, são:")
    for i in range(n - 1, 0, -2):
        print(i, end="  ")
else:
    print("Não é um número inteiro par.")
