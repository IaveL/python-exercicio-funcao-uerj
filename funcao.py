base = int(input("Digite a base: "))
exp = int(input("Digite o expoente: "))


def potencia(base, exp):
    # inicializar um array com a base e fazer um loop multiplicando cada item por si mesmo
    total = 1
    arr = ([base] * exp)

    for i in range(0, len(arr)):
        total = total * arr[i]

    return print(f'{base} elevado à {exp} é: {total}')


potencia(base, exp)
