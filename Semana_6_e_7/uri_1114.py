def main():
    senha = 10
    while senha != 2002:
        senha = int(input("Senha: "))
        if senha != 2002:
            print("Senha inválida")
        elif senha == 2002:
            print("Acesso permitido")

main()