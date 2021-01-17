def main():
    # Entrada
    p1 = str(input("Primeira palavra: "))
    p2 = str(input("Segunda palavra: "))
    p3 = str(input("Terceira palavra: "))
    # Procesamento e Saída
    if p1 == "vertebrado":
        if p2 == "ave":
            if p3 == "carnivoro":
                animal = "aguia"
            else:
                animal = "pomba"
        else:
            if p3 == "onivoro":
                animal = "homem"
            else:
                animal == "vaca"
    else:
        if p2 == "inseto":
            if p3 == "hematofogo":
                animal == "pulga"
            else:
                animal == "lagarta"
        else:
            if p3 == "hematofogo":
                animal == "sanguessuga"
            else:
                animal == "minhoca"

    print(str(animal))
main()