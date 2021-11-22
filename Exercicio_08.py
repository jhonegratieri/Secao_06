print("Informe dez números, será retornado o maior e o menor deles.")
maior = -9999
menor = 9999

for i in range(1, 11):
    num = float(input(f"{i}: "))
    if num > maior:
        maior = num
    if num < maior:
        menor = num

print(f"O maior número é {maior} e o menor número é {menor}")
