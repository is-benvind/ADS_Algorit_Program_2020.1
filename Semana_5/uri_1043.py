def main():
    # Entrada
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    # Processamento e Saída
    if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
        perimetro = a + b + c
        print(f"Perímetro = {perimetro:.1f}")
    else:
        area = ((a + b) * c) / 2
        print(f"Área = {area:.1f}")

main()