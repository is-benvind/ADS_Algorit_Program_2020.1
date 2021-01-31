def main():
    x = 100
    y = 1000
    while x != y:
        v = input("X e Y: ")
        dados = v.split()
        x = int(dados[0])
        y = int(dados[1])

        if x > y:
            print("Decrescente")
        elif x < y:
            print("Crescente")

main()