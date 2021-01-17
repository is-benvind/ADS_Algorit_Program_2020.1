def main():
    # Entrada
    a = int(input("A: "))
    b = int(input("B: "))
    # Processamento e Saída
    if a > b:
        if a % b == 0:
            print("São múltiplos")
        else:
            print("Não são múltiplos")
    elif b > a:
        if b % a == 0:
            print("São múltiplos")
        else:
            print("Não são múltiplos")

main()