def main():
    # Entrada
    h1 = int(input("Hora inicial: "))
    h2 = int(input("Hor final: "))
    # Processamento e Saída
    if h2 > h1:
        tempo = h2 - h1
        print(f"O JOGO DUROU {tempo} HORA(S)")
    elif h1 == h2:
        print(f"O JOGO DUROU 24 HORA(S)")
    else:
        tempo = 24 - h1 + h2
        print(f"O JOGO DUROU {tempo} HORA(S)")

main()