n = int(input("Informe quantos números primos deseja saber, te informaremos os primeiros: "))
qt_primos = 0
count = 2
aux = 0

if n > 0:
    while qt_primos < n:
        for i in range(3, count, 2):    # testa dodos os dividores ímpares
            if count % i == 0 or count % 2 == 0:  # verifica se o número é primo
                aux += 1
                break

        if aux == 0 or count == 2:
            print(count, end="  ")
            qt_primos += 1

        aux = 0
        count += 1
else:
    print("Número inválido!")
