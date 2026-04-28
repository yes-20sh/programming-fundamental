rows = int(input("Enter the number of rows: "))

for row in range(rows):
    for column in range(row + 1):
        if row % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()