def main():
    # entrada
    A = float(input("Primeira nota:"))
    B = float(input("Segunda nota:"))
    C = float(input("Terceira nota:"))
    # processamento
    media = ((A * 2) + (B * 3) + (C * 5)) / 10
    # saída
    print(f"MEDIA = {media:.1f}")

main()