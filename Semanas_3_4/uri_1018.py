
def main():
    # Entrada
    valor = int(input("Valor: "))
    valor_inicial = valor

    # processamento
    notas_cem, valor = quociente_resto(valor, 100)

    notas_cinquenta, valor = quociente_resto(valor, 50)

    notas_vinte, valor = quociente_resto(valor, 20)

    notas_dez, valor = quociente_resto(valor, 10)

    notas_cinco, valor = quociente_resto(valor, 5)

    notas_dois, valor = quociente_resto(valor, 2)

    notas_um, valor = quociente_resto(valor, 1)

    # Saída
    print(valor_inicial)
    print(f"{notas_cem} nota(s) de R$ 100,00")
    print(f"{notas_cinquenta} nota(s) de R$ 50,00")
    print(f"{notas_vinte} nota(s) de R$ 20,00")
    print(f"{notas_dez} nota(s) de R$ 10,00")
    print(f"{notas_cinco} nota(s) de R$ 5,00")
    print(f"{notas_dois} nota(s) de R$ 2,00")
    print(f"{notas_um} nota(s) de R$ 1,00")

def quociente_resto(valor1, valor2):
    quociente = valor1 // valor2
    resto = valor1 % valor2
    return quociente, resto

main()