def main():
    # Entrada
    N = int(input("Segundos: "))

    # Processamento
    horas = N // 3600
    resto = N % 3600
    minutos = resto // 60
    segundos = resto % 60

    # Saída
    print(f"{horas} : {minutos} : {segundos}")

main()