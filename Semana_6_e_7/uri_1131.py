def main():
    continuar = 1
    e = 0
    v_inter = 0
    v_gre = 0

    while continuar == 1:
        gols = (input("Gols (Interncionl / Grêmio): "))
        dados = gols.split()
        gols_inter = int(dados[0])
        gols_gre = int(dados[1])

        if gols_inter > gols_gre:
            v_inter += 1
        elif gols_gre > gols_inter:
            v_gre += 1
        elif gols_gre == gols_inter:
            e += 1

        print("Novo grenal (1-Sim 2-Não)")
        continuar = int(input(":"))

    if continuar == 2:
        total = v_inter + v_gre + e
        print(f"{total} grenais")
        print(f"Inter: {v_inter}")
        print(f"Grêmio: {v_gre}")
        print(f"Empates: {e}")
        if v_inter > v_gre:
            print("Interncional venceu mais")
        elif v_gre > v_inter:
            print("Grêmio venceu mais")
        elif v_inter == v_gre:
            print("Não houve vencedor")

main()