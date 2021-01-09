def main():
    # Entrada
    distancia = int(input("Distância: "))
    combustivel = float(input("Combustível: "))

    # Processamento
    consumo = distancia / combustivel

    # Saída
    print(f'{consumo:.3f} km/l')

main()