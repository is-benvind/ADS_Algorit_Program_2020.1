def main():
    n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    valor = int(input("Valor: "))

    for i in range(len(n)):
        n[i] = valor
        valor = valor * 2
        print(f"N[{i}] = {n[i]}")

main()