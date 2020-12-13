def main():
    # entrada
    vendedor = str(input("Nome:"))
    salario_fixo = float(input("Salário fixo:"))
    total_vendas = float(input("Dinheiro das vendas:"))
    # processamento
    comissao = (total_vendas * 15) / 100
    salario_final = salario_fixo + comissao
    # saída
    print(f"TOTAL: R$ {salario_final:.2f}")

main()