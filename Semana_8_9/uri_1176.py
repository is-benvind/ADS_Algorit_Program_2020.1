teste = int(input('Número de testes: '))
for i in range(teste):
    numero = int(input('Número para conversão: '))
    fibonacci = [0, 1]
    if numero > 1:
        for n in range(2, numero + 1):
            fibonacci.append(fibonacci[n-2] + fibonacci[n-1])
    print(f'Fib({numero}) = {fibonacci[numero]}')
