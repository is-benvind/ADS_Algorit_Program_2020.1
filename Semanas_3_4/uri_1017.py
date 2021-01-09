def main():
    # Entrada
    horas = int(input("Horas em viagem: "))
    velocidade = int(input("km/h: "))

    # Processamento
    distancia = horas * velocidade
    litros = distancia / 12

    # Saída
    print(f"{litros:.3f}")

main()