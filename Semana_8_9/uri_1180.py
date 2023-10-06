tamanho = int(input('Tamanho do vetor: '))
vetor = input('Valores do vetor: ')
vetor = vetor.split()

for i in range(len(vetor)):
    vetor[i] = int(vetor[i])

menor = vetor[0]
posicao = 0
for j in range(1,len(vetor)):
    if vetor[j] < menor:
        menor = vetor[j]
        posicao = j

print('Menor valor: {}'.format(menor))
print('Posição: {}'.format(posicao))
