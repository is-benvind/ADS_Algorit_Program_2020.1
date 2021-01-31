def main():
    x = 10
    y = 100
    while x != 0 and y != 0:
        coordenadas = input("X e Y: ")
        dados = coordenadas.split()
        x = int(dados[0])
        y = int(dados[1])

        if x > 0 and y > 0:
            print("Primeiro quadrante")
        elif y > 0 and x < 0:
            print("Segundo quadrante ")
        elif y < 0 and x < 0:
            print("Terceiro quadrante")
        elif x > 0 and y < 0:
            print("Quarto quadrante")

main()