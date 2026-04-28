'''
11111
10001
10001
10001
11111

'''

rows = int(input("Enter the number of rows: "))

for row in range(rows):
    for column in range(rows):
        if row == 0 or row == (rows -1) or column == 0 or column == (rows -1):
            print("1", end="")
        else:
            print("0", end="")
    print()