vetor = []
for i in range(100):
    numero = float(input('Número: '))
    vetor.append(numero)
for i in range(100):
    if vetor[i] <= 10:
        print (f'N[{i}] = {vetor[i]:.1f}')
