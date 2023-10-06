def main():
    vetorX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
    
    for i in range(len(vetorX)):
        vetorX[i] = int(input(': '))

        if vetorX[i] <= 0:
            vetorX[i] = 1

        print(f"X[{i}] = {vetorX[i]}")

main()
