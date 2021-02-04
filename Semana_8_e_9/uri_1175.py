def main():
    v = []
    for i in range(20):
        elemento = int(input("Elemento: "))
        v.append(elemento)
    j = v[::-1]
    for k in range(20):
        print(f'N[{k}] = {j[k]}')

main()