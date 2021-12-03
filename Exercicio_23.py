num = int(input("Informe um número inteiro positivo, serão retornados os divisores desse número: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end="  ")
