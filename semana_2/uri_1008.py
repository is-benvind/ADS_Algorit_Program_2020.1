def main():
    # entrada
    num_fun = int(input("Número do funcionário:"))
    hrs_trab = int(input("Horas trabalhadas:"))
    salario_hr = float(input("Salário por hora:"))
    # processamento
    salario = hrs_trab * salario_hr
    # saída
    print(f"NÚMERO: {num_fun} SALÁRIO: R$ {salario:.2f}")

main()