def main():
    i = 1
    j = 7

    while i <= 9:
        for k in range(1, 4):
            print(f"I={i}" " " f"J={j}")
            j = j - 1
        i = i + 2
        j = j + 5

main()