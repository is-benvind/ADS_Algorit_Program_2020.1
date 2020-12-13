def main():
    # entrada
    peca = int(input("Código da peça:"))
    num_pecas = int(input("Número de peças:"))
    valor = float(input("Valor da peça:"))
    peca_2 = int(input("Código da segunda peça:"))
    num_pecas_2 = int(input("Número de peças:"))
    valor_2 = float(input("Valor da segunda peça:"))
    # processamento
    a_pagar = num_pecas * valor
    a_pagar_2 = num_pecas_2 * valor_2
    total = a_pagar + a_pagar_2
    # saída
    print(f"VALOR A PAGAR: R$ {total:.2f}")

main()