n = int(input("Informe um número inteiro positivo par:"))

if n % 2 == 0:
    print("Os números ímpares de 1 até o número escolhido, são:")
    for i in range(1, n, 2):
        print(i, end="  ")
else:
    print("Não é um número inteiro par.")
