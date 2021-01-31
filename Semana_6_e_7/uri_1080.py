def main():
    maior = 0
    lista = {}
    posicao = 0

    for i in range(100):
        numero = int(input("Número: "))
        if  numero > maior:
            maior = numero
            lista[numero] = posicao
        posicao += 1

    print(maior)
    print(lista[maior]+1)

main()