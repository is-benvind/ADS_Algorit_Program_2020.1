def main():
    n = int(input("Quantidade: "))

    for i in range(n):
        linha = input("Valores: ")
        dados = linha.split()
        valor1 = float(dados[0])
        valor2 = float(dados[1])
        valor3 = float(dados[2])

        media_ponderada = (valor1*2 + valor2*3 + valor3*5) / (2 + 3 + 5)

        print(f"{media_ponderada:.1f}")

main()