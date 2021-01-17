def main():
    # Entrada
    h1 = int(input("Hora inicial: "))
    m1 = int(input("Minuto inicial: "))
    h2 = int(input("Hora final: "))
    m2 = int(input("Minuto final: "))

    # Processamento e Saída
    if h2 > h1 and m2 >= m1:
        tempoh = h2 - h1
        tempom = m2 - m1
        print(f"O JOGO DUROU {tempoh} HORA(S) E {tempom} MINUTO(S)")
    if h2 > h1 and m2 < m1:
        tempoh = h2 - h1 - 1
        tempom = 60 - m1 + m2 
        print(f"O JOGO DUROU {tempoh} HORA(S) E {tempom} MINUTO(S)")
    elif h1 == h2 and m1 == m2:
        print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    elif h1 == h2 and m2 < m1:
        tempom = 60 - m1 + m2 
        print(f"O JOGO DUROU 24 HORA(S) E {tempom} MINUTO(S)")
    elif h2 < h1 and m2 >= m1:
        tempoh = 24 - h1 + h2
        tempom = m2 - m1
        print(f"O JOGO DUROU {tempo} HORA(S) E {tempom} MINUTO(S)")
    elif h2 < h1 and m2 < m1:
        tempoh = 24 - h1 + h2
        tempom = 60 - m1 + m2 
        print(f"O JOGO DUROU {tempo} HORA(S) E {tempom} MINUTO(S)")

main()