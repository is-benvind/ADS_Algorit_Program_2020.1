def main():
    # Entrada
    salario = float(input("Salário: "))

    # Processamento e Saída
    if salario <= 400:
        novo_s = 1.15 * salario
        reajuste = novo_s - salario
        print(f"NOVO SALÁRIO: {novo_s:.2f}")
        print(f"REAJUSTE GANHO: {reajuste:.2f}")
        print("EM PERCENTUAL: 15 %")
    elif salario <= 800:
        novo_s = 1.12 * salario
        reajuste = novo_s - salario
        print(f"NOVO SALÁRIO: {novo_s:.2f}")
        print(f"REAJUSTE GANHO: {reajuste:.2f}")
        print("EM PERCENTUAL: 12 %")
    elif salario <= 1200:
        novo_s = 1.10 * salario
        reajuste = novo_s - salario
        print(f"NOVO SALÁRIO: {novo_s:.2f}")
        print(f"REAJUSTE GANHO: {reajuste:.2f}")
        print("EM PERCENTUAL: 10 %")
    elif salario <= 2000:
        novo_s = 1.07 * salario
        reajuste = novo_s - salario
        print(f"NOVO SALÁRIO: {novo_s:.2f}")
        print(f"REAJUSTE GANHO: {reajuste:.2f}")
        print("EM PERCENTUAL: 7 %")
    else:
        novo_s = 1.04 * salario
        reajuste = novo_s - salario
        print(f"NOVO SALÁRIO: {novo_s:.2f}")
        print(f"REAJUSTE GANHO: {reajuste:.2f}")
        print("EM PERCENTUAL: 4 %")

main()