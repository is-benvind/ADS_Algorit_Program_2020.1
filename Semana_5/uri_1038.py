def main():
    # Entrada
    cod = int(input("Código: "))
    qntd = int(input("Quantidade: "))

    # Processamento e Saída
    if cod == 1:
        total = qntd * 4
        print(f"Total: R$ {total:.2f}")
    elif cod == 2: 
        total = qntd * 4.50
        print(f"Total: R$ {total:.2f}")
    elif cod == 3:
        total = qntd * 5
        print(f"Total: R$ {total:.2f}")
    elif cod == 4:
        total = qntd * 2
        print(f"Total: R$ {total:.2f}")
    elif cod == 5:
        total = qntd * 1.50
        print(f"Total: R$ {total:.2f}")

main()