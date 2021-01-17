def main():
    # Entrada
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))

    # Processamento e Saída
    media = (n1*2 + n2*3 + n3*4 + n4*1) / (2 + 3 + 4 + 1)
    print(f"Média: {media:.1f}")
    
    if media >= 7:
        print("Aluno aprovado.")

    elif media >= 5 and media <= 6.9:
        print("Aluno em exame.")
        
        n5 = float(input("Nota do exame: "))
        media2 = (media + n5) / 2

        if media2 >= 5:
            print("Aluno aprovado.")

        else:
            print("Aluno reprovado.")

        print(f"Média final: {media2:.1f}")

    else:
        print("Aluno reprovado.")

main()