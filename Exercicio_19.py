num = input("Informe um número entre 100 e 999: ")

if 100 <= int(num) <= 999:
    for i in range(3):
        print(num[i])
else:
    print("O número não está entre 100 e 999")
