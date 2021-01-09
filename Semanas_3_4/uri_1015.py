def main():
    # Entrada
    x1 = float(input("X1: ")) 
    y1 = float(input("Y1: "))
    x2 = float(input("X2: ")) 
    y2 = float(input("Y2: "))

    # Processamento
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)

    # Saída
    print(f"{distancia:.4f}")

main()
