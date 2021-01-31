def main():
    n = int(input("Número de pares: "))
    
    for i in range(n):
        v = input("X e Y: ")
        dados = v.split()
        x = float(dados[0])
        y = float(dados[1])

        if y == 0:
            print("Divisão impossível")
        else:
            divisao = x / y 
            print(f"{divisao:.1f}")

main()