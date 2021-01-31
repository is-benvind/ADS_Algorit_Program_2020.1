def main():
    nota1 = -1
    nota2 = -2
    while 10 < nota1 or nota1 < 0:
        nota1 = float(input("Nota 1: "))
        if 10 < nota1 or nota1 < 0:
            print("Nota inválida")
    while 10 < nota2 or nota2 < 0:
        nota2 = float(input("Nota 2: "))
        if 10 < nota2 or nota2 < 0:
            print("Nota inválida")
    if 10 >= nota1 and nota1 > 0 and 10 >= nota2 and nota2 > 0:
        media = (nota1+nota2) / 2
        print(f"Média = {media:.2f}")

main()