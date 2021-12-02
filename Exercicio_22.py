print("Informe suas notas. Lembre-se, notas válidas estão em um intervalo de 10 a 20.\n"
      "Insira uma nota inválida para sair do programa. Será retornado a média de suas notas.")

nota = 15
num_notas = 0
soma = 0

while 10 <= nota <= 20:
    nota = float(input())

    if 10 <= nota <= 20:
        num_notas += 1
        soma += nota

print(f"A média aritmética das notas inseridas é {soma / num_notas}")
