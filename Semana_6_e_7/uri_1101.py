def main():
    M = 1
    N = 1
    quantia_numeros = 0
    soma = 0
    while M != 0 and N != 0:
        X = input('M e N: ').split(' ')
        M = int(X[0])
        N = int(X[1])
        if M == 0 or N == 0:
            break
        if M <= N:
            while M <= N:
                quantia_numeros = M
                M = M + 1
                soma = soma + quantia_numeros
                print(quantia_numeros, end=' ')
            print(f'Sum={soma}')
            if soma > 0:
                soma = 0
        if N <= M:
            while N <= M:
                quantia_numeros = N
                N = N + 1
                soma = soma + quantia_numeros
                print(quantia_numeros, end=' ')
            print(f'Sum={soma}')
            if soma > 0:
                soma = 0
                
main()