def main():
    # Entrada
    v1 = int(input("Valor 1: "))
    v2 = int(input("Valor 2: "))
    v3 = int(input("Valor 3: "))

    # Processamento e Saída
    if v1 < v2 < v3:
        print(v1)
        print(v2)
        print(v3)
    elif v1 < v3 < v2:
        print(v1)
        print(v3)
        print(v2)
    elif v2 < v1 < v3:
        print(v1)
        print(v2)
        print(v3)
    elif v2 < v3 < v1:
        print(v2)
        print(v3)
        print(v1)
    elif v3 < v1 < v2:
        print(v3)
        print(v1)
        print(v2)
    elif v3 < v2 < v1:
        print(v3)
        print(v2)
        print(v1)

    print()
    print(v1)
    print(v2)
    print(v3)

main()