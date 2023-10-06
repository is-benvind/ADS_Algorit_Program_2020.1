numero = int(input('Número: '))
vetor = [numero]
i = 0
while i < 100:
    vetor.append(f'{(numero / 2):.4f}')
    numero = numero / 2
    i = i + 1
    print (f'N[{i}] = {vetor[i]}')
