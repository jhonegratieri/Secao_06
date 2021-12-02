qt_num = int(input("Quantos números deseja inserir:"))
qt_maior = 0
maior = -9999

for i in range(0, qt_num):
    num = float(input(f"Número {i + 1}: "))
    if num > maior:
        maior = num
        qt_maior += 1

print(f"O maior número digitado é {maior}")
print(f"O maior número foi alterado {qt_maior - 1} vezes")
