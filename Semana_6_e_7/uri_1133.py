def main():
    x = int(input("X: "))
    y = int(input("Y: "))

    if x > y:
        a = y
        b = x
    if x < y:
        a = x
        b = y

    while a < b:
        if a % 5 == 2 or a % 5 == 3:
            print(a)
        a = a + 1

main()