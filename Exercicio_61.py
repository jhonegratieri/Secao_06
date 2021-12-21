polindromo = ""
j = 0

for i in range(999, 100, -1):

    for j in range(i, 100, -1):
        polindromo = str(i * j)

        if polindromo[::1] == polindromo[::-1]:
            break

    if polindromo[::1] == polindromo[::-1]:
        print(f"{polindromo} = {i} * {j}")
        break
