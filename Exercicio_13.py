n = int(input("Informe um número inteiro positivo:"))

if n % 2 == 0:
    print("Os números pares de zero até o número escolhido, são:")
    for i in range(0, n + 1, 2):
        print(i, end="  ")
else:
    print("Não é um número inteiro par!")
