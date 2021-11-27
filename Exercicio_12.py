n = int(input("Informe um número, será retornado uma lista com todos os números naturais "
              "iniciando no número escolhido, e terminando em zero:"))

for i in range(n, -1, -1):
    print(i, end="  ")
