def main():
    # Entrada
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))

    # Processamento
    triangulo = (a * c) / 2
    pi = 3.14159
    circulo = pi * (c ** 2)
    trapezio = ((a + b) * c) / 2
    quadrado = b * b
    retangulo = a * b

    # Saída
    print(f"TRIÂNGULO = {triangulo:.3f}")
    print(f"CÍRCULO = {circulo:.3f}")
    print(f"TRAPÉZIO = {trapezio:.3f}")
    print(f"QUADRADO = {quadrado:.3f}")
    print(f"RETÂNGULO = {retangulo:.3f}")

main()