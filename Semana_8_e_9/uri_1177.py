def main():
    t = int(input('Valor: '))
    n = []
    i = 0
    x = 0

    while i < (1000):
        n.append(x)
        print(f'N[{i}] = {x}')

        if x < (t - 1):
            x = x + 1
        else:
            x == t - 1
            x = 0

        i += 1

main()