def main():
    alcool = 0
    gasolina = 0
    diesel = 0
    codigo = 0
    print("1.Álcool " " " " 2.Gasolina" " ""3.Diesel" " " "4.Fim")

    while codigo != 4:
        codigo = int(input("Código: "))

        if codigo == 1:
            alcool +=1
        elif codigo == 2:
            gasolina +=1
        elif codigo == 3:
            diesel += 1
        elif codigo == 4:
            print("MUITO OBRIGADO")
            print(f"Álcool: {alcool}")
            print(f"Gasolina: {gasolina}")
            print(f"Diesel: {diesel}")


main()