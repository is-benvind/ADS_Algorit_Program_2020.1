par = []
impar = []
n = 0
p = 0
i = 0

while n < 15:
    numero = int(input('Número: '))
    if numero % 2 == 0:
        par.append(numero)
        print (f'par[{p}] = {par[p]}')
        p = p + 1
    else:
        impar.append(numero)
        print (f'impar[{i}] = {impar[i]}')
        i = i + 1
    if p > 4:
        par.clear()
        p = 0
    elif i > 4:
        impar.clear()
        i = 0
    n = n + 1