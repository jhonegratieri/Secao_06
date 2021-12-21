soma = 0

for i in range(1, 1001):

    centena = i // 100
    dezena = (i % 100) // 10
    unidade = i % 10

    # UNIDADES
    if dezena != 1:
        if unidade == 1:
            soma += 2
        elif unidade == 2 or unidade == 3 or unidade == 6 or unidade == 7 or unidade == 8 or unidade == 9:
            soma += 4
        elif unidade == 4:
            soma += 6
        elif unidade == 5:
            soma += 5

    # DEZENAS
    if dezena == 1:
        if unidade == 0:
            soma += 3
        elif unidade == 1 or unidade == 2:
            soma += 4
        elif unidade == 3:
            soma += 5
        elif unidade == 4 or unidade == 9:
            soma += 8
        elif unidade == 5:
            soma += 6
        elif unidade == 6 or unidade == 7:
            soma += 9
        else:
            soma += 7

    elif dezena == 2:
        if unidade == 0:
            soma += 5   # Vinte
        else:
            soma += 6   # Vinte e ...

    elif dezena == 3:
        if unidade == 0:
            soma += 6   # Trinta
        else:
            soma += 7   # trinta e ...

    elif dezena == 4 or dezena == 6:
        if unidade == 0:
            soma += 8   # Quarenta ou sessenta
        else:
            soma += 9   # Quarenta e ... ou sessenta e ...

    elif dezena == 7 or dezena == 8 or dezena == 9:
        if unidade == 0:
            soma += 7   # setenta, oitenta ou noventa
        else:
            soma += 8   # setenta e ..., oitenta e ... ou noventa e ...

    elif dezena == 5:
        if unidade == 0:
            soma += 9   # cinquenta
        else:
            soma += 10   # cinquenta e ...

    # CENTENAS
    if centena == 1:
        if dezena == 0 and unidade == 0:
            soma += 3   # cem
        else:
            soma += 6   # cento e ...

    elif centena == 2:
        if dezena == 0 and unidade == 0:
            soma += 8   # duzentos
        else:
            soma += 9   # duzentos e ...

    elif centena == 3:
        if dezena == 0 and unidade == 0:
            soma += 9   # trezentos
        else:
            soma += 10   # trezentos e ...

    elif centena == 4:
        if dezena == 0 and unidade == 0:
            soma += 12   # quatrocentos
        else:
            soma += 13   # quatrocentos e ...

    elif centena == 5 or centena == 6 or centena == 7 or centena == 8 or centena == 9:
        if dezena == 0 and unidade == 0:
            soma += 10   # Quinhentos, seiscentos, setecentos, oitocentos ou novecentos
        else:
            soma += 11   # Quinhentos e ..., seiscentos e ..., setecentos e ..., oitocentos e ... ou novecentos e ...

    if i == 1000:
        soma += 5   # um mil

print(f"Aos escrevermos todos os números de 1 a 1000 por extenso, escreveremos {soma} letras (espaços não são letras).")
