num = 0
maior = -99999
menor = 99999

print("Informe uma sequência de números inteiros, para encerrar digite um número negativo:")

while num >= 0:
    num = int(input())
    if num > maior:
        maior = num
    if menor > num >= 0:
        menor = num

print(f"O maior número lido é {maior} e o menor número lido é {menor}")
