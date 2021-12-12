num = 1
soma = 0
qt = 0
maior = -99999
menor = 99999
soma_pares = 0
qt_pares = 0

print("Informe quais números deseja utilizar nas operações. Digite 0 para concluir.")
while num != 0:
    num = float(input())
    soma += num

    if num != 0:
        qt += 1
    if num > maior and num != 0:
        maior = num
    if num < menor and num != 0:
        menor = num
    if num % 2 == 0 and num != 0:
        soma_pares += num
        qt_pares += 1

print(f"A soma dos números digitados é {soma}\n"
      f"A quantidade de números digitados é {qt}\n"
      f"A média dos números digitados é {round(soma / qt, 2)}\n"
      f"O maior número digitado é {maior}\n"
      f"O menor número digitado é {menor}\n"
      f"A média dos números pares é {round(soma_pares / qt_pares, 2)}")
