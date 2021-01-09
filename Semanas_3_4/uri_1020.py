def main():
    # Entrada
    idade = int(input("Dias: "))

    # Processamento
    anos = idade // 365
    resto = idade % 365
    meses = resto // 30
    dias = resto % 30

    # Saída
    print(f"{anos} ano(s)")
    print(f"{meses} mes(es)")
    print(f"{dias} dia(s)")

main()