def main():
    n = int(input("Quantidade de linhas: "))
    x = 1
    
    for i in range(1, n + 1):
        print(f"{x} {x+1} {x+2} PUM")
        x = x + 4

main()