n = int(input("Informe um número inteiro positivo:"))

if n % 2 == 0:
    print("Os números pares do número escolhido até zero, são:")
    for i in range(n, -1, -2):
        print(i, end="  ")
else:
    print("Não é um número inteiro par!")
