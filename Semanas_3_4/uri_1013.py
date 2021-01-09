def main():
    # Entrada
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    
    # Processamento
    maior_ab = (a + b + abs(a - b)) // 2
    maior_abc = (maior_ab + c + abs(maior_ab - c)) // 2

    # Saída
    print(f"{maior_abc} eh o maior")

main()